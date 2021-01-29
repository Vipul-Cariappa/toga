from .base import Widget


class Page(Widget):
    """This is a Widget that contains other widgets, but has no rendering or
    interaction of its own.
    Args:
        id (str): An identifier for this widget.
        style (:class:colosseum.CSSNode`): An optional style object. If no
            style is provided then a new one will be created for the widget.
        children (``list`` of :class:`toga.Widget`):  An optional list of child
            Widgets that will be in this box.
        factory (:obj:`module`): A python module that is capable to return a
            implementation of this class with the same name. (optional &
            normally not needed)
    """

    def __init__(self, id=None, children=None, style=None, factory=None):
        super().__init__(id=id, style=style, factory=factory)

        self._children = []
        if children:
            self.add(*children)

        self._impl = self.factory.Page(interface=self)


class MultiPageView(Widget):
    """This is a Widget containes pages where a single page is a Box like
    widget. And handles manipulation of pages.
    Args:
        id (str): An identifier for this widget.
        style (:class:`colosseum.CSSNode`): An optional style object. If no
            style is provided then a new one will be created for the widget.
        factory (:obj:`module`): A python module that is capable to return a
            implementation of this class with the same name. (optional &
            normally not needed)
    """

    def __init__(self, id=None, style=None, factory=None):
        super().__init__(id=id, style=style, factory=factory)

        self.pages = []
        self._children = []
        self._impl = self.factory.MultiPageView(interface=self)

    def create_page(self, style=None, children=None, id=None, factory=None):
        """Create's a box like widget and return it.
        Args:
            id (str): An identifier for this widget.
            style (:class:`colosseum.CSSNode`): An optional style object. If no
                style is provided then a new one will be created for the widget.
            children (``list`` of :class:`toga.Widget`):  An optional list of child
                Widgets that will be in this box.
            factory (:obj:`module`): A python module that is capable to return a
                implementation of this class with the same name. (optional &
                normally not needed)
        Returns:
            A box like widget.
        """
        page = Page(style=style, children=children, id=id, factory=factory)

        self.pages.append(page)
        self.add(page)

        self._impl.add_page(page._impl)
        return page

    def top(self, page):
        """Sets the top most page to interact and view.
        Args:
            page (:class:`toga.widgets.multipageview.Page`): Page to set at top.
        """
        self._impl.set_top(page._impl)
