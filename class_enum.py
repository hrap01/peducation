# když chci uživatele svázat jen s pár možnostmi např. dny v týdnu

import enum

class Day(enum.Enum):
    MONDAY = 1 # MUZU DAT str a muze se i michat NEBO OPAKOVAT NALEVO
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    def is_weekend(self):
        return self in [Day.SATURDAY, Day.SUNDAY]



# def is_weekend(day: Day) -> bool:
#
#     if isinstance(day, Day) is False:
#         raise ValueError('Expected type is Day')
#
#     return day in [Day.SATURDAY, Day.SUNDAY]

my_day= Day(1)
print(my_day.is_weekend())
your_day = Day['SUNDAY']
print(your_day.is_weekend())

print(my_day is Day.MONDAY)
#print(is_weekend(Day.SATURDAY))
