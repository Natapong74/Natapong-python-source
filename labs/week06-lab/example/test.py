#เขียน function แปลงหน่วยเงินที่สามารถแปลงจาก
#THB <--> USD ... 1 USd = 32 THB

#โดยใช่ชื่อการใช่งาน
#function convert_currency(100,USD)

#แสดงผลออกทางหน้าจอ
#100 THB = 3.3 USD

#และทดสอบการใช่งาน function 

def convert_currency(thd,usd):
    if usd == "USD":
        print(f"{thd} THD = {thd / 32} USD")
    else:
        print(f"{thd} USD = {thd * 32} THB")

convert_currency(100,"USD")
convert_currency(100,"THD")










    

