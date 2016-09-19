from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):

    def has_permission(self,request,view):
        """
        Define si el usuario autenticado en request.user tiene permiso para realizar
        la acción(GET,POST,PUT o Delete)
        """
        if view.action == 'create':
            return True
        elif request.user.is_superuser:
            return True
        elif view.action in ['retrieve','update','destroy']:
            return True
        else:
            return False
    def has_object_permission(self,request,view,obj):
        """
        Define si el usuario autenticado en request.user tiene permiso para realizar
        la accion (GET,PUT o delete) sobre el object obj
        """
        return request.user.is_superuser or request.user == obj
