from rest_framework import serializers

from .models import Shop

class ShopSerializer(serializers.ModelSerializer):
    gps  = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
         model = Shop
         fields = ['name', 'gps', 'tags']

    def get_gps(self, obj):
        gps  = {
            'lat' : obj.lat,
            'lon' : obj.lon
            }

        return gps

    def get_tags(self, obj):
        tags  = obj.tags.split()

        return tags