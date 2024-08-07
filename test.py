import unittest
import Login
import Signup
import Person
from config import *

# test Unit


class TestLogin(unittest.TestCase):
    def test_checkinfo0(self):
        login = Login.Login("Nima", "5676")
        result = login.checkinfo()
        self.assertEqual(result, 0)

    def test_checkinfo1(self):
        login = Login.Login("Nima", "123")
        result = login.checkinfo()
        self.assertEqual(result, 1)

    def test_checkinfo2(self):
        login = Login.Login("z", "1234")
        result = login.checkinfo()
        self.assertEqual(result, -1)


class TestSignUp(unittest.TestCase):
    def test_insert1(self):
        signup = Signup.Signup("Test", "0914Test", "Test")
        result = signup.insert()
        self.assertEqual(result, 1)
        DatabaseTestRemove()

    def test_insert0(self):
        signup = Signup.Signup("Test", "", "Test")
        result = signup.insert()
        self.assertEqual(result, 0)

    def test_DuplicateUsernameCheck0(self):
        signup = Signup.Signup("Nima", "Test", "Test")
        result = signup.DuplicateUsernameCheck()
        self.assertEqual(result, 0)

    def test_DuplicateUsernameCheck1(self):
        signup = Signup.Signup("Test", "Test", "Test")
        result = signup.DuplicateUsernameCheck()
        self.assertEqual(result, 1)


class TestPerson(unittest.TestCase):
    def test_reserveremove0(self):
        person=Person.Person("Test","Test","Test")
        result=person.ReserveRemove("0")
        self.assertEqual(result, 0)
    def test_reserveremove1(self):
        TestReserveAdd()
        person=Person.Person("Test","Test","Test")
        

        
        
