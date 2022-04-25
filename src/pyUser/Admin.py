import libuser

class Admin:
    """
    @brief Admin The base class for all libuser implementations.

    This handles the access to the libuser.admin instance utilized to
    modify the system entries for user and group.
    """
    __ADMIN = libuser.admin()

    @classmethod
    def _get_admin(cls):
        """
        @brief _get_admin Returns the instance of the libuser admin
        used in this library.

        @return Returns the libuser admin
        """
        return cls.__ADMIN

