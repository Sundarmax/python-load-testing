import requests


SERVER_URL = ""

# Get superbook -data 

USER_TOKEN ="TOKEN " + "00b34a029704eece31ca7320f4ba2ae34d7d55eb"


data = {"subject_list":"[]","grade_list":"[]"}
respose = requests.post(SERVER_URL+"/student/book/",data)


# check user login..

login_data = {}
response = requests.post(SERVER_URL+"/student/login/",login_data)

# check table of contents data . 

student_data = {"student_id":569,"subject_id":12242}
response = requests.post(SERVER_URL+"/student/content/",student_data)

# check left side menu data. 

content_data = {"student_id": 569, "maintopic_id": 22508, "subject_id": 12242}
response = requests.post(SERVER_URL + "/student/content/list/",content_data)

# check question folder data. 

quizbank = { "quiz_bankid" : 56038}
response = requests.post(SERVER_URL + "/student/course/quiz/",quizbank)

# check text content data. 
text = {"student_id":111579,"text_id": 82155}
response = requests.post(SERVER_URL + "/student/course/text/",text)

# get user-details
user = { "account_id": 111579}
response = requests.post(SERVER_URL + "/register/user-details/",user)

# store student panel issue. 
issue_data = {"super_book":12242,"student":569,"issue":1002,"issue_description":"","image_url":"","component_id":65819,"component_type":"question","status":0,"device_info":"Desktop","user_browser":"Chrome","operating_system":"windows-10","screen_size":"1707 x 250"}
result = requests.post(SERVER_URL+ "/api/store-student-panel-issues/",issue_data, headers = {'Authorization': USER_TOKEN} )

qs_data = {"student_id":569,"question_id":65819,"quizbank_id":53002,"type_of":"question","result":2,"answer_given":[{"id":"im7ib1xl7","q_type":"MCQ","answer":1},{"id":"fnnuryedm","q_type":"MCQ","answer":2},{"id":"7w902e7fh","q_type":"MCQ","answer":3},{"id":"5qvk0sy5v","q_type":"MCQ","answer":0},{"id":"csukv7z4w","q_type":"MCQ","answer":3},{"id":"mw3zvk09p","q_type":"MCQ","answer":1}],"time_taken":867,"total_mark":6,"actual_mark":5}
res     = requests.post(SERVER_URL + '/student-question-log/', qs_data, headers = {'Authorization': USER_TOKEN})

log = {"student_id":569,"component_type":"text","component_id":81928,"time":4}
result_log = requests.post(SERVER_URL + '/student-course-log/', log, headers = {'Authorization': USER_TOKEN})
print(result_log.text)


