from datetime import datetime
from rest_framework import versioning, generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ResponseInfo(object):
    def __init__(self, **args):
        self.response = {"token": args.get('token', ""),
                         "message": args.get('message', ""),
                         }

class BaseApiView(APIView):
    """ Base class for all ApiViews """
    versioning_class = versioning.AcceptHeaderVersioning

    def __init__(self, **kwargs):
        super(BaseApiView, self).__init__(**kwargs)
        self.response = ResponseInfo().response

    def render_response(self, data, success, message, data_to_list=False, token="", status=200):
        response = ResponseInfo().response
        if data_to_list:
            data = list(data)

        response['isSuccess'] = success
        response['token'] = token
        response['message'] = message
        response['dataInfo'] = data
        return Response(response, status)

    def return_response(self):
        return Response(self.response)

    def json_date_time_serializer(self, obj):
        """JSON serializer for objects not serializable by default json code"""
        serial = False
        if isinstance(obj, datetime):
            serial = datetime.strftime(obj, '%d %b %Y, %H:%M:%S:%f')

        return serial


class AuthenticatedAPIView(BaseApiView):
    """ Base class for the views which needs to be authenticated. """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def __init__(self):
        super(AuthenticatedAPIView, self).__init__()

class BaseAPIListView(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginated_response = self.get_paginated_response(serializer.data)
            response = ResponseInfo().response
            response['isSuccess'] = True
            response['dataInfo'] = paginated_response.data['results']
            response['count'] = paginated_response.data['count']
            response['next'] = paginated_response.data['next']
            response['previous'] = paginated_response.data['previous']
            return Response(response)

        serializer = self.get_serializer(queryset, many=True)
        response = ResponseInfo().response
        response['isSuccess'] = True
        response['dataInfo'] = serializer.data
        return Response(response)
