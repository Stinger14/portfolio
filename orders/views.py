import stripe
from django.conf import settings
from django.contrib.auth.models import Permission
from django.views.generic.base import TemplateView
from django.shortcuts import render

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class OrdersPageView(TemplateView):
    template_name = 'orders/donate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
    # get permission
    permission = Permission.objects.get(codename='special_status')
    # get user
    u = request.user
    # add to user's permission set
    u.user_permissions.add(permission)
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='Donate and get full access',
            source=request.POST['stripeToken']
        )
        return render(request, 'orders/charge.html')
    