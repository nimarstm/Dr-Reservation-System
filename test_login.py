from unittest.mock import MagicMock, patch
from Login import Login
import config

# Peron Fake class
class FakePerson:
    def __init__(self, username, password, phone_number):
        self.username = username
        self.password = password
        self.phone_number = phone_number

    def ReservedListShow(self):
        return []  


@patch('Login.Connection0')
@patch('Login.Person', new=FakePerson)  
def test_checkinfo_success(mock_connection):
    #Fake Data base
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (1, 'testuser', '1234567890', 'password')
    mock_connection.return_value.cursor.return_value = mock_cursor

    config.person_list = []

    login = Login("testuser", "password")

    result = login.checkinfo()

    assert result == 1
    assert len(config.person_list) == 1
    assert isinstance(config.person_list[0], FakePerson)
    assert config.person_list[0].username == "testuser"
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM userinfo WHERE Username = %s",
        ("testuser",)
    )
    mock_cursor.close

@patch('Login.Connection0')
@patch('Login.Person', new=FakePerson)  
def test_checkinfo_wrong_password(mock_connection):
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = (1, 'testuser', '1234567890', 'wrongpassword')
    mock_connection.return_value.cursor.return_value = mock_cursor

    config.person_list = []

    login = Login("testuser", "password")

    result = login.checkinfo()

    assert result == 0
    assert len(config.person_list) == 0
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM userinfo WHERE Username = %s",
        ("testuser",)
    )
    mock_cursor.close

@patch('Login.Connection0')
@patch('Login.Person', new=FakePerson)  
def test_checkinfo_no_record(mock_connection):
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_connection.return_value.cursor.return_value = mock_cursor

    config.person_list = []

    login = Login("nonexistentuser", "password")

    result = login.checkinfo()

    assert result == -1
    assert len(config.person_list) == 0
    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM userinfo WHERE Username = %s",
        ("nonexistentuser",)
    )
    mock_cursor.close.assert_called_once()

