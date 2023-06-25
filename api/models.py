from django.db import models


# Create your models here.
class SFTask(models.Model):
    #task_type = models.IntegerField(null=True)
    title = models.CharField(max_length=200)
    contents = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add = True, blank = True)
    #timestamp = models.DateTimeField(auto_now = True, blank = True)
    #completed = models.BooleanField(default = False, blank = True)
    completed_date = models.DateTimeField(null = True, blank = True)
    due_date = models.DateTimeField()
    creator = models.CharField(null=True, max_length=20)
    assignee = models.CharField(null=True, max_length=20)
    priority = models.CharField(max_length=10, null=True)

    class Meta:
        verbose_name = "Remark"
        verbose_name_plural = "Remarks"

    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.title, self.contents, self.created_date, self.completed_date,
                                            self.creator)


class SFComments(models.Model):
    comment = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now=True, blank=True)
    creator_id = models.IntegerField(null=True)
    task_id = models.IntegerField(null=True)

    def __str__(self):
        return '{0}  {1}  {2}  {3}'.format(self.comment, self.created_date, self.creator_id, self.task_id)


class SFInward(models.Model):
    created_date = models.DateTimeField(auto_now_add = True, blank = True)
    supplier = models.CharField(max_length=30)
    products = models.TextField()
    eta = models.DateTimeField()
    received_date = models.DateTimeField(null=True, blank=True)
    person_ordered = models.CharField(max_length=20)
    person_received = models.CharField(max_length=20, blank=True)
    product_owner = models.CharField(max_length=50, null=True)
    memo = models.TextField(blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)  # 25/06/23

    class Meta:
        verbose_name = "Inward Delivery"
        verbose_name_plural = "Inward Delivery"
	

    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.created_date, self.supplier, self.products, self.eta,
                                            self.person_ordered)


class SFOutward(models.Model):
    created_date = models.DateTimeField(auto_now_add = True, blank = True)
    customer = models.CharField(max_length=30)
    product_type = models.CharField(max_length=10)
    pallet_space = models.CharField(max_length=30, null=True)
    etd = models.DateTimeField()
    freight_company = models.CharField(max_length=30)
    booked_date = models.DateTimeField(null=True, blank=True)
    dispatched_date = models.DateTimeField(null=True, blank=True)
    person_booked = models.CharField(max_length=20, null=True, blank=True)
    person_dispatched = models.CharField(max_length=20, null=True, blank=True)
    memo = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Outward Dispatch"
        verbose_name_plural = "Outward Dispatch"

    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.created_date, self.customer, self.product_type, self.etd,
                                            self.freight_company)
