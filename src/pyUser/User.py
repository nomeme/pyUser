import os
import libuser
import time

from pathlib import Path
from .BaseUser import BaseUser

class User(BaseUser):
    """
    @brief User Class representing a system user.

    Utilizes the python3 libuser .Entity instance to manage system users.
    """

    def __init__(self, user):
        """
        @brief __init__ Constructor taking the libuser .Entity instance to be represented.

        @param user The libuser .Entity instance representing the system user
        """
        if user is None:
            super().__init__(None, None)
            self._gid = None
            self._home = None
            self._loginshell = None
        else:
            super().__init__(user.get(libuser.USERNAME)[0], user.get(libuser.UIDNUMBER)[0])
            self._gid = user.get(libuser.GIDNUMBER)[0]
            self._home = user.get(libuser.HOMEDIRECTORY)[0]
            self._loginshell = user.get(libuser.LOGINSHELL)[0]

    @classmethod
    def create(cls, name, home = None, loginshell = None, create_home = True):
        """
        @brief create Create a new system user with the given name and home directory.

        Uses the system-default if no home or loginshell is provided.

        @param name The name of the user to be created
        @param home The home folder path for the user
        @param loginshell The loginshell for the user
        @param create_home Set to True if a home folder should be created
        @return Returns the User instance representing the system user
        """
        user = cls.init(name)
        if home:
            user[libuser.HOMEDIRECTORY] = home
        if loginshell:
            user[libuser.LOGINSHELL] = loginshell
        if cls.add(user, create_home = create_home) > 0:
            return cls(cls._by_name(name))
        return None

    def delete(self): # @Override
        """
        @brief delete Delete the user.

        @return Returns True if success
        """
        if not self.is_valid():
            return
        user = self._by_id(self._uid)
        if not user:
            return
        result = super().delete(user)
        if Path(self._home).exists() and Path(self._home).is_dir():
            result = result and super()._remove_home(user)
        result = result and super()._remove_mail(user)
        return result

    def remove_home(self):
        """
        @brief remove_home Remove the users home directory.

        @return Returns True of success
        """
        user = self._by_id(self._uid)
        return super()._remove_home(user)

    def create_home(self):
        """
        @brief create_home Creates the users home directory.

        @return Returns True if success
        """
        if self.has_home():
            self.remove_home()
        user = self._by_id(self._uid)
        return super()._create_home(user)

    def has_home(self):
        """
        @brief has_home Returns true if the User has a home directory.

        @return Returns True if the user has a home directory
        """
        return self.is_valid() and Path(self._home).exists() and Path(self._home).is_dir()

    def update(self):
        """
        @brief update Update the user properties.

        This includes username, homedirectory, and loginshell.
        @return Returns True if success
        """
        user = self._by_id(self._uid)
        user[libuser.USERNAME] = self._name
        user[libuser.HOMEDIRECTORY] = self._home
        user[libuser.LOGINSHELL] = self._loginshell
        return super().modify(user)

    @staticmethod
    def is_valid(user):
        """
        @brief is_valid Returns True if the given user is valid.

        @param user The user instance to be validated
        @return Returns True if the user instance is valid
        """
        return user._name is not None and user._uid is not None

    def is_valid(self):
        """
        @brief is_valid Returns True if the user is valid.

        @return Returns True if the user instance is valid
        """
        return self._name is not None and self._uid is not None

