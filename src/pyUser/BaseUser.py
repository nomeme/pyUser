from .Base import Base

class BaseUser(Base):
    """
    @brief BaseGroup Basic implementation for the User class.

    This handles the direct interaction with the python3 libuser implementation.
    """

    def __init__(self, name, uid):
        """
        @brief __init__ Constructor taking the name and of of the user.
        """
        self._name = name
        self._uid = uid

    def get_name(self): # @Override
        """
        @brief get_name Returns the name of the User.

        @return Returns the name of the user
        """
        return self._name

    def get_id(self): # @Override
        """
        @brief _by_id Returns the libuser .Entitiy representing the User.

        @param id The id of the user
        @return Returns the libuser .Entity or None
        """
        return self._uid

    @classmethod
    def _by_id(cls, id): # @Override
        """
        @brief _by_id Returns the libuser .Entitiy representing the User.

        @param name The name of the user
        @return Returns the libuser .Entity or None
        """
        return cls._get_admin().lookupUserById(id)

    @classmethod
    def _by_name(cls, name): # @Override
        """
        @brief _by_name Returns the libuser .Entitiy representing the User.

        @param name The name of the user
        @return Returns the libuser .Entity or None
        """
        return cls._get_admin().lookupUserByName(name)

    @classmethod
    def _init(cls, name): # @Override
        """
        @brief _init Creates a new libuser .Entity object for the User.

        @param name The name for the libuser .Entity object to create
        @return Returns the libuser .Entity object
        """
        return cls._get_admin().initUser(name)

    @classmethod
    def _add(cls, value, create_home = True, create_mail = True): # @Override
        """
        @brief _add Adds a new User to the system.

        @param value The libuser .Entity object to be added to the system
        @param create_home True if the home folder for the user shall be created
        @param create_mail True if the mail spool for the user shall be created
        @return Returns True if success
        """
        return cls._get_admin().addUser(value, create_home, create_mail) > 0

    @classmethod
    def add(cls, name, create_home = True, create_mail = True): # @Override
        """
        @brief _add Adds a new User to the system.

        @param value The libuser .Entity object to be added to the system
        @param create_home True if the home folder for the user shall be created
        @param create_mail True if the mail spool for the user shall be created
        @return Returns True if success
        """
        return cls._add(name, create_home, create_mail)


    @classmethod
    def _delete(cls, value): # @Override
        """
        @brief _delete Deletes the given libuser .Entity from the system.

        @param value The libuser .Entity object to be deleted from the system
        @return Returns True if success
        """
        return cls._get_admin().deleteUser(value) > 0

    @classmethod
    def _modify(cls, value): # @Override
        """
        @brief _modify Modifies information about the system libuser .Entity.

        @param value The libuser .Entity object to be modified
        @return Returns True if success
        """
        return cls._get_admin().modifyUser(value) > 0

    @classmethod
    def _lock(cls, value): # @Override
        """
        @brief _lock Locks the libuser .Entity object.

        @param value The libuser .Entity object to be locked
        @return Returns True if success
        """
        return cls._get_admin().lockUser(value) > 0

    @classmethod
    def _unlock(cls, value): # @Override
        """
        @brief _unlock Unlocks the libuser .Entity object.

        @param value The libuser .Entity object to be unlocked
        @return Returns True if success
        """
        return cls._get_admin().unlockUser(value) > 0

    @classmethod
    def _enumerate(cls, expr): # @Override
        """
        @brief _enumerate Enumerates the libuser .Entity objects matching the given expression.

        @param expr The expression to be matched
        @return Returns The groups matching the expression
        """
        return cls._get_admin().enumerateUsers(expr)

    @classmethod
    def _remove_mail(cls, user):
        """
        @brief _remove_mail Removes the mail spool for the given User.

        @param user The libuser .Entity object representing the user
        @return Returns True if success
        """
        return cls._get_admin().removeMail(user) > 0

    @classmethod
    def _remove_home(cls, user):
        """
        @brief _remove_home Removes the home folder for the given User.

        @param user The libuser .Entity object representing the user
        @return Returns True if success
        """
        return cls._get_admin().removeHome(user) > 0

    @classmethod
    def _create_home(cls, user):
        """
        @brief _create_home Creates the home folder for the user.

        @param user The user to create the home folder for
        @return Returns True if success
        """
        return cls._get_admin().createHome(user) > 0

