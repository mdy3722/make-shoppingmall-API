from .models import Member
from .serializers import MemberSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError    # 중복으로 인한 무결성 에러 처리를 위해 가져옴

def severMessage(msg):
    return {'message' : f"{msg}"}

@api_view(['GET', 'POST'])
def members(request):
    match request.method:
        case 'GET':
          members = Member.objects.all()
          try:
              serializer = MemberSerializer(members, many=True)
              return Response(serializer.data, status=status.HTTP_200_OK)
          except members.DoesNotExist():
              return Response(severMessage("회원이 존재하지 않습니다."), status=status.HTTP_404_NOT_FOUND)
        case 'POST':
            serializer = MemberSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except IntegrityError:
                    # 중복된 항목 등의 데이터베이스 무결성 오류 처리
                    return Response(severMessage("회원 중복 등록"), status=status.HTTP_409_CONFLICT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PATCH', 'DELETE'])
def members_detail(request, pk):
    try:
        member = Member.objects.get(pk=pk)
    except member.DoesNotExist:
        return Response(severMessage("회원이 존재하지 않습니다."), status=status.HTTP_404_NOT_FOUND)
    match request.method:
        case 'GET':     # 특정 회원 조회
            serializer = MemberSerializer(member)
            return Response(serializer.data)
        case 'PATCH':     # 수정
            serializer = MemberSerializer(member, data=request.data) 
            # request 요청을 받은 item 내용을 serializer에 담음
            if not serializer.is_valid():
                return Response(severMessage("요청 양식 불량"), status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        case 'DELETE':
            member.delete()
            return Response(severMessage("회원 삭제 성공"), status=status.HTTP_200_OK)
