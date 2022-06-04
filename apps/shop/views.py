from django.shortcuts import render, redirect
from django.views import generic

from apps.shop.forms import OrderForm
from apps.shop.models import Device


class MainView(generic.ListView):
    template_name = 'shop/devices.html'
    model = Device
    context_object_name = 'devices'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('account_login')
        return super(MainView, self).get(request)


class CreateOrderView(generic.FormView):
    form_class = OrderForm
    template_name = 'shop/order.html'
    success_url = '/'

    def get(self, request, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account_login')
        return super(CreateOrderView, self).get(request, **kwargs)

    def get_context_data(self, *args, **kwargs):
        data = super(CreateOrderView, self).get_context_data(**kwargs)
        id = self.kwargs['pk']
        device = Device.objects.get(id=id)
        data['device'] = device
        return data
    
    def form_valid(self, form):
        form.save()
        return super(CreateOrderView, self).form_valid(form)

    def get_initial(self):
        initial = super(CreateOrderView, self).get_initial()
        device = Device.objects.get(id=self.kwargs['pk'])
        initial.update({
            'user': self.request.user,
            'device': device
        })
        return initial

