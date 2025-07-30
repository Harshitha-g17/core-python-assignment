def calculate_avg(students):
    average = {
        name: round(sum(marks) / len(marks), 2)
        for name, marks in students.items()
    }
    print(f"Average Marks:{average}")
    return average
def top_performer(average):
    print(f"Top performer:{max(average,key=average.get)}")
students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
average=calculate_avg(students)
top_performer(average)
