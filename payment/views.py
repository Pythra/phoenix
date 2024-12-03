import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Payment
from cap.models import Profile

def create_payment(request):
    # Set context with the public Stripe key and amount
    amount = 10.00  # Example amount in dollars (you can set this dynamically from your payment logic)
    context = {
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        'amount': amount
    }

    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe_token = request.POST.get('stripeToken')

        if not stripe_token:
            return render(request, 'payment/error.html', {'error': 'Stripe token not found.'})

        try:
            # Create a charge on Stripe
            charge = stripe.Charge.create(
                amount=int(amount * 100),  # Convert dollars to cents
                currency='usd',
                source=stripe_token,
                description='Example charge'
            )

            # Store payment details in the database
            payment = Payment.objects.create(
                charge_id=charge.id,
                amount=charge.amount / 100  # Convert from cents to dollars
            )

            # Update the user's balance
            user = Profile.objects.get(user=request.user)
            user.balance = float(user.balance) + payment.amount  # Use the amount from the payment model
            user.save()  # Don't forget to save the profile object

            # Redirect to the payment success page
            return redirect('payment_success')

        except stripe.error.StripeError as e:
            return render(request, 'payment/error.html', {'error': str(e)})

    # For GET requests, render the payment page with the amount
    return render(request, 'payment/create_payment.html', context)

# Payment Success View
def payment_success(request):
    return render(request, 'payment/payment_success.html')

# Payment Error View (Optional)
def payment_error(request):
    return render(request, 'payment/payment_error.html')
