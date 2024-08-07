import pytest
from unittest.mock import MagicMock
from Person import Person
import config
from datetime import date
from unittest.mock import MagicMock, patch
from Signup import Signup


@pytest.fixture
def person(monkeypatch):
    monkeypatch.setattr(config, 'Id0', 'test_user_id')
    return Person("testuser", "1234567890", "password")


def test_reserved_list_show(person, monkeypatch):
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        ("1", "Dr. Ali", "2024-08-08", "10:00")]
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    monkeypatch.setattr('Person.Connection0', lambda: mock_connection)

    reserve_list = person.ReservedListShow()

    assert reserve_list == [("1", "Dr. Ali", "2024-08-08", "10:00")]
    mock_cursor.execute.assert_called_once_with(
        "SELECT ID, drName, Date, Time FROM reserve_info WHERE userID = %s",
        ('test_user_id',)
    )


def test_reserve_remove(person, monkeypatch):
    mock_cursor = MagicMock()
    mock_cursor.rowcount = 1
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    monkeypatch.setattr('Person.Connection0', lambda: mock_connection)

    result = person.ReserveRemove('1')

    assert result == 1
    mock_cursor.execute.assert_called_once_with(
        "Delete From reserve_info Where ID=%s",
        ('1',)
    )


def test_change_field(person, monkeypatch):
    mock_cursor = MagicMock()
    mock_cursor.rowcount = 1
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    monkeypatch.setattr('Person.Connection0', lambda: mock_connection)

    result = person.ChangeField("Username", "newuser")

    assert result == 1
    mock_cursor.execute.assert_called_once_with(
        "UPDATE userinfo SET Username=%s WHERE ID=%s",
        ("newuser", 'test_user_id')
    )


def test_change_username(person, monkeypatch):
    mock_cursor = MagicMock()
    mock_cursor.rowcount = 1
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    monkeypatch.setattr('Person.Connection0', lambda: mock_connection)

    result = person.ChangeUsername("newuser")

    assert result == 1
    mock_cursor.execute.assert_called_once_with(
        "UPDATE userinfo SET Username=%s WHERE ID=%s",
        ("newuser", 'test_user_id')
    )


def test_change_phone_number(person, monkeypatch):
    mock_cursor = MagicMock()
    mock_cursor.rowcount = 1
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    monkeypatch.setattr('Person.Connection0', lambda: mock_connection)

    result = person.ChangePhoneNumber("0987654321")

    assert result == 1
    mock_cursor.execute.assert_called_once_with(
        "UPDATE userinfo SET PhoneNumber=%s WHERE ID=%s",
        ("0987654321", 'test_user_id')
    )


def test_change_password(person, monkeypatch):
    mock_cursor = MagicMock()
    mock_cursor.rowcount = 1
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    monkeypatch.setattr('Person.Connection0', lambda: mock_connection)

    result = person.ChangePassword("newpassword")

    assert result == 1
    mock_cursor.execute.assert_called_once_with(
        "UPDATE userinfo SET Password=%s WHERE ID=%s",
        ("newpassword", 'test_user_id')
    )


def test_show_doctor_name(person, monkeypatch):
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        ("1", "Dr. Ali", "2024-08-08", "10:00")]
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    monkeypatch.setattr('Person.Connection0', lambda: mock_connection)

    drlist = person.ShowDoctorName("Dermotologist")

    assert drlist == ["Dr. Ali"]
    mock_cursor.execute.assert_called_once_with(
        "Select * From drinfo Where Expert=%s and Date>=%s and Capacity>0 ",
        ("Dermotologist", str(date.today()))
    )


def test_show_doctor_date(person, monkeypatch):
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        ("1", "Dr. Ali", "Dermotologist", "2024-08-08", "10:00")]
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    monkeypatch.setattr('Person.Connection0', lambda: mock_connection)

    drdate = person.ShowDoctorDate("Dermotologist", "Dr. Ali")

    assert drdate == ["2024-08-08"]
    mock_cursor.execute.assert_called_once_with(
        "Select * From drinfo Where Expert=%s and Date>=%s and Capacity>0 and Name=%s ",
        ("Dermotologist", str(date.today()), "Dr. Ali")
    )


def test_show_doctor_time(person, monkeypatch):
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [
        ("1", "Dr. Ali", "Dermotologist", "2024-08-08", "10:00")]
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    monkeypatch.setattr('Person.Connection0', lambda: mock_connection)

    drtime = person.ShowDoctorTime("Dermotologist", "Dr. Ali", "2024-08-08")

    assert drtime == ["10:00"]
    mock_cursor.execute.assert_called_once_with(
        "Select * From drinfo Where Expert=%s and Date>=%s and Capacity>0 and Name=%s and Date=%s",
        ("Dermotologist", str(date.today()), "Dr. Ali", "2024-08-08")
    )


def test_submit_reserve(person, monkeypatch):
    mock_cursor = MagicMock()
    mock_cursor.rowcount = 1
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    monkeypatch.setattr('Person.Connection0', lambda: mock_connection)

    result = person.SubmitReserve(
        "Dermotologist", "Dr. Ali", "2024-08-08", "10:00")

    assert result == 1
    mock_cursor.execute.assert_called_once_with(
        "UPDATE drinfo SET Capacity=%s WHERE Expert=%s and Name=%s and Date=%s and Time=%s",
        (0, "Dermotologist", "Dr. Ali", "2024-08-08", "10:00")
    )


def test_add_to_reserve_info(person, monkeypatch):
    mock_cursor = MagicMock()
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor

    monkeypatch.setattr('Person.Connection0', lambda: mock_connection)

    person.AddtoReserveInfo("Dr. Ali", "2024-08-08", "10:00")

    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO reserve_info (drName, userID, Date, Time) VALUES (%s, %s, %s,%s)",
        ("Dr. Ali", 'test_user_id', "2024-08-08", "10:00")
    )
