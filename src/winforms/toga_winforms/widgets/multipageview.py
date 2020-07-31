from toga_winforms.colors import native_color
from toga_winforms.libs import Point, Size, WinForms

from .base import Widget


class Page(Widget):
    def create(self):
        self.native = WinForms.Panel()
        self.native.interface = self.interface

    def set_bounds(self, x, y, width, height):
        if self.native:
            horizontal_shift = self.interface.style.padding_left
            horizontal_size_adjustment = self.interface.style.padding_right + horizontal_shift
            vertical_size_adjustment = self.interface.style.padding_bottom
            self.native.Size = Size(width + horizontal_size_adjustment, height + vertical_size_adjustment)
            self.width = width + horizontal_size_adjustment
            self.height = height + vertical_size_adjustment

            # The location should be 0, 0 to the parent WinForms.Panel
            self.native.Location = Point(0, 0)

    def set_background_color(self, value):
        if value:
            self.native.BackColor = native_color(value)


class MultiPageView(Widget):
    def create(self):
        self.native = WinForms.Panel()
        self.native.interface = self.interface
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)

    def set_top(self, page):
        for i in self.pages:
            if i == page:
                i.native.BringToFront()
                i.native.Visible = True
            else:
                i.native.Visible = False

    def set_background_color(self, value):
        if value:
            self.native.BackColor = native_color(value)
