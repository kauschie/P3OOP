import datetime

last_item_no = 0

class ToDoItem:
    """Represents a 'To-Do' item. Add this item to a to-do list."""

    def __init__(self, Brief_desc="", Priority=0, Tags=""):
        """initialize item with brief description, optional full description, 
        optional priority, optional tags, and optional deadline date. 
        Automatically set the creation date"""
        self.brief_desc = Brief_desc
        self.priority = Priority
        self.tags = Tags
        self.creation_date = datetime.date.today
        self.completed = False
        global last_item_no
        last_item_no += 1
        self.item_no = last_item_no

    def match(self, filter):
        return ((filter in self.brief_desc) or 
                (filter in self.full_desc) or 
                (filter in self.tags)
        )

    
class ToDoList:
    """Represents a Collection of To-Do Items"""
    def __init__(self):
        self.todolist = []
    
    def add_todo(self, brief_desc, priority=0, tags=""):
        self.todolist.append(ToDoItem(brief_desc, priority, tags))

    def _find_todo(self, item_no):
        for todo in self.todolist:
            if todo.item_no == item_no:
                return todo
        return None
    
    def modify_brief_desc(self, item_no, brief_desc):
        self._find_todo(item_no).brief_desc = brief_desc

    def modify_priority(self, item_no, priority):
        self._find_todo(item_no).priority = priority

    def modify_tags(self, item_no, tags):
        self._find_todo(item_no).tags = tags

    def complete_todo(self, item_no):
        self._find_todo(item_no).completed = True

    # reference may or may not still exist.. need to investigate
    def delete_todo(self, item_no):
        self.todolist.remove(self._find_todo(item_no))

    def search_todo(self, filter):
        return [todo for todo in self.todolist if todo.match(filter)]

def main():
    l = ToDoList()
    l.add_todo("sweep the kitchen", tags='cleaning') 
    l.add_todo("sweep the hallway", tags='cleaning') 
    l.add_todo("do the dishes", priority=1, tags='cleaning')
    l.add_todo("take a shower", priority=3, tags="hygiene")
    for todo in l.todolist:
        print(todo.brief_desc)

if __name__ == "__main__":
    main()