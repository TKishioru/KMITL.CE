#โจทย์ให้ทำ if-else ปกติโดยดูว่าช่วงไหนต้องแสดงอะไร

print(' *** Wind classification ***')
inp = float(input('Enter wind speed (km/h) : '))
if inp >= 0 and inp <= 51.99:
    print('Wind classification is Breeze.')
elif inp >= 52.00 and inp <= 55.99:
    print('Wind classification is Depression.')
elif inp >= 56.00 and inp <= 101.99:
    print('Wind classification is Tropical Storm.')
elif inp >= 102.00 and inp <= 208.99:
    print('Wind classification is Typhoon.')
elif inp >= 209:
    print('Wind classification is Super Typhoon.')
else:
    print('!!!Wrong value can\'t classify.')