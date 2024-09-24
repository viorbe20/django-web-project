class Cart:
    def __init__(self, request):
        """
        Initialize the cart object with the request. 
        If a cart does not exist in the session, create an empty one.
        """
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        
        if cart is None:
            # If no cart exists in the session, create a new empty cart
            cart = {}
        
        # Always set self.cart
        self.cart = cart

    
    def add_product(self, product):
        """
        Add a product to the cart. If the product is already in the cart,
        increment its quantity. Otherwise, add it with quantity set to 1.
        """
        if str(product.id) not in self.cart.keys():
            # Add a new product to the cart with initial quantity 1
            self.cart[product.id] = {
                "product_id": product.id,
                "name": product.name,
                "prize": float(product.prize),
                "quantity": 1,
                "image": product.image.url,
            }
        else:
            # If the product is already in the cart, increase its quantity and the prize
            for key, value in self.cart.items():
                if key == str(product.id):
                    value["quantity"] += 1
                    value["prize"] = float(product.prize) * value["quantity"]
                    break
        self.save_cart()
        
    def save_cart(self):
        """
        Save the current state of the cart in the session and mark it as modified.
        """
        self.session["cart"] = self.cart
        self.session.modified = True
    
    def remove_product(self, product):
        """
        Remove a product from the cart entirely based on its product ID.
        """
        product_id = str(product.id)
        
        if product_id in self.cart:
            # Delete the product from the cart if it exists 
            del self.cart[product_id] 
            self.save_cart()
    
    def reduce_quantity(self, product):
        """
        Decrease the quantity of a product in the cart. 
        If the quantity goes below 1, remove the product from the cart.
        """
        for key, value in self.cart.items():
            if key == str(product.id):
                # Decrease the product's quantity and prize
                value["quantity"] -= 1
                value["prize"] -= float(product.prize)
                # If quantity is less than 1, remove the product from the cart
                if value["quantity"] < 1:
                    self.remove_product(product)
                break
        self.save_cart()
                
    def empty_cart(self):
        """
        Empty the entire cart by clearing all items and marking the session as modified.
        """
        self.session["cart"] = {}
        self.session.modified = True
