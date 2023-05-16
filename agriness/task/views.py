from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from .models import Task


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        is_done = self.request.query_params.get('is_done', None)
        search = self.request.query_params.get('search', None)

        if is_done is not None:
            if eval(is_done):
                queryset = Task.objects.filter(finished_at__isnull=False)
            else:
                queryset = Task.objects.filter(finished_at__isnull=True)
            return queryset

        if search is not None:
            queryset = Task.objects.filter(name__icontains=search)
            return queryset

        queryset = Task.objects.all()
        return queryset
