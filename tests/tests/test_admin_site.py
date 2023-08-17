from django.contrib.auth.models import AbstractUser
from django.test import Client


def test_admin_site_opens(client: Client, django_user_model: AbstractUser):
    user = django_user_model.objects.create_user(username="test", password="test", is_superuser=True, is_staff=True)
    client.force_login(user)

    response = client.get("/admin/")
    assert response.status_code == 200
    assert "Django administration" in response.content.decode("utf-8")
