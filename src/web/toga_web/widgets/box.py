from .base import Widget


class Box(Widget):
    def __html__(self):
        return """
            <div id="toga_{id}" class="container" style="{style}">
            {content}
            </div>
        """.format(
            id=self.interface.id,
            content="\n".join(
                child._impl.__html__()
                for child in self.interface.children
            ),
            style=''
        )

    def __js__(self):
        return """
        console.log("Box Widget {id}")
        // JS associated with box goes here
        {content}
        """.format(
            id=self.interface.id,
            content="\n".join(
                child._impl.__js__()
                for child in self.interface.children
            ),
        )

    def create(self):
        pass

    def add_child(self, child):
        pass
