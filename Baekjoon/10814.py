
n = int(input())  # 온라인 저지 회원의 수


people = []

for i in range(n):
    age, name = input().split()
    member = {'age': int(age), 'name': name}
    people.append(member)

new_people = sorted(people, key=lambda x: x['age'])

for person in new_people:
    print(f"{person['age']} {person['name']}")
