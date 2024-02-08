def register_user():
    
    firt_name = input ('Enter first name: ')
    last_name = input ('Enter last name:  ')
    
    user_dict ={
      'user_name': first_name + last_name
      'user_email' :firt_name +'@gmail.com' 
      }
     return user_dict


  def  edit_user(user):
   if user ==   '':
        user = register_user()
	else:
		print('\n No user found')
	return user
