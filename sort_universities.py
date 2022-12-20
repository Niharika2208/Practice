import random
from operator import attrgetter


class University:
    def __init__(self, name: str, founding_year: int, country: str) -> None:
        self.name = name
        # TODO: Add the missing properties
        self.founding_year = founding_year
        self.country = country

    def __repr__(self) -> str:
        return repr((self.name, self.founding_year, self.country))


if __name__ == "__main__":
    tmp_list = list(range(1000))
    random.shuffle(tmp_list)
    # TODO: Get familiar with pythons `sort` and `sorted`. Play around a bit
    # with list `tmp_list` and print the results.
    tmp_list.sort()
    print(tmp_list)
    tmp_list.sort(reverse=True)
    print(tmp_list)

    # Stores universities in the format (name, founding year, country)
    universities = [
        ("Otto-von-Guericke-Universität Magdeburg", 1993, "Germany"),
        ("Harvard University", 1636, "USA"),
        ("Technische Universität München", 1868, "Germany"),
        ("RWTH Aachen", 1870, "Germany")
    ]

    # TODO: Sort universities by age
    print(sorted(universities, key=lambda year: year[1]))
    # print(sorted(universities, key=lambda niharika: niharika[1]))
    # print(universities)

    # TODO: Sort universities by name
    print(sorted(universities, key=lambda name: name[0]))
    # print(universities)
    universities.sort()
    print(universities)

    # Stores the universities as `University` objects
    university_objects = [University(name=u[0], founding_year=u[1], country=u[2]) for u in universities]

    # TODO: Sort university_objects by age
    print(sorted(university_objects, key=attrgetter('founding_year')))

    # TODO: Sort university_objects by name
    print(sorted(university_objects, key=attrgetter('name')))
