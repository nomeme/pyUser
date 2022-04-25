from .Admin import Admin

class Base(Admin):
    """
    @brief Base Basic implementation for libuser .Entry instance handling.
    """

    def get_name(self):
        """
        @brief get_name Returns the name of the libuser .Entiry instance.

        @return Returns the name of the libuser .Entity
        """
        raise Exception("Child class must override")

    def get_id(self):
        """
        @brief get_id Returns the id of the libuser .Entitiy instance.

        @return Returns the id of the libuser .Entity
        """
        raise Exception("Child class must override")

    @classmethod
    def _by_id(cls, id):
        """
        @brief _by_id Returns the libuser .Entitiy .

        @param name The name of the libuser .Entity
        @return Returns the libuser .Entity or None
        """
        raise Exception("Child class must override")

    @classmethod
    def _by_name(cls, name):
        """
        @brief _by_name Returns the libuser .Entitiy matching the name.

        @param name The name of the libuser .Entity
        @return Returns the libuser .Entity or None
        """
        raise Exception("Child class must override")

    @classmethod
    def _init(cls, name):
        """
        @brief _init Creates a new libuser .Entity object with the given name.

        @param name The name for the libuser .Entity object to create
        @return Returns the libuser .Entity object
        """
        raise Exception("Child class must override")

    @classmethod
    def _add(cls, value):
        """
        @brief _add Adds a new libuser .Entity to the system.

        @param value The libuser .Entity object to be added to the system
        @return Returns True if success
        """
        raise Exception("Child class must override")

    @classmethod
    def _delete(cls, value):
        """
        @brief _delete Deletes the given libuser .Entity from the system.

        @param value The libuser .Entity object to be deleted from the system
        @return Returns True if success
        """
        raise Exception("Child class must override")

    @classmethod
    def _modify(cls, value):
        """
        @brief _modify Modifies information about the system libuser .Entity.

        @param value The libuser .Entity object to be modified
        @return Returns True if success
        """
        raise Exception("Child class must override")

    @classmethod
    def _lock(cls, value):
        """
        @brief _lock Locks the libuser .Entity object.

        @param value The libuser .Entity object to be locked
        @return Returns True if success
        """
        raise Exception("Child class must override")
    
    @classmethod
    def _unlock(cls, value):
        """
        @brief _unlock Unlocks the libuser .Entity object.

        @param value The libuser .Entity object to be unlocked
        @return Returns True if success
        """
        raise Exception("Child class must override")

    @classmethod
    def _enumerate(cls, expr):
        """
        @brief _enumerate Enumerates the libuser .Entity objects matching the given expression.

        @param expr The expression to be matched
        @return Returns The groups matching the expression
        """
        raise Exception("Child class must override")

    @classmethod
    def by_id(cls, id):
        """
        @brief by_id Returns the implementation type for the given libuser .Entity id.

        @param id The id of the libuser .Entity
        @return Returns the implementation type for the libuser .Entity
        """
        return cls(cls._by_id(id))

    @classmethod
    def by_name(cls, name):
        """
        @brief by_name Returns the implementation type for the given libuser .Entity name.

        @param name The name of the libuser .Entity
        @return Returns the implementation type for the libuser .Entity
        """
        return cls(cls._by_name(name))

    @classmethod
    def init(cls, name):
        """
        @brief init Initializes a new libuser .Entity with the given name.

        @param name The name of the libuser .Entity
        @return Returns the libuser .Entity
        """
        return cls._init(name)

    @classmethod
    def add(cls, value):
        """
        @brief add Add a libuser .Entity to the system.

        @param value The libuser .Entity to be added to the system
        @return Returns True if success
        """
        return cls._add(value)

    @classmethod
    def delete(cls, value):
        """
        @brief delete Deletes a libuser .Entity from the system.

        @param value The libuser .Entity to be deleted from the system
        @return Returns True if success
        """
        return cls._delete(value)

    @classmethod
    def modify(cls, value):
        """
        @brief modify Modifies a libuser .Entity instance.

        @param value The libuser .Entity to be modified
        @return Returns True if success
        """
        return cls._modify(value)

    @classmethod
    def lock(cls, value):
        """
        @brief lock Locks the given libuser .Entity.

        @param value The libuser .Entity to be locked
        @return Returns True if success
        """
        return cls._lock(value)

    @classmethod
    def unlock(cls, value):
        """
        @brief unlock Unlocks the given libuser .Entity.

        @param value The libuser .Entity to be unlocked
        @return Returns True if success
        """
        return cls._unlock(value)

    @classmethod
    def enumerate(cls, expr):
        """
        @brief enumerate enumerates all libuser .Entity instances matching 
        the given expression.

        @param expr The expression to match
        @return Returns a list of matching libuser .Entity instances
        """
        result = []
        for entry in cls._enumerate(expr):
            result.append(cls.by_name(entry))
        return result

    @classmethod
    def list(cls):
        """
        @brief list returns a list of all libuser .Enitity instances

        @return Returns the list of libuser .Entity instances
        """
        return cls.enumerate('*')

    def print(self):
        """
        @biref print Print the content of the instance
        """
        result = {}
        for entry in self.__dict__:
            if entry.startswith("_"):
                result[entry.replace("_", "", 1)] = self.__dict__[entry]
            else:
                result[entry] = self.__dict__[entry]
        print(result)

