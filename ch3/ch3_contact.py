class ContactList(list):
    def search(self, name):
        """Return all contacts that contain the search value
        in their name"""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts
        
class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        print(
            "If this were a real system we would send "
            f"'{order}' order to '{self.name}'"
        )


c1 = Contact("John A", "JohnA@example.net")
c2 = Contact("John B", "JohnB@example.net")
c3 = Contact("John C", "JohnC@example.net")
print([c.name for c in Contact.all_contacts.search('John')])
