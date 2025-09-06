from rest_framework import serializers
from django.apps import apps
# from .models import Fundraiser

# class FundraiserSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.id')

#     class Meta:
#         model = apps.get_model('fundraisers.Fundraiser')
#         fields = '__all__'

class FundraiserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'
        read_only_fields = ['owner', 'date_created']

    def validate(self, data):
        goal_amount = data.get('goal_amount')
        item_name = data.get('item_name')
        price = data.get('price')
        quantity_needed = data.get('quantity_needed')

        is_cash = goal_amount is not None
        is_item = item_name is not None

        # Only one of cash or item must be provided
        if is_cash and is_item:
            raise serializers.ValidationError("You can only set either 'goal_amount' or 'item_name', not both.")
        if not is_cash and not is_item:
            raise serializers.ValidationError("You must set either 'goal_amount' or 'item_name'.")

        # If item is selected, price and quantity are required
        if is_item:
            if price is None:
                raise serializers.ValidationError("'price' is required when 'item_name' is set.")
            if quantity_needed is None:
                raise serializers.ValidationError("'quantity_needed' is required when 'item_name' is set.")

        return data

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')

    class Meta:
        model = apps.get_model('fundraisers.Pledge')
        fields = '__all__'

    # def update (self, instance, validated_data):
    #     instance.id = validated_data.get('id', instance.id)
    #     instance.supporter = validated_data.get('supporter', instance.supporter)
    #     instance.amount = validated_data.get('amount', instance.amount)
    #     instance.comment = validated_data.get('comment', instance.comment)
    #     instance.anonymous = validated_data.get('anonymous', instance.anonymous)
    #     instance.fundraiser = validated_data.get('fundraiser', instance.fundraiser)
    #     instance.save()
    #     return instance

class FundraiserDetailSerializer(FundraiserSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
    
# class ItemSerializer(serializers.ModelSerializer):
#     quantity_funded = serializers.SerializerMethodField()
#     quantity_remaining = serializers.SerializerMethodField()
#     is_fully_funded = serializers.SerializerMethodField()

#     class Meta:
#         model = apps.get_model('fundraisers.Item')
#         fields = ['id', 'name', 'description', 'price', 'quantity_needed',
#             'quantity_funded', 'quantity_remaining', 'is_fully_funded', 'external_url']

#     def get_quantity_funded(self, obj):
#         return obj.quantity_funded()

#     def get_quantity_remaining(self, obj):
#         return obj.quantity_remaining()

#     def get_is_fully_funded(self, obj):
#         return obj.is_fully_funded()