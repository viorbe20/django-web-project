def total_cart_amount(request):
    total = 0
    
    if request.user.is_authenticated:
        # Obtener el carrito de la sesión, si no existe, usa un diccionario vacío
        cart = request.session.get("cart", {})
        
        # Calcular el total sumando los precios de cada producto en el carrito
        for key, value in cart.items():
            total += float(value["prize"]) * value["quantity"]  # Verifica que el campo es 'quantity', no 'amount'

    # El return debe estar fuera del bucle para asegurar que todo se calcule correctamente
    return {"total_cart_amount": total}