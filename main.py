from util import greet_user
from hello import greet_admin
def main():
    
    user_name="World"
    print(greet_user(user_name))
    admin_name="Alice"
    greet_admin(admin_name)

if __name__ == "__main__": \
    main()