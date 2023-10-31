class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('sh_cart') #obtain the actual shopping cart
        if not cart:
            self.cart = self.session['sh_cart'] = {} #obtain the object sh_cart, create a {} dictionary and assing this to the sh_cart obtained
        else:
            self.cart = cart #continue using the same cart object
        
    def add_product(self, product):
        if (str(product.id) not in self.cart.keys()):
            self.cart[product.id] = {
                'product_id': product.id,
                'product_name': product.name,
                'product_price': str(product.price),
                'product_quantity': 1,
                'product_image': product.image.url,
            }
        else:
            #self.cart[product.id]['product_quantity'] += 1 
            for key, value in self.cart.items():
                if key == str(product.id):
                    value['product_quantity'] += 1
                    break
        
        self.save_cart()

    

    def save_cart(self):
        self.session['sh_cart'] = self.cart
        self.session.modified = True


    def delete_product(self, product):
        product.id = str(product.id)

        if product.id in self.cart:
            del self.cart[product.id]
            self.save_cart()


    def substract_product(self, product):
        for key, value in self.cart.items():
                if key == str(product.id):
                    value['product_quantity'] -= 1
                    if value['product_quantity'] <1:
                        self.delete_product(product)
                    break
        self.save_cart()

    def delete_products(self):
        self.session['sh_cart'] = {}
        self.session.modify = True