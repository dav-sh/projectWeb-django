class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('sh_cart') #obtain the actual shopping cart
        if not carrito:
            self.carrito = self.session['sh_cart'] = {} #obtain the object sh_cart, create a {} dictionary and assing this to the sh_cart obtained
        else:
            self.carrito = carrito #create a new carrito?
        
        
    def add_product(self, product):
        if (str(product.id) not in self.carrito.keys()):
            self.carrito[product.id] = {
                'product_id': product.id,
                'product_name': product.name,
                'product_price': str(product.price),
                'product_quantity': 1,
                #'product_image': product.image.url,
            }
        else:
            #self.cart[product.id]['product_quantity'] += 1 
            for key, value in self.carrito.items():
                if key == str(product.id):
                    value['product_quantity'] += 1
                    break
        
        self.save_cart()

    

    def save_cart(self):
        self.session['sh_cart'] = self.carrito
        self.session.modified = True


    def delete_product(self, product):
        product.id = str(product.id)

        if product.id in self.carrito:
            del self.carrito[product.id]
            self.save_cart()


    def substract_product(self, product):
        for key, value in self.carrito.items():
                if key == str(product.id):
                    value['product_quantity'] -= 1
                    if value['product_quantity'] <1:
                        self.delete_product(product)
                    break
        self.save_cart()

    def clean_cart(self):
        self.session['sh_cart'] = {}
        self.session.modify = True