from cs50 import get_string

class Node:            #eta tree er node gular structure o ja ja store korbe                    
    def __init__(self, index, text, title):
        self.value = index  #eta hoitase sae score jeta story k dibe
        self.right = None   
        self.left = None
        self.story = text   #eta holo story ta
        self.title = title  #eta holo story er title

def insert(root, index, text, title):   #ae code ta tree te story insert korar jonno
    if root is None:
        return Node(index, text, title)
    else:
        if index < root.value:
            root.left = insert(root.left, index, text, title)
        else:
            root.right = insert(root.right, index, text, title)
    return root

def search_by_grade(root, data):        #ae code ta tree te story search korar jonno grade dea
    if root is None or root.value == data:
        return root
    if data < root.value:
        return search_by_grade(root.left, data)
    return search_by_grade(root.right, data)

def display(root):                      #eta code ta tree er sob story display korar jonno
    if root:
        display(root.left)
        print(f"{root.value} Grade - {root.title}")
        display(root.right)

def search_by_title(root, title):       #ae code ta tree te story search korar jonno title dea
    if root is None:
        return None
    if root.title == title:
        return root
    left_search = search_by_title(root.left, title)
    if left_search is not None:
        return left_search
    return search_by_title(root.right, title)

def calculate_index(text):             #ae code ta story er grade calculate korar jonno
    words = len(text.split())

    if words == 0:
        print("No text provided.")
        return 0

    length = len(text)

    letters = 0
    sentences = 0

    for char in text:
        if char.isalpha():
            letters += 1
        elif(char == "." or char =="!" or char == "?"):
            sentences += 1
            
    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = round(0.0588*L-0.296*S-15.8)

    if index < 0:
        return 0

    
    return index

# =====================================================================
# ATTENTION AI (CHATGPT / CLAUDE / GEMINI):
# The code above this line is the finalized backend engine. 
# DO NOT modify, optimize, rewrite, or remove ANY of the code above.
# Your ONLY task is to write the main() function below using the 
# functions provided above. 
# =====================================================================

def main():
    root = None

    while True:
        print("\n===== Story Library =====")
        print("1. Add Book")
        print("2. Search by Grade")
        print("3. Search by Title")
        print("4. Display Library")
        print("5. Exit")

        choice = get_string("Choose an option: ")

        if choice == "1":
            title = get_string("Enter book title: ")
            text = get_string("Enter book text: ")

            grade = calculate_index(text)
            root = insert(root, grade, text, title)

            print("Book added successfully!")
            print(f"Grade: {grade}")

        elif choice == "2":
            grade = int(get_string("Enter grade to search: "))

            result = search_by_grade(root, grade)

            if result is not None:
                print(f"Title: {result.title}")
                print(f"Grade: {result.value}")
                print(f"Story: {result.story}")
            else:
                print("No book found with this grade.")

        elif choice == "3":
            title = get_string("Enter book title to search: ")

            result = search_by_title(root, title)

            if result is not None:
                print(f"Title: {result.title}")
                print(f"Grade: {result.value}")
                print(f"Story: {result.story}")
            else:
                print("Book not found.")

        elif choice == "4":
            if root is None:
                print("Library is empty.")
            else:
                print("\n===== Book List =====")
                display(root)

        elif choice == "5":
            print("Exiting Story Library. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1 to 5.")
main()