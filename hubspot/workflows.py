class Workflows(object):
    BASE_URL = "automation/v3"

    def __init__(self, client):
        self._client = client

    def get_workflows(self):
        endpoint = "/workflows"
        return self._client._get(self.BASE_URL + endpoint)

    def get_workflow(self, workflow_id, **params):
        endpoint = "/workflows/{}".format(workflow_id)
        return self._client._get(self.BASE_URL + endpoint, params=params)
    
    def create_workflow(self, data):
        endpoint = "/workflows"
        return self._client._post(self.BASE_URL + endpoint, json=data)

    def delete_workflow(self, workflow_id):
        endpoint = "/workflows/{}".format(workflow_id)
        return self._client._delete(self.BASE_URL + endpoint)

    def enroll_a_contact_into_workflow(self, workflow_id, contact_email):
        endpoint = "/workflows/{}/enrollments/contacts/{}".format(workflow_id, contact_email)
        return self._client._post("automation/v2" + endpoint)
    
    def unenroll_a_contact_into_workflow(self, workflow_id, contact_email):
        endpoint = "/workflows/{}/enrollments/contacts/{}".format(workflow_id, contact_email)
        return self._client._delete("automation/v2" + endpoint)
