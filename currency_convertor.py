import re
import urllib.request
import json

API_conversion = "https://api.exchangerate-api.com/v4/latest/"
def page_exists(page):
	try:
		urllib.request.urlopen(page)
		return True
	except:
		return False


def currenct_conversion( convert_from, convert_to):
  try:
    if(page_exists(API_conversion+convert_from)):
      page = urllib.request.urlopen(API_conversion+convert_from)
      content = page.read().decode("utf-8")
      data = json.loads(content)
      from_cur = data["rates"]
      rate = from_cur[convert_to]
      return rate
    else:
      print("ERROR:invalid API endpoint")
  except:
      print("one or more currency codes not found")
  


def isValidCurrency(currency):
  if currency.isupper() and len(currency)==3:
    return True
  return False


while True:
  amount = input("Enter amount to be converted(q to quit):")
  if(amount == 'q' or amount == 'Q'):
    print('Input is "q",Aborting!')
    break
  try:
      val = int(amount)
  except ValueError:
      try:
          val = float(amount)
      except ValueError:
        print("No.. input is not a valid amount")
        continue

  from_country = input("Enter FROM currency 3 letter code: ")
  if isValidCurrency(from_country) == False:
    print("Invalid input...please enter 3 letters in uppler case")
    continue

  to_country = input("Enter TO currency 3 letter code: ")
  if isValidCurrency(from_country) == False:
    print("Invalid input...please enter 3 letters in uppler case")
    continue
  
  conversion_rate = currenct_conversion(from_country, to_country)
  if(conversion_rate):
    final_amount = float(conversion_rate) * float(amount)
    print(amount+ " in "+ from_country + " = " + str(final_amount) + " in "+ to_country)