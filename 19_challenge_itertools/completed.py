from dataclasses import dataclass
from faker import Faker
import random

import itertools
import functools

@dataclass
class Person:
    name: str
    age: int
    city: str
    country: str


# Instantiate the Faker module
fake = Faker()

# List of possible countries
countries = [
    "UK",
    "USA",
    "Japan",
    "Australia",
    "France",
    "Germany",
    "Italy",
    "Spain",
    "Canada",
    "Mexico",
]

# Generate 1000 random Person instances
PERSON_DATA: list[Person] = [
    Person(fake.name(), random.randint(18, 70), fake.city(), random.choice(countries))
    for _ in range(1000)
]


def main() -> None:

    filtered_data = filter(lambda p : p.age >=21, PERSON_DATA)
    countries = map(lambda p:p.country, filtered_data)

    def acc(p:dict[str,int],n:str) -> dict[str,int]:
        if n in p.keys():
            p[n]+=1
        else:
            p[n]=1
        return p

    summary = functools.reduce(acc, countries, {})   

    print(summary)


if __name__ == "__main__":
    main()
