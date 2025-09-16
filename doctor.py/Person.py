class Person:
    """Person Class"""

    def __init__(self, first_name, surname):
        """
        Initialize a Person instance.
        Args:
            first_name (str): The first name of the person.
            surname (str): The surname of the person.
        """
        self.__first_name = first_name
        self.__surname = surname

    def full_name(self):
        """
        Returns the full name of the person.
        Returns:
            str: Full name in the format "FirstName Surname".
        """
        return f"{self.__first_name} {self.__surname}"

    def get_first_name(self):
        """
        Get the first name of the person.
        Returns:
            str: The first name.
        """
        return self.__first_name

    def set_first_name(self, new_first_name):
        """
        Set a new first name for the person.
        Args:
            new_first_name (str): The new first name.
        """
        self.__first_name = new_first_name

    def get_surname(self):
        """
        Get the surname of the person.
        Returns:
            str: The surname.
        """
        return self.__surname

    def set_surname(self, new_surname):
        """
        Set a new surname for the person.
        Args:
            new_surname (str): The new surname.
        """
        self.__surname = new_surname

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       