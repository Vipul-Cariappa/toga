from asyncio import get_event_loop
from unittest import registerResult

from travertino.size import at_least

from toga_winforms.keys import toga_key
from toga_winforms.libs import Action, String, Task, TaskScheduler, Uri, WebView2, CoreWebView2CreationProperties

from .base import Widget


class TogaWebBrowser(WebView2):
    def __init__(self, interface):
        super().__init__()
        self.interface = interface


class WebView(Widget):
    def create(self):
        self.native = WebView2()
        self.native.CoreWebView2InitializationCompleted += self.winforms_initialization_completed
        self.native.NavigationCompleted += self.winforms_navigation_completed

        props = CoreWebView2CreationProperties()
        props.UserDataFolder = None
        self.native.CreationProperties = props

        # Trigger the configuration of the webview
        self.native.EnsureCoreWebView2Async(None)

    def winforms_initialization_completed(self, sender, args):
        # The WebView2 widget has an "internal" widget (CoreWebView2) that is
        # the actual web view. The view isn't ready until the internal widget has
        # completed initialization, and that isn't done until an explicit
        # request is made (EnsureCoreWebView2Async).
        if args.IsSuccess:
            try:
                # settings = sender.CoreWebView2.Settings
                settings = self.native.CoreWebView2.Settings

                debug = True
                settings.AreDefaultContextMenusEnabled = debug
                settings.AreDefaultScriptDialogsEnabled = True
                settings.AreDevToolsEnabled = debug
                settings.IsBuiltInErrorPageEnabled = True
                settings.IsScriptEnabled = True
                settings.IsWebMessageEnabled = True
                settings.IsStatusBarEnabled = debug
                settings.IsZoomControlEnabled = True

                self.set_user_agent(self.interface.user_agent)

                if self.interface._html_content:
                    self.set_content(self.interface.url, self.interface._html_content)
                else:
                    self.set_url(self.interface.url)

            except Exception as e:
                import traceback
                traceback.print_exc()
        else:
            print(args.InitializationException)

    def winforms_navigation_completed(self, sender, args):
        if self.interface.on_webview_load:
            self.interface.on_webview_load(self.interface)

    def set_on_key_down(self, handler):
        pass

    def set_on_webview_load(self, handler):
        pass

    def set_url(self, value):
        self.native.Source = Uri(self.interface.url)

    def set_content(self, root_url, content):
        if self.native.CoreWebView2:
            self.native.CoreWebView2.NavigateToString(content)

    def get_dom(self):
        self.interface.factory.not_implemented('WebView.get_dom()')

    def set_user_agent(self, value):
        user_agent = value if value else "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46"  # NOQA
        if self.native.CoreWebView2:
            self.native.CoreWebView2.Settings.UserAgent = user_agent

    async def evaluate_javascript(self, javascript):
        loop = get_event_loop()
        future = loop.create_future()

        task_scheduler = TaskScheduler.FromCurrentSynchronizationContext()
        try:
            def callback(task):
                future.set_result(task.Result)

            self.native.ExecuteScriptAsync(javascript).ContinueWith(
                Action[Task[String]](callback),
                task_scheduler
            )
        except Exception as e:
            future.set_result(None)

        return await future

    def invoke_javascript(self, javascript):
        # The script will execute async, but you weren't going to get the result
        # anyway, so it doesn't really matter.
        self.native.ExecuteScriptAsync(javascript)

    def rehint(self):
        self.interface.intrinsic.width = at_least(self.interface.MIN_WIDTH)
        self.interface.intrinsic.height = at_least(self.interface.MIN_HEIGHT)
