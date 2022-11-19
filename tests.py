from datetime import datetime
import unittest

from date_time_span import DateTimeSpan


class DateTimeSpanAsHoursTests(unittest.TestCase):
    def test_as_hours(self):
        span = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )
        self.assertEquals(4.0, span.as_hours)


class DateTimeSpanTests(unittest.TestCase):
    def test_equals(self):
        span_1 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )

        span_2 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )
        self.assertEqual(span_1, span_2)

    def test_not_equals_start_date(self):
        span_1 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )

        span_2 = DateTimeSpan(
            datetime(2016, 3, 28, 1), datetime(2016, 3, 28, 4),
        )
        self.assertNotEqual(span_1, span_2)

    def test_not_equals_end_date(self):
        span_1 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )

        span_2 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 5),
        )
        self.assertNotEqual(span_1, span_2)

    def test_eq_logic(self):
        span_1 = DateTimeSpan(
            datetime(2016, 3, 27, 0), datetime(2016, 3, 27, 4),
        )

        span_2 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )

        self.assertNotEqual(span_1, span_2)


class DateTimeSpanTestsStrictlyWithin(unittest.TestCase):
    def test_is_strictly_within_pass(self):
        span_1 = DateTimeSpan(
            datetime(2016, 3, 28, 1), datetime(2016, 3, 28, 3),
        )

        span_2 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )

        self.assertTrue(span_1.is_strictly_within(span_2))

    def test_is_strictly_within_same_start(self):
        span_1 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 3),
        )

        span_2 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )

        self.assertFalse(span_1.is_strictly_within(span_2))

    def test_is_strictly_within_same_end(self):
        span_1 = DateTimeSpan(
            datetime(2016, 3, 28, 1), datetime(2016, 3, 28, 4),
        )

        span_2 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )

        self.assertFalse(span_1.is_strictly_within(span_2))

    def test_is_strictly_within_start_before(self):
        span_1 = DateTimeSpan(
            datetime(2016, 3, 28, 1), datetime(2016, 3, 28, 3),
        )

        span_2 = DateTimeSpan(
            datetime(2016, 3, 28, 2), datetime(2016, 3, 28, 4),
        )

        self.assertFalse(span_1.is_strictly_within(span_2))

    def test_is_strictly_within_end_after(self):
        span_1 = DateTimeSpan(
            datetime(2016, 3, 28, 1), datetime(2016, 3, 28, 4),
        )

        span_2 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 3),
        )

        self.assertFalse(span_1.is_strictly_within(span_2))

    def test_is_strictly_within_start_befor_and_end_after(self):
        span_1 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )

        span_2 = DateTimeSpan(
            datetime(2016, 3, 28, 1), datetime(2016, 3, 28, 3),
        )

        self.assertFalse(span_1.is_strictly_within(span_2))

    def test_is_strictly_within_start_and_end_exactly_same_time(self):
        span_1 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )

        span_2 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )

        self.assertFalse(span_1.is_strictly_within(span_2))

    def test_is_strictly_within_no_overlap(self):
        span_1 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )

        span_2 = DateTimeSpan(
            datetime(2016, 3, 28, 5), datetime(2016, 3, 28, 6),
        )
        self.assertFalse(span_1.is_strictly_within(span_2))


class DateTimeSpanTestsIntersects(unittest.TestCase):
    def test_intersects_pass(self):
        span_1 = DateTimeSpan(
            datetime(2016, 3, 28, 1), datetime(2016, 3, 28, 3),
        )

        span_2 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )

        self.assertTrue(span_1.intersects(span_2))
        self.assertTrue(span_2.intersects(span_1))

    def test_intersects_no_overlap(self):
        span_1 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )

        span_2 = DateTimeSpan(
            datetime(2016, 3, 28, 5), datetime(2016, 3, 28, 6),
        )
        self.assertFalse(span_1.intersects(span_2))
        self.assertFalse(span_2.intersects(span_1))

    def test_intersects_end_of_first_is_start_of_second(self):
        span_1 = DateTimeSpan(
            datetime(2016, 3, 28, 0), datetime(2016, 3, 28, 4),
        )

        span_2 = DateTimeSpan(
            datetime(2016, 3, 28, 4), datetime(2016, 3, 28, 6),
        )
        self.assertFalse(span_1.intersects(span_2))
        self.assertFalse(span_2.intersects(span_1))


if __name__ == '__main__':
    unittest.main()
