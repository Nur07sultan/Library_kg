from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Order
from .forms import OrderForm


class OrderListView(ListView):
    model = Order
    template_name = 'basket/order_list.html'
    context_object_name = 'orders'
    paginate_by = 10
    ordering = ['-created_at']


order_list = OrderListView.as_view()


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'basket/order_form.html'
    success_url = reverse_lazy('basket:order_list')


order_add = OrderCreateView.as_view()


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'basket/order_form.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('basket:order_list')


order_edit = OrderUpdateView.as_view()


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'basket/order_confirm_delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('basket:order_list')


order_delete = OrderDeleteView.as_view()

