from rest_framework.permissions import BasePermission

class Instructorcheck(BasePermission):
    def has_permission(self, request, view):
        if request.user.usertype=='INSTRUCTOR':
            return True
        return False
        # return super().has_permission(request, view)

class NormalUserCheck(BasePermission):
    def has_permission(self, request, view):
        if request.user.usertype=='NORMAL':
            return True
        return False
        # return super().has_permission(request, view)