# datalens_app/models.py
from django.db import models

class Dataset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/', null=True, blank=True, default='')  # Добавляем значение по умолчанию

    
    def __str__(self):
        return self.name
    
class Data(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    data_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f"{self.dataset.name} - Data"
    

class Visualization(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Добавь здесь поля для хранения информации о визуализации (например, тип визуализации, параметры и т. д.)

