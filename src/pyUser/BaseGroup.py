from .Base import Base

class BaseGroup(Base):
    """
    @brief BaseGroup Basic implementation for the Group class.

    This handles the direct interaction with the python3 libuser implementation.
    """

    def __init__(self, name, gid):
        """
        @brief __init__ Constructor taking the name and of of the group.
        """
        self._name = name
        self._gid = gid

    def get_name(self): # @Override
        """
        @brief get_name Returns the name of the Group.

        @return Returns the name of the group
        """
        return self._name

    def get_id(self): # @Override
        """
        @brief get_id Returns the id of the Group.

        @return Returns the id of the group
        """
        return self._gid

    @classmethod
    def _by_id(cls, id):
        """
        @brief _by_id Returns the libuser .Entitiy representing the Group.

        @param id The id of the group
        @return Returns the libuser .Entity or None
        """
        return cls._get_admin().lookupGroupById(id)

    @classmethod
    def _by_name(cls, name):
        """
        @brief _by_name Returns the libuser .Entitiy representing the Group.

        @param name The name of the group
        @return Returns the libuser .Entity or None
        """
        return cls._get_admin().lookupGroupByName(name)

    @classmethod
    def _init(cls, name):
        """
        @brief _init Creates a new libuser .Entity object for the Group.

        @param name The name for the libuser .Entity object to create
        @return Returns the libuser .Entity object
        """
        return cls._get_admin().initGroup(name)

    @classmethod
    def _add(cls, value):
        """
        @brief _add Adds a new Group to the system.

        @param value The libuser .Entity object to be added to the system
        @return Returns True if success
        """
        return cls._get_admin().addGroup(value) > 0

    @classmethod
    def _delete(cls, value):
        """
        @brief _delete Deletes the given libuser .Entity from the system.

        @param value The libuser .Entity object to be deleted from the system
        @return Returns True if success
        """
        return cls._get_admin().deleteGroup(value) > 0

    @classmethod
    def _modify(cls, value):
        """
        @brief _modify Modifies information about the system libuser .Entity.

        @param value The libuser .Entity object to be modified
        @return Returns True if success
        """
        return cls._get_admin().modifyGroup(value) > 0

    @classmethod
    def _lock(cls, value):
        """
        @brief _lock Locks the libuser .Entity object.

        @param value The libuser .Entity object to be locked
        @return Returns True if success
        """
        return cls._get_admin().lockGroup(value) > 0

    @classmethod
    def _unlock(cls, value):
        """
        @brief _unlock Unlocks the libuser .Entity object.

        @param value The libuser .Entity object to be unlocked
        @return Returns True if success
        """
        return cls._get_admin().unlockGroup(value) > 0

    @classmethod
    def _enumerate(cls, expr):
        """
        @brief _enumerate Enumerates the libuser .Entity objects matching the given expression.

        @param expr The expression to be matched
        @return Returns The groups matching the expression
        """
        return cls._get_admin().enumerateGroups(expr)

    @classmethod
    def _get_users(cls, name):
        """
        @brief _get_users Returns the users that are members of this group.

        @param name The name of the group
        @return Returns the user names in the group
        """
        return cls._get_admin().enumerateUsersByGroup(name)

