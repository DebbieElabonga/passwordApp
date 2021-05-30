import unittest
from user_accounts import userAccounts
from user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        '''
        Set method to run before test classes
        '''
        self.new_user = User('Debbie', 'Salano', 'Dee254', 'admin')

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_info =[]

    def test_init(self):
        '''
        function to test for initialization of variables
        '''
        self.assertEqual(self.new_user.first_name, 'Debbie')
        self.assertEqual(self.new_user.last_name, 'Salano')
        self.assertEqual(self.new_user.username, 'Dee254')
        self.assertEqual(self.new_user.password, 'admin')
    
    def test_save_user_info(self):
        '''
        Function that checks if user credentials are being saved
        '''
        User.save_user_info(self.new_user)
        self.assertEqual(len(User.user_info),1)
    def test_save_multiple_user(self):
        '''
        to check saving multiple users to our user_list is possible
        '''
        self.new_user.save_user_info()
        self.assertEqual(len(User.user_info),1)
    def test_user_exists(self):
        '''
        a test function that returns true or false to check if a certain user exists
        '''
        self.new_user.save_user_info()
        test_user = User("Test","user","6656","becken.jose@gmail.com")
        test_user.save_user_info()

        user_exists = User.user_exists("6656")

        self.assertTrue(user_exists)

    def test_get_user_info(self):
        '''
        function that allows the user to view their account details
        '''
        # User.save_user_info(self.new_user)
        self.new_user.save_user_info()
        user_account=User.get_user_info('Dee254')
        self.assertEqual(user_account.first_name,self.new_user.first_name)

    def test_user_login(self):
        User.save_user_info(self.new_user)
        self.assertTrue(User.user_login('Dee254','admin'))

    def test_delete_user_info(self):
        '''
        to test if we can remove user from our list
        '''
        self.new_user.save_user_info()
        self.new_user.delete_user_info() # Delete user
        self.assertEqual(len(User.user_info),0)

if __name__ == '__main__':
    unittest.main()