# Urban Airship Assignment

## Notes
- I used Django for this assignment.
- I kept data in memory by creating a variable, CONTACTS_LIST, in the /api/views.py file that will hold all of the API functions.
- Authentication Credentials are held in /api/auth_credientials.py. They are kept in a tuple with the username, password, and base64 encoding needed for the header. I included the encoding for ease of replication.
- The GET endpoint for listing all Contacts allows for the searching of any Contact fields.
- I used Django 2.1.7 and Python 3.5.2

## Assumptions
- I assumed that all fields for the Contact are required and they all must be strings.
- When given the task of 'Replace a contact's data' I assumed this meant a PUT method to replace all data for a Contact and not updating individual fields with a PATCH.

## Setup
- Clone the Repository
- Install pip packages in requirements.txt
- Run `python manage.py runserver`

## API Endpoints
API Endpoints can be found in the API.md file
