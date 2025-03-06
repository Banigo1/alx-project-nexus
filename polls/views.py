from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.db.models import Count
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Poll, Option, Vote
from .serializers import (
    PollSerializer, 
    OptionSerializer, 
    VoteSerializer,
    PollResultsSerializer
)


class PollViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing polls.
    """
    queryset = Poll.objects.all().order_by('-created_at')
    serializer_class = PollSerializer
    
    @swagger_auto_schema(
        operation_description="Retrieve poll results with vote counts",
        responses={200: PollResultsSerializer()}
    )
    @action(detail=True, methods=['get'])
    def results(self, request, pk=None):
        """
        Get results for a specific poll.
        """
        poll = self.get_object()
        serializer = PollResultsSerializer(poll)
        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_description="Add options to an existing poll",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'options': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'text': openapi.Schema(type=openapi.TYPE_STRING)
                        }
                    )
                )
            }
        ),
        responses={201: OptionSerializer(many=True)}
    )
    @action(detail=True, methods=['post'])
    def add_options(self, request, pk=None):
        """
        Add options to an existing poll.
        """
        poll = self.get_object()
        options_data = request.data.get('options', [])
        
        created_options = []
        for option_data in options_data:
            option = Option.objects.create(poll=poll, **option_data)
            created_options.append(option)
        
        serializer = OptionSerializer(created_options, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VoteCreateView(generics.CreateAPIView):
    """
    API endpoint for casting a vote.
    """
    serializer_class = VoteSerializer
    
    @swagger_auto_schema(
        operation_description="Cast a vote for a poll option",
        request_body=VoteSerializer,
        responses={
            201: openapi.Response("Vote successfully recorded", VoteSerializer),
            400: "Bad request - validation error"
        }
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ActivePollsView(generics.ListAPIView):
    """
    API endpoint to list all active polls.
    """
    serializer_class = PollSerializer
    
    def get_queryset(self):
        return Poll.objects.filter(is_active=True).order_by('-created_at')