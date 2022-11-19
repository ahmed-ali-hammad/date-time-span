from datetime import date, datetime, time, timedelta
from typing import Optional


class InvalidSpan(ValueError):
    pass


class DateTimeSpan(object):
    """
    Represents the period between two datetimes
    """

    @classmethod
    def from_day_and_times(
        cls, day: date, start_time: time, end_time: time
    ) -> 'DateTimeSpan':
        """
        Create a DateTimeSpan from passed date and times.
        """
        return cls(
            datetime.combine(day, start_time), datetime.combine(day, end_time)
        )

    def __init__(self, start_dt: datetime, end_dt: datetime):
        if end_dt < start_dt:
            raise InvalidSpan
        self.start_dt = start_dt
        self.end_dt = end_dt

    @property
    def as_timedelta(self) -> timedelta:
        return self.end_dt - self.start_dt

    @property
    def as_seconds(self) -> float:
        return self.as_timedelta.total_seconds()

    @property
    def as_hours(self) -> float:
        return self.as_seconds / 3600

    @property
    def is_instant(self) -> bool:
        return self.as_seconds == 0

    def is_strictly_within(self, other: 'DateTimeSpan') -> bool:
        """Return if self is within, and not touching either edge of, other."""
        return self.start_dt > other.start_dt and self.end_dt < other.end_dt

    def datetime_within(self, dt: datetime) -> bool:
        """Return whether the given datetime is within self."""
        return dt >= self.start_dt and dt < self.end_dt

    def intersects(self, other: 'DateTimeSpan') -> bool:
        """Return whether self and other overlap."""
        first, second = (
            (self, other) if self.start_dt < other.start_dt else (other, self)
        )
        return first.end_dt > second.start_dt

    def overlap(self, other: 'DateTimeSpan') -> Optional['DateTimeSpan']:
        """Return any part of self which is also in other."""
        if self.end_dt < other.start_dt or other.end_dt < self.start_dt:
            return None

        return DateTimeSpan(
            max(self.start_dt, other.start_dt), min(self.end_dt, other.end_dt)
        )

    def __eq__(self, other: 'DateTimeSpan') -> bool:
        return self.start_dt == other.start_dt and self.end_dt == other.end_dt
