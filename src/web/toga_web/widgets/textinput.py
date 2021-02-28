from .base import Widget


class TextInput(Widget):
    def __html__(self):
        return """
            <input id="toga_{id}" class="" style="{style}">
        """.format(
            id=self.interface.id,
            style='',
        )

    def __js__(self):
        return """
        console.log("TextInput Widget {id}")
        // JS associated with textinput goes here
        """.format(
            id=self.interface.id,
        )

    def create(self):
        pass

    def set_value(self, value):
        pass

    def get_value(self):
        pass

    def set_enabled(self, value):
        pass

    def set_on_change(self, handler):
        pass

    def set_placeholder(self, value):
        pass

    def set_readonly(self, value):
        pass

    def set_on_gain_focus(self, handler):
        pass

    def set_on_lose_focus(self, handler):
        pass

    def clear_error(self):
        pass

    def set_error(self, error_message):
        pass
