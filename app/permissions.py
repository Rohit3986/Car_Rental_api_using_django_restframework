from rest_framework.permissions import BasePermission

class CarPermssions(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method=="GET" and request.user.user_type=="2":
            return True
        if request.user.is_authenticated and request.user.user_type=="1":
            return True
        return False

class BookingRequestPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method=="GET" and request.user.user_type=="2":
            return True
        if request.method in ("GET","PATCH") and request.user.is_authenticated and request.user.user_type=="1":
            return True
        return False