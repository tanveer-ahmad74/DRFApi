from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from .models import user
from .serializers import UserSerializer




class UserList(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = user.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserListRUD(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = user.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = user.objects.all()
#     serializer_class = UserSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = user.objects.all()
#     serializer_class = UserSerializer


# class UserViewSet(viewsets.ViewSet):
#     def list(self, request):
#         users = user.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response({'message': 'Created Successfully'})
#
#     def retrieve(self, request, pk=None):
#         id =pk
#         if id is not None:
#             stu = user.objects.get(id=id)
#             serializer = UserSerializer(stu)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         id=pk
#         us = user.objects.get(pk=id)
#         serializer = UserSerializer(us, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response({'message': 'Updated Successfully'})
#
#     def partial_update(self, request, pk=None):
#         id = pk
#         us = user.objects.get(pk=id)
#         serializer = UserSerializer(us, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#         return Response({'message': ' Partial Updated Successfully'})
#
#     def destroy(self, request, pk=None):
#         id=pk
#         us =user.objects.get(pk=id)
#         us.delete()
#         return Response({'message': 'Successfully Deleted'})
