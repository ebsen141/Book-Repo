from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page

class HomePage(Page):
    max_count = 0
    templates = "home/home_page.html"

# Model for create author
class Author(Page):

    subpage_types = []

    author_description = models.CharField(max_length=500, blank=False, null=True)

    content_panels = Page.content_panels+[
        FieldPanel("author_description")
    ]

#Model for create Book
class Book(Page):

    subpage_types = []

    book_description = models.CharField(max_length=500, blank=False, null=True)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    content_panels = Page.content_panels+[
        FieldPanel("book_description"), FieldPanel("book_author")
    ]

#Model for Author Parent
class AuthorPage(Page):
    max_count = 1
    subpage_types = [Author]

    class Meta:
        verbose_name = "Author List"
        verbose_name_plural = "Authors List"

#Model for Book parent
class BookPage(Page):
    max_count = 1
    subpage_types = [Book]

    class Meta:
        verbose_name = "Book List"
        verbose_name_plural = "Books List"




