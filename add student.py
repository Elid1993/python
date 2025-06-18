students = {}
def add_student():
    name = input(" name of student:").strip()
    grade_input= input( "grade:").strip()
    try:
        grade= int(grade_input)
    except ValueError:
        print( " grade has to be a number")
        return 
    students[name]= grade
    print( "student added \n")
def show_students():
    if not students:
        print(" we have no student \n")
        return
    for name, grade in students.items():
        status= "pass " if grade >=10 else "fail"
        print (f" {name}: {grade}({ status})")
    print()
def save_to_file():
    with open ( "student.txt","w", encoding= "utf-8") as file:
        for name,grade in students.items():
            status = "pass " if grade >=10 else "fail"
            file.write(f" {name}:{grade}({status})\n")
    print( "informatin saved in 'student.txt' .\n")
while True:
    print ("menu:")
    print( "1. add student")
    print(" 2. show students")
    print(" 3. save in file")
    print(" 4. exit")
    choice = input (" your choice (1-4):").strip()
    if choice== "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice=="3":
        save_to_file()
    elif choice == "4":
        print("goodbye")
        break
    else:
        print (" invalid choice. try again\n")