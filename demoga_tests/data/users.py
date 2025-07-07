import dataclasses
import enum
from enum import Enum
from datetime import datetime


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class Hobbies(Enum):
    SPORTS = "Sports"
    READING = "Reading"
    MUSIC = "Music"


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: enum
    mobile: str
    date_of_birth: datetime
    subjects: str
    hobbies: enum
    picture: str
    current_address: str
    state: str
    city: str


student = User(first_name='Фамилия',
               last_name='Имя',
               email='address@mail.ru',
               gender=Gender.FEMALE.value,
               mobile='81234567890',
               date_of_birth=datetime(1991, 9, 15),
               subjects='Commerce',
               hobbies=Hobbies.MUSIC.value,
               picture='img.jpg',
               current_address='г. Москва, ул. Шарикоподшипниковская, 13c33',
               state='Haryana',
               city='Panipat'
               )