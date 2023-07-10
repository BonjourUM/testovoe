from django.db.models import RESTRICT, Model, AutoField, TextField, DateTimeField, ForeignKey, IntegerField, CharField
import datetime


class CreditRequest(Model):

    credit_request_id = AutoField(db_column='credit_request_id', primary_key=True)

    credit_request_num = IntegerField(db_column='credit_request_num')

    info = TextField(null=True)

    name_owner = TextField(db_column='name_owner', null=False)

    surname_owner = TextField(db_column='surname_owner', null=False)

    create_date = DateTimeField(db_column='create_date', default=datetime.datetime.now)

    class Meta:
        db_table = 'credit_request'


class Contract(Model):

    contract_id = AutoField(db_column='contract_id', primary_key=True)

    contract_num = IntegerField(db_column='contract_num')

    info = TextField(null=True)

    name_owner = TextField(db_column='name_owner', null=False)

    surname_owner = TextField(db_column='surname_owner', null=False)

    phone = TextField(null=True)

    credit_request_id = ForeignKey(CreditRequest, db_column='credit_request_id', on_delete=RESTRICT, null=False,
                                   related_name='credit')

    create_date = DateTimeField(db_column='create_date', default=datetime.datetime.now)

    class Meta:
        db_table = 'contract'


class Product(Model):
    product_id = AutoField(db_column='product_id', primary_key=True)

    product_name = TextField(db_column='product_name', null=False)

    info = TextField(null=True)

    inv_num = CharField(db_column='inv_num', null=False)

    credit_request_id = ForeignKey(CreditRequest, db_column='credit_request_id', on_delete=RESTRICT, null=False,
                                   related_name='credit_pr')

    create_date = DateTimeField(db_column='create_date', default=datetime.datetime.now)

    class Meta:
        db_table = 'product'


class Manufacturer(Model):
    manufacturer_id = AutoField(db_column='manufacturer_id', primary_key=True)

    manufacturer_name = TextField(db_column='manufacturer_name', null=False)

    info = TextField(null=True)

    inv_num = CharField(db_column='inv_num', null=False)

    product_id = ForeignKey(Product, db_column='product_id', on_delete=RESTRICT, null=False, related_name='product')

    create_date = DateTimeField(db_column='create_date', default=datetime.datetime.now)

    class Meta:
        db_table = 'manufacturer'
