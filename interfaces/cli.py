from cmd import Cmd
import sys

from models.admin import Admin
from models.user import User
from models.volunteer import Volunteer

class EmsShell(Cmd):
    """
    EmsShell is the main class for the command line interface.
    """

    def __init__(self, user=None) -> object:
        super().__init__()
        self.user = user
        if user != None:
            self.prompt = f'{user.username} ({user.__class__.__name__}) > '

    def login(self) -> None:
        """
        Prompts the user for a username and password to login to EMS.
        Loop until the user enters a valid username and password.
        """
        from interfaces.admin_cli import AdminShell
        from interfaces.volunteer_cli import VolunteerShell

        while self.user is None:
            username = input('Username: ')
            password = input('Password: ')
            try:
                user = User.find(username)
                if not user:
                    print("\033[31m {}\033[00m".format('** User not found'))
                    continue
                self.user = user.login(password)
                self.prompt = f'{self.user.username}> '
                print(f'Welcome {self.user.username}. Your role is {self.user.__class__.__name__}.\n')
                if isinstance(self.user, Admin):
                    AdminShell(self.user).cmdloop()
                elif isinstance(self.user, Volunteer):
                    VolunteerShell(self.user).cmdloop()
            except (KeyError, User.InvalidPassword):
                print("\033[31m {}\033[00m".format("** Invalid username or password. Please try again."))

    def do_logout(self, args):
        """
        Logout the current user, prompting for a new username and password.
        """
        self.user = None
        print('Logged out. Re-log in to continue')
        self.login()

    def preloop(self) -> None:
        """
        Ask the user to login before entering the shell.
        """
        print("\033[96m{}\033[0m".format("Welcome to EMS, please enter your details."))
        self.login()

    def do_exit(self, arg):
        print(f'\nThank you for using EMS. Bye bye!')
        sys.exit()
