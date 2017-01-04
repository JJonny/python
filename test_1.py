import json
import find_on_pathes

json_string = """ {
  "orderID": 42,
  "customerName": "John Smith",
  "customerPhoneN": "555-1234",
  "orderContents": [
    {
      "productID": 23,
      "productName": "keyboard",
      "quantity": 1
    },
    {
      "productID": 13,
      "productName": "mouse",
      "quantity": 1
    }
  ],
  "orderCompleted": true
} """

# распарсенная строка
parsed_string = json.loads(json_string)
ls = parsed_string['orderContents']
for blok in ls:
    for k, v in blok.items():
        print(k, v)
    print()



p = [1,4,5,2,6,7,3,7]

some_l = [100, 110, 111]
ls = lambda ll: reduce(lambda a,b: a + b, ll, [])
print(ls)



#test module find_on_pathes
#r = find_on_pathes.checkPathesFromEnvVar('SQL11')
#find_on_pathes.printResult(r)

