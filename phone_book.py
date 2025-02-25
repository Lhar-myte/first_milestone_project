# Project Overview:
# Create a simple phone book manager where users can add, view, update, and delete contacts
# in a file named `phone_book.py`.

# Requirements:
# Data Storage: Use a list of dictionaries to store contact information. Each contact should have the following 
# attributes:
# Name (string)
# Phone Number (string)
# Favorite (boolean)
# Functions/Actions:
# add_contact(): Add a new contact to the phone book.
# view_contacts(): Display all the contacts in the phone book.
# update_contact(phone_number): Update the information of a contact given their phone number.
# delete_contact(phone_number): Remove a contact from the phone book using their phone
# number.
# search_contact(name): Search for a contact by their exact name.
# mark_favorite(phone_number): Mark a contact as a favorite.
# unmark_favorite(phone_number): Unmark a contact as a favorite.
# User Interface: Use a loop to display a menu and prompt the user for an action above until they choose to exit. Assume the user always inputs the correct data types.



my_phone_book = [
    {"name": "Bamidele Olamide", "phone number": "08147047062", "is_favourite":True},
    {"name": "Ajayi Rebecca", "phone number": "08147087062", "is_favourite":True},
    {"name": "Okonkwo Timothy", "phone number": "08147047090", "is_favourite":False},
    {"name": "Adeoye Paul", "phone number": "08141047062", "is_favourite":True},
    {"name": "Raja kasanblaca", "phone number": "07147047082", "is_favourite":False},
]


def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    favorite = input("Mark as favorite? (yes/no): ").strip().lower() 
    
    contact = {"name": name, "phone": phone, "favorite": favorite}
    my_phone_book.append(contact)
    print(f"Contact {name} added successfully!\n")

def update_contact(contact):
    p = input("Phone to update: ")
    for contact in my_phone_book:
        if contact["phone"] == p:
            contact.update({"name": input("New Name: ")})
            return print("Updated!")
    print("Not found.")



       
def delete_contact(contacts, name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():  # Case-insensitive search
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully.")
            return
    print(f"Contact '{name}' not found.")

        
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}:")
        for key, value in contact.items():
            print(f"  {key.capitalize()}: {value}")


add_contact()
view_contacts(my_phone_book)
update_contact(my_phone_book)
delete_contact(my_phone_book)





