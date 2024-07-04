from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from orders.serializers import OrderRequestSerializer, OrderResponseSerializer
from .models import Order

def serverMessage(msg):
    return {'message': f"{msg}"}

@api_view(['POST'])
def create_order(request):
    if request.method == 'POST':
        serializer = OrderRequestSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            return Response(OrderResponseSerializer(order).data, status=status.HTTP_201_CREATED)
        return Response(serverMessage("요청 양식 불량"), status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def order_detail(request, pk):
    if request.method == 'GET':
        try:
            order = Order.objects.get(pk=pk)
        except order.DoesNotExist:
            return Response(serverMessage("주문 내용이 존재하지 않습니다."), status=status.HTTP_404_NOT_FOUND) 
        serializer = OrderResponseSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        try:
          order = Order.objects.get(pk=pk)
        except order.DoesNotExist:
          return Response(serverMessage("주문 내용이 존재하지 않습니다."), status=status.HTTP_404_NOT_FOUND)
        order.delete()
        return Response(serverMessage("주문 취소 성공"), status=status.HTTP_200_OK)

@api_view(['GET'])
def list_orders_by_member(request):
    member_id = request.query_params.get('member_id')
    if not member_id:
        return Response(serverMessage("회원 ID 에러입니다."), status=status.HTTP_400_BAD_REQUEST)

    orders = Order.objects.filter(member_id=member_id)
    if not orders.exists():
        return Response(serverMessage("주문 내용이 존재하지 않습니다."), status=status.HTTP_404_NOT_FOUND)
    
    serializer = OrderResponseSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

