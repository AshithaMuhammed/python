mobiles=[

    {"id":100,"title":"s23 ultra","brand":"samsung","price":125000,"network":"5g"},
    {"id":101,"title":"s23","brand":"samsung","price":54000,"network":"4g"},
    {"id":102,"title":"edge14pro","brand":"moto","price":25000,"network":"5g"},
    {"id":103,"title":"edgeneo","brand":"moto","price":22000,"network":"4g"},
    {"id":104,"title":"redminote13pro","brand":"mi","price":25000,"network":"5g"},
    {"id":105,"title":"redmi13","brand":"mi","price":12000,"network":"4g"},
]
#Q:Print all mobile names
# mobile_name=[mob.get("title")for mob in mobiles]
# print("mobiles are:",mobile_name)


#Q:Print all brands
# all_brands={mob.get("brand")for mob in mobiles}
# print("brands are:",all_brands)


#Q:print all samsung mobiles
# sam_mob=[mob.get("title") for mob in mobiles if mob.get("brand")=="samsung"]
# print(sam_mob)

#Q:print all mobiles available in range of 23k to 40k
# mobile_price=[mob.get("title")for mob in mobiles if mob.get("price")in range(23000,40000)]
# print(mobile_price)

#Q:print highest price of the mobile
# max_price=0
# for mob in mobiles:
#     if mob.get("price") > max_price:
#         max_price=mob.get("price")
# costly_mobiles=[mob.get("title")for mob in mobiles if mob.get("price")==max_price]
# print(max_price)
        #  OR
        #-------
# def get_price(mob):
#     return mob.get("price")
# costly_mobile=max(mobiles,key=get_price)
# print(costly_mobile)


#Q:print lowest price mobile
# def get_price(mob):
#     return mob.get("price")
# cheapest_mobile=min(mobiles,key=get_price)
# print(cheapest_mobile)

#sorting
def get_price(mob):
    return mob.get("price")
sorted_mobiles=sorted(mobiles,key=get_price,reverse=True)
print(sorted_mobiles)

#Q:total price
# def get_price(mob):
#     return mob.get("price")
# total_cost=sum([mob.get("price") for mob in mobiles])
# print(total_cost)
