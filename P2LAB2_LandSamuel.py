current_price = int(input())
last_months_price = int(input())

print(f'This house is ${current_price}. The change is ${current_price - last_months_price} since last month.')
print(f'The estimated monthly mortgage is ${(current_price * 0.051) / 12:.2f}.')
   