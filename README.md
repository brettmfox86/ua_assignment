# Urban Airship Assignment

## Notes
- I used Django for this assignment.
- I tested the endpoints via Postman.
- I kept data in memory by creating a variable, CONTACTS_LIST, in the /api/views.py file that will hold all of the API functions.
- Authentication Credentials are held in /api/auth_credientials.py. They are kept in a tuple with the username, password, and base64 encoding needed for the header. I included the encoding for ease of replication.
- The GET endpoint for listing all Contacts allows for the searching of any Contact fields.
- I used Django 2.1.7 and Python 3.5.2

## Assumptions
- I assumed that all fields for the Contact are required and they all must be strings.
- When given the task of 'Replace a contact's data' I assumed this meant a PUT method to replace all data for a Contact and not updating individual fields with a PATCH.
- For the POST and PUT I assumed the JSON data being passed in the request will be done so through the raw body with a content type of JSON(application/json)

## Setup
- Clone the Repository
- Install pip packages in requirements.txt
- Run `python manage.py runserver`

## API Endpoints
- /contacts/ 
  - GET | POST
- /contact/:contact_id
  - GET | PUT | DELETE
- Detailed API Endpoint information can be found in the API.md file
