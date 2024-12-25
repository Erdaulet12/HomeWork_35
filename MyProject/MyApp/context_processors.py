from django.contrib.auth.models import Group


def user_groups(request):
	if request.user.is_authenticated:
		groups = request.user.groups.all()
	else:
		groups = Group.objects.none()

	return {'user_groups': groups}
