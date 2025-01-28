from django.shortcuts import render
from datetime import datetime

def my_view(request):
    products = [
        {'name': 'Shirt', 'price': 19.99, 'created_at': datetime(2025, 1, 10)},
        {'name': 'Jeans', 'price': 39.99, 'created_at': datetime(2025, 1, 12)},
        {'name': 'Jacket', 'price': 59.99, 'created_at': datetime(2025, 1, 20)}
    ]
    return render(request, 'my_template.html', {'products': products})
