import dataclasses

@dataclasses.dataclass
class UserSimpl:
    name: str
    email: str
    current_address: str
    permanent_address: str

student_simpl = UserSimpl(name='Июньский Июнь Июнович',
               email='address@mail.ru',
               current_address='г. Петропавловск-Камчатский, ул. Озерновская Коса, 3/5',
               permanent_address='г. Москва, ул. Шарикоподшипниковская, 13c33',
               )