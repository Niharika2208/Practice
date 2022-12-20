class Clock:
    def __init__(self, hours: int, minutes: int) -> None:
        self.hours = hours
        self.minutes = minutes

        # def normalize(self):
        hr = self.hours

        self.hours = hr + (self.minutes // 60)
        self.minutes = self.minutes % 60

        while self.hours >= 24:
            self.hours = self.hours - 24

        # print(self.hours, ":", "%02d" % self.minutes)

    def __eq__(self, other: object) -> bool:
        # if self and other are of different, incompatible types, they are not equal

        if not isinstance(other, Clock):
            return NotImplemented

        if isinstance(other, Clock):
            return self.hours == other.hours and self.minutes == other.minutes

    def __add__(self, other: "Clock") -> "Clock":
        Clock_hours = self.hours + other.hours
        Clock_minutes = self.minutes + other.minutes
        return Clock(Clock_hours, Clock_minutes)

    def add_minutes(self, minutes: int) -> "Clock":
        adding_minutes = self.minutes + minutes
        return Clock(self.hours, adding_minutes)

    def __str__(self) -> str:
        return 'Clock(hours = ' + str(self.hours) + ' ,minutes = ' + str(self.minutes) + ')'


if __name__ == "__main__":
    C1 = Clock(23, 103)
    # C1.normalize()
    C2 = Clock(7, 90)
    print(C1 == C2)
    C3 = C1 + C2
    # C3.normalize()
    print(C3.hours, C3.minutes)
    C4 = C1.add_minutes(45)
    print(C4.minutes)
    print(C4.__str__())
