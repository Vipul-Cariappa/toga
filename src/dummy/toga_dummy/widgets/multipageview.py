from .base import Widget


# class Page(Widget):
#     def create(self):
#         self._action('create Page')


class MultiPageView(Widget):
    def create(self):
        self._action('create MultiPageView')

    def set_top(self, page):
        pass
