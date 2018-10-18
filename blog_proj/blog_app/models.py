
# create a new attribute in your model




from django.contrib.auth.models import User
username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
