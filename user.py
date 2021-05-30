import pyperclip

class User:
    '''
    Class that allows the users to create their login details
    '''
    user_info = []
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def save_user_info(self):
        '''
        function that appends user login info
        '''
        self.user_info.append(self)

    def delete_user_info(self):

        '''
        deletes user from list
        '''

        User.user_info.remove(self)

    @classmethod
    def find_by_password(cls, password):
        '''
        Method that takes in a password and returns user that match the password
        Args:
            password: pass to search
        Returns :
            user
        '''

        for user in cls.user_info:
            if user.password == password:
                return user

    @classmethod
    def user_exists(cls,username):
        '''
        a class function that checks if a certain user with the inputted username exists and returns true or false
        '''
        for user in cls.user_info:
            if user.username==username:
                return True
        return False
    @classmethod
    def display_users(cls):
        '''
        shows the user list
        '''
        return cls.user_info

    @classmethod
    def get_user_info(cls,username):
        '''
        function that allows users to view their account details
        '''
        for user in cls.user_info:
            if user.username == username:
                return user
    
    @classmethod
    def user_login(cls,username,password):
        '''
        function that checks if the username of a registered account equals the inputted password
        '''
        if cls.get_user_info(username).password == password:
            return True
        return False

    @classmethod
    def copy_username(cls,password):
        user_found = User.find_by_password(password)
        pyperclip.copy(user_found.username)
