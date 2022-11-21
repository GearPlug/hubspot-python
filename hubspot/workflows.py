class Workflows(object):
    BASE_URL = "automation/v3"

    def __init__(self, client):
        self._client = client

    def get_workflows(self):
        """
        Get a list of workflows for a HubSpot portal. This endpoint is
        particularly useful if you are looking for a particular workflow
        and need to look it up by an Id. The endpoint only returns metadata
        for each workflow.
        """
        endpoint = "/workflows"
        return self._client._get(self.BASE_URL + endpoint)

    def get_workflow(self, workflow_id, **params):
        """
        Returns metadata for a workflow.

        This endpoint will not return the contacts that are enrolled in the
        workflow. Workflow IDs can be found by using the get all workflows endpoint.
        """
        endpoint = "/workflows/{}".format(workflow_id)
        return self._client._get(self.BASE_URL + endpoint, params=params)

    def create_workflow(self, data):
        """
        Create a new workflow in a portal. Workflows are an essential
        component of the HubSpot marketing product, allowing marketing
        automation that relies on triggering relevant and timely actions,
        based on a user's context.
        """
        endpoint = "/workflows"
        return self._client._post(self.BASE_URL + endpoint, json=data)

    def delete_workflow(self, workflow_id):
        """
        Delete a workflow. Because deleting a workflow could be very
        disruptive to a user - you might be deleting a marketing automation
        workflow - a good best practice is to only delete workflows that your
        integration created.
        """
        endpoint = "/workflows/{}".format(workflow_id)
        return self._client._delete(self.BASE_URL + endpoint)

    def enroll_a_contact_into_workflow(self, workflow_id, contact_email):
        """
        Add a contact to a workflow.

        You will want to use this in the event that a contact meets a set
        of criteria that makes enrolling them in a workflow relevant to them,
        for example downloading a whitepaper and then getting enrolled in a
        workflow that sends emails based on the content of that whitepaper.
        """
        endpoint = "/workflows/{}/enrollments/contacts/{}".format(workflow_id, contact_email)
        return self._client._post("automation/v2" + endpoint)

    def unenroll_a_contact_into_workflow(self, workflow_id, contact_email):
        """
        Remove a contact from a workflow.

        If a contact is removed from a workflow, all future events that
        they are scheduled for will not take place. One application of this
        endpoint could be removing a contact from a marketing automation workflow
        if they are closed as a customer in your CRM.
        """
        endpoint = "/workflows/{}/enrollments/contacts/{}".format(workflow_id, contact_email)
        return self._client._delete("automation/v2" + endpoint)
