# -*- coding: utf-8 -*-
"""IMS

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_BivNKP-L9LyTwCzalSrvOIJ6UKwUBfH

Data of the 40 items in general store with mentioned attributes:
    Product_id  -  Product_Name -  Manufacturing_date -  Price -  Expiry_date -  Quantity  - Category
"""

Records = { 1001 : {"prod_name":"Parle-G","manu_date":"jan-2021","price":20,"exp_date":"jun-2022","quan":50,"categ":"snacks"},
            1002 : {"prod_name":"Roasted nuts","manu_date":"jan-2021","price":40,"exp_date":"jun-2022","quan":40,"categ":"snacks"},
            1003 : {"prod_name":"Lays","manu_date":"jan-2021","price":10,"exp_date":"jun-2022","quan":70,"categ":"snacks"},
            1004 : {"prod_name":"Tomato puff","manu_date":"jan-2021","price":10,"exp_date":"jun-2022","quan":20,"categ":"snacks"},
            1005 : {"prod_name":"Kurkure","manu_date":"jan-2021","price":10,"exp_date":"jun-2022","quan":100,"categ":"snacks"},
            1006 : {"prod_name":"Craks","manu_date":"jan-2021","price":15,"exp_date":"jun-2022","quan":80,"categ":"snacks"},
            1007 : {"prod_name":"Doritoes","manu_date":"jan-2021","price":25,"exp_date":"jun-2022","quan":50,"categ":"snacks"},
            1008 : {"prod_name":"Bingo","manu_date":"jan-2021","price":20,"exp_date":"dec-2022","quan":40,"categ":"snacks"},
            1009 : {"prod_name":"Tiger biscuit","manu_date":"jan-2021","price":10,"exp_date":"jun-2022","quan":70,"categ":"snacks"},
            10010 : {"prod_name":"Monaco","manu_date":"jan-2021","price":10,"exp_date":"jun-2022","quan":40,"categ":"snacks"},
            10011 : {"prod_name":"Yougurt","manu_date":"jan-2021","price":30,"exp_date":"jun-2022","quan":"200kg","categ":"dairy"},
            10012 : {"prod_name":"Milk","manu_date":"jan-2021","price":25,"exp_date":"jun-2022","quan":500,"categ":"dairy"},
            10013 : {"prod_name":"Cheese","manu_date":"jan-2021","price":45,"exp_date":"nov-2022","quan":80,"categ":"dairy"},
            10014 : {"prod_name":"Butter","manu_date":"jan-2021","price":50,"exp_date":"jun-2022","quan":50,"categ":"dairy"},
            10015 : {"prod_name":"Tofu","manu_date":"jan-2021","price":160,"exp_date":"jun-2022","quan":"30kg","categ":"dairy"},
            10016 : {"prod_name":"Pulse","manu_date":"jan-2021","price":230,"exp_date":"jun-2022","quan":"400kg","categ":"food"},
            10017 : {"prod_name":"Rice","manu_date":"jan-2021","price":150,"exp_date":"jan-2023","quan":"300kg","categ":"food"},
            10018 : {"prod_name":"Wheat","manu_date":"jan-2021","price":200,"exp_date":"jun-2022","quan":"100kg","categ":"food"},
            10019 : {"prod_name":"Suagr","manu_date":"jan-2021","price":150,"exp_date":"jun-2022","quan":"50kg","categ":"food"},
            10020 : {"prod_name":"Flour","manu_date":"jan-2021","price":198,"exp_date":"jun-2022","quan":50,"categ":"food"},
            10021 : {"prod_name":"Jaggery","manu_date":"jan-2021","price":170,"exp_date":"jun-2022","quan":"230kg","categ":"food"},
            10022 : {"prod_name":"Pasta","manu_date":"jan-2021","price":45,"exp_date":"jun-2022","quan":50,"categ":"food"},
            10023 : {"prod_name":"Sunsilk","manu_date":"jan-2021","price":30,"exp_date":"dec-2023","quan":78,"categ":"Body care"},
            10024 : {"prod_name":"Clinic-plus","manu_date":"jan-2021","price":60,"exp_date":"jun-2022","quan":50,"categ":"Body care"},
            10025 : {"prod_name":"Dettol","manu_date":"jan-2021","price":45,"exp_date":"jun-2022","quan":113,"categ":"Body Care"},
            10026 : {"prod_name":"Himalayan","manu_date":"jan-2021","price":40,"exp_date":"jun-2022","quan":50,"categ":"Body care"},
            10027 : {"prod_name":"Clean-n-clear","manu_date":"jan-2021","price":40,"exp_date":"jun-2022","quan":50,"categ":"Body care"},
            10028 : {"prod_name":"Handsoap","manu_date":"jan-2021","price":35,"exp_date":"jun-2022","quan":50,"categ":"Body care"},
            10029 : {"prod_name":"Shaving Cream","manu_date":"jan-2021","price":50,"exp_date":"jun-2022","quan":50,"categ":"Body care"},
            10030 : {"prod_name":"Fanta","manu_date":"jan-2021","price":30,"exp_date":"jun-2022","quan":100,"categ":"Beverages"},
            10031 : {"prod_name":"Coke","manu_date":"jan-2021","price":30,"exp_date":"jun-2022","quan":150,"categ":"Beverages"},
            10032 : {"prod_name":"Soda","manu_date":"jan-2021","price":35,"exp_date":"jun-2022","quan":10,"categ":"Beverages"},
            10033 : {"prod_name":"Coffee","manu_date":"jan-2021","price":35,"exp_date":"jun-2022","quan":50,"categ":"Beverages"},
            10034 : {"prod_name":"Orange Juice","manu_date":"jan-2021","price":45,"exp_date":"jun-2022","quan":53,"categ":"Beverages"},
            10035 : {"prod_name":"Appy fizz","manu_date":"jan-2021","price":20,"exp_date":"jun-2022","quan":51,"categ":"Beverages"},
            10036 : {"prod_name":"Battery","manu_date":"jan-2021","price":15,"exp_date":"jun-2022","quan":50,"categ":"Other"},
            10037 : {"prod_name":"Papertowel","manu_date":"jan-2021","price":20,"none":"jun-2022","quan":30,"categ":"Other"},
            10038 : {"prod_name":"Aluminium foil","manu_date":"jan-2021","price":10,"none":"jun-2022","quan":50,"categ":"Other"},
            10039 : {"prod_name":"Box","manu_date":"jan-2021","price":70,"exp_date":"none","quan":5,"categ":"Other"},
            10040 : {"prod_name":"Stand","manu_date":"jan-2021","price":195,"exp_date":"none","quan":15,"categ":"Other"}}

for i in Records:
    print(i)

for i in Records:
    print(Records[i],"\n")

import json

js = json.dumps(Records)

js

fd = open("Records.json",'w')
fd.write(js)
fd.close()

fd = open("Records.json",'r')
data = fd.read()
fd.close()

type(data)

data

Records = json.loads(data)
type(Records)

Records

shop = int(input("Enter number of items you will buy:"))

for i in range(shop):
    prod = str(input("Enter product you want to buy:"))
    quan = int(input("Quantity you require:"))
    
    for i in Records:
        item_no = i
    
        if (prod == Records[i]["prod_name"] and Records[i]["quan"]>0):
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
            print("Product_id is",item_no)
            print("Product name is",Records[i]["prod_name"])
            print("Manufacturing date is",Records[i]["manu_date"])
            print("Price is",Records[i]["price"])
            print("Quantity you mentioned:",quan,"\n") 
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
            bill = quan*Records[i]["price"]
            print("Bill of your Cart:",bill)
print("Happy Shopping")

