from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import User
from .serializers import UserSerializer

# Only admin দেখতে পারবে সকল রেজিস্টার্ড ইউজার
@api_view(['GET'])
@permission_classes([IsAdminUser])
def user_list(request):
    users = User.objects.filter(is_admin=False)  # Admin ছাড়া সবাই
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# Admin চাইলে ইউজার delete করতে পারবে
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({'message': 'User deleted'})
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)
