from owner import views
from django.urls import path
urlpatterns=[
    path("books/all",views.BookList.as_view(),name='listbook'),
    path("books/add",views.AddBook.as_view(),name="addbook"),
    path("book/view/<int:id>",views.BookDetails.as_view(),name="bookdetails"),
    path("book/delete/<int:id>",views.BookDelete.as_view(),name="deletebook"),
    path("signout", views.sign_out, name="signout"),
    path("books/change/<int:id>",views.BookUpdate.as_view(),name="bookedit"),

]