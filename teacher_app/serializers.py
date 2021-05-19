from rest_framework import serializers
from teacher_app import models


class HelloSerializer(serializers.Serializer):
    name =serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = models.UserProfile
        fields =('id', 'email', 'name', 'password')

        extra_kwargs  ={
            'password':{
                'write_only': True,
                'style':{'input_type' : 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
        email =validated_data['email'],
        name=validated_data['name'],
        password= validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

# class ProfileFeedItemSerializer(serializers.ModelSerializer):
#     """Serializes profile feed items"""
#
#     class Meta:
#         model = models.ProfileFeedItem
#         fields = ('id', 'user_profile', 'status_text', 'created_on')
#         extra_kwargs = {'user_profile': {'read_only': True}}

class StudentItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    name =serializers.CharField(max_length=100)
    mobile_no=serializers.CharField(max_length=10)
    class Meta:
        model = models.StudentItem
        fields = ('id', 'name', 'email','admission_date', 'picture','mobile_no','gender','standard','reg_no')
        extra_kwargs = {'user_profile': {'read_only': True}}
class TeacherItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    name =serializers.CharField(max_length=100)
    subjects =serializers.CharField(max_length=100)
    mobile_no=serializers.CharField(max_length=10)
    designation=serializers.CharField(max_length=10)
    class Meta:
        model = models.TeacherItem
        fields = ('id', 'name','joining_date','subjects', 'age', 'mobile_no','designation','gender','reg_no')
        extra_kwargs = {'user_profile': {'read_only': True}}

class StaffItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    name =serializers.CharField(max_length=100)
    scale =serializers.CharField(max_length=100)
    pay =serializers.CharField(max_length=10)
    mobile_no=serializers.CharField(max_length=10)
    class Meta:
        model = models.StaffItem
        fields = ('id', 'name','joining_date','scale', 'pay', 'age', 'reg_no','mobile_no','gender')
        extra_kwargs = {'user_profile': {'read_only': True}}
