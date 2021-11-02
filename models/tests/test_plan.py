import unittest
from datetime import date

from models.camp import Camp
from models.plan import Plan


class PlanTest(unittest.TestCase):

    def test_create_plan(self):
        plan = Plan('My Plan',
                    emergency_type=Plan.EmergencyType.EARTHQUAKE,
                    description='Test emergency plan',
                    geographical_area='',
                    start_date=date(2020, 1, 1))
        self.assertEqual("Plan 'My Plan'", str(plan))

    def test_open_camps(self):
        camp_1 = Camp('Camp 1')
        camp_2 = Camp('Camp 2')
        camp_3 = Camp('Camp 3')
        camp_4 = Camp('Camp 4')
        plan = Plan('My Plan',
                    emergency_type=Plan.EmergencyType.EARTHQUAKE,
                    description='Test emergency plan',
                    geographical_area='',
                    start_date=date(2020, 1, 1))
        plan.open_camps(camp_1, camp_2, camp_3)
        self.assertEqual({camp_1, camp_2, camp_3}, plan.camps)
        plan.open_camps(camp_3, camp_4)
        self.assertEqual({camp_1, camp_2, camp_3, camp_4}, plan.camps)

    def test_close_camps(self):
        camp_1 = Camp('Camp 1')
        camp_2 = Camp('Camp 2')
        camp_3 = Camp('Camp 3')
        camp_4 = Camp('Camp 4')
        plan = Plan('My Plan',
                    emergency_type=Plan.EmergencyType.EARTHQUAKE,
                    description='Test emergency plan',
                    geographical_area='',
                    start_date=date(2020, 1, 1))
        plan.open_camps(camp_1, camp_2, camp_3)
        plan.close_camps(camp_3)
        self.assertEqual({camp_1, camp_2}, plan.camps)
        plan.close_camps(camp_2, camp_4)
        self.assertEqual({camp_1}, plan.camps)
