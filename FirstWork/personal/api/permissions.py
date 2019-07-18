from rest_framework import permissions

class PostOwnPersonal(permissions.BasePermission):
    '''allow users to edit the own file'''

    def has_object_permission(self, request, view ,obj):
        '''Check if the user is trying to edit own record'''

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile == request.user