from django.db import models
from django.utils import timezone
import uuid
from .managers import PollManager, OptionManager


class Poll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
        # Use custom manager
    objects = PollManager()
    
    class Meta:
        db_table = 'polls'
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['expires_at']),
            models.Index(fields=['is_active']),
        ]
    
    def __str__(self):
        return self.title
    
    @property
    def is_expired(self):
        if self.expires_at and timezone.now() > self.expires_at:
            return True
        return False
    
    def save(self, *args, **kwargs):
        # Automatically set is_active to False if the poll has expired
        if self.is_expired:
            self.is_active = False
        super().save(*args, **kwargs)


class Option(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
        # Use custom manager
    objects = OptionManager()
    
    class Meta:
        db_table = 'poll_options'
        indexes = [
            models.Index(fields=['poll']),
        ]
    
    def __str__(self):
        return self.text

class Vote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    option = models.ForeignKey('Option', on_delete=models.CASCADE, related_name='votes')
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, related_name='votes')
    # voter_id = models.CharField(max_length=255)
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'votes'
        indexes = [
            models.Index(fields=['option']),
            # models.Index(fields=['voter_id']),
            models.Index(fields=['voted_at']),
            models.Index(fields=['poll']),
        ]
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=['voter_id', 'poll'],
        #         name='unique_voter_per_poll'
        #     )
        # ]

    def __str__(self):
        return f"Vote for {self.option} in poll {self.poll}"