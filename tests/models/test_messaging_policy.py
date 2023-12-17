from django_slack_bot.models import SlackMessagingPolicy
from tests._helpers import ModelTestBase

from ._factories import SlackMessagingPolicyFactory


class SlackMessagingPolicyTests(ModelTestBase):
    model_cls = SlackMessagingPolicy
    factory_cls = SlackMessagingPolicyFactory
