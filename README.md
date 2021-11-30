# hubspot-python
HubSpot API wrapper written in Python.

## Installing

```
pip install hubspot-python
```

## Requirements

```
- requests
```

## Usage

#### Client instantiation
```
from hubspot.client import Client
client = Client(APP_ID, HAPIKEY, CLIENT_ID, CLIENT_SECRET)
```

### Companies
#### Get all companies
```
response = client.companies.get_companies(data)
```

#### Create a Company
```
data = {
    "name": "A company name",
    "description": "A company description"
}
response = client.companies.create_company(data)
```

#### Delete a Company
```
response = client.companies.delete_company(COMPANY_ID)
```

#### Get Recently Created Companies
```
response = client.companies.get_recently_created_companies()
```

#### Get a Company
```
response = client.companies.get_company(COMPANY_ID)
```

### Contact Lists
#### Get contact lists
```
response = client.contact_lists.get_contact_lists()
```

#### Create a new contact list
```
data = {
    "name": "tweeters",
    "dynamic": true,
    "portalId": 62515,
    "filters": 
    [
        [{
            "operator": "EQ",
            "value": "@hubspot",
            "property": "twitterhandle",
            "type": "string"
        }]
    ]
}
response = client.contact_lists.create_contact_list(data)
```

#### Delete a contact list
```
response = client.contact_lists.delete_contact_list(CONTACT_LIST_ID)
```

#### Get recently added contacts from a list
```
response = client.contact_lists.get_recently_added_contacts_in_a_list()
```

#### Get a contact list by its unique ID
```
response = client.contact_lists.get_contact_list(CONTACT_LIST_ID)
```

#### Add existing contacts to a list
```
data = {
  "vids": [
    3057124,
	5524274
  ],
  "emails": [
    "testingapis@hubspot.com"
  ]
}
response = client.contact_lists.add_contact_to_list(CONTACT_LIST_ID, data)
```

### Contacts
#### Get all contacts
```
response = client.contacts.get_contacts()
```

#### Create a new contact
```
data = {
    "email": "testingapis@hubspot.com",
    "firstname": "Adrian",
    "lastname": "Mott",
    "website": "http://hubspot.com",
    "company": "HubSpot",
    "phone": "555-122-2323",
    "address": "25 First Street",
    "city": "Cambridge",
    "state": "MA",
    "zip": "02139",
}
response = client.contacts.create_contact(data)
```

#### Delete a contact
```
response = client.contacts.delete_contact(CONTACT_ID)
```

#### Get recently created contacts
```
response = client.contacts.get_recently_created_contacts()
```

#### Get a contact list by its unique ID
```
response = client.contacts.get_contact(CONTACT_ID)
```

### Deals
#### Get all deals
```
response = client.deals.get_deals()
```

#### Create a Deal
```
data = {
    "dealname": "Tim's Newer Deal",
    "dealstage": "appointmentscheduled",
    "pipeline": "default",
    "hubspot_owner_id": "24",
    "closedate": 1409443200000,
    "amount": "60000",
    "dealtype": "newbusiness",
}
response = client.deals.create_deal(data)
```

#### Delete a Deal
```
response = client.deals.delete_deal(DEAL_ID)
```

#### Get Recently Created Deals
```
response = client.deals.get_recently_created_deals()
```

#### Get a contact list by its unique ID
```
response = client.deals.get_deal(DEAL_ID)
```

### Fields (Properties)
#### Get all fields
```
response = client.fields.get_fields(MODULE)
```

### Integrations
#### Get all fields
```
response = client.integrations.get_account_details()
```

#### Get all fields
```
response = client.integrations.get_daily_api_usage()
```

### Webhooks
#### Viewing Settings
```
response = client.webhooks.get_settings()
```

#### Updating Settings
```
data = {
    "webhookUrl": "https://testing.com/webhook-modified", 
    "maxConcurrentRequests": 25
}

response = client.webhooks.update_settings(data)
```

#### Get Subscriptions
```
response = client.webhooks.get_subscriptions()
```

#### Create a New Subscription
```
data = { 
    "subscriptionDetails" : {
        "subscriptionType" : "company.propertyChange", 
        "propertyName" : "companyname" 
    }, 
    "enabled": False
}

response = client.webhooks.create_subscription(data)
```

#### Update a Subscription
```
data = { 
    "enabled": False
}

response = client.webhooks.create_subscription(SUBSCRIPTION_ID, data)
```

#### Delete a Subscription
```
response = client.webhooks.delete_subscription(SUBSCRIPTION_ID)
```

### Workflows
#### Get workflows
```
response = client.workflows.get_workflows()
```

#### Get workflow
```
response = client.workflows.get_workflow(WORKFLOW_ID)
```

#### Create a workflow
```
data = {
    "name": "Test Workflow",
    "type": "DRIP_DELAY",
    "onlyEnrollsManually": true,
    "actions": [
        {
            "type": "DELAY",
            "delayMillis": 3600000
        },
        {
            "newValue": "HubSpot",
            "propertyName": "company",
            "type": "SET_CONTACT_PROPERTY"
        },
        {
            "type": "WEBHOOK",
            "url": "https://www.myintegration.com/webhook.php",
            "method": "POST",
            "authCreds": {
                "user": "user",
                "password": "password"
            }
        }
    ]
}
response = client.workflows.create_workflow(data)
```

#### Delete a Deal
```
response = client.workflows.delete_workflow(WORKFLOW_ID)
```

#### Enroll a contact into a workflow
```
response = client.workflows.enroll_a_contact_into_workflow(WORKFLOW_ID, EMAIL)
```

#### Unenroll a contact from a workflow
```
response = client.workflows.unenroll_a_contact_into_workflow(WORKFLOW_ID, EMAIL)
```

