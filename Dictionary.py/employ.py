# employe={"name -":"hari","dept -":"r&d","salary -":50000,"combo_offer -":1000}

# #print all key value
# for k,v in employe.items():
#     print(k,v)

#-------------------------------------
#print employe net pay
employe={"name":"hari","dept":"r&d","salary":50000,"combo_offer":1000,"extra_working_days":3}
if "extra_working_days" in employe:
    net_pay=employe.get("salary")+employe.get("combo_offer")*employe.get("extra_working_days")
    print(net_pay)
else:
    net_pay=employe.get("salary")
    print(net_pay)

    # fetching value from dictionary using key dict.get(key)
    # adding a new key value pair dict[key]=value
    