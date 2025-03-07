from rest_framework import serializers
from .models import Poll, Option, Vote
from django.db.models import Count


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'created_at']
        read_only_fields = ['id', 'created_at']


class PollSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, required=False)
    
    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'created_at', 'expires_at', 'is_active', 'options']
        read_only_fields = ['id', 'created_at', 'is_active']
    
    def create(self, validated_data):
        options_data = validated_data.pop('options', [])
        poll = Poll.objects.create(**validated_data)
        
        for option_data in options_data:
            Option.objects.create(poll=poll, **option_data)
        
        return poll


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'option', 'voter_id', 'voted_at']
        read_only_fields = ['id', 'voted_at']
    
    def validate(self, data):
        # Check if the poll is active
        poll = data['option'].poll
        if not poll.is_active:
            raise serializers.ValidationError("This poll is not active.")
        
        # Check if the poll has expired
        if poll.is_expired:
            raise serializers.ValidationError("This poll has expired.")
        
        # Check if voter has already voted in this poll
        # voter_id = data['voter_id']
        # existing_votes = Vote.objects.filter(
        #     option__poll=poll, 
        #     voter_id=voter_id
        # ).exists()
        
        # if existing_votes:
        #     raise serializers.ValidationError("You have already voted in this poll.")
        
        return data


class PollResultsSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    total_votes = serializers.SerializerMethodField()
    
    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'created_at', 'expires_at', 'is_active', 'total_votes', 'options']
    
    def get_options(self, obj):
        # Efficient query to get options with vote counts in a single database query
        options = Option.objects.filter(poll=obj).annotate(
            vote_count=Count('votes')
        ).values('id', 'text', 'vote_count')
        
        return options
    
    def get_total_votes(self, obj):
        # Sum of all votes for this poll
        return Vote.objects.filter(option__poll=obj).count()