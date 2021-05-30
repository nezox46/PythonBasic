tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

for _ in range(len(tutors) - len(klasses)):
    if len(tutors) - len(klasses) > 0:
        klasses.append(None)

generate = ((t, k) for t, k in zip(tutors, klasses))

print(type(generate))  # <class 'generator'>
print(*generate)
