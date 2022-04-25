#!/usr/bin/python3

import sys
import inspect
import libuser
from pathlib import Path

path = Path(__file__)
path = str(Path(str(path).replace(str(path.name), "")).parent) + "/src/"
sys.path.append(path)

from pyUser import User, Group

def print_success(method):
    """
    @brief print_success Prints success messages for successful tests.
    """
    print("Test: '{method}' report: 'success'".format(method = method))

def expect_eq(expected, actual):
    """
    @brief expect_eq Raises an exception if the given values do not match.

    @param expected The expected value
    @param actual The actual value
    """
    if not expected == actual:
        raise Exception("Expected '{actual}' to be equal to '{expected}'"
                .format(actual = actual, expected = expected))

def expect_true(actual):
    """
    @brief expect_true Expects the given value to be True.

    @param actual The value to be verified
    """
    expect_eq(True, actual)

def expect_false(actual):
    """
    @brief expect_false Expects the given value to be False.

    @param actual The value to be verified
    """
    expect_eq(False, actual)

def does_user_exist(user):
    """
    @brief does_user_exist Verifies that the given user does exist.

    @return Returns true if the user exists
    """
    path = Path("/etc/passwd")
    with path.open("r") as file:
        for line in file:
            if user.get_name() in line:
                return True
    return False

def does_group_exist(group):
    """
    @brief does_group_exist Verifies that the given group does exist.

    @return Returns true if the group exists
    """
    path = Path("/etc/group")
    with path.open("r") as file:
        for line in file:
            if group.get_name() in line:
                return True
    return False

def test_find_user():
    """
    @brief test_find_user Verify that an existing user can be found.
    """
    user = User.by_name("root")
    user.print()
    expect_eq("root", user._name)
    expect_eq(0, user._uid)
    expect_eq(0, user._gid)
    expect_eq("/root", user._home)
    expect_eq("/bin/bash", user._loginshell)
    print_success(inspect.stack()[0][3])

def test_list_users():
    """
    @brief test_list_users Verify that all system users are found
    """
    users = User.list()
    count = 0
    path = Path("/etc/passwd")
    with path.open("r") as file:
        for line in file:
            count += 1
    expect_eq(len(users), count)

def test_create_user():
    """
    @brief test_create_user Verify that a new user can be created.
    """
    user = User.by_name("__piraidbay")
    if user.is_valid():
        user.delete()

    user = User.create("__piraidbay")
    expect_eq("__piraidbay", user._name)
    expect_eq("/home/__piraidbay", user._home)
    expect_true(User.by_name("__piraidbay").is_valid())
    expect_true(Path(user._home).exists())
    expect_true(Path(user._home).is_dir())
    expect_true(does_user_exist(user))
    user.delete()
    print_success(inspect.stack()[0][3])

def test_create_user_no_home():
    """
    @brief test_create_user Verify that a new user can be created without home directory.
    """
    user = User.by_name("__piraidbay")
    if user.is_valid():
        user.delete()

    user = User.create("__piraidbay", create_home = False)
    expect_eq("__piraidbay", user._name)
    expect_true(User.by_name("__piraidbay").is_valid())
    expect_false(user.has_home())
    expect_false(Path(user._home).exists())
    expect_false(Path(user._home).is_dir())
    expect_true(does_user_exist(user))
    user.delete()
    print_success(inspect.stack()[0][3])

def test_delete_user():
    """
    @brief test_delete_user Verify that an existing user can be deleted.
    """
    user = User.by_name("__piraidbay")
    if user.is_valid():
        user.delete()

    user = User.create("__piraidbay")
    expect_eq("__piraidbay", user._name)
    expect_eq("/home/__piraidbay", user._home)
    expect_true(user.delete())
    expect_eq(False, User.by_name("__piraidbay").is_valid())
    print_success(inspect.stack()[0][3])

def test_remove_home():
    """
    @brief test_remove_home Verify that the users home directory can be removed.
    """
    user = User.by_name("__piraidbay")
    if user.is_valid():
        user.delete()

    user = User.create("__piraidbay")
    expect_eq("__piraidbay", user._name)
    expect_eq("/home/__piraidbay", user._home)
    expect_true(user.has_home())
    expect_true(user.remove_home())
    expect_false(user.has_home())
    expect_false(Path(user._home).exists())
    user.delete()
    expect_false(Path(user._home).exists())
    print_success(inspect.stack()[0][3])

def test_add_user_home():
    """
    @brief test_add_user_home Verifies that an user can be created with a special home folder.
    """
    expect_false(Path("/tmp/__piraidbay").exists())
    user = User.by_name("__piraidbay")
    if user.is_valid():
        user.delete()

    user = User.create("__piraidbay", "/tmp/__piraidbay")
    expect_eq("__piraidbay", user._name)
    expect_eq("/tmp/__piraidbay", user._home)
    expect_true(Path("/tmp/__piraidbay").exists())
    user.delete()
    print_success(inspect.stack()[0][3])

def test_create_user_home():
    """
    @brief test_create_user_home Verifies that a home folder can be added to a user.
    """
    user = User.by_name("__piraidbay")
    if user.is_valid():
        user.delete()

    user = User.create("__piraidbay", create_home = False)
    expect_eq("__piraidbay", user._name)
    expect_eq("/home/__piraidbay", user._home)
    expect_false(Path("/home/__piraidbay").exists())
    expect_false(user.has_home())
    expect_true(user.create_home())
    expect_true(Path("/home/__piraidbay").exists())
    expect_true(user.has_home())
    user.delete()
    expect_false(Path("/home/__piraidbay").exists())
    print_success(inspect.stack()[0][3])

