from django.test import TestCase
from django.utils import timezone

from subordinates.models import Subordinate
from transductors.models import EnergyTransductor
from campi.models import Campus

from django.db import IntegrityError
from django.core.exceptions import ValidationError, ObjectDoesNotExist


class TestSubordinatesModels(TestCase):

    def setUp(self):
        self.subordinate = Subordinate.objects.create(
            ip_address="1.1.1.1",
            location="UED FGA",
            broken=False
        )

        self.subordinate_1 = Subordinate.objects.create(
            ip_address="1.1.1.2",
            location="UAC FGA",
            broken=False
        )

        self.campus = Campus.objects.create(
            name='UnB - Faculdade Gama',
            acronym='FGA',
        )

        self.energy_transductor = EnergyTransductor.objects.create(
            serial_number='87654321',
            ip_address='192.168.1.1',
            geolocation_latitude=20.1,
            geolocation_longitude=37.9,
            name="MESP 1",
            broken=True,
            active=False,
            creation_date=timezone.now(),
            firmware_version='0.1',
            model='EnergyTransductorModel',
            campus=self.campus
        )

        # Jango Fett would be proud
        self.subordinate_1.transductors.add(self.energy_transductor)

    def test_should_create_new_subordinate(self):
        subordinates_before = len(Subordinate.objects.all())
        Subordinate.objects.create(
            ip_address="1.1.1.3",
            location="MESP FGA",
            broken=False
        )
        subordinates_after = len(Subordinate.objects.all())

        self.assertEqual(subordinates_before + 1, subordinates_after)

    def test_should_read_a_existent_subordinate_by_ip_address(self):
        subordinate = Subordinate.objects.get(ip_address="1.1.1.1")

        self.assertEqual(subordinate, self.subordinate)

    def test_should_update_a_specific_subordinate(self):
        subordinate = Subordinate.objects.get(ip_address="1.1.1.1")

        original_ip_address = subordinate.ip_address
        original_location = subordinate.location
        original_broken = subordinate.broken

        subordinate.ip_address = "2.2.2.2"
        subordinate.location = "FAU Darcy Ribeiro"
        subordinate.broken = True

        subordinate.save()

        new_ip_address = subordinate.ip_address
        new_location = subordinate.location
        new_broken = subordinate.broken

        self.assertNotEqual(original_ip_address, new_ip_address)
        self.assertNotEqual(original_location, new_location)
        self.assertNotEqual(original_broken, new_broken)

    def test_should_update_a_speficic_subordinate_with_dns(self):
        subordinate = Subordinate.objects.get(ip_address="1.1.1.1")
        subordinate.ip_address = "https://api.herokuapp.com/"

        self.assertIsNone(subordinate.save())

    def test_should_delete_a_existent_subordinate(self):
        subordinate = Subordinate.objects.get(ip_address="1.1.1.1")
        self.assertTrue(subordinate.delete())

    def test_should_not_delete_a_inexistent_subordinate(self):
        with self.assertRaises(ObjectDoesNotExist):
            Subordinate.objects.get(ip_address="10.10.10.10").delete()

    def test_associate_transductor_to_subordinate_server(self):
        length = len(self.subordinate.transductors.all())

        self.assertIsNone(
            self.subordinate.transductors.add(
                self.energy_transductor
            )
        )

        self.assertEqual((length + 1), len(self.subordinate.transductors.all()))

    def test_remove_transductor_from_subordinate_server(self):
        length = len(self.subordinate_1.transductors.all())

        self.assertIsNone(
            self.subordinate_1.transductors.remove(
                self.energy_transductor
            )
        )

        self.assertEqual((length - 1), len(self.subordinate_1.transductors.all()))
