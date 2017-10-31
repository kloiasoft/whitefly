from unittest import TestCase
from whitefly.utils.linebuilder import LineBuilder


class TestLineBuilder(TestCase):
    def test_append_short_should_update_line_with_given_text_and_sixteen_column_length(self):
        line_builder = LineBuilder()
        line_builder.append_short("Test")
        self.assertEqual("Test            \t", line_builder.LINE)

    def test_append_long_should_update_line_with_given_text_and_forty_eight_column_length(self):
        line_builder = LineBuilder()
        line_builder.append_long("Test")
        self.assertEqual("Test                                            \t", line_builder.LINE)

    def test_append_should_update_line_with_given_text_and_given_column_length(self):
        line_builder = LineBuilder()
        line_builder.append(10, "Test")
        self.assertEqual("Test      \t", line_builder.LINE)

    def test_println_should_reset_the_line(self):
        line_builder = LineBuilder()
        line_builder.append(0, "Test")
        line_builder.println()
        self.assertEqual("", line_builder.LINE)

    def test_reset(self):
        line_builder = LineBuilder()
        line_builder.append(0, "Test")
        line_builder.reset()
        self.assertEqual("", line_builder.LINE)
