# tests.py in your app folder (e.g., Q4/tests.py)
from django.test import RequestFactory, TestCase
from django.urls import reverse
from Q4.views import vehicle_list
from django.template.response import TemplateResponse
import json

class VehicleListViewTests(TestCase):

    def run_test(self, test_name, func):
        try:
            func()
            print(f"Passed {test_name}")
        except AssertionError:
            print(f"Failed {test_name}")

    def test_template_name(self):
        self.run_test("test_vehicle_list_view_template_name", lambda: self._test_template_name())

    def _test_template_name(self):
        rf = RequestFactory()
        request = rf.get(reverse('vehicle_list'))
        response = vehicle_list(request)

        self.assertEqual(response.status_code, 200)

        # Ensure that the response is rendered
        response.render()

        self.assertContains(response, 'Vehicle List')

    def test_context_data(self):
        self.run_test("test_vehicle_list_view_context_data", lambda: self._test_context_data())

    def _test_context_data(self):
        rf = RequestFactory()
        request = rf.get(reverse('vehicle_list'))
        response = vehicle_list(request)

        self.assertEqual(response.status_code, 200)

        # Use response.context_data instead of response.context
        data = response.context_data

        self.assertIn('vehicles', data)

    def test_context_data_type(self):
        self.run_test("test_vehicle_list_view_context_data_type", lambda: self._test_context_data_type())

    def _test_context_data_type(self):
        rf = RequestFactory()
        request = rf.get(reverse('vehicle_list'))
        response = vehicle_list(request)

        self.assertEqual(response.status_code, 200)

        # Use response.context_data instead of response.context
        data = response.context_data

        self.assertIsInstance(data['vehicles'], list)

    def test_html_content(self):
        self.run_test("test_vehicle_list_view_html_content", lambda: self._test_html_content())

    def _test_html_content(self):
        rf = RequestFactory()
        request = rf.get(reverse('vehicle_list'))
        response = vehicle_list(request)

        self.assertEqual(response.status_code, 200)

        # Ensure that the response is rendered
        response.render()

        # Check if specific information about each vehicle is present in the HTML content
        expected_html_content = [
            'Toyota', 'Camry', '2022',
            'Ford', 'Mustang', '2021',
            'Honda', 'Civic', '2023'
        ]

        content = response.content.decode('utf-8')

        for item in expected_html_content:
            self.assertContains(response, item)

    def test_context_data_content(self):
        self.run_test("test_vehicle_list_view_context_data_content", lambda: self._test_context_data_content())

    def _test_context_data_content(self):
        rf = RequestFactory()
        request = rf.get(reverse('vehicle_list'))
        response = vehicle_list(request)

        self.assertEqual(response.status_code, 200)

        # Use response.context_data instead of response.context
        data = response.context_data

        expected_vehicles = [
            {'make': 'Toyota', 'model': 'Camry', 'year': 2022},
            {'make': 'Ford', 'model': 'Mustang', 'year': 2021},
            {'make': 'Honda', 'model': 'Civic', 'year': 2023},
        ]

        self.assertEqual(data['vehicles'], expected_vehicles)
