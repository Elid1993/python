students={}
while True:
    name= input("Enter name( or type 'end' to stop):").strip().lower()
    if name == "end":
        break
    grade_input= input(f" enter grade for {name}:"). strip()
    try:
        grade= int(grade_input)
    except ValueError:
        print("grade has to be a number")
        continue
    students[name]= grade
print("\n final grade list:")
total=0
for name, grade in students.items():
    status= "pass" if grade>=10 else "fall"
    print(f" {name}, {grade}, {status}")
    total += grade
if len(students) > 0:
    average= total/len(students)
    print(f"\n average of class:{average:.2f}")
else:
    print("\n we have any number")
print("\n just pass students")
found= False
for name,grade in students.items():
    if grade >= 10:
        print(f"{name}, {grade}")
        found=True
if not found:
    print( " no one pass") 
with open("student2.txt", "w", encoding= "utf_8") as file:
    for name, grade in students.items():
        status= "pass" if grade>=10 else "fail"
        file.write(f" {name},{grade},{ status}\n")
print( information  in "student2.txt saved successfully")

        
    