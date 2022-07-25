from django.core.exceptions import PermissionDenied

class GroupRequiredMixin(object):
    group_required = []

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or self.request.user.groups.filter(name__in=self.group_required).exists():
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied