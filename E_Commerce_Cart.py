def cal_total(cart_items):
    total_items=len(cart_items)
    if total_items==0:
        print("Cart is empty")
        return
    total_price=sum(cart_items.values())
    if total_items>5:
        discount=total_price*0.10
        total_price-=discount
    print(f"Total Price={int(total_price)}")
cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
cal_total(cart_items)
