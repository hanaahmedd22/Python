import re
from datetime import datetime
users=[]
projects=[]
def register():
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    phone_pattern = r"^01[0-2,5]{1}[0-9]{8}$"


    print("Welcome to the registration page!")
    while True:
        first_name = input("Enter your first name: ")
        if first_name.isalpha() == True:
            break
        else:
            print("First name should contain only alphabets. Please try again.")
    
    
    while True:
        last_name = input("Enter your last name: ")
        if last_name.isalpha() == True:
            break
        else:
            print("Last name should contain only alphabets. Please try again.")
    
    
    while True:
        email = input("Enter your email: ")
        if  re.match(email_pattern, email):
            break
        else:
            print("Invalid email! Please try again.")


    while True:
        mobile_number = input("Enter your mobile number: ")
        if re.match(phone_pattern, mobile_number):
            break
        else:
            print("Invalid mobile number! Please try again.")
            

    while True:
        
        password = input("Enter your password: ")
        if len(password) < 6:
            print("Password should contain at least 6 characters. Please try again.")
            continue
            
        confirm_password = input("Confirm your password: ")
        if password == confirm_password:
            print("You have successfully registered!")
            break
        else:
            print("Passwords do not match. Please try again.")
    users.append({"first_name": first_name, "last_name": last_name, "email": email, "mobile_number": mobile_number, "password": password})
    print(users)
    return
def login():

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    print("Welcome to the login page!")
    while True: 
        email = input("Enter your email: ")
        if re.match(email_pattern, email):
            break
        else:
            print("Invalid email! Please try again.")
    while True:
        password = input("Enter your password: ")
        if len(password) < 6:
            print("Password should contain at least 6 characters. Please try again.")
        else:
            break
        
    for user in users:
        if user["email"] == email and user["password"] == password:
            print("You have successfully logged in!")
            return user
    else:
        print("Invalid email or password! Please try again.")
    return 

def create(user):

    format = "%d-%m-%Y"

    print("Welcome to the create project page!")
    project_title = input("Enter the name of your project: ")
    project_details = input("Enter the details of your project: ")
    total_target = input("Enter the total target amount: ")
    today = datetime.today().strftime(format)
    
    while True:
        start_date = input("Enter the start date of your project:(DD-MM-YYYY) ")
        try:
            sdate=datetime.strptime(start_date, format).date()
            if sdate < today:
                print("Start date should be greater than or equal to today's date. Please try again.")
                continue
            else:   
                break
        except ValueError:
            print("Invalid date format! Please try again.")
    while True:
        end_date = input("Enter the end date of your project:(DD-MM-YYYY) ")
        try:
            edate=datetime.strptime(end_date, format).date()
            if edate < start_date:
                print("End date should be greater than or equal start date. Please try again.")
                continue
            else:
                break
        except ValueError:
            print("Invalid date format! Please try again.")
    projects.append({"project_title": project_title, "project_details": project_details, "total_target": total_target, "start_date": start_date, "end_date": end_date, "created_by": user["email"]})

def view_projects(user):
    flag=True
    if len(projects) == 0:
        print("No projects available!")
        return
    for project in projects:
        if project["created_by"] == user["email"]:
            print(project)
            flag=False

    if flag:
        print("No projects available!")
    return
def delete_project(user):
    project_title = input("Enter the name of the project you want to delete: ")
    for project in projects:
        if project["project_title"] == project_title and project["created_by"] == user["email"]:
            projects.remove(project)
            print("Project deleted successfully!")
            return
    else:
        print("Project not found!")
    return
def update_project(user):
    project_title = input("Enter the name of the project you want to update: ") 
    for project in projects:
        if project["project_title"] == project_title and project["created_by"] == user["email"]:
            print("Enter the new details of the project:")
            project_details = input("Enter the details of your project: ")
            total_target = input("Enter the total target amount: ")
            projects.remove(project)
            projects.append({"project_title": project_title, "project_details": project_details, "total_target": total_target, "start_date": project["start_date"], "end_date": project["end_date"], "created_by": user["email"]})
            print("Project updated successfully!")
            return
    else:
        print("Project not found!")
    return
def search_by_date(user):
    format = "%d-%m-%Y"
    if len(projects) == 0:
        print("No projects available!")
        return
    while True:
        start_date = input("Enter the start date of your project:(DD-MM-YYYY) ")
        try:
            datetime.strptime(start_date, format)
            break
        except ValueError:
            print("Invalid date format! Please try again.")
    while True:
        end_date = input("Enter the end date of your project:(DD-MM-YYYY) ")
        try:
            datetime.strptime(end_date, format)
            break
        except ValueError:
            print("Invalid date format! Please try again.")
    flag=True
    
    for project in projects:
        if project["start_date"] == start_date and project["end_date"] == end_date:
            print(project)
            flag=False
    if flag:
        print("No projects available!")
    return

    
        
    


def main():
    while True:
        print("Welcome to the crowd funding app!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if isinstance(choice, int) and choice>0 and choice<4:
                    break
                else:
                    print("Invalid choice! Please try again.")
            except ValueError:
                print("Invalid choice! Please try again.")
        match choice:
            case 1:
                register()
            case 2:
                user = login()
                if user:
                    while True:
                        print("1. Create a project")
                        print("2. View your projects")
                        print("3. Delete a project")
                        print("4. Update a project")
                        print("5. Search projects by date")
                        print("6. Logout")
                        while True:
                            try:
                                choice = int(input("Enter your choice: "))
                                if choice>0 and choice<7:
                                    break
                                else:
                                    print("Invalid choice! Please try again.")
                            except ValueError:
                                print("Invalid choice! Please try again.")
                        match choice:
                            case 1:
                                create(user)
                            case 2:
                                view_projects(user)
                            case 3:
                                delete_project(user)
                            case 4:
                                update_project(user)
                            case 5:
                                search_by_date(user)
                            case 6:
                                break
            case 3:
                print("Thank you for using the crowd funding app!")
                break

main()