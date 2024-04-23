from unittest.mock import Mock
from datetime import datetime

tuesday = datetime(year=2024, month=4, day=23)
print(tuesday)
sunday = datetime(year=2024, month=4, day=28)
print(sunday)

datetime = Mock()


def is_weekday():
    today = datetime.today()
    return 0 <= today.weekday() < 5


datetime.today.return_value = tuesday
print(datetime.today())
assert is_weekday(), "Not workday!"
datetime.today.return_value = sunday
print(datetime.today())
assert is_weekday(), "Not workday!"
