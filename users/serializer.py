from django.contrib.auth.models import User
from rest_framework import serializers


class UserCreateSeriliazer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name"]

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        # it will return the validated data and will not show the password bcoz of the 1st comment.
        # we can return new_user in case we want to add a sentence where username = f"(sentence {username})"
        return validated_data
