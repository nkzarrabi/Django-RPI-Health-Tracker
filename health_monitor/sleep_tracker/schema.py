from datetime import timedelta
import graphene
from graphene_django.types import DjangoObjectType
from .models import SleepData, SleepwalkingEvent


class SleepDataType(DjangoObjectType):
    class Meta:
        model = SleepData
        fields = "__all__"

class SleepwalkingEventType(DjangoObjectType):
    class Meta:
        model = SleepwalkingEvent
        fields = "__all__"

class Query(graphene.ObjectType):
    all_sleep_data = graphene.List(SleepDataType)
    all_sleepwalking_events = graphene.List(SleepwalkingEventType)

    def resolve_all_sleep_data(self, info):
        return SleepData.objects.all()
    
    def resolve_all_sleepwalking_events(self, info):
        return SleepwalkingEvent.objects.all()

class CreateSleepData(graphene.Mutation):
    class Arguments:
        start_time = graphene.DateTime(required=True)
        end_time = graphene.DateTime(required=True)
        deep_sleep_duration = graphene.Int(required=True)  # Expected as minutes
        light_sleep_duration = graphene.Int(required=True)  # Expected as minutes

    sleep_data = graphene.Field(SleepDataType)

    def mutate(self, info, start_time, end_time, deep_sleep_duration, light_sleep_duration):
        sleep_data = SleepData(
            start_time=start_time,
            end_time=end_time,
            deep_sleep_duration=timedelta(minutes=deep_sleep_duration),
            light_sleep_duration=timedelta(minutes=light_sleep_duration),
            sleep_score=calculate_sleep_score(deep_sleep_duration, light_sleep_duration)
        )
        sleep_data.save()
        return CreateSleepData(sleep_data=sleep_data)

def calculate_sleep_score(deep, light):
    # Example: Simple scoring based on duration of deep sleep
    return deep * 2 + light


class CreateSleepwalkingEvent(graphene.Mutation):
    class Arguments:
        start_time = graphene.DateTime(required=True)
        end_time = graphene.DateTime(required=True)
        intensity = graphene.String(required=True)

    sleepwalking_event = graphene.Field(SleepwalkingEventType)

    def mutate(self, info, start_time, end_time, intensity):
        event = SleepwalkingEvent(
            start_time=start_time,
            end_time=end_time,
            intensity=intensity
        )
        event.save()
        return CreateSleepwalkingEvent(sleepwalking_event=event)
class Mutation(graphene.ObjectType):
    create_sleep_data = CreateSleepData.Field()
    create_sleepwalking_event = CreateSleepwalkingEvent.Field()
schema = graphene.Schema(query=Query, mutation=Mutation)
