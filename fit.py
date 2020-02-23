import matplotlib.pyplot as plt
import math

def get_data():
	with open("data.csv") as f:
		mileage = []
		price = []
		for index, line in enumerate(f):
			if index != 0:
				line = line.rstrip("\n").split(",")
				try:
					mileage.append(int(line[0]))
					price.append(int(line[1]))
				except:
					print("Wrong data!")
					return (0, 0)
	return mileage, price

def drow(mileage, price, msc):
	plt.scatter(mileage, price)
	plt.plot(mileage, msc)
	plt.ylabel("Price, $")
	plt.xlabel("Mileage, km")
	plt.show()

def estimatet_prise(mileage, theta0, theta1):
	return theta0 + theta1 * mileage

def normalazer(data):
	normal = []
	for i in data:
		normal.append(i / max(data))
	return normal

def get_theta0(mileage, price, theta0, theta1):
	l = len(mileage)
	res = 0
	for i in range(l):
		res += estimatet_prise(mileage[i], theta0, theta1) - price[i]
	return res / l

def get_theta1(mileage, price, theta0, theta1):
	l = len(mileage)
	res = 0
	for i in range(l):
		res += (estimatet_prise(mileage[i], theta0, theta1) - price[i]) * mileage[i]
	return res / l

def gradient_descent(mileage, price):
	theta0 = 0
	theta1 = 0
	learning_rate = 0.1
	i = 10000
	while i:
		i -= 1
		tmp_theta0 = learning_rate * get_theta0(mileage, price, theta0, theta1)
		tmp_theta1 = learning_rate * get_theta1(mileage, price, theta0, theta1)
		theta0 -= tmp_theta0
		theta1 -= tmp_theta1
		if abs(float(tmp_theta0)) < 0.000001 and abs(float(tmp_theta1)) < 0.000001:
			break
	print('Number of iterations', 10000 - i)
	return theta0, theta1

def keep_thetas_in_csv(theta0, theta1):
	file = open("thetas.csv", "w")
	file.write(str(theta0) + "," + str(theta1))
	file.close()

def main():
	mileage, price = get_data()
	if type(mileage) == list:
		normal_mileage = normalazer(mileage)
		normal_price = normalazer(price)
		theta0, theta1 = gradient_descent(normal_mileage, normal_price)
		theta0 = theta0 * max(price);
		theta1 = theta1 * (max(price) / max(mileage))
		print('Theta0 :', theta0)
		print('Theta1 :', theta1)
		msc = []
		m = len(mileage)
		for i in range(len(mileage)):
			msc.append(estimatet_prise(mileage[i], theta0, theta1))
		keep_thetas_in_csv(theta0, theta1)
		drow(mileage, price, msc)

if __name__ == "__main__":
	main()
