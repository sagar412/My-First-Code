# Program for build person example, Chapter 8
def build_person(first_name,last_name,age=None):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

Sagar = build_person('Shailesh','Dwivedi','27')
Ruchi = build_person('Ruchika','Dwivedi', '25')
print(Sagar,Ruchi)
