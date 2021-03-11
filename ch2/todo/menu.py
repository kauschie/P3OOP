import sys
from todo_list import ToDoList

class Menu:
    """Display a menu and respond to choices when run."""
    
    def __init__(self):
        self.L = ToDoList()
        self.choices = {
            "1": self.addnew,
            "2": self.complete,
            "3": self.modify,
            "4": self.quit,
        }
    
    def display_menu(self):
        print(
            """
Notebook Menu
---------------------------
1. Add New Item
2. Mark Item as Completed
3. Modify Item
4. Quit Program
        """)

    
    def run(self):
        """Display the menu and respond to choices."""
        while True:
            self.show_todos()
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")
    
    def show_todos(self):
        print("Item No.)\t<Priority>\t[Completed]\tDescription")
        print("   -\t\t   -\t\t   -\t\t   -")
        for item in self.L.todolist:
            if item.completed == False:
                print(f"  {item.item_no}.)\t\t   <{item.priority}>\t\t   [ ]\t\t{item.brief_desc}")
            if item.completed == True:
                print(f"  {item.item_no}.)\t\t   <{item.priority}>\t\t   [X]\t\t{item.brief_desc}")
        print("########################################################")

    def addnew(self):
        brief = input("Enter the brief description: ")
        p = input("Enter the priority (1=low | 10=high): ")
        tags_text = input("input any tags: ")
        self.L.add_todo(brief, priority=p, tags=tags_text)
        print("Your note has been added.")
    
    def complete(self):
        print("Enter the Item No. that is completed ")
        n_str = input("Return a blank line to exit: ")
        if n_str == '': return
        try:
            n = int(n_str)
            self.L.complete_todo(n)
        except:
            print(f"{n_str} is not a valid number")
            print("returning to the main menu with no changes")
            return
        
    def modify(self):
        item_no = input("Enter a Item No.: ")
        item_no_list = [todo.item_no for todo in self.L.todolist]
        print(item_no_list)
        if int(item_no) not in item_no_list:
            print(f"{item_no} was not in the item list")
            return
        print("""
        What do you want to modify?
        1. Modify Description
        2. Modify Priority
        3. Modify Tags
        """)
        mod = input("Enter your selection: ")
        if '1' in mod:
            self.desc(int(item_no))
        elif '2' in mod:
            self.priority(int(item_no))
        elif '3' in mod:
            self.tags(int(item_no))

    def desc(self, item_no):
        print("Enter a description")
        brief_desc = input("Return a blank line to make no changes: ")
        if brief_desc == '':
            print("No changes were made")
            return
        self.L.modify_brief_desc(item_no, brief_desc)

    def priority(self, item_no):
        text = input('Enter a new priority number: ')
        if text == '': return
        try:
            n = int(text)
        except:
            print(f"{text} is not a valid number. No changes will be made")
            return
        self.L.modify_priority(item_no, n)

    def tags(self, item_no):
        text = input('Enter the new tags: ')
        if text == '': return
        self.L.modify_tags(item_no, text)
    
    def quit(self):
        print("Thank you for using Dooo-to-doo")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()