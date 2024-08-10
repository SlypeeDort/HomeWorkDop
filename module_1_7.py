from statistics import mean
# from statistics import mean
# как понимаю библеотека для работы mean
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
print(students)
dictionary = {}
# len определяет количество элементов
# range позволяет запастить  список нужное количество раз (в данном случае = длине списка grades
# mean среднее
for i in range(len(grades)):
    grades[i] = mean(grades[i])
    dictionary[students[i]] = grades[i]

print(dictionary)