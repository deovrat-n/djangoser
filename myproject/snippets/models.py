from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']

"""
This model defines a Snippet object with fields for creation date, title, code, line numbers,
 programming language, and style. The language and style fields use choices populated from 
 the pygments library, which provides a comprehensive set of options for syntax highlighting.
 The Meta class ensures that snippets are ordered by their creation date by default.
"""

"""
In Django, a model is a Python class that represents a database table. Models are used 
to define the structure of your database, including the fields and behaviors of the data 
you are storing. Each model class maps to a single database table, and each attribute of 
the class represents a database field.

Here’s a basic example of a Django model:

python
Copy code
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
In this example:

The Person class is a model that represents a table in the database.
The first_name and last_name attributes are defined as character fields with a maximum length of 30 characters.
The birth_date attribute is defined as a date field.
The __str__ method is a special method that defines the string representation of the model objects.
Key Concepts in Django Models
Field Types:

Django provides a variety of field types to use in your models, such as CharField,
 IntegerField, DateField, EmailField, and many others. Each field type corresponds to 
 a column in the database.
Meta Class:

The inner Meta class in a Django model is used to define metadata for the model.
 This can include ordering, verbose names, and unique constraints.
python
Copy code
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()

    class Meta:
        ordering = ['last_name']
        verbose_name = 'person'
        verbose_name_plural = 'people'
Model Methods:

You can define custom methods on your model to encapsulate business logic. 
These methods can operate on the model’s fields and provide additional functionality.
python
Copy code
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
Relationships:

Django models can define relationships between different tables using fields 
such as ForeignKey, ManyToManyField, and OneToOneField.
python
Copy code
class Group(models.Model):
    name = models.CharField(max_length=30)

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    
By defining models in Django, you can use Django’s ORM (Object-Relational Mapping) 
to interact with your database in a high-level, Pythonic way without writing raw SQL queries. 
This allows for creating, retrieving, updating, and deleting records in a more straightforward manner.

"""