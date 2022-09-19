class Person:
    def __init__(self,name,date):
        self.name = name
        self.date=date
    def date_int(self):
        lis = self.date.split("-")
        lis.reverse()
        return int("".join(lis))

person_list=[ Person(input(),input()) for i in range(2)]

if person_list[0].date_int() >=person_list[1].date_int():
    print(person_list[0].name)
else:
    print(person_list[1].name)

