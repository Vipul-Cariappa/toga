from .base import Widget


class Label(Widget):
    def __html__(self):
        return """
            <h4 id="toga_{id}" class="" style="{style}">
            {label}
            </h4>
        """.format(
            id=self.interface.id,
            label=self.interface.text,
            style='',
        )

    def __js__(self):
        return """
        console.log("Label Widget {id}")
        // JS associated with label goes here
        """.format(
            id=self.interface.id,
        )

    def create(self):
        pass

    def set_text(self, value):
        pass
