"""API permissions module.

This module specifies permissions that allow different actions over
the application objects using `Django Rest Framework`_.

.. _Django Rest Framework:
   http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/

"""
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Determines if the authenticated user should have permissions
        to perform GET, POST, PUT or DELETE actions.

        :param view: The view where the permission should be granted
        :param request: The request object
        """
        if view.action == 'create' or view.action == 'login' or view.action in ['retrieve', 'update', 'destroy']:
            return True
        elif view.action == 'list':
            return False
        else:
            return request.user.is_authenticated()


    def has_object_permission(self, request, view, obj):
        """
        Determines if the authenticated user should have permissions
        to perform GET, POST, PUT or DELETE actions on an object.

        :param view: The view where the permission should be granted
        :param request: The request object
        :param obj: The object
        """
        if view.action == 'retrieve':
            return request.user.is_authenticated()
        else:
            return request.user.is_superuser or request.user == obj
