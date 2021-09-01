class Book:
	def __init__(self, name, author, price):
		self.name = name
		self.author = author
		self.price = price
	def info():
		print("%s - Written by %s - Price: $%d" % (self.name, self.author, self.price))

class Customer:
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance
		self.cart = {}
		self.cart_value = 0
	def set_bal(value):
		self.balance = value
	def add_to_cart(book, amount):
		if self.cart.keys().count(book) == 0:
			self.cart.update({book: amount})
		else:
			self.cart.update({book: self.cart[book]+amount})
		cart_value += book.price * amount
		if cart_value > balance:
			print("Warning! Your cart currently has $%d worth of books, which is more than your sufficient balance of %d" % (cart_value, balance))

class Bookstore:
	def __init__(self, capacity):
		self.capacity = capacity
		self count = 0
		self.books = []
		self.database = {}
	def add_books(book, amount):
		if count + amount > capacity:
			print("We can't add these books, the storage is full!")
		else:
			if self.books.count(book) == 0:
				self.database.update({book: amount})
				self.books.append(book)
			else:
				self.database.update({book: self.database[book] + amount})
	def browse(input):
		matches = []
		for book in self.books:
			if (book.name.count(input) > 1) or (book.author.count(input) > 1):
				matches.append(book)
		for results in matches:
			print("%s by %s - Price: $%d - Left in stock: %d" % (result.name, result.author, result.price, self.database[result]))
	def checkout(buyer, cart):
		total_price = 0
		for item in cart.keys():
			if cart[item] > self.database[item]:
				print("The book '%s' doesn't have enough copies for you. Your purchased amount is set to %d. We sincerely sorry!" % (item.name, self.database[item]))
				cart[item] = self.database[item]
			total_price += item.price * cart[item]
		if buyer.balance < total_price:
			print("%s's balance is insufficient, cancelling the checkout process..." % (buyer.name,))
		else:
			for book in cart.keys():
				self.database.update({books: self.database[book]-cart[book]})
				if self.database[book] == 0:
					self.database.pop(book)
			buyer.set_bal(buyer.balance - total_price)
			print("Thank you for shopping here! Your bill is %d" % (total_price,))
