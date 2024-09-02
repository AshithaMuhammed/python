from json import load
f=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\jsonWorks\\products.json","r",encoding="UTF-8")
products=load(f)
# # print(len(products))

# # print product title 
# products_titles=[p.get("title") for p in products]
# # print(products_titles)


# # print jewellerys
# jewelery_products=[i.get("title")for i in products if i.get("category")=="jewelery"]
# # print(jewelery_products)

# # print product price
# product_price=[i.get("title")for i in products if i.get("price")>100]
# # print(product_price)


# # products available in range of 100  to 150
# product_range=[i.get("title")for i in products  if i.get("price")>=100 and i.get("price")<=150]
# # print(product_range)
# price_filter=[i.get("id") for i in products if i.get("price")>=100 and i.get("price")<=150]
# # print(price_filter)

#product with most number of ratings
def get_rating_count(dic):
    return dic.get("rating").get("count")
top_selling_product=max(products,key=get_rating_count)
print(top_selling_product)






