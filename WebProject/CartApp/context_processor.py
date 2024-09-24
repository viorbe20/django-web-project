def total_cart_amount(request):
    total = 0
    
    # if request.user.is_authenticated:
    #     # Get the cart of the session
    #     cart = request.session.get("cart", {})
        
    #     # Add all the car items prizes
    #     for key, value in request.session['cart'].items():
    #         total = total + float(value['prize'])
        
    return {"total_cart_amount": total}