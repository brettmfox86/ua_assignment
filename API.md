**API Endpoints**
----

* **URL**

  <_/contacts/_>

* **Method:**

  `GET` | `POST`
  
*  **Query Components**
 
   `{search_field}={search_value}`

   **Example:**
   
   `/contacts/?last_name=Fox&first_name=Brett`

* **Data Params**

  `{
    "first_name": "Brett",
    "last_name": "Fox",
    "email": "brettfox@email.com",
    "phone_number": "5555555555"
    }`

* **Success Responses:**
  * **Method:** GET
  * **Code:** 200 <br />
  * **Content:** `{
     "contacts": [
        {
            "phone_number": "5555555555",
            "last_name": "Fox",
            "email": "brettfox@email.com",
            "first_name": "Brett",
            "id": "49845a3d-f5ab-4b3a-8e16-965037549d71",
            "entered_by": "admin",
            "updated_by": null
        },...
    ]
}`

  OR

  * **Method:** POST
  * **Code:**  201 <br />
  * **Content:** `{
      "phone_number": "5555555555",
      "last_name": "Fox",
      "id": "b5d1dbd2-c16b-484f-91a2-5a77f2a7b279",
      "email": "brettfox@email.com",
      "first_name": "Brrett",
      "entered_by": "admin",
      "updated_by": null
  }`

* **Error Responses:**
  * **Method:** GET
  * **Code:** 400 BAD REQUEST <br />
  * **Content:**  `{"detail": "Invalid search value 'last'"}`

  OR
  * **Method:** POST
  * **Code:** 401 UNAUTHORIZED <br />
  * **Content:**  `{ "detail": "Authentication Failed" }`
  
  OR
  * **Method:** POST
  * **Code:** 400 BAD REQUEST <br />
  * **Content:** `{ "detail": "'pho4ne_number' is not a a valid Contact field" }`
      
  OR
  * **Code:**  405 METHOD NOT ALLOWED <br />
  * **Content:** `{ "detail": "This request method is not allowed." }`
  
  
  ----------------
* **URL**

  <_/contact/:contact_id_>

* **Method:**

  `GET` | `PUT` | `DELETE`
  
* **URL Params**

   **Required:**
 
   `contact_id=[str]`

* **Data Params**

  `{
    "first_name": "Brett",
    "last_name": "Fox",
    "email": "brettfox@email.com",
    "phone_number": "5555555555"
    }`

* **Success Responses:**
  * **Method:** GET | PUT
  * **Code:** 200 <br />
  * **Content:** `{
    "phone_number": "5555555555",
    "last_name": "Fox",
    "email": "brettfox@email.com",
    "first_name": "Brett",
    "id": "49845a3d-f5ab-4b3a-8e16-965037549d71",
    "entered_by": "admin",
    "updated_by": null
}`

  OR
  
  * **Method:** DELETE
  * **Code:** 200 <br />
  * **Content:** `{}`
  
* **Error Responses:**
  * **Code:** 400 BAD REQUEST <br />
  * **Content:**  `{"detail": "Contact does not exist.'"}`

  OR
  * **Methods:** PUT | DELETE
  * **Code:** 401 Unauthorized <br />
  * **Content:**  `{'detail': "Authentication Failed"}`
  
  OR
  
  * **Method:** PUT
  * **Code:** 400 BAD REQUEST <br />
  * **Content:** `{ "detail": "'pho4ne_number' is not a a valid Contact field" }`
  
  OR
  
  * **Code:**  405 METHOD NOT ALLOWED <br />
  * **Content:** `{ "detail": "This request method is not allowed." }`
  
  
