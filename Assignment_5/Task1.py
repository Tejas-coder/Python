dic = {"Michel": 90, "John": 89, "Samsung": 60, "Ronnie": 78}

studName = input(rf"Enter the student's name: ")
if studName in dic:
    print(rf"{studName}'s marks: {dic[studName]}")
else:
    print("Student not found.")