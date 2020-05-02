from locust import HttpLocust, TaskSet, task, between

# SERVER_URL =  http://158.140.141.101:8000

class TestBehaviour(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def hello_world(self):
        self.client.get("https://api.aeiser.com/api/student/subject-grade/list/")

class WebsiteTest(HttpLocust):
    task_set = TestBehaviour
    wait_time = between(0, 0)
