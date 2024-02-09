
def register_user():
    user_dict = {}
    user_dict['user_name'] = input("Enter user name: ")
    user_dict['user_email'] = input("Enter user email: ")
    return user_dict

def edit_user(user_dict):
    if user_dict:
        print("Current user details:")
        print("User name:", user_dict['user_name'])
        print("User email:", user_dict['user_email'])
       
        choice = input("Do you want to edit user details? (yes/no): ").lower()
        if choice == 'yes':
            user_dict['user_name'] = input("Enter new user name: ")
            user_dict['user_email'] = input("Enter new user email: ")
            print("User details updated successfully!")
        else:
            print("No changes made.")
    else:
        print('No user found')

user = register_user()
edit_user(user)