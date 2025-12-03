class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(self.name)
class Book(Publication):
    def __init__(self, name, page_count, author):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        super().print_info()
        print(f"Author: {self.author} and the page number is {self.page_count}")


class Magazine(Publication):
    def __init__(self, name , chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_info(self):
        super().print_info()
        print(f"chief editor: {self.chief_editor}")

#main
num = []

x1 = Book("Compartment No. 6", 192, "Rosa Liksom")
x2 = Magazine( "Donald Duck","Aki Hyyppä")
num.append(x1)
num.append(x2)
for i in num:
    i.print_info()