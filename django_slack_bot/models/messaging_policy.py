"""Messaging policy model."""
from __future__ import annotations

from django.db import models
from django.utils.translation import gettext_lazy as _

from django_slack_bot.utils import validators
from django_slack_bot.utils.model_mixins import TimestampMixin

from .message_recipient import SlackMessageRecipient


class SlackMessagingPolicyManager(models.Manager["SlackMessagingPolicy"]):
    """Manager for Slack messaging policies."""

    def get_by_code(self, code: str) -> SlackMessagingPolicy:
        """Get policy by its code."""
        return self.get(code=code)


class SlackMessagingPolicy(TimestampMixin, models.Model):
    """An Slack messaging policy which determines message content and those who receive messages."""

    code = models.CharField(
        verbose_name=_("Code"),
        help_text=_("Unique message code for lookup, mostly by human."),
        max_length=32,
        unique=True,
    )
    enabled = models.BooleanField(
        verbose_name=_("Enabled"),
        help_text=_("Turn on or off current messaging policy."),
        default=True,
    )
    recipients = models.ManyToManyField(
        SlackMessageRecipient,
        verbose_name=_("Message recipients"),
        help_text=_("Those who will receive messages."),
    )
    template = models.JSONField(
        verbose_name=_("Message template object"),
        help_text=_("Dictionary-based template object."),
        validators=[validators.dict_template_validator],
        null=True,
        blank=True,
    )

    # Type is too obvious but due to limits...
    objects: SlackMessagingPolicyManager = SlackMessagingPolicyManager()

    class Meta:  # noqa: D106
        verbose_name = _("Messaging Policy")
        verbose_name_plural = _("Messaging Policies")

    # TODO(lasuillard): Type stubs for related managers

    def __str__(self) -> str:  # noqa: D105
        if self.enabled:
            return _("{code} (Enabled)").format(code=self.code)

        return _("{code} (Disabled)").format(code=self.code)
