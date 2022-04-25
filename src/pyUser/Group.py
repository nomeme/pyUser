
import os
import libuser
import time

from .BaseUser import BaseUser
from .BaseGroup import BaseGroup

class Group(BaseGroup):
    """
    @brief Group Class representing a system group.

    Utilizes the python3 libuser .Entity instance to manage system groups.
    """

    def __init__(self, group):
        """
        @brief __init__ Constructor taking the libuser .Entity instance to be represented.

        @param group The libuser .Entity instance representing the system group 
        """
        if group is None:
            self._name = None
            self._gid = None
            self._admin = None
            self._members = None
        else:
            self._name = group.get(libuser.GROUPNAME)[0]
            self._gid = group.get(libuser.GIDNUMBER)[0]
            self._admin = group.get(libuser.ADMINISTRATORNAME)
            self._members = group.get(libuser.MEMBERNAME)

    @classmethod
    def create(cls, name, members = None):
        """
        @brief create Create a new system group with the given name and home directory.

        Uses the system-default if no home or loginshell is provided.

        @param name The name of the group to be created
        @param home The home folder path for the group
        @param loginshell The loginshell for the group
        @param create_home Set to True if a home folder should be created
        @return Returns the Group instance representing the system group
        """
        group = cls.init(name)
        if members:
            if len(members) > 0:
                _members
                for member in [value for value in members if isinstance(value, str)]:
                    members.append(member)
                for member in [value for value in members if isinstance(value, BaseUser)]:
                    members.append(member.get_name())
                group[libuser.MEMBERNAME] = _members
        if cls.add(group):
            return cls(group)
        return None

    def delete(self):
        """
        @brief delete Delete the group.

        @return Returns True if success
        """
        group = self._by_id(self._gid)
        return super().delete(group)

    def update(self):
        """
        @brief update Update the content of the system group

        @return Returns True if success
        """
        group = self._by_id(self._gid)
        group[libuser.GROUPNAME] = self._name
        group[libuser.MEMBERNAME] = self._members
        return super().modify(group)

    def add_member(self, user):
        """
        @brief add_member Add a member to the Group.

        @param user The user to add to the group
        @return Returns True if success
        """
        group = self._by_id(self._gid)
        if isinstance(user, BaseUser):
            user = user.get_name()
        self._members.append(user)
        return self.update()

    def get_user_names(self):
        """
        @brief get_user_names Returns the names of the system users that
        are part of the group.

        @return Returns a list of user names
        """
        return super()._get_users(self._name)

    @staticmethod
    def is_valid(group):
        """
        @brief is_valid Returns True if the given user is valid.

        @param user The user instance to be validated
        @return Returns True if the user instance is valid
        """
        return group._name is not None and group._gid is not None

    def is_valid(self):
        """
        @brief is_valid Returns True if the user is valid.

        @return Returns True if the user instance is valid
        """
        return self._name is not None and self._gid is not None

