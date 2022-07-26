from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

class GroupRequiredMixin(object):
    group_required = []

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.groups.filter(name__in=self.group_required).exists():
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied


