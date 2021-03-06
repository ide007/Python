from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А', '7A']

mentor = ((name, klass) for (name, klass) in zip_longest(tutors, klasses))
print(type(mentor))

for i in mentor:
    print(i)

print(mentor, list(mentor)) # генератор истощен
