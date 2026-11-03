customer=input("Customer_name:")
units=int(input("Units_consumed:"))
if units<0:
  print("Invalid Units")
else:
  if units<=100:
     rate=2
  elif units<=200:
     rate=3
  elif units<=400:
     rate=5
  else:
     rate=7
  service=50
  electric=units*rate
  print(f"{"Electricity_charge:"} {electric}")
  print(f"{"Service_charge:"}{service}")
  print(f"{"Total_Bill:"}{service+electric}")
