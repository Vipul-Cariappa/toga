from unittest.mock import patch

import toga
from toga.widgets.multipageview import Page
import toga_dummy
from toga_dummy.utils import TestCase


class MultiPageViewTests(TestCase):
    def setUp(self):
        super().setUp()

        self.pageview = toga.MultiPageView(factory=toga_dummy.factory)

    def test_widget_created(self):
        self.assertEqual(self.pageview._impl.interface, self.pageview)
        self.assertActionPerformed(self.pageview, 'create MultiPageView')

    # def test_set_top(self, page):
    #     pass
