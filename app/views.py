from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Car,User,BookingRequest
from rest_framework import status
from .serializers import UserSerializer,UserLoginSerializer,UserProfileSeriallizer,CarSerializer,BookingRequestSerializer
from django.contrib.auth import authenticate,login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from .permissions import CarPermssions,BookingRequestPermissions


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistraion(APIView):
    def post(self,request,format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'registration succeed'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            username=serializer.data.get("username")
            password=serializer.data.get("password")
            user=authenticate(username=username,password=password)
            login(request,user)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({"tokens":token,"msg":"login sucessfull"})
            else:
                return Response({"error":"username or password is not valid"},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class UserProfileView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        serializer=UserProfileSeriallizer(request.user)

        return Response(serializer.data,status=status.HTTP_200_OK)
        #return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

class CarView(ModelViewSet):
    serializer_class=CarSerializer
    queryset=Car.objects.all()
    #authentication_classes=[BasicAuthentication]
    permission_classes=[CarPermssions]
    
    def get_queryset(self):
        if self.request.user.user_type=="1":
            return Car.objects.filter(owner_id=self.request.user.id)
        return Car.objects.all()

    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if request.user.user_type=="2":
            renter=User.objects.get(pk=int(request.user.id))
            requested_car=Car.objects.get(pk=int(kwargs['pk']))
            booking_data=BookingRequest(requested_by=renter,requested_to=requested_car.owner,requested_for=requested_car).save()
            return Response({'vehicle_details':serializer.data,'msg':'booking request has been sent to the owner for this vehicle'})
        return Response({'vehicle_details':serializer.data})
    
    def create(self, request, *args, **kwargs):
        if "owner" in request.data.keys():
            return Response({"error":["owner is not editable"]},status=status.HTTP_400_BAD_REQUEST)
        request.data["owner"]=request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookingRequestView(ModelViewSet):
    serializer_class=BookingRequestSerializer
    queryset=BookingRequest.objects.all()
    #authentication_classes=[BasicAuthentication]
    permission_classes=[BookingRequestPermissions]
    
    def get_queryset(self):
        if self.request.user.user_type=="1":
            return BookingRequest.objects.filter(requested_to=self.request.user.id)
        return BookingRequest.objects.filter(requested_by=self.request.user)

    def update(self, request, *args, **kwargs):
        print("requested data is ",request.data)
        if 'request_status' not in request.data.keys() or len(request.data)==0:
            return Response({"error":["request_status is not updated"]})
        if len(request.data)>1:
            return Response({'error':["only request_status is editable"]})
        instance = self.get_object()
        
        if instance.requested_to!=request.user:
            return Response({'error':["only vehicle owner can edit booking request"]})
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        self.perform_update(serializer)
        return Response(serializer.data)

    
        

    
    
    

        
    


