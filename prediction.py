def estimatet_prise(theta0, theta1, mileage):
	return theta0 + theta1 * mileage

def get_thetas_from_csv():
	with open("thetas.csv") as f:
		return list(map(float, f.read().split(",")))

def main():
	theta0, theta1 = get_thetas_from_csv()
	mileage = 0
	while (not mileage):
		mileage = input("Enter the vehicle mileage in kilometers :")
		try:
			mileage = int(mileage)
		except:
			print("Enter only a number")
			mileage = 0
		if mileage < 0:
			print("Mileage must be positive")
			mileage = 0
		price = estimatet_prise(theta0, theta1, mileage)
	print("Your car rating " + str(int(price)) + "$")

if __name__ == "__main__":
	main()