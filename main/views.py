from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MemberSerializer
from .models import Member


@api_view()
def get_users(request):
    members = Member.objects.all()
    ser_members = MemberSerializer(members, many=True)
    return Response(ser_members.data)
