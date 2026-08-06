#我想讓使用者輸入身高體重計算BMI並根據BMI值給予健康建議，請幫我寫一個Python程式。
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
def get_bmi_advice(bmi):
    if bmi < 18.5:
        return "體重過輕"
    elif 18.5 <= bmi < 24:
        return "體重正常"
    elif 24 <= bmi < 27:
        return "體重過重"
    elif 27 <=bmi < 30:
        return "輕度肥胖"
    elif 30 <= bmi < 35:
        return "中度肥胖"
    else:
        return "重度肥胖"

def main():
    height = float(input("請輸入身高(公尺): "))
    weight = float(input("請輸入體重(公斤): "))
    bmi = calculate_bmi(weight, height)
    advice = get_bmi_advice(bmi)
    print(f"你的BMI值為: {bmi:.2f}")
    print(f"健康建議: {advice}")

if __name__ == "__main__":
    main()