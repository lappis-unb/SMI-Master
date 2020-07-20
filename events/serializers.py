from rest_framework import serializers as s

from .models import FailedConnectionSubordinateEvent
from .models import FailedConnectionTransductorEvent
from .models import VoltageRelatedEvent
from .models import Event


class VoltageRelatedEventSerializer(s.HyperlinkedModelSerializer):
    class Meta:
        model = VoltageRelatedEvent
        fields = (
            'id',
            'data',
            'created_at',
            'ended_at',
            'transductor'
        )


class FailedConnectionSubordinateEventSerializer(s.HyperlinkedModelSerializer):
    class Meta:
        model = FailedConnectionSubordinateEvent
        fields = (
            'id',
            'data',
            'created_at',
            'ended_at',
            'subordinate'
        )


class FailedConnectionTransductorEventSerializer(s.HyperlinkedModelSerializer):
    class Meta:
        model = FailedConnectionTransductorEvent
        fields = (
            'id',
            'data',
            'created_at',
            'ended_at',
            'transductor'
        )


class AllEventSerializer(s.HyperlinkedModelSerializer):
    count = s.IntegerField()
    subordinate_connection_fail = s.ListField(child=s.DictField())
    transductor_connection_fail = s.ListField(child=s.DictField())
    critical_tension = s.ListField(child=s.DictField())
    precarious_tension = s.ListField(child=s.DictField())
    phase_drop = s.ListField(child=s.DictField())

    class Meta:
        model = Event
        fields = (
            'count',
            'critical_tension',
            'precarious_tension',
            'phase_drop',
            'subordinate_connection_fail',
            'transductor_connection_fail'
        )
