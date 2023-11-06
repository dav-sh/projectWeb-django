#similar to a global variable and it is registered in settings
def total_cart(request):
    total = 0

    #if request.user.is_authenticated:
    # for key, value in request.session['sh_cart'].items():
    #     total = total + (float(value['product_price'])*value['product_quantity']) 

    return {'total_cart': total}


