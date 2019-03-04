import base64
import json
import uuid

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.auth_credentials import authenticated_users

CONTACTS_LIST = [
    {
        "id": "49845a3d-f5ab-4b3a-8e16-965037549d71",
        "first_name": "Brett",
        "last_name": "Fox",
        "email": "brettfox@email.com",
        "phone_number": "5555555555"
    },
    {
        "id": "e1473de5-dc9d-497b-9541-beff4f9e988e",
        "first_name": "John",
        "last_name": "Guy",
        "email": "Johnguy@email.com",
        "phone_number": "5555555552"
    },
    {
        "id": "958b38bd-827c-4e45-9775-3fa7c547a524",
        "first_name": "Jane",
        "last_name": "Fox",
        "email": "Janewoman@email.com",
        "phone_number": "5555555556"
    }
]

CONTACT_FIELDS = ['first_name', 'last_name', 'email', 'phone_number']


@csrf_exempt
def contacts(request):
    """
    List all contacts, optionally filtering by a search query or create a contact

    Handles methods: GET, POST
    """
    # GET - Get a list of contacts, optionally filtering by a search query.
    # localhost:8000/api/contacts/?{search_value}={search_key}&{search_value}={search_key}
    if request.method == 'GET':
        final_contacts = CONTACTS_LIST

        # Perform filtering if there are search queries available in the request
        for search_term, search_value in request.GET.items():
            try:
                final_contacts = [i for i in final_contacts if i[search_term] == search_value]
            except KeyError:  # PROPER STATUS?!?!?!?!?!?!?!?!
                return JsonResponse({"detail": "Invalid search value '{}'".format(search_term)}, status=400)

        return JsonResponse({"contacts": final_contacts}, status=200)

    # POST - Create a new contact.
    elif request.method == 'POST':
        # Authenticate based on Authentication credentials located in the header
        if not authenticate(request.META['HTTP_AUTHORIZATION']):
            return JsonResponse({'detail': "Authentication Failed"}, status=401)

        # Retrieve and transform body values form bytes to JSON
        body_obj = (json.loads(request.body.decode('utf-8')))

        # Validate the Contact object to be saved.
        message, status = validate_contacts(body_obj)

        # If the Contact object is valid then save it
        if status == 'ok':
            body_obj['id'] = str(uuid.uuid4())
            CONTACTS_LIST.append(body_obj)
            return JsonResponse(body_obj, status=201)
        # Else if the Contact object is not valid return the error message.
        else:
            return JsonResponse({'detail': message}, status=400)

    # Invalid Request Method.
    else:
        return JsonResponse({"detail": "This request method is not allowed."}, status=405)


@csrf_exempt
def contact(request, contact_id):
    """
    Get contact details, update a contact, delete a contact

    Handles methods: GET, PUT, DELETE
    """
    # Find the Contact with the provided ID in the CONTACTS_LIST.
    # Return an error if the Contact does not exist.
    for index, contact_obj in enumerate(CONTACTS_LIST):
        if contact_obj['id'] == contact_id:
            final_contact = contact_obj
            break
    else:
        return JsonResponse({"detail": "Contact does not exist."}, status=400)

    # GET - Get a contact.
    if request.method == 'GET':
        return JsonResponse(final_contact, status=200)

    # DELETE - Delete a contact.
    elif request.method == 'DELETE':
        # Authenticate based on Authentication credentials located in the header
        if not authenticate(request.META['HTTP_AUTHORIZATION']):
            return JsonResponse({'detail': "Authentication Failed"}, status=401)

        CONTACTS_LIST.pop(index)
        return JsonResponse({}, status=200)

    # PUT - Replace a contact's data.
    elif request.method == 'PUT':
        # Authenticate based on Authentication credentials located in the header
        if not authenticate(request.META['HTTP_AUTHORIZATION']):
            return JsonResponse({'detail': "Authentication Failed"}, status=401)

        # Retrieve and transform body values form bytes to JSON
        body_obj = (json.loads(request.body.decode('utf-8')))

        # Validate the Contact object to be saved.
        message, status = validate_contacts(body_obj)

        # If the Contact object is valid then update it
        if status == "ok":
            for key, value in body_obj.items():
                CONTACTS_LIST[index][key] = value
            return JsonResponse(body_obj, status=200)
        # Else if the Contact object is not valid return the error message.
        else:
            return JsonResponse({"detail": message}, status=400)

    # Invalid Request Method.
    else:
        return JsonResponse({"detail": "This request method is not allowed."}, 405)


def validate_contacts(body_obj):
    """
    Validate a Contact JSON object.
    """
    for key, value in body_obj.items():
        # Check that the given value is a string.
        if isinstance(value, str) is False:
            return "'{}' field value, {}, is not a string.".format(key, value), "error"
        # Check that the given field is a valid Contact field.
        elif key not in CONTACT_FIELDS:
            return "'{}' is not a a valid Contact field".format(key), "error"

    # Check that all required fields are present.
    for field in CONTACT_FIELDS:
        if field not in (list(body_obj.keys())):
            return "Required fields are missing.", "error"

    return "Object is Clean!", "ok"


def authenticate(auth_header):
    # Removes "Basic " to isolate credentials
    encoded_credentials = auth_header.split(' ')[1]
    # Split Username and Password
    decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8").split(':')
    username = decoded_credentials[0]
    password = decoded_credentials[1]
    if (username, password, encoded_credentials) in authenticated_users:
        return True
    else:
        return False

