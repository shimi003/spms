from django.db import models

# Create your models here.

# 部品リスト
class Parts(models.Model):
    class Meta:
        db_table = 'parts'

    omit_name = models.CharField(verbose_name='略記', max_length=30, null=True)
    name = models.CharField(verbose_name='名称', max_length=100)
    maker = models.CharField(verbose_name='製造会社', max_length=100, null=True)
    type = models.CharField(verbose_name='部品種別', max_length=30, null=True)
    spec = models.CharField(verbose_name='型式', max_length=30, null=True)
    package = models.CharField(verbose_name='パッケージ', max_length=30, null=True)
    tolerance = models.TextField(verbose_name='公称精度', max_length=10, null=True)
    max_voltage = models.CharField(verbose_name='最大電圧', max_length=10, null=True)
    max_current = models.CharField(verbose_name='最大電流', max_length=10, null=True)
    max_wattage = models.CharField(verbose_name='最大電力', max_length=10, null=True)
    stocker = models.CharField(verbose_name='保管場所', max_length=30, null=True)
    mount_type = models.CharField(verbose_name='実装方法', max_length=10, null=True) # smd / dip
    last_used_date = models.DateField(verbose_name='最終使用日', null=True)
    distribute_status = models.CharField(verbose_name='ライフステータス', max_length=10, null=True) # 開発中/active/nrnd/製造中止/流通なし
    stock_type = models.CharField(verbose_name='保管形態', max_length=30, null=True) # Bulk/CutTape/Reel/Tray/Stick/Using/CommonReel
    rohs_status = models.CharField(verbose_name='Rohs対応', max_length=30, null=True) # rohs3とか？
    total_amount = models.IntegerField(verbose_name='在庫数量', null=False, default=0)
    use_amount = models.IntegerField(verbose_name='使用予定数', null=False, default=0)
    note = models.CharField(verbose_name='特記事項', max_length=100, null=True)


# 製品
class Product(models.Model):
    class Meta:
        db_table = 'product'

    name = models.CharField(verbose_name='製品名称', max_length=100)
    type_name = models.CharField(verbose_name='製品型式', max_length=100, null=True)
    company = models.CharField(verbose_name='受注元', max_length=100)
    note = models.CharField(verbose_name='特記事項', max_length=100, null=True)


# 受注リスト
class Order(models.Model):
    class Meta:
        db_table = 'order'

    ordered_date = models.DateField(verbose_name='受注日')
    ordered_product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    units = models.IntegerField(verbose_name='受注台数', null=False)
    price = models.IntegerField(verbose_name='受注金額', null=False)
    estimate_delivery_date = models.DateField(verbose_name='希望納期', null=True)
    actual_shipment_date = models.DateField(verbose_name='発送日', null=True)
    shipment_company = models.CharField(verbose_name='配送業者', max_length=30, null=True)
    shipment_code = models.CharField(verbose_name='送り状番号', max_length=30, null=True)
    bill_collect_date = models.DateField(verbose_name='売掛回収日', null=True)
    is_done = models.BooleanField(verbose_name='完了', null=True)
    note = models.CharField(verbose_name='特記事項', max_length=100, null=True)


# 内示リスト
class Order(models.Model):
    class Meta:
        db_table = 'order'

    ordered_date = models.DateField(verbose_name='受注日')
    ordered_product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    units = models.IntegerField(verbose_name='受注台数', null=False)
    price = models.IntegerField(verbose_name='受注金額', null=False)
    estimate_delivery_date = models.DateField(verbose_name='希望納期', null=False)
    actual_shipment_date = models.DateField(verbose_name='発送日', null=False)
    shipment_company = models.CharField(verbose_name='配送業者', max_length=30, null=True)
    shipment_code = models.CharField(verbose_name='送り状番号', max_length=30, null=True)
    note = models.CharField(verbose_name='特記事項', max_length=100, null=True)


# 予備部品リスト
class SpareParts(models.Model):
    class Meta:
        db_table = 'spare_parts'

    parts_id = models.ForeignKey(Parts, null=True, on_delete=models.SET_NULL)
    arrival_date = models.DateField(verbose_name='受け入れ日', null=False)
    packing_type = models.CharField(verbose_name='梱包形態', max_length=30, null=True) # Bulk/CutTape/Reel/ ...
    amount = models.IntegerField(verbose_name='受け入れ数量')
    out_of_date = models.DateField(verbose_name='払い出し日', null=False)
    note = models.CharField(verbose_name='特記事項', max_length=100, null=True)


# 予約済み部品リスト
class ReservedParts(models.Model):
    class Meta:
        db_table = 'reserved'

    parts_id = models.ForeignKey(Parts, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    schedule_date = models.DateField(verbose_name='受け入れ日', null=False)
    amount = models.IntegerField(verbose_name='受け入れ数量')
    note = models.CharField(verbose_name='特記事項', max_length=100, null=True)
