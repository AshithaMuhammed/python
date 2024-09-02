from json import load
f=open("C:\\Users\\user\Desktop\\PythonJuneWorks\\jsonWorks\\country.json","r",encoding="UTF-8")
data=load(f)
print(len(data))

#Q:1print  capitals of country
# country_capital=[c.get("name") for c in data]
# print(country_capital)


#Q2:return country data

def fetch_country_by_name(name):
    return[c for c in data if c.get("name")==name][0]
# country_data=fetch_country_by_name("india")

# if "regionalBlocks" in country_data:
#     block_data=country_data.get("regionalBlocks")[0]
# if other_names in block_data:

# else:
#     print(country_data.get("name"))

for c in data:
    for l in c.get("languages"):
        if l.get("name")=="English":
            print(l.get("name"))