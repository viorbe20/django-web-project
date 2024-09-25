def total_cart_amount(request):
    total = 0
    
    if request.user.is_authenticated:
        for key, value in request.session.get("cart", {}).items():
            total += float(value["prize"])
    else:
        total="Debes registrarte"
    return {"total_cart_amount": total}