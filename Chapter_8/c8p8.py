# User Profile program, Chapter 8

def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Shailesh','Dwivedi',
                            location = 'Mumbai',
                            hometown = 'Varanasi',
                            graduation = 'Northeastern University')

print(user_profile)
