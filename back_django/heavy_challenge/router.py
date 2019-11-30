from rest_framework import routers
from core.api.viewsets import ReportViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('reports', ReportViewSet, base_name='report')
router.register('users', UserViewSet, base_name='user')
