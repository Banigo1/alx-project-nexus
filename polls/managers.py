from django.db import models
from django.db.models import Count, F, Window
from django.db.models.functions import Rank


class PollManager(models.Manager):
    def get_with_vote_stats(self, poll_id):
        """
        Get a poll with preloaded vote statistics in a single, optimized query.
        """
        return self.filter(id=poll_id).annotate(
            total_votes=Count('options__votes', distinct=True),
            option_count=Count('options', distinct=True)
        ).first()
    
    def get_trending_polls(self, limit=5):
        """
        Get trending polls based on recent vote activity.
        """
        return self.filter(is_active=True).annotate(
            vote_count=Count('options__votes')
        ).order_by('-vote_count')[:limit]


class OptionManager(models.Manager):
    def get_with_vote_counts(self, poll_id):
        """
        Get all options for a poll with vote counts in a single query.
        """
        return self.filter(poll_id=poll_id).annotate(
            vote_count=Count('votes')
        ).order_by('-vote_count')
    
    def get_ranked_options(self, poll_id):
        """
        Get options with rank based on vote count.
        """
        return self.filter(poll_id=poll_id).annotate(
            vote_count=Count('votes'),
            rank=Window(
                expression=Rank(),
                order_by=F('vote_count').desc()
            )
        ).order_by('rank')