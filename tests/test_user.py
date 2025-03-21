from lib.user import User

"""
we want to check the user object
can be constructed 
"""


def test_user_object():
    user = User(1, "test user", "1234pass")

    assert user.id == 1
    assert user.username == "test user"
    assert user.encrypted_password == "b3d34352fc26117979deabdf1b9b6354"


"""
user can be represented as a formatted 
string
"""


def test_repr_of_user_object():
    user = User(1, "test user", "1234pass")

    assert str(user) == "User(ID: 1, Username: test user, Encrypted Password: b3d34352fc26117979deabdf1b9b6354)"


"""
we want to check to matching user objects are equal
"""


def test_eq_of_user_object():
    user1 = User(1, "test user", "1234pass")
    user2 = User(1, "test user", "1234pass")

    assert user1 == user2
