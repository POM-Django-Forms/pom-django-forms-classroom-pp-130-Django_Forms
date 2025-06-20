from django.db import models
from author.models import Author

class Book(models.Model):
    """
    Represents a Book entity.

    Attributes:
    -----------
    name : str
        The title of the book (max length 128).
    description : str
        Detailed description of the book.
    count : int
        Number of copies available (default 10).
    authors : ManyToManyField
        Authors related to the book (can be multiple).
    """

    name = models.CharField(max_length=128)
    description = models.TextField()
    count = models.IntegerField(default=10)
    authors = models.ManyToManyField(Author, blank=True)

    def __str__(self):
        authors_str = ', '.join(f"{a.surname} {a.name}" for a in self.authors.all())
        return f"{self.id}: {self.name} ({self.count}) - Authors: [{authors_str}]"

    def __repr__(self):
        return f"<Book {self.id}>"

    @staticmethod
    def get_by_id(book_id):
        return Book.objects.filter(id=book_id).first()

    @staticmethod
    def delete_by_id(book_id):
        book = Book.get_by_id(book_id)
        if book:
            book.delete()
            return True
        return False

    @staticmethod
    def create(name, description, count=10, authors=None):
        book = Book.objects.create(name=name, description=description, count=count)
        if authors:
            book.authors.set(authors)
        return book

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'count': self.count,
            'authors': [author.to_dict() for author in self.authors.all()]
        }

    def update(self, name=None, description=None, count=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if count is not None:
            self.count = count
        self.save()

    def add_authors(self, authors):
        for author in authors:
            self.authors.add(author)

    def remove_authors(self, authors):
        for author in authors:
            self.authors.remove(author)

    @staticmethod
    def get_all():
        return Book.objects.all()
