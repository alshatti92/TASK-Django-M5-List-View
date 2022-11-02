from re import T
from django.contrib.auth.models import User
from rest_framework import serializers


class UserCreateSeriliazer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name"]

    def create(self, validated_data):
        # username = validated_data["username"]
        password = validated_data.pop("password")
        new_user = User(**validated_data)
        new_user.set_password(password)
        new_user.save()
        # it will return the validated data and will not show the password bcoz of the 1st comment.
        # we can return new_user in case we want to add a sentence where username = f"(sentence {username})"
        return new_user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        try:
            username = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError("if you forgot your username how you will remember your password !!")

        if not username.check_password(password):
            raise serializers.ValidationError("we didn't learn hot to retreive password, HAPPY ???")

        return data