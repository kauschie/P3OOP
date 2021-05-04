class Contact:
    all_contacts = []

    def __init__(self, name="", email="", **kwargs):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class AddressHolder:
    def __init__(self, street="", city="", state="", code="", **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code
    
class Friend(Contact, AddressHolder):
    def __init__(self, phone="", **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

# There are a few ways to ensure that the variable is passed upward. 
# Assume the Contact class does, for some reason, need to be initialized 
# with a phone parameter, and the Friend class will also need access to it. 
# We can do any of the following:

# 1 Don't include phone as an explicit keyword argument.
#          Instead, leave it in the kwargs dictionary. 
#           Friend can look it up using the kwargs['phone']  syntax. 
#           When it passes **kwargs to the super call, phone will still 
#           be in the dictionary.
# 2 Make phone an explicit keyword argument, 
#       but update the kwargs dictionary before passing it to super, 
#       using the standard dictionary kwargs['phone'] = phone syntax.
# 3 Make phone an explicit keyword argument, 
#       but update the kwargs dictionary using the kwargs.update method. 
#       This is useful if you have several arguments to update. You can 
#       create the dictionary passed into update using either the 
#       dict(phone=phone) constructor, or the dictionary {'phone': phone} 
#       syntax.
# 4 Make phone an explicit keyword argument, but pass it to the super call 
#       explicitly with the super().__init__(phone=phone, **kwargs) syntax.
