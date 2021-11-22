from cmd import Cmd

from data.users import users_catalog
from models.user import User


class EmsShell(Cmd):
    """
    EmsShell is the main class for the command line interface.
    """
    action_words = ['create']  # prefix words for two-word commands
    user: User = None

    def login(self) -> None:
        """
        Prompts the user for a username and password to login to EMS.
        Loop until the user enters a valid username and password.
        """
        while self.user is None:
            username = input('Username: ')
            password = input('Password: ')
            try:
                self.user = users_catalog[username].login(password)
                self.prompt = f'{self.user.username}> '
                print(f'Welcome {self.user.username}')
            except (KeyError, User.InvalidPassword):
                print('Invalid username or password. Please try again.')

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
        print('Welcome to EMS, please login.')
        self.login()

    def precmd(self, line: str) -> str:
        """
        Handles two-word commands made with action words
        """
        for action_word in self.action_words:
            if line.startswith(action_word + ' '):
                return action_word + '_' + line[len(action_word) + 1:]
            elif line.startswith('help ' + action_word + ' '):
                return 'help ' + action_word + '_' + line[len(action_word) + 6:]
        return line

    def do_profile(self, arg):
        """
        Print user info
        """
        print(f'username: {self.user.username}\n'
              f'role: {self.user.__class__.__name__}')

