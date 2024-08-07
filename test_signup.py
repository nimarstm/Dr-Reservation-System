from unittest.mock import MagicMock
from unittest.mock import MagicMock, patch
from Signup import Signup

@patch('Signup.Connection0')
def test_insert_success(mock_connection):
#Fake date base
    mock_cursor = MagicMock()
    mock_cursor.rowcount = 1
    mock_connection.return_value.cursor.return_value = mock_cursor

    signup = Signup("testuser", "1234567890", "password")

    result = signup.insert()

    assert result == 1
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO userinfo (Username, phonenumber, password) VALUES (%s, %s, %s)",
        ("testuser", "1234567890", "password")
    )
    mock_cursor.close.assert_called_once()
    mock_connection.return_value.close.assert_called_once()



@patch('Signup.Connection0')
def test_insert_failure(mock_connection):
    mock_cursor = MagicMock()
    mock_connection.return_value.cursor.return_value = mock_cursor

    signup = Signup("", "1234567890", "password")

    result = signup.insert()

    assert result == 0
    mock_cursor.execute.assert_not_called()
    mock_cursor.close.assert_not_called()
    mock_connection.return_value.close.assert_not_called()



@patch('Signup.Connection0')
def test_duplicate_username_check_found(mock_connection):
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = ('testuser',)
    mock_connection.return_value.cursor.return_value = mock_cursor

    signup = Signup("testuser", "1234567890", "password")

    result = signup.DuplicateUsernameCheck()

    assert result == 0
    mock_cursor.execute.assert_called_once_with(
        "SELECT Username FROM userinfo WHERE Username = %s LIMIT 1",
        ("testuser",)
    )



@patch('Signup.Connection0')
def test_duplicate_username_check_not_found(mock_connection):
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None
    mock_connection.return_value.cursor.return_value = mock_cursor

    signup = Signup("newuser", "1234567890", "password")

    result = signup.DuplicateUsernameCheck()

    assert result == 1
    mock_cursor.execute.assert_called_once_with(
        "SELECT Username FROM userinfo WHERE Username = %s LIMIT 1",
        ("newuser",)
    )
