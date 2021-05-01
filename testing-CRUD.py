import unittest
import CRUD

class UserTestCase(unittest.TestCase):
    "Examples of unit testing"

    def test_get_user_by_email(self):
        assert CRUD.get_user_by_email("username0@gmail.com")==<User 0> 
    
    def test_get_user_by_username(self):
        assert CRUD.get_user_by_username("username0")==<User 0>

    def test_get_user_by_id(self):
        assert CRUD.get_user_by_id(4)==<User 4>


class UserTestCase(unittest.TestCase):
    def test_get_plant_by_plant_id(self):
        assert CRUD.get_plant_by_plant_id(3)==<UserPlant 3>

class UserTestCase(unittest.TestCase):
    def test_get_entry_by_id(2)==<GrowLog 2>

if __name__ == "__main__":
    # If called like a script, run our tests
    unittest.main()