from utils import greet_user

def main():
    
    """
    Run the program's main entry point: create a default user name ("World"), call greet_user(user_name), and print its returned greeting to standard output.
    
    This function has no return value; it performs the side effect of writing the greeting to stdout.
    """
    user_name="World"
    print(greet_user(user_name))

if __name__ == "__main__": \
    main()