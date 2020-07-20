from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.utils import timezone

from events.models import *
from campi.models import Campus

from transductors.models import EnergyTransductor

from subordinates.models import Subordinate

from measurements.models import MonthlyMeasurement
from measurements.models import MinutelyMeasurement
from measurements.models import QuarterlyMeasurement


class EventTestCase(TestCase):
    def setUp(self):
        self.campus = Campus.objects.create(
            name='UnB - Faculdade Gama',
            acronym='FGA',
        )

        self.transductor = EnergyTransductor.objects.create(
            serial_number='8764321',
            ip_address='111.101.111.11',
            broken=False,
            active=True,
            model='TR4020',
            geolocation_longitude=-24.4556,
            geolocation_latitude=-24.45996,
            firmware_version='0.1',
            campus=self.campus
        )

        self.subordinate = Subordinate.objects.create(
            ip_address='666.666.666.666',
            port=80,
            location='Somewhere near Wkïskh - Czech Republic',
            broken=False
        )

    def test_create_failed_connection_with_subordinate_event(self):
        before = len(FailedConnectionSubordinateEvent.objects.all())

        self.subordinate.set_broken(True)
        event = FailedConnectionSubordinateEvent.objects.last()

        self.assertEqual(
            before + 1, len(FailedConnectionSubordinateEvent.objects.all()))
        self.assertEqual(self.subordinate.ip_address, event.subordinate.ip_address)
