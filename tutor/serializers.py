from rest_framework import serializers
from .models import User,Class,Connect,Connect_Message,Connect_Message_Attach, level, country, city, rating, connect_status

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class ConnectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect
        fields = '__all__'

class CnctMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect_Message
        fields = '__all__'

class CMAttachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect_Message_Attach
        fields = '__all__'

class Level(serializers.ModelSerializer):
    class Meta:
        model = level
        fields = '__all__'

class Country(serializers.ModelSerializer):
    class Meta:
        model = country
        fields = '__all__'

class City(serializers.ModelSerializer):
    class Meta:
        model = city
        fields = '__all__'

class Rating(serializers.ModelSerializer):
    class Meta:
        model = rating
        fields = '__all__'

class ConnectStatus(serializers.ModelSerializer):
    class Meta:
        model = connect_status
        fields = '__all__'

