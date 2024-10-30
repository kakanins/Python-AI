print("halo")
movie_price = 213
print("The Movie is " + str(movie_price))
name = input("What is your name? ")
print(name)
print("""Burger Pricelist : 
1. Beef Burger $15.4
2. Cheese Burger $20.2
3. Kids Burger $9.2""")
menu_price = input("Menu price : ") #harga menu nilainya berdasarkan input
amount = input("Amount : ")
bill= float(menu_price)*float(amount) #Total pembelian
print("You need to pay $" +str(bill))