import requests

url = "http://158.140.141.101:8000/api/student/book/"

data = {"subject_list":"[]","grade_list":"[]"}

respose = requests.post(url,data)

print(respose.text)
