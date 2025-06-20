from django.db import models

class Author(models.Model):
    """
    This class represents an Author.
    
    Attributes:
    -----------
    name : str
        Name of the author (max_length=20)
    surname : str
        Last name of the author (max_length=20)
    patronymic : str
        Middle name of the author (max_length=20)
    """

    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)

    def __str__(self):
        """
        Return string representation showing full name and ID.
        """
        return f"{self.id}: {self.surname} {self.name} {self.patronymic}"

    def __repr__(self):
        """
        Return concise representation of the Author instance.
        """
        return f"<Author {self.id}>"

    @staticmethod
    def get_by_id(author_id):
        """
        Get author by id.
        
        :param author_id: int - ID of the author
        :return: Author instance or None
        """
        return Author.objects.filter(id=author_id).first()

    @staticmethod
    def delete_by_id(author_id):
        """
        Delete author by id.
        
        :param author_id: int
        :return: True if deleted, False otherwise
        """
        author = Author.get_by_id(author_id)
        if author:
            author.delete()
            return True
        return False

    @staticmethod
    def create(name, surname, patronymic):
        """
        Create and save a new Author.
        
        :param name: str
        :param surname: str
        :param patronymic: str
        :return: Author instance
        """
        return Author.objects.create(name=name, surname=surname, patronymic=patronymic)

    def to_dict(self):
        """
        Return dictionary representation of the author.
        """
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'patronymic': self.patronymic,
        }

    def update(self, name=None, surname=None, patronymic=None):
        """
        Update author fields if given and save.
        """
        if name is not None:
            self.name = name
        if surname is not None:
            self.surname = surname
        if patronymic is not None:
            self.patronymic = patronymic
        self.save()

    @staticmethod
    def get_all():
        """
        Return queryset of all authors.
        """
        return Author.objects.all()
