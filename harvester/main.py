from managerHTML import *
from readingSates import State
from fileManager import *

file_addresses = "./files/Addresses.txt"
file_emails = "./files/Emails.txt"

email_list = []

addresses = importListFromFile(file_addresses)

for addr in addresses:
    emails = harvest(addr)
    email_list += emails

email_list = distinct(email_list)
print(email_list)

exportListFromFile(file_emails, email_list)
