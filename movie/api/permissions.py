from rest_framework import permissions

class ReviewPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return request.user.is_staff or request.user == obj.user
        if request.method == 'GET':
            return True
        else:
            return request.user == obj.user
