from abc import ABC, abstractmethod
from typing import List
import xml.etree.ElementTree as ET
import json


# Contact data container class
class Contact:
    def __init__(self, full_name, email, phone_number, is_friend):
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.is_friend = is_friend
    
    def __str__(self):
        return f"{self.full_name} ({self.email}) - {self.phone_number} {'(Friend)' if self.is_friend else ''}"


# Our base class for reading file data
class FileReader(ABC) :
    def __init__(self, file_name):
        self.file_name = file_name

    abstractmethod
    def read(self) -> str:
        pass

# Abstract base class for all Contact Data Adapters
class ContactsAdapter(ABC):
    def __init__(self, data_source: FileReader):
        self.data_source = data_source
    
    abstractmethod
    def get_contacts(self) -> List[Contact]:
        pass

############################## Adapter Implementation ##############################


####################################################################################

# Specific implementation of the file reader to be used with XML Files
class XMLReader(FileReader):
    def read(self):
        # Read the contents of the XML file and return as a string
        with open(self.file_name, 'r') as f:
            return f.read()

# Specific implementation of the file reader to be used with JSON files
class JSONReader(FileReader):
    def read(self):
        # Read the contents of the JSON file and return as a string
        with open(self.file_name, 'r') as f:
            return f.read()

# Simple display routine to display Contact data to the console      
def print_contact_data(contacts_source : ContactsAdapter):
    # Print the Contact objects
    for contact in contacts_source.get_contacts():
        print(contact)

# Example usage
xml_reader = XMLReader('contacts.xml')
# Create an XML adapter and convert the data to a list of Contact objects
xml_adapter = XMLContactsAdapter(xml_reader)
# Print the Contact objects
print_contact_data(xml_adapter)

json_reader = JSONReader('contacts.json')
# Create a JSON adapter and convert the data to a list of Contact objects
json_adapter = JSONContactsAdapter(json_reader)
# Print the Contact objects
print_contact_data(json_adapter)
