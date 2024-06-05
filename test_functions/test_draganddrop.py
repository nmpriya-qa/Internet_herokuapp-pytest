from pagefunctions.DragAndDrop import DragAndDrop
import utilities.customlogger as lg
import pytest
import time


class TestDragAndDrop:
    log = lg.custom_logger()

    def test_drag_column_a_to_b(self, setup_browser):
        try:
            self.driver = setup_browser
            self.da = DragAndDrop(self.driver)
            self.da.go_to_drag_and_drop_page()
            time.sleep(2)
            self.da.drag_column_a_to_b()
            column_b_header = self.da.get_column_b_header()
            assert column_b_header == "A"
        except AssertionError as e:
            pytest.fail(f"failed with assertion error: {e}")
        except Exception as e:
            pytest.fail(f"Failed with other reason: {e}")
