from django.test import TestCase
from .models import Input
from compute import compute
# Create your tests here.
class InputTestCase(TestCase):




    def test_handleslowest(self):


        # verify that for n=1, results=1
        numsides=1
        Input.objects.create(Numsides=numsides)


        self.assertEqual(compute(numsides), 1)

    def test_handleshigh(self):
        #verify that for n=1000, program does not overflow

        numsides=1000
        Input.objects.create(Numsides=numsides)
        self.assertTrue(compute(numsides))

    def test_negative(self):
        #verify that the compute raises an exception for negative number
        error_occured = False
        numsides = -1


        try:
            Input.objects.create(Numsides=numsides)
            print compute(numsides)

        except:
            error_occured = True

        self.assertTrue(error_occured)

    def test_alpha(self):
        numsides = "xyz"
        error_occured = False


        try:
            Input.objects.create(Numsides=numsides)
            compute(numsides)
        except:
            error_occured = True

        self.assertTrue(error_occured)

    def test_decimal(self):
        numsides = 1.5
        error_occured = False


        try:
            Input.objects.create(Numsides=numsides)
            compute(numsides)
        except:
            error_occured = True
        self.assertTrue(error_occured)