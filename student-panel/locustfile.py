from locust import HttpLocust, TaskSet, task, between

# SERVER_URL = ""

SERVER_URL = ""

USER_TOKEN ="TOKEN " + "00b34a029704eece31ca7320f4ba2ae34d7d55eb"

class TestBehaviour(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def get_subject_grade_list(self):
        self.client.get( SERVER_URL + "/student/subject-grade/list/")

    @task(2)
    def get_superbook_data(self):
        data = {"subject_list":"[]","grade_list":"[]"}
        self.client.post(SERVER_URL + "/student/book/",data)
    
    @task(3)
    def check_user_login(self):
        login_data = {}
        self.client.post(SERVER_URL+"/student/login/",login_data)
    
    @task(4)
    def list_toc_data(self):
        student_data = {"student_id":569,"subject_id":12242}
        self.client.post(SERVER_URL+"/student/content/",student_data)

    @task(5)
    def list_content_data(self):
        content_data = {"student_id": 569, "maintopic_id": 22508, "subject_id": 12242}
        self.client.post(SERVER_URL + "/student/content/list/",content_data)
    
    @task(6)
    def get_question_data(self):
        quizbank = { "quiz_bankid" : 56038}
        self.client.post(SERVER_URL + "/student/course/quiz/",quizbank)

    @task(7)
    def get_text_data(self):
        text = {"student_id":111579,"text_id": 82155}
        self.client.post(SERVER_URL + "/student/course/text/",text)
    
    @task(8)
    def store_panel_issue(self):
        issue_data = {"super_book":12242,"student":569,"issue":1002,"issue_description":"","image_url":"","component_id":65819,"component_type":"question","status":0,"device_info":"Desktop","user_browser":"Chrome","operating_system":"windows-10","screen_size":"1707 x 250"}
        self.client.post(SERVER_URL+ "/api/store-student-panel-issues/",issue_data, headers = {'Authorization': USER_TOKEN})

    @task(9)
    def store_question_log(self):
        qs_data = {"student_id":569,"question_id":65819,"quizbank_id":53002,"type_of":"question","result":2,"answer_given":[{"id":"im7ib1xl7","q_type":"MCQ","answer":1},{"id":"fnnuryedm","q_type":"MCQ","answer":2},{"id":"7w902e7fh","q_type":"MCQ","answer":3},{"id":"5qvk0sy5v","q_type":"MCQ","answer":0},{"id":"csukv7z4w","q_type":"MCQ","answer":3},{"id":"mw3zvk09p","q_type":"MCQ","answer":1}],"time_taken":867,"total_mark":6,"actual_mark":5}
        self.client.post(SERVER_URL + '/student-question-log/', qs_data, headers = {'Authorization': USER_TOKEN})

    @task(10)
    def store_component_log(self):
        log = {"student_id":569,"component_type":"text","component_id":81928,"time":4}
        self.client.post(SERVER_URL + '/student-course-log/', log, headers = {'Authorization': USER_TOKEN})

class WebsiteTest(HttpLocust):
    task_set = TestBehaviour
    wait_time = between(0, 0)

