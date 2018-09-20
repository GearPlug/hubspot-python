# hubspot-python
HubSpot API wrapper written in Python.

### Installing

```
pip install hubspot-python
```

## Requirements

```
- Requests
```

## Usage

```
from hubspot.client import Client
client = Client("HERE YOUR TOKEN")

Create a contact:

data={'email':'grplugtest1@gmail.com'}
Client.contacts.create_contact(data)

Get Contacts:

Client.contacts.get_contacts()

Delete Contact:

Client.contacts.delete_contact()
```

## TODO

### CalendarAPI

### Companies

- Update_company
- Get contacts of a company
- Get contacts IDs of a company
- Add contact to company
- Remove contact from a company

### Contacts

- Update a contact
- Create or update a group of contacts
- Get contact by email
- Get a group of contacts by email

### COS

### CRM Extensions API

### Deals

- Update a Deal
- Update a Deal
- Associate a Deal
- Remove association of deal
- Get associated deals

### Deal pipelines

### Email

### Engagements

### Forms

### Keywords

### Owners

### SocialMedia

### Timeline

### Workflows

### Webhooks


