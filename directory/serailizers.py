from rest_framework import serializers

from directory.models import Site, SiteLog, SiteType, Direction


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = [
            'title_uz',
            'title_ru',
            'is_new'
        ]


class SiteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteType
        fields = [
            'title_uz',
            'title_ru'
        ]


class SiteLogSerailizer(serializers.ModelSerializer):
    class Meta:
        model = SiteLog
        fields = [
            'visitor_count',
            'created_at',
            'updated_at',
        ]


class SiteLogMainSerailizer(serializers.ModelSerializer):
    class Meta:
        model = SiteLog
        fields = [
            'site',
            'visitor_count',
            'created_at',
            'updated_at',
        ]


class SiteSerializer(serializers.ModelSerializer):
    types = SiteTypeSerializer(many=True)
    logs = SiteLogSerailizer(many=True)

    class Meta:
        model = Site
        fields = [
            'title_uz',
            'title_ru',
            'url',
            'about_uz',
            'about_ru',
            'about_ru',
            'types',
            'logs'
        ]


class SiteGetSerializer(serializers.ModelSerializer):
    types = SiteTypeSerializer(many=True)

    class Meta:
        model = Site
        fields = [
            'title_uz',
            'title_ru',
            'url',
            'about_uz',
            'about_ru',
            'types',
        ]


class SiteLogGetSerailizer(serializers.ModelSerializer):
    site = SiteGetSerializer(many=False)

    class Meta:
        model = SiteLog
        fields = [
            'site',
            'visitor_count',
            'created_at',
            'updated_at',
        ]
