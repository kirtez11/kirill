grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron' }
df = sorted(list(students))
rik = {}
for i in range(len(grades)):
    rik[df[i]] = sum(grades[i]) / len(grades[i])
print(rik)