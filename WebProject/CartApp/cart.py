class Cart:
    def __init__(self, request):
        """
        Initialize the cart object with the request. 
        If a cart does not exist in the session, create an empty one.
        """
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        
        # If no cart exists in the session, create a new empty cart
        if cart is None:
            cart = {}
        
        self.cart = cart

    
    def add_item(self, item):
        """
        Add a item to the cart. If the item is already in the cart,
        increment its quantity. Otherwise, add it with quantity set to 1.
        """
        if str(item.id) not in self.cart.keys():
            # Add a new item to the cart with initial quantity 1
            self.cart[item.id] = {
                "item_id": item.id,
                "name": item.name,
                "prize": float(item.prize),
                "quantity": 1,
                "image": item.image.url,
            }
        else:
            # If the item is already in the cart, increase its quantity and the prize
            for key, value in self.cart.items():
                if key == str(item.id):
                    value["quantity"] += 1
                    value["prize"] = float(item.prize) * value["quantity"]
                    break
        self.save_cart()
        
    def save_cart(self):
        """
        Save the current state of the cart in the session and mark it as modified.
        """
        self.session["cart"] = self.cart
        self.session.modified = True
    
    def remove_item(self, item):
        """
        Remove a item from the cart entirely based on its item ID.
        """
        item_id = str(item.id)
        
        if item_id in self.cart:
            # Delete the item from the cart if it exists 
            del self.cart[item_id] 
            self.save_cart()
    
    def reduce_quantity(self, item):
        """
        Decrease the quantity of a item in the cart. 
        If the quantity goes below 1, remove the item from the cart.
        """
        for key, value in self.cart.items():
            if key == str(item.id):
                # Decrease the item's quantity and prize
                value["quantity"] -= 1
                value["prize"] -= float(item.prize)
                # If quantity is less than 1, remove the item from the cart
                if value["quantity"] < 1:
                    self.remove_item(item)
                break
        self.save_cart()
                
    def empty_cart(self):
        """
        Empty the entire cart by clearing all items and marking the session as modified.
        """
        self.session["cart"] = {}
        self.session.modified = True