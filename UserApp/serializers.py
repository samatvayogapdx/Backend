from rest_framework import serializers
from .models import UserModel

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields =  '__all__'
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        validated_data.pop('groups', None) 
        validated_data.pop('user_permissions', None) 

        user=None
        try:
            print('Two')
            user=UserModel.objects.create_user(**validated_data)
            print('three')
        except Exception as e:
            print(e)

        return user