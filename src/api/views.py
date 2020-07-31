from . import serializers
from utils.models import Announcement, Feedback, Discussion, Note, Rating
from django.http import Http404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

#Announcements 
class Announcements(viewsets.ViewSet):
    """
    A simple ViewSet for listing  announcements.
    """

    def lists(self, request):
        announcements = Announcement.objects.all()
        serializer = serializers.AnnouncementSerializer(
            announcements, many=True)
        return Response(serializer.data)


    """
    A simple ViewSet for listing announcement based on table_name and table_id
    """

    def retrieve(self, request, table_name, table_id):
        announcements = Announcement.objects.filter(table_name=table_name, table_id=table_id)
        serializer = serializers.AnnouncementSerializer(
            announcements, many=True)
        return Response(serializer.data)


    """
    A simple ViewSet for storing announcement
    """

    def create(self, request):
        serializer = serializers.AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Discussions
class Discussions(viewsets.ViewSet):
    """
    A simple ViewSet for listing  discussions.
    """

    def lists(self, request):
        discussions = Discussion.objects.all()
        serializer = serializers.DiscussionSerializer(
            discussions, many=True)
        return Response(serializer.data)

    """
    A simple ViewSet for listing discussions based on table_name and table_id
    """

    def retrieve(self, request, table_name, table_id):
        discussions = Discussion.objects.filter(
            table_name=table_name, table_id=table_id)
        serializer = serializers.DiscussionSerializer(
            discussions, many=True)
        return Response(serializer.data)

    """
    A simple ViewSet for storing discussion
    """

    def create(self, request):
        serializer = serializers.DiscussionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Feedback
class Feedback(viewsets.ViewSet):
    """
    A simple ViewSet for listing  feedback.
    """

    def lists(self, request):
        feedback = Feedback.objects.all()
        serializer = serializers.FeedbackSerializer(
            feedback, many=True)
        return Response(serializer.data)

    """
    A simple ViewSet for listing feedback based on table_name and table_id
    """

    def retrieve(self, request, table_name, table_id):
        feedback = Feedback.objects.filter(
            table_name=table_name, table_id=table_id)
        serializer = serializers.FeedbackSerializer(
            feedback, many=True)
        return Response(serializer.data)

    """
    A simple ViewSet for storing feedback
    """

    def create(self, request):
        serializer = serializers.FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Ratings
class Ratings(viewsets.ViewSet):
    """
    A simple ViewSet for listing  ratings.
    """

    def lists(self, request):
        ratings = Rating.objects.all()
        serializer = serializers.RatingSerializer(
            ratings, many=True)
        return Response(serializer.data)

    """
    A simple ViewSet for listing ratings based on table_name and table_id
    """

    def retrieve(self, request, table_name, table_id):
        ratings = Rating.objects.filter(
            table_name=table_name, table_id=table_id)
        serializer = serializers.RatingSerializer(
            ratings, many=True)
        return Response(serializer.data)

    """
    A simple ViewSet for storing ratings
    """

    def create(self, request):
        serializer = serializers.RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Notes
class Notes(viewsets.ViewSet):
    """
    A simple ViewSet for listing  notes.
    """

    def lists(self, request):
        notes = Note.objects.all()
        serializer = serializers.NoteSerializer(
            notes, many=True)
        return Response(serializer.data)

    """
    A simple ViewSet for listing notes based on table_name and table_id
    """

    def retrieve(self, request, table_name, table_id):
        notes = Note.objects.filter(
            table_name=table_name, table_id=table_id)
        serializer = serializers.NoteSerializer(
            notes, many=True)
        return Response(serializer.data)

    """
    A simple ViewSet for storing notes
    """

    def create(self, request):
        serializer = serializers.NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

