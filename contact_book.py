contact=[]

while True:
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. search Contact")
    print("4. Exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter name: ")
        phone=input("Enter phone number: ")
        email=input("Enter email: ")
        contact.append({"name":name,"phone":phone,"email":email})
    if choice==2:
        for c in contact:
            print("Name:",c["name"])
            print("Phone:",c["phone"])
            print("Email:",c["email"])
    if choice==3:
        search_name=input("Enter name to search: ")
        found=False
        for c in contact:
            if c["name"]==search_name:
                print("Name:",c["name"])
                print("Phone:",c["phone"])
                print("Email:",c["email"])
                found=True
                break
        if not found:
            print("Contact not found")
    if choice==4:
        break
    