def test_create_user_home_exists():
    """
    @brief test_create_user_home_exists Verifies that the home folder can be set for an user
    with an existing home folder.
    """
    user = User.by_name("__piraidbay")
    if user.is_valid():
        user.delete()

    user = User.create("__piraidbay", create_home = True)
    expect_eq("__piraidbay", user._name)
    expect_eq("/home/__piraidbay", user._home)
    expect_true(Path("/home/__piraidbay").exists())
    expect_true(user.has_home())
    expect_true(user.create_home())
    expect_true(Path("/home/__piraidbay").exists())
    expect_true(user.has_home())
    user.delete()
    print_success(inspect.stack()[0][3])

def test_create_user_home_replace():
    """
    @brief test_create_user_home_replace Verify that the home folder can be replaced.
    """
    user = User.by_name("__piraidbay")
    if user.is_valid():
        user.delete()

    user = User.create("__piraidbay", create_home = True)
    expect_eq("__piraidbay", user._name)
    expect_eq("/home/__piraidbay", user._home)
    expect_true(Path("/home/__piraidbay").exists())
    expect_true(user.has_home())
    # TODO: implement
    expect_true(user.create_home())
    expect_true(Path("/home/__piraidbay").exists())
    expect_true(user.has_home())
    user.delete()
    print_success(inspect.stack()[0][3])

def test_delete_user_not_exists():
    """
    @brief test_delete_user_not_exists Verify that trying to remove a nonexistent user
    does not result in an error
    """
    userList = User.list()
    user = User(None)
    user.delete()
    expect_eq(len(userList), len(User.list()))
    user._uuid = 1334
    user.delete()
    expect_eq(len(userList), len(User.list()))
    print_success(inspect.stack()[0][3])

def test_change_user_name():
    """
    @brief test_create_user_home_replace Verify that the home folder can be replaced.
    """
    user = User.by_name("__piraidbay")
    if user.is_valid():
        user.delete()

    user = User.create("__piraidbay", create_home = True)
    expect_true(does_user_exist(user))
    expect_eq("__piraidbay", user._name)
    expect_eq("/home/__piraidbay", user._home)
    expect_true(Path("/home/__piraidbay").exists())
    user._name = "__pyraidbay"
    expect_true(user.update())
    expect_true(does_user_exist(user))
    expect_eq("/home/__piraidbay", user._home)
    expect_true(user.has_home())
    user.delete()
    print_success(inspect.stack()[0][3])

def test_find_group():
    """
    @brief test_find_group Verify that an existing group can be found.
    """
    group = Group.by_name("root")
    expect_eq("root", group._name)
    expect_eq(0, group._gid)
    expect_eq([], group._admin)
    expect_eq([], group._members)
    print_success(inspect.stack()[0][3])

def test_list_groups():
    """
    @brief test_list_groups Verify that all groups are listed.
    """
    groups = Group.list()
    count = 0
    path = Path("/etc/group")
    with path.open("r") as file:
        for line in file:
            count += 1
    expect_eq(len(groups), count)
    print_success(inspect.stack()[0][3])

def test_create_group():
    """
    @brief test_create_group Verify that a new group can be created.
    """
    group = Group.by_name("__piraidbay")
    if group.is_valid():
        group.delete()

    group = group.create("__piraidbay")
    expect_eq("__piraidbay", group._name)
    expect_true(Group.by_name("__piraidbay").is_valid())
    expect_true(does_group_exist(group))
    group.delete()
    print_success(inspect.stack()[0][3])

def test_delete_group():
    """
    @brief test_delete_group Verify that an existing group can be deleted.
    """
    group = Group.by_name("__piraidbay")
    if group.is_valid():
        group.delete()

    group = Group.create("__piraidbay")
    expect_eq("__piraidbay", group._name)
    expect_true(group.delete())
    expect_eq(False, Group.by_name("__piraidbay").is_valid())
    print_success(inspect.stack()[0][3])

def test_list_members():
    """
    @brief test_list_members Verify that all group members are listed.
    """
    group = Group.by_name("sudo")
    userNames = group.get_user_names()
    expect_eq(True, "root" in userNames or "pi" in userNames)
    print_success(inspect.stack()[0][3])

def test_add_member():
    """
    @brief test_delete_group Verify that an existing group can be deleted.
    """
    user_name = "__piraidbay1"
    group = Group.by_name("__piraidbay_members")
    if group.is_valid():
        group.delete()
    user = User.by_name(user_name)
    if user.is_valid():
        user.delete()

    group = Group.create("__piraidbay_members")
    user = User.create(user_name)
    group.add_member(user)
    expect_eq(True, user_name in group.get_user_names())
    group.delete()
    user.delete()
    print_success(inspect.stack()[0][3])

def test_change_group_name():
    """
    @brief test_create_group Verify that a group name can be changed.
    """
    group = Group.by_name("__piraidbay")
    if group.is_valid():
        group.delete()

    group = group.create("__piraidbay")
    expect_eq("__piraidbay", group._name)
    expect_true(Group.by_name("__piraidbay").is_valid())
    expect_true(does_group_exist(group))
    group._name = "__pyraidbay"
    expect_true(group.update())
    expect_true(does_group_exist(group))
    group.delete()
    print_success(inspect.stack()[0][3])

def main():
    test_find_user()
    test_list_users()
    test_create_user()
    test_create_user_no_home()
    test_create_user_home()
    test_create_user_home_exists()
    test_create_user_home_replace()
    test_delete_user()
    test_remove_home()
    test_add_user_home()
    test_delete_user_not_exists()
    test_change_user_name()

    # Group tests.
    test_find_group()
    test_list_groups()
    test_list_members()
    test_create_group()
    test_delete_group()
    test_add_member()
    test_change_group_name()

if __name__ == "__main__":
    main()
