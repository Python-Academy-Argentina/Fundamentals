from django.http import Http404
from django.db import transaction
from django.contrib.auth.hashers import make_password
from rest_framework import filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import UserSerializer, TuitSerializer
from .models import UserModel, TuitModel


class BaseView(APIView):
    '''
    Base view.
    '''
    model_class = None

    def filter_queryset(self, queryset):
        '''
        Custom filter parser.
        '''
        for backend in list(self.filter_backends):
            queryset = backend() \
                .filter_queryset(self.request, queryset, self)
        return queryset

    def get_queryset(self):
        '''
        Custom queryset.
        '''
        return self.model_class.objects.all()

    def get(self, request, format=None):
        '''
        Retrieve objects.
        '''
        objs = self.filter_queryset(self.get_queryset())
        serializer = self.serializer_class(objs, many=True)
        return Response(serializer.data)


class BaseDetailedView(APIView):
    '''
    Base detailed view.
    '''
    model_class = None

    def get_object(self, pk):
        '''
        Retrieve object by primary key.
        '''
        try:
            return self.model_class.objects.get(pk=pk)
        except self.model_class.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''
        Retrieve object.
        '''
        obj = self.get_object(pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)


class UserRegisterView(APIView):

    serializer_class = UserSerializer
    
    @transaction.atomic
    def post(self, request, format=None):
        '''
        Post new object.
        '''
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class UserView(BaseView):
    '''
    API User View.
    '''
    model_class = UserModel
    serializer_class = UserSerializer
    authentication_classes = [
        authentication.TokenAuthentication,
    ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = ['username']
    filterset_fields = [
        'username',
        'email',
    ]


class UserDetailedView(BaseDetailedView):
    '''
    User detailed view.
    '''
    model_class = UserModel
    serializer_class = UserSerializer
    authentication_classes = [
        authentication.TokenAuthentication,
    ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    @transaction.atomic
    def patch(self, request, pk, format=None):
        '''
        Patch object.
        '''
        obj = self.get_object(pk)
        
        if obj != request.user:
            msg = 'You cannot modify someone else\'s user.'
            return Response({'detail': [msg]},
                status=status.HTTP_401_UNAUTHORIZED
            )

        serializer = self.serializer_class(obj,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            if password:
                serializer.validated_data['password'] = make_password(password)
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class TuitView(BaseView):
    '''
    Tuit view.
    '''
    owner_class = UserModel
    model_class = TuitModel
    serializer_class = TuitSerializer
    authentication_classes = [
        authentication.TokenAuthentication,
    ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = [
        'content',
        'author__id',
    ]
    filterset_fields = [
        'content',
        'author__id',
    ]

    @transaction.atomic
    def post(self, request, format=None):
        '''
        Post new object.
        '''
        request.data['author'] = request.user.id
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class TuitDetailedView(BaseDetailedView):
    '''
    Tuit detailed view.
    '''
    model_class = TuitModel
    serializer_class = TuitSerializer
    authentication_classes = [
        authentication.TokenAuthentication,
    ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    @transaction.atomic
    def delete(self, request, pk, format=None):
        '''
        Delete object.
        '''
        obj = self.get_object(pk)

        if obj.author != request.user:
            msg = 'You cannot delete someone else\'s tuit.'
            return Response({'detail': [msg]},
                status=status.HTTP_401_UNAUTHORIZED
            )

        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
