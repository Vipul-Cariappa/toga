MultiPageView
=============

.. rst-class:: widget-support
.. csv-filter::
   :header-rows: 1
   :file: ../../data/widgets_by_platform.csv
   :included_cols: 4,5,6,7,8,9
   :exclude: {0: '(?!^(MultiPageView|Component)$)'}

.. |y| image:: /_static/yes.png
    :width: 16

A widget to group widgets into pages and show a single page at a time.

Usage
-----

.. code-block:: Python

    from toga Label, Button, MultiPageView

    # Creating MultiPanelWidget
    pageview = MultiPageView()

    # Creating first page
    page1 = pageview.create_page(
        children=[
            Label("Page 1"),
            Button("Click Me!", on_press=button1)
        ],
        style=Pack(
            direction=COLUMN,
        )
    )

    # Creating second page
    page2 = self.pageview.create_page(
        children=[
            Label("Page 2"),
            Button("Click Me!", on_press=button2),
        ],
        style=Pack(
            direction=COLUMN,
        )
    )

    def button1(self, widget):
        pageview.top(page2)
    
    def button2(self, widget):
        pageview.top(page1)

Reference
---------

.. autoclass:: toga.widgets.multipageview.MultiPageView
   :members:
   :undoc-members:
   :inherited-members:
