# currency_converter.py

USD_TO_EUR = 0.92
USD_TO_INR = 83.0
EUR_TO_USD = 1.09
EUR_TO_INR = 90.0
INR_TO_USD = 0.012
INR_TO_EUR = 0.011

def eur_to_usd(amt):
    return amt * EUR_TO_USD

def eur_to_inr(amt):
    return amt * EUR_TO_INR

def inr_to_usd(amt):
    return amt * INR_TO_USD

def inr_to_eur(amt):
    return amt * INR_TO_EUR

def usd_to_eur(amt):
    return amt * USD_TO_EUR

def usd_to_inr(amt):
    return amt * USD_TO_INR

currs=["eur","inr","usd"]
amount=float(input("Enter Amount: "))
currc=input("Enter Ur currency ('eur', 'inr', 'usd'): ")
toCurrc=input("Enter Ur currency ('eur', 'inr', 'usd'): ")

if currc not in currs or toCurrc not in currs:
    print("Does not exist.")
    exit()
elif currc==toCurrc:
    print("Can't convert same currency.")
    exit()

con=f"{currc}_to_{toCurrc}"
exec(f"result= {con}({amount})")
print(f"Amount: {result}")
