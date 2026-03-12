import os
os.system("cls")
book_List = {}
while True :
    choice = int(input("""Menu:
     1- Add Book
     2- Check Out Book
     3- Check In Book
     4- List Books
     5- Exit
     Enter your choice (1-5) : """))
    if choice == 1 :
        while True :
            os.system("cls")
            ISBN_input = input("Enter ISBN of the book : ")
            title = input("Enter the Name of the book : ")
            author =input("Who is the author of the book : ")
            book_List[ISBN_input] = { "Title":title  , "Author":author , "Available" : True }
            print(f"Book {title} by {author} added to the catalog with ISBN : {ISBN_input}  ")
            if input("Do you want to add another book ( y / n ) :").lower() == "y" :
                continue
            else:
                break
    if choice == 2 :
        while True :
            os.system("cls")
            ISBN = input("Enter ISBN to check out a book : ")
            if ISBN in book_List :
                if book_List[ISBN]["Available"] == False :
                    print("This book has been checked out already")
                else :
                    book_List[ISBN]["Available"] = False
                    print(f"Book ({book_List[ISBN]["Title"]}) checked out successfully ")
            else:
                print("This book is not found")
            if input("Do you want to check out another book ( y / n ) :").lower() == "y" :
                continue
            else:
                break
    if choice == 3 :
        while True :
            os.system("cls")
            ISBN = input("Enter ISBN to check in a book : ")
            if ISBN in book_List :
                if book_List[ISBN]["Available"] == True :
                    print("This book has been checked in already")
                book_List[ISBN]["Available"] = True
                print(f"Book ({book_List[ISBN]["Title"]}) checked in successfully ")
            else:
                print("This book is not found")
            if input("Do you want to check in another book ( y / n ) :").lower() == "y" :
                continue
            else:
                break
    if choice == 4:
        while True:
            os.system("cls")
            for key in book_List :
                print("--------------------------")
                print(f" ISPN : {key} ,\n Title : {book_List[key]["Title"]} ,\n Author : {book_List[key]["Author"]} ,\n Available : {book_List[key]["Available"]}")
            if input("----------------------------\nDo you want to back to main Menu ( y / n ) :").lower() == "y" :
                break
            else:
                break
    if choice == 5:
                break
