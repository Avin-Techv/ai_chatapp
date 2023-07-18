from rest_framework import APITestCase
from apps.users_management import User





class TestMosel(APITestCase):


    def test_creates_user(self):
        user=User.object.create_user('lekshmi','lekshmijayan@techversantinfotech.com','tech@123')
        self.assertIsInstance(user,User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email,'lekshmijayan@techversantinfotech.com')

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError,User.object.create_user,username = "",email='lekshmijayan@techversantinfotech.com',password='tech@123')
        
    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError,"The given username must be set"):
            User.object.create_user(username = '',email='lekshmijayan@techversantinfotech.com',password='tech@123')
        

    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError,User.object.create_user,username = "lekshmi",email='',password='tech@123')
        
    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError,"The given email must be set"):
            User.object.create_user(username = 'lekshmi',email='',password='tech@123')
        
    def test_creates_super_user_with_is_staff_status(self):
        with self.assertRaisesMessage(ValueError,"Superuser must have is_staff=True"):
            User.object.create_superuser(username = '',email='lekshmijayan@techversantinfotech.com',password='tech@123',is_staff=False)
    
    def test_creates_super_user_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError,"Superuser must have superuser=True"):
            User.object.create_superuser(username = '',email='lekshmijayan@techversantinfotech.com',password='tech@123',is_superuser=False)
            
    


    def test_creates_super_user(self):
        user=User.object.create_super_user('lekshmi','lekshmijayan@techversantinfotech.com','tech@123')
        self.assertIsInstance(user,User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email,'lekshmijayan@techversantinfotech.com')


    
