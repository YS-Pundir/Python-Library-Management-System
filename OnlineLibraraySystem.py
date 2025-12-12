class Book:
    def __init__(self,Title,Auther,isbn,is_borrowed):
        self.Title=Title
        self.Auther=Auther
        self.isbn=isbn
        self.is_borrowed=False

class Library():
    def __init__(self,name):
        self.name=name
        self.listOfBooks= [
            ["Death", "Sadguru", "35713", False],
            ["Samadhi", "OSHO", "384333", False],
            ["Sambhog", "OSHO", "283361", False],
            ["To Kill a Mockingbird", "Harper Lee", "9780446310789", False],
            ["1984", "George Orwell", "9780451524935", False],
            ["Pride and Prejudice", "Jane Austen", "9780141439518", False],
            ["The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", False],
            ["Moby Dick", "Herman Melville", "9781503280786", False],
            ["War and Peace", "Leo Tolstoy", "9781400079988", False],
            ["The Catcher in the Rye", "J.D. Salinger", "9780316769488", False],
            ["The Hobbit", "J.R.R. Tolkien", "9780547928227", False],
            ["Fahrenheit 451", "Ray Bradbury", "9781451673319", False],
            ["Brave New World", "Aldous Huxley", "9780060850524", False],
            ["Jane Eyre", "Charlotte Bronte", "9780141441146", False],
            ["Wuthering Heights", "Emily Bronte", "9780141439556", False],
            ["Crime and Punishment", "Fyodor Dostoevsky", "9780143058144", False],
            ["The Brothers Karamazov", "Fyodor Dostoevsky", "9780374528379", False],
            ["Anna Karenina", "Leo Tolstoy", "9780143035008", False],
            ["Don Quixote", "Miguel de Cervantes", "9780060934347", False],
            ["The Odyssey", "Homer", "9780140268867", False],
            ["Ulysses", "James Joyce", "9780199535675", False],
            ["The Divine Comedy", "Dante Alighieri", "9780142437223", False],
            ["The Iliad", "Homer", "9780140275360", False],
            ["Les Misérables", "Victor Hugo", "9780451419439", False],
            ["The Count of Monte Cristo", "Alexandre Dumas", "9780140449266", False],
            ["Great Expectations", "Charles Dickens", "9780141439563", False],
            ["A Tale of Two Cities", "Charles Dickens", "9780141439600", False],
            ["The Picture of Dorian Gray", "Oscar Wilde", "9780141439570", False],
            ["Frankenstein", "Mary Shelley", "9780141439471", False],
            ["Dracula", "Bram Stoker", "9780141439846", False],
            ["The Adventures of Huckleberry Finn", "Mark Twain", "9780142437179", False],
            ["The Adventures of Tom Sawyer", "Mark Twain", "9780143039563", False],
            ["Heart of Darkness", "Joseph Conrad", "9780141441672", False],
            ["Catch-22", "Joseph Heller", "9781451626650", False],
            ["The Lord of the Rings", "J.R.R. Tolkien", "9780544003415", False],
            ["One Hundred Years of Solitude", "Gabriel Garcia Marquez", "9780060883287", False],
            ["The Alchemist", "Paulo Coelho", "9780061122415", False],
            ["The Kite Runner", "Khaled Hosseini", "9781594631931", False],
            ["The Da Vinci Code", "Dan Brown", "9780307474278", False],
            ["Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "9780590353427", False],
            ["The Hunger Games", "Suzanne Collins", "9780439023481", False],
            ["The Girl with the Dragon Tattoo", "Stieg Larsson", "9780307949486", False],
            ["Gone Girl", "Gillian Flynn", "9780307588371", False],
            ["The Shining", "Stephen King", "9780307743657", False],
            ["It", "Stephen King", "9781501142970", False],
            ["Dune", "Frank Herbert", "9780441172719", False],
            ["The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "9780345391803", False],
            ["The Road", "Cormac McCarthy", "9780307387899", False],
            ["Life of Pi", "Yann Martel", "9780156027328", False],
            ["The Book Thief", "Markus Zusak", "9780375831003", False]
        ]
        
       
        
    def addBooks(self):
        maxLim=int(input("Add the maximum limit of book that can be added at once : ",))
        print(f"the maximum limit of adding the book is {maxLim}")
        print("---------Add Books---------")
        for  i in range(maxLim): 
            print("enter the details of the book that  needed to be added ->")
            
            Title=input("enter the name of the book : ",)
            Auther=input("enter the name of the auther : ",)
            ISBN=input("enter the isbn of the book :",)

            self.listOfBooks.append([Title,Auther,ISBN,False])
            print(f"<><><>The Book {Title} has been added successfully <><><>")

    def show(self):
        for i in self.listOfBooks:# for every list in nested list , i will be the sublist at every iteration
            print(f"Book : {i[0]} & Auther : {i[1]}")#then for that single iteration , it will  print the first element of that sublist
    
    def removeBooks(self):
        book=input("enter the name of the book that you want to remove from the library --",)
        found=False
        for i in self.listOfBooks:
            if book==i[0]:
                self.listOfBooks.remove(i)
                found=True
        if  found:
            print("The book has been removed")
        else:
            print("The book , that you want to remove does not exsist in the library")

class member(Library):
    def __init__(self,name):
        super().__init__(name)
        self.member_info= {
    "Yuvraj Singh": {"id": "12345"},
    "Rohit Sharma": {"id": "67890"},
    "Virat Kohli": {"id": "111213"},
    "MS Dhoni": {"id": "141516"},
    "Rahul Dravid": {"id": "171819"},
    "Sachin Tendulkar": {"id": "202122"},
    "Sunil Gavaskar": {"id": "232425"},
    "Kapil Dev": {"id": "262728"},
    "Anil Kumble": {"id": "293031"},
    "Virender Sehwag": {"id": "323334"},
    "Gautam Gambhir": {"id": "353637"},
    "Harbhajan Singh": {"id": "383940"},
    "Zaheer Khan": {"id": "414243"},
    "Yuzvendra Chahal": {"id": "444546"},
    "Jasprit Bumrah": {"id": "474849"}
}
        self.Borrowlist=[]
        
    def Borrow(self):
        member_name=input("Please enter the member's name :",)
        memberFound=False
        bookfound=False
        for key in self.member_info:
            if key == member_name :
                memberFound=True
                Bookname=input("Enter the name of the book to be borrowed : ",)
                
                for i in self.listOfBooks:
                    
                    if i[0] == Bookname:
                        self.Borrowlist.append(Bookname)
                        self.member_info[member_name]["Book Collection"]=self.Borrowlist
                        print(f"The book {self.Borrowlist} has been Borrowed")
                        bookfound=True
                        break
                break #stop scanning member info once we have handled this member
        
        if not memberFound:
            print(f"Error <!> : Member {member_name} not fund")

        elif not bookfound:
            print("Error <!> : Book not found")
        
        

                      
    def ShowMembers(self):  
         for name, info in self.member_info.items():
                            print(f"Name: {name}")
                            for field, value in info.items():
                                print(f"  {field}: {value}")
                                print()  # blank line between members  
    
    def Return(self):
         print()
         membername=input("Enter the Name of the member , Who is Returing the Book ",)
         Memberfound=False
         bookfound=False
         for keys in self.member_info:
              if membername == keys:
                   membername=True
                   bookName=input("Enter the name of the Book to be Returned -->",)
                   for key ,value in self.member_info.items():
                        for value ,feild in value.items():
                             if bookName in self.Borrowlist:
                                  self.Borrowlist.remove(bookName)
                                  print("The Book has Been returned")
         if  Memberfound==True:
              print("Error : there is no such member ")
         elif  bookfound==True:
              print("Error:the Book has not been borrowed")
    
    def addMember(self):
        membername=input("Enter the name person --> ",)
        memberID=input("Enter the ID of the Perosn-->",)
        if membername in self.member_info:
             print(f"Member {membername} alreadyb exsist .")

        self.member_info[membername]={"id":memberID}

    def RemoveMember(self):
         membername=input("Enter the name person --> ",)
         if membername not in self.member_info:
              print(f"The person {membername} is not the member of library")
         self.member_info.pop(membername,None)
         print(f"The Person {membername} has been removed from the membership successfully ")
         

       
def main():
     lib=member("<><><><><><>----City Central Library----<><><><><><>")

     while True:
               
               print("\n" + "="*50)
               print()
               print("Hezlich willkommen bie Stads Zentrum Bibliothek")
               print("="*50)
               print()
               print("Biite wählen sie ein Option")
               print(">>>>>>>>>>>>MENU<<<<<<<<<<<<")
               print("1. Add Books   2. Remove Books\n3.Add Members   4. Remove Members\n5. Borrow Book   6. Return a Book ")
               print("7. Show Books Available   8. Show Member's Details")
               print()
               Choice=int(input("Enter the number of your choice of service-->",))
 
               if Choice==1:
                    lib.addBooks()
               elif Choice==2:
                    lib.removeBooks()
               elif Choice==3:
                    lib.addMember()
               elif Choice==4:
                    lib.RemoveMember()
               elif Choice==5:
                    lib.Borrow()
               elif Choice==6:
                    lib.Return()
               elif Choice==7:
                    lib.show()
               elif Choice==8:
                    lib.ShowMembers()
     
     if __name__ == "__main__":
      main()


main()


