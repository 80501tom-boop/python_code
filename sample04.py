def calculate_bmi(weight_kg, height_cm):
	height_m = height_cm / 100
	return weight_kg / (height_m ** 2)


def main():
	try:
		height_cm = float(input("請輸入身高（公分）: "))
		weight_kg = float(input("請輸入體重（公斤）: "))

		if height_cm <= 0 or weight_kg <= 0:
			print("身高與體重都必須大於 0")
			return

		bmi = calculate_bmi(weight_kg, height_cm)
		print(f"你的 BMI 是: {bmi:.2f}")
	except ValueError:
		print("請輸入有效的數字。")


if __name__ == "__main__":
	main()