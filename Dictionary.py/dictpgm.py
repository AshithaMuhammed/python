#create a dictionary mobile with keys name,brand,price,is_available
# mobile={"name":"motoge14","brand":"moto","price":22000,"is_available":True}
# for k,v in mobile.items():
#     print(k,v)
#------------------------------------------------------
#print all keys
# mobile={"name":"motoge14","brand":"moto","price":22000,"is_available":True}
# all_keys=mobile.keys()
# print(all_keys)
#-----------------------------------------------------------
# mobile={"name":"motoge14","brand":"moto","price":22000,"is_available":True}
# print(mobile.get("name"))    #for getting name
# # print(mobile["name"])
#---------------------------------------
#getting values
# mobile={"name":"motoge14","brand":"moto","price":22000,"is_available":True}
# print(mobile.values())
#-------------------------------------------------------------
#pop name
# mobile={"name":"motoedge14","brand":"moto","price":22000,"is_available":True}
# mobile.pop("name")
# print(mobile)

#-------------------------------------------------
#add offer
# mobile={"name":"motoedge14","brand":"moto","price":22000,"is_available":True}
# mobile["offer"]=500
# print(mobile)

#--------------------------------------------------

#for checking a key in the dictionary # return true
# mobile={"name":"motoge14","brand":"moto","price":22000,"is_available":True}
# print("name" in mobile)

#--------------------------------------

mobile={"name":"motoge14","brand":"moto","price":22000,"is_available":True}
if "price" in mobile:
    print("present")
else:
    print("not present")
#--------------------------------------------------------------

#find selling price

# mobile={"name":"motoedge14","brand":"moto","price":22000,"is_available":True,"offer":500}

# if "offer" in mobile:
#     selling_price=mobile.get("price")-mobile.get("offer")
#     print(selling_price)
# else:
#     selling_price=mobile.get("price")
#     print(selling_price)


#---------------------------------------------------------
