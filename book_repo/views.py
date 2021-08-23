from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse

from home.models import Book, Author

# This view is interacts with user and returns the list of books
def home_page(request):
    ctx = {}
    search_parameter = request.GET.get("q")
    filter_parameter = request.GET.get("f")

    authors = Author.objects.all()

    if search_parameter:
        books = Book.objects.filter(title__icontains=search_parameter)
    else:
        books = Book.objects.all()

    if filter_parameter != None:
        if int(filter_parameter)>0:
            books = books.filter(book_author=filter_parameter)

    ctx["books_dataset"] = books
    ctx["authors_dataset"] = authors
    if request.is_ajax():

        html = render_to_string(
            template_name="home/partial_book_list.html", context={"books_dataset": books}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "home/book_list.html", context=ctx)