import unittest
from models.plan_statistics import find_volunteers, find_refugees
from models.camp import Camp
from models.refugee import Refugee
from models.volunteer import Volunteer
from models.plan import Plan
from datetime import date

class PlanStatisticsVolunteerTest(unittest.TestCase):
    """
    Class for testing cases involving volunteer counts in plan statistics.
    """

    def test_active_volunteer_count(self):
        """
        Test case where only active volunteers are in the file.
        If this passes, volunteer_count and number of volunteers added in test case should be equal.
        Expecting volunteer_count = 3.
        """
        Plan(name='test_plan1',
             emergency_type=Plan.EmergencyType.EARTHQUAKE,
             description='Test emergency plan',
             geographical_area='London',
             camps=[Camp(name='camp1')])
        volunteer_a = Volunteer(username='yunsy', password='root', firstname='Yunsy', lastname='Yin',
                                phone='+447519953189')
        volunteer_b = Volunteer(username='paul', password='root', firstname='Paul', lastname='Shoemaker',
                                phone='+447519955439')
        volunteer_c = Volunteer(username='gerald', password='root', firstname='Gerald', lastname='Smith',
                                phone='+447511111111')
        test_plan = Plan.find('test_plan1')
        test_camp = test_plan.camps.get('camp1')
        test_camp.volunteers.add(volunteer_a, volunteer_b, volunteer_c)

        volunteer_count = find_volunteers(test_camp)

        self.assertEqual(volunteer_count, 3)

    def test_deactivated_volunteer_not_counted(self):
        """
        Test case where only deactive volunteers are in the file.
        If this passes, volunteer_count should equal 0, since deactivated volunteers are not counted in this function.
        """
        Plan(name='test_plan2',
             emergency_type=Plan.EmergencyType.EARTHQUAKE,
             description='Test emergency plan',
             geographical_area='London',
             camps=[Camp(name='camp2')])
        volunteer_a = Volunteer(username='yunsy', password='root', firstname='Yunsy', lastname='Yin',
                                phone='+447519953189')
        volunteer_b = Volunteer(username='paul', password='root', firstname='Paul', lastname='Shoemaker',
                                phone='+447519955439')
        volunteer_c = Volunteer(username='gerald', password='root', firstname='Gerald', lastname='Smith',
                                phone='+447511111111')
        test_plan = Plan.find('test_plan2')
        test_camp = test_plan.camps.get('camp2')
        test_camp.volunteers.add(volunteer_a, volunteer_b, volunteer_c)
        volunteer_a.account_activated = False
        volunteer_b.account_activated = False
        volunteer_c.account_activated = False

        volunteer_count = find_volunteers(test_camp)
        self.assertEqual(volunteer_count, 0)

    def test_partially_active_volunteer_count(self):
        """
        Test case where some active and some deactivated volunteers are in the file.
        This test is to make sure that only the active volunteers are counted and the deactivated volunteers
        are disregarded in the count.
        """
        Plan(name='test_plan3',
             emergency_type=Plan.EmergencyType.EARTHQUAKE,
             description='Test emergency plan',
             geographical_area='London',
             camps=[Camp(name='camp3')])
        volunteer_a = Volunteer(username='yunsy', password='root', firstname='Yunsy', lastname='Yin',
                                phone='+447519953189')
        volunteer_b = Volunteer(username='paul', password='root', firstname='Paul', lastname='Shoemaker',
                                phone='+447519955439')
        volunteer_c = Volunteer(username='gerald', password='root', firstname='Gerald', lastname='Smith',
                                phone='+447511111111')
        test_plan = Plan.find('test_plan3')
        test_camp = test_plan.camps.get('camp3')
        test_camp.volunteers.add(volunteer_a, volunteer_b, volunteer_c)
        volunteer_a.account_activated = False

        volunteer_count = find_volunteers(test_camp)
        self.assertEqual(volunteer_count, 2)

    def test_deactivated_volunteer_not_counted(self):
        """
        Test case where only deactive volunteers are in the file.
        If this passes, volunteer_count should equal 0, since deactivated volunteers are not counted in this function.
        """
        Plan(name='test_plan4',
             emergency_type=Plan.EmergencyType.EARTHQUAKE,
             description='Test emergency plan',
             geographical_area='London',
             camps=[Camp(name='camp4')])
        volunteer_a = Volunteer(username='yunsy', password='root', firstname='Yunsy', lastname='Yin',
                                phone='+447519953189')
        volunteer_b = Volunteer(username='paul', password='root', firstname='Paul', lastname='Shoemaker',
                                phone='+447519955439')
        volunteer_c = Volunteer(username='gerald', password='root', firstname='Gerald', lastname='Smith',
                                phone='+447511111111')
        test_plan = Plan.find('test_plan4')
        test_camp = test_plan.camps.get('camp4')
        test_camp.volunteers.add(volunteer_a, volunteer_b, volunteer_c)
        volunteer_a.account_activated = False
        volunteer_b.account_activated = False
        volunteer_c.account_activated = False

        volunteer_count = find_volunteers(test_camp)
        self.assertEqual(volunteer_count, 0)


    def test_available_volunteer_count(self):
        """
        Test case where only active volunteers are in the file.
        If this passes, volunteer_count and number of volunteers added in test case should be equal.
        Expecting volunteer_count = 3.
        """
        Plan(name='test_plan4',
             emergency_type=Plan.EmergencyType.EARTHQUAKE,
             description='Test emergency plan',
             geographical_area='London',
             camps=[Camp(name='camp5')])
        volunteer_a = Volunteer(username='yunsy', password='root', firstname='Yunsy', lastname='Yin',
                                phone='+447519953189')
        volunteer_b = Volunteer(username='paul', password='root', firstname='Paul', lastname='Shoemaker',
                                phone='+447519955439')
        volunteer_c = Volunteer(username='gerald', password='root', firstname='Gerald', lastname='Smith',
                                phone='+447511111111')
        test_plan = Plan.find('test_plan4')
        test_camp = test_plan.camps.get('camp5')
        test_camp.volunteers.add(volunteer_a, volunteer_b, volunteer_c)

        volunteer_count = find_volunteers(test_camp)

        self.assertEqual(volunteer_count, 3)

    def test_unavailable_volunteer_not_counted(self):
        """
        Test case where only deactive volunteers are in the file.
        If this passes, volunteer_count should equal 0, since deactivated volunteers are not counted in this function.
        """
        Plan(name='test_plan5',
             emergency_type=Plan.EmergencyType.EARTHQUAKE,
             description='Test emergency plan',
             geographical_area='London',
             camps=[Camp(name='camp6')])
        volunteer_a = Volunteer(username='yunsy', password='root', firstname='Yunsy', lastname='Yin',
                                phone='+447519953189')
        volunteer_b = Volunteer(username='paul', password='root', firstname='Paul', lastname='Shoemaker',
                                phone='+447519955439')
        volunteer_c = Volunteer(username='gerald', password='root', firstname='Gerald', lastname='Smith',
                                phone='+447511111111')
        test_plan = Plan.find('test_plan5')
        test_camp = test_plan.camps.get('camp6')
        test_camp.volunteers.add(volunteer_a, volunteer_b, volunteer_c)
        volunteer_a.availability = False
        volunteer_b.availability = False
        volunteer_c.availability = False

        volunteer_count = find_volunteers(test_camp)
        self.assertEqual(volunteer_count, 0)

    def test_partially_available_volunteer_count(self):
        """
        Test case where some active and some deactivated volunteers are in the file.
        This test is to make sure that only the active volunteers are counted and the deactivated volunteers
        are disregarded in the count.
        """
        Plan(name='test_plan6',
             emergency_type=Plan.EmergencyType.EARTHQUAKE,
             description='Test emergency plan',
             geographical_area='London',
             camps=[Camp(name='camp7')])
        volunteer_a = Volunteer(username='yunsy', password='root', firstname='Yunsy', lastname='Yin',
                                phone='+447519953189')
        volunteer_b = Volunteer(username='paul', password='root', firstname='Paul', lastname='Shoemaker',
                                phone='+447519955439')
        volunteer_c = Volunteer(username='gerald', password='root', firstname='Gerald', lastname='Smith',
                                phone='+447511111111')
        test_plan = Plan.find('test_plan6')
        test_camp = test_plan.camps.get('camp7')
        test_camp.volunteers.add(volunteer_a, volunteer_b, volunteer_c)
        volunteer_a.availability = False

        volunteer_count = find_volunteers(test_camp)
        self.assertEqual(volunteer_count, 2)

    def test_unavailable_volunteer_not_counted(self):
        """
        Test case where only deactive volunteers are in the file.
        If this passes, volunteer_count should equal 0, since deactivated volunteers are not counted in this function.
        """
        Plan(name='test_plan7',
             emergency_type=Plan.EmergencyType.EARTHQUAKE,
             description='Test emergency plan',
             geographical_area='London',
             camps=[Camp(name='camp8')])
        volunteer_a = Volunteer(username='yunsy', password='root', firstname='Yunsy', lastname='Yin',
                                phone='+447519953189')
        volunteer_b = Volunteer(username='paul', password='root', firstname='Paul', lastname='Shoemaker',
                                phone='+447519955439')
        volunteer_c = Volunteer(username='gerald', password='root', firstname='Gerald', lastname='Smith',
                                phone='+447511111111')
        test_plan = Plan.find('test_plan7')
        test_camp = test_plan.camps.get('camp8')
        test_camp.volunteers.add(volunteer_a, volunteer_b, volunteer_c)
        volunteer_a.availability = False
        volunteer_b.availability = False
        volunteer_c.availability = False

        volunteer_count = find_volunteers(test_camp)
        self.assertEqual(volunteer_count, 0)


    def test_no_volunteers_in_file(self):
        """
        Test case where no volunteers are in the file for a camp.
        In this case, expecting volunteer_count = 0, since there are no volunteers to count.
        """
        Plan(name='test_plan8',
             emergency_type=Plan.EmergencyType.EARTHQUAKE,
             description='Test emergency plan',
             geographical_area='London',
                         camps=[Camp(name='camp9')])
        test_plan = Plan.find('test_plan8')
        test_camp = test_plan.camps.get('camp9')
        volunteer_count = find_volunteers(test_camp)

        self.assertEqual(volunteer_count, 0)

    def test_volunteer_count_multiple_camps(self):
        """
        Test case where only active volunteers are in the file and active volunteers are at multiple camps.
        """
        Plan(name='test_plan8',
             emergency_type=Plan.EmergencyType.EARTHQUAKE,
             description='Test emergency plan',
             geographical_area='London',
             camps=[Camp(name='camp10'), Camp(name='camp11')])
        volunteer_a = Volunteer(username='yunsy', password='root', firstname='Yunsy', lastname='Yin',
                                phone='+447519953189')
        volunteer_b = Volunteer(username='paul', password='root', firstname='Paul', lastname='Shoemaker',
                                phone='+447519955439')
        volunteer_c = Volunteer(username='gerald', password='root', firstname='Gerald', lastname='Smith',
                                phone='+447511111111')
        test_plan = Plan.find('test_plan8')
        test_camp1 = test_plan.camps.get('camp10')
        test_camp1.volunteers.add(volunteer_a)
        test_camp2 = test_plan.camps.get('camp11')
        test_camp2.volunteers.add(volunteer_b, volunteer_c)

        volunteer_count_camp1 = find_volunteers(test_camp1)
        volunteer_count_camp2 = find_volunteers(test_camp2)

        self.assertEqual(volunteer_count_camp1, 1)
        self.assertEqual(volunteer_count_camp2, 2)


class PlanStatisticsRefugeeTest(unittest.TestCase):
    """
    Class for testing cases involving refugee counts in plan statistics.
    """
# Notes for find_refugee testing:
    def test_refugee_count_single_family(self):
        """
        Test to check that refugee count is correct for a single refugee family.
        """
        Plan(name='test_plan9',
             emergency_type=Plan.EmergencyType.EARTHQUAKE,
             description='Test emergency plan',
             geographical_area='London',
             camps=[Camp(name='camp12')])
        refugee1 = Refugee(firstname="Tom",
                           lastname="Bond",
                           num_of_family_member=6,
                           starting_date=date(2020, 1, 2),
                           medical_condition_type=[Refugee.MedicalCondition.HIV, Refugee.MedicalCondition.CANCER])
        test_plan = Plan.find('test_plan9')
        test_camp = test_plan.camps.get('camp12')
        test_camp.refugees.add(refugee1)

        refugee_count = find_refugees(test_camp)

        self.assertEqual(refugee_count, 6)
#         NEED TO CHECK THIS 7 IS CORRECT

    def test_refugee_count_multiple_families_one_camp(self):
        """
        Test to check that refugee count is correct for multiple refugee families at a single camp.
        """
        Plan(name='test_plan10',
             emergency_type=Plan.EmergencyType.EARTHQUAKE,
             description='Test emergency plan',
             geographical_area='London',
             camps=[Camp(name='camp13')])
        refugee1 = Refugee(firstname="Tom",
                           lastname="Bond",
                           num_of_family_member=6,
                           starting_date=date(2020, 1, 2),
                           medical_condition_type=[Refugee.MedicalCondition.HIV, Refugee.MedicalCondition.CANCER])
        refugee2 = Refugee(firstname="Harry",
                           lastname="Ranger",
                           num_of_family_member=1,
                           starting_date=date(2020, 1, 2),
                           medical_condition_type=[Refugee.MedicalCondition.HIV, Refugee.MedicalCondition.CANCER])
        test_plan = Plan.find('test_plan10')
        test_camp = test_plan.camps.get('camp13')
        test_camp.refugees.add(refugee1, refugee2)

        refugee_count = find_refugees(test_camp)

        self.assertEqual(refugee_count, 7)

    def test_refugee_count_multiple_camps(self):
        """
        Test to check that refugee count is correct for a single camp when refugee families exist at multiple
        camps under the same plan.            """
        Plan(name='test_plan11',
             emergency_type=Plan.EmergencyType.EARTHQUAKE,
             description='Test emergency plan',
             geographical_area='London',
             camps=[Camp(name='camp14'), Camp(name='camp15')])
        refugee1 = Refugee(firstname="Tom",
                           lastname="Bond",
                           num_of_family_member=6,
                           starting_date=date(2020, 1, 2),
                           medical_condition_type=[Refugee.MedicalCondition.HIV, Refugee.MedicalCondition.CANCER])
        refugee2 = Refugee(firstname="Harry",
                           lastname="Ranger",
                           num_of_family_member=1,
                           starting_date=date(2020, 1, 2),
                           medical_condition_type=[Refugee.MedicalCondition.HIV, Refugee.MedicalCondition.CANCER])
        test_plan = Plan.find('test_plan11')
        test_camp1 = test_plan.camps.get('camp14')
        test_camp2 = test_plan.camps.get('camp15')
        test_camp2.refugees.add(refugee1, refugee2)


        refugee_count_camp1 = find_refugees(test_camp1)
        refugee_count_camp2 = find_refugees(test_camp2)

        self.assertEqual(refugee_count_camp1, 0)
        self.assertEqual(refugee_count_camp2, 7)


# Notes for plan_statistics_function testing:
# 1. Test volunteer_count and refugee_count correct for each camp
