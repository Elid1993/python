contacts=[]
def add_contact():
    name= input("enter contact name:").strip()
    phone = input ("enter phone number:").strip()
    contacts.append({"name":name,"phone": phone})
    print(f" contact added\n")
def show_contacts():
    if not contacts:
        print("we dont have contact\n")
        return
    print("\n list of contacts")
    for contact in contacts:
        print(f"{contact['name']}, {contact['phone']}")
    print()
def search_contact():
    keyword= input ("enter the name you looking for:").strip().lower()
    found= False
    for contact in contacts:
        if keyword in contact["name"].lower():
            print(f" {contact['name']}, {contact['phone']}")
            found= True
    if not found:
        print("contact not found\n")
def save_contacts():
        with open ("contacts.txt","w", encoding="utf-8")as file:
            for contact in contacts:
                file.write(f"{contact['name']}:{contact['phone']}\n")
        print( "contacts saved in file\n")
def edit_contacts():
    name= input("contact name you want to edit").strip()
    for contact in contacts:
        if contact["name"].lower()== name.lower():
            print(f"contact found: {contact['name']},{contact['phone']}")
            new_name=input("new name").strip()
            new_phone= input(" new phone").strip()
            if new_name:
                contact["name"]=new_name
            if new_phone:
                contact["phone"]= new_phone
            print("contact edited\n")
            return
    print( "contact not found\n")
def delete_contacts():
    name= input(" name that you want to delete").strip()
    for contact in contacts:
        if contact["name"].lower()== name.lower():
            contacts.remove(contact)
            print("contact was remove\n")
            return
    print("contact not found")  
import csv
def export_to_csv(filename="contacts.csv"):
    with open(filename,mode="w", newline='', encoding="utf-8") as file:
        writer=csv.writer(file)  
        writer.writerow(["name","phone"]) 
        for contact in contacts:
            writer.writerow ([contact["name"],contact["phone"]])   
    print(f"contacts saved succesfully") 
import shutil
def backup_file(source="contacts.csv", backup_name="contacts_backup.csv"):
    try:
        shutil.copy(source,backup_name)
        print(f"file  created with '{backup_name }'")
    except FileNotFoundError:
        print( "main file dose not exist ")   
import zipfile
def zip_backup(filename="contacts_backup.csv",zip_name="backup.zip"):
    try:
        with zipfile.Zipfile(zip_name,"w")as zipf:
            zipf.write(filename) 
            print(f"'{zip_name}'file created")
    except FileNotFoundError:
        print("backup file dose not found")
            
# def load_contacts():
#     try:
#         with open("contacts.txt","r",encoding="utf-8") as file:
#             for line in file:
#                 parts= line.strip().split(":")
#                 if len(parts)==2:
#                     name,phone= parts
#                     contacts.append({"name":name,"phone":phone})
#     except FileNotFoundError:
#         pass
    
# load_contacts()
        
    
while True:
    print( " number notebook")
    print("1. add contact")
    print("2. show contacts")
    print("3. search contacts")
    print("4. save_contacts")
    print("5. exit")
    print("6. edit contacts")
    print("7. delete contacts")
    print("8. export to csv")
    print("9. backup file")
    print("10. zip backup")
    choice= input( "our choice")
    if choice== "1":
        add_contact()
    elif choice=="2":
        show_contacts()
    elif choice == "3":
        search_contact()
    elif choice=="4":
        save_contacts()
    elif choice =="5":
        print("goodbye")
        break
    elif choice=="6":
        edit_contacts()
    elif choice == "7":
        delete_contacts()
    elif choice=="8":
        export_to_csv()
    elif choice=="9":
        backup_file()
    elif choice=="10":
        zip_backup()
    else:
        print(" invalid choice try again")
        