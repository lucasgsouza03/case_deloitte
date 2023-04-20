import json
from rest_framework.test import APITestCase

from api.models import Discipline, ReportCard, Student, Grades

# Create your tests here.

class ApiUrlsTests(APITestCase):
    fixtures = ['./fixtures/db.json',]

    def setUp(self) -> None:
        data = {
            "email": "admin@email.com",
            "password": "admin"
        }
        response = self.client.post('/user/token/', data=json.dumps(data), content_type='application/json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.json()['access'])

        return super().setUp()

    def test_discipline(self):
        data = {
            "name": "Test Discipline",
            "workload": 10
        }
        response_create = self.client.post('/api/discipline/', data=json.dumps(data), content_type='application/json')

        discipline_id = response_create.json()['id']

        discipline_created = Discipline.objects.get(id=discipline_id)

        assert response_create.status_code == 201

        assert discipline_created

        response_list = self.client.get('/api/discipline/')

        assert response_list.status_code == 200

        response_retrieve = self.client.get(f"/api/discipline/{discipline_id}/")

        assert response_retrieve

        update_data = {
            "name": "Test Discipline",
            "workload": 20
        }
        response_update = self.client.put(f"/api/discipline/{discipline_id}/", data=json.dumps(update_data), content_type='application/json')

        assert response_update.status_code == 200

        discipline_updated = Discipline.objects.get(id=discipline_id)

        assert discipline_updated.workload == 20

        response_delete = self.client.delete(f"/api/discipline/{discipline_id}/")

        assert response_delete.status_code == 204

    def test_student(self):
        data = {
            "user": 1,
            "full_name": "Test Student",
            "birth_date": "1997-06-10"
        }
        response_create = self.client.post('/api/student/', data=json.dumps(data), content_type='application/json')

        student_id = response_create.json()['id']

        student_created = Student.objects.get(id=student_id)

        assert response_create.status_code == 201

        assert student_created

        response_list = self.client.get('/api/student/')

        assert response_list.status_code == 200

        response_retrieve = self.client.get(f"/api/student/{student_id}/")

        assert response_retrieve

        update_data = {
            "user": 1,
            "full_name": "Test Student Update",
            "birth_date": "1997-06-10"
        }
        response_update = self.client.put(f"/api/student/{student_id}/", data=json.dumps(update_data), content_type='application/json')

        assert response_update.status_code == 200

        student_updated = Student.objects.get(id=student_id)

        assert student_updated.full_name == "Test Student Update"

        response_delete = self.client.delete(f"/api/student/{student_id}/")

        assert response_delete.status_code == 204

    def test_grades(self):
        data = {
            "discipline": "Linguagem de Programação",
            "report_card": 1,
            "grade": '10'
        }
        response_create = self.client.post('/api/grades/', data=json.dumps(data), content_type='application/json')

        grade_id = response_create.json()['id']

        grade_created = Grades.objects.get(id=grade_id)

        assert response_create.status_code == 201

        assert grade_created

        response_list = self.client.get('/api/grades/')

        assert response_list.status_code == 200

        response_retrieve = self.client.get(f"/api/grades/{grade_id}/")

        assert response_retrieve

        update_data = {
            "discipline": "Linguagem de Programação",
            "report_card": 1,
            "grade": '5'
        }
        response_update = self.client.put(f"/api/grades/{grade_id}/", data=json.dumps(update_data), content_type='application/json')

        assert response_update.status_code == 200

        grade_updated = Grades.objects.get(id=grade_id)

        assert grade_updated.grade == '5'

        response_delete = self.client.delete(f"/api/grades/{grade_id}/")

        assert response_delete.status_code == 204

    def test_cards(self):

        response = self.client.get('/api/cards/')

        assert response.status_code == 200

        response = self.client.get('/api/cards/3/')

        assert response.status_code == 200

        data = {
            "discipline": "Linguagem de Programação",
            "report_card": 1,
            "grade": '10'
        }

        response = self.client.post('/api/cards/', data=json.dumps(data), content_type='application/json')

        assert response.status_code == 405

        update_data = {
            "discipline": "Linguagem de Programação",
            "report_card": 1,
            "grade": '5'
        }

        response = self.client.put('/api/cards/3/', data=json.dumps(update_data), content_type='application/json')

        assert response.status_code == 405

        response = self.client.delete('/api/cards/3/')

        assert response.status_code == 405

