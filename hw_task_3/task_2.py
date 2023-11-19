import random


class Person:

    def __init__(self, first_name, patronymic, last_name, age, gender):
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name
        self.age = age
        self.gender = gender


class Student(Person):

    def __init__(self, first_name, patronymic, last_name, age, gender, knowledge=None):
        if knowledge is None:
            knowledge = []
        self.knowledge = knowledge
        super().__init__(first_name, patronymic, last_name, age, gender)

    def __len__(self):
        return len(self.knowledge)

    def take(self, new_knowledge):
        self.knowledge.append(new_knowledge)

    def forget(self):
        forg_i = random.randrange(0, len(self.knowledge))
        self.knowledge.remove(self.knowledge[forg_i])


class Subjects:

    def __init__(self, *args):
        self.sub_list = [*args]

    def __len__(self):
        return len(self.sub_list)


class Teacher(Person):

    def __init__(self, first_name, patronymic, last_name, age, gender, taught_students=0):
        self.taught_students = taught_students
        super().__init__(first_name, patronymic, last_name, age, gender)

    def teach(self, subject, *students):
        for student in students:
            student.take(subject)
            self.taught_students += 1


edu_program = Subjects(
    "Python",
    "Version Control Systems",
    "Relational Databases",
    "NoSQL databases",
    "Message Brokers"
)

mar_ivanna = Teacher(
    "Мария",
    "Ивановна",
    "Иванова",
    30,
    "Женский"
)

vova = Student(
    "Владимир",
    "Юрьевич",
    "Морозов",
    5,
    "Мужской"
)
sasha = Student(
    "Александр",
    "Александрович",
    "Нестеров",
    20,
    "?"
)
masha = Student(
    "Мария",
    "Андреевна",
    "Шишкина",
    40,
    None
)
katya = Student(
    "Екатерина",
    "Максимовна",
    "Андреева",
    69,
    "Женский"
)

mar_ivanna.teach(edu_program.sub_list[0], vova, masha)
mar_ivanna.teach(edu_program.sub_list[1], vova, sasha, masha)
mar_ivanna.teach(edu_program.sub_list[2], katya)
mar_ivanna.teach(edu_program.sub_list[3], katya, masha, sasha)
mar_ivanna.teach(edu_program.sub_list[4], vova, sasha, masha, katya)

masha.forget()

print(f"Знания Вовы: {vova.knowledge}, {len(vova)}")
print(f"Знания Саша: {sasha.knowledge}, {len(sasha)}")
print(f"Знания Маши: {masha.knowledge}, {len(masha)}")
print(f"Знания Кати: {katya.knowledge}, {len(katya)}")

