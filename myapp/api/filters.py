import django_filters
from .models import BlogPost

class BlogPostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # ກອງຂໍ້ມູນທີ່ຊື່ຕົງກັນ
    published_date = django_filters.DateFilter(lookup_expr='exact')  # ຕາມວັນທີ່ພໍດີ
    published_date__gte = django_filters.DateFilter(field_name='published_date', lookup_expr='gte')  # ກອງມີທືຫຼາຍກວ່າ
    published_date__lte = django_filters.DateFilter(field_name='published_date', lookup_expr='lte')  # ກອງມື້ທີ່ນ້ອຍກວ່າ
    
    class Meta:
        model = BlogPost
        fields = ['title', 'published_date']  # ສ້າງຟິວທີ່ຕ້ອງການກອງ
