from django.urls import reverse_lazy
from django.views import generic
from .models import Order
from .forms import OrderForm

class OrderListView(generic.ListView):
    model = Order
    template_name = 'basket/order_list.html'
    context_object_name = 'orders'
    paginate_by = 10
    ordering = ['-created_at']

class OrderCreateView(generic.CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'basket/order_form.html'
    success_url = reverse_lazy('basket:order_list')

class OrderUpdateView(generic.UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'basket/order_form.html'
    success_url = reverse_lazy('basket:order_list')

class OrderDeleteView(generic.DeleteView):
    model = Order
    template_name = 'basket/order_confirm_delete.html'
    success_url = reverse_lazy('basket:order_list')

class OrderCreateView(generic.CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'basket/order_form.html'
    success_url = reverse_lazy('basket:order_list')

    def get_initial(self):
        initial = super().get_initial()
        book_id = self.request.GET.get('book')
        if book_id:
            initial['book'] = book_id
        return initial
