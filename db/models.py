from tortoise import fields
from tortoise.models import Model


class Purchase(Model):
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField()
    category = fields.CharField(max_length=50)
    name = fields.CharField(max_length=200)
    quantity = fields.FloatField()
    price = fields.FloatField()
    total = fields.FloatField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "purchases"