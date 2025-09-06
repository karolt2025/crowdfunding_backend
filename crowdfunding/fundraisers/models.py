from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ValidationError

# class Fundraiser(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     goal = models.IntegerField()
#     is_open = models.BooleanField()
#     date_created = models.DateTimeField(auto_now_add=True)
#     deadline = models.DateTimeField(null=True, blank=True)
#     owner = models.ForeignKey(
#         get_user_model(),
#         related_name='owned_fundraisers',
#         on_delete=models.CASCADE
#     )
#     def total_contributions(self):
#         return sum(c.amount for c in self.contributions.all())

#     def __str__(self):
#         return self.title

class Fundraiser(models.Model):
    # Common fields
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_open = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    owner = models.ForeignKey(
        get_user_model(),
        related_name='owned_fundraisers',
        on_delete=models.CASCADE
    )

    # Option 1: Monetary Goal Fundraiser
    goal_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Total amount to raise if this is a cash fundraiser."
    )

    # Option 2: Item-Based Fundraiser
    item_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Name of the item if this is an item-based fundraiser."
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Price per item."
    )
    quantity_needed = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    external_url = models.URLField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    def clean(self):
        """Custom validation to ensure either goal_amount or item is set, but not both."""
        is_cash = self.goal_amount is not None
        is_item = self.item_name is not None

        if is_cash and is_item:
            raise ValidationError("You can only set either 'goal_amount' or 'item_name', not both.")
        if not is_cash and not is_item:
            raise ValidationError("You must set either 'goal_amount' or 'item_name'.")

        # If item is set, ensure price and quantity are provided
        if is_item:
            if self.price is None or self.quantity_needed is None:
                raise ValidationError("If 'item_name' is set, 'price' and 'quantity_needed' are required.")

    def total_contributions(self):
        return sum(c.amount for c in self.contributions.all())

    def __str__(self):
        return self.title

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    fundraiser = models.ForeignKey(
        'Fundraiser',
        related_name='pledges',
        on_delete=models.CASCADE
    )
    supporter = models.ForeignKey(
        get_user_model(),
        related_name='pledges',
        on_delete=models.CASCADE
    )
