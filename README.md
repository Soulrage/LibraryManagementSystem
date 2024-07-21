# LibraryManagementSystem
Console application in Python that implements a library management system

the classes folder contains two classes, the DataBase class is intended for connecting to the database, the Library class is a layer between the database and the client, they have functionality:
- receiving all books
- getting a new id
- adding a book
- book search
- deleting a book
- change the status of the book
there are also additional methods for DataBase:
-_open_file
-_save_file

There is also a Test folder in which these classes are tested.

The application can be launched via docker-compose (but it is not stable, depending on the development environment)
the application can also be launched via main.py
