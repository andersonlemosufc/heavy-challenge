from rest_framework import viewsets
from django.contrib.auth.models import User
from core.models import Report
from .serializers import UserSerializer, ReportSerializer


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class ReportViewSet(viewsets.ModelViewSet):

    serializer_class = ReportSerializer

    def get_queryset(self):

        user_id = self.request.query_params.get('user_id', None)
        pagination_offset = self.request.query_params.get('pagination_offset', 0)
        pagination_limit = self.request.query_params.get('pagination_limit', None)

        if user_id:
            author = User.objects.get(id=user_id)
            written = set(author.report_set.all())
            answered = {response.report for response in author.report_response_set.all()}
            supervised = set(author.supervised_report_set.all())
            queryset = list(written.union(answered, supervised))
        else:
            queryset = Report.objects.all()

        if pagination_limit:
            pagination_limit = int(pagination_limit)+int(pagination_offset)

        queryset = queryset[pagination_offset:pagination_limit]

        return queryset
