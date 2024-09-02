olympic_medal_count = [
    {"country": "United States", "gold": 39, "silver": 41, "bronze": 33},
    {"country": "China", "gold": 38, "silver": 32, "bronze": 18},
    {"country": "Japan", "gold": 27, "silver": 14, "bronze": 17},
    {"country": "Great Britain", "gold": 22, "silver": 21, "bronze": 22},
    {"country": "Russia", "gold": 20, "silver": 28, "bronze": 23},
    {"country": "Australia", "gold": 17, "silver": 7, "bronze": 22},
    {"country": "Netherlands", "gold": 10, "silver": 12, "bronze": 14},
    {"country": "France", "gold": 10, "silver": 12, "bronze": 11},
    {"country": "Germany", "gold": 10, "silver": 11, "bronze": 16},
    {"country": "Italy", "gold": 10, "silver": 10, "bronze": 20}
]

#Q1: country mist most number of gold medals

# def get_gold(med):
#     return med.get("gold")
# most_gold_medal=max(olympic_medal_count,key=get_gold)
# gold_medal=[m.get("country")for m in olympic_medal_count if m.get("gold")==most_gold_medal.get("gold")]
# print(gold_medal)



#Q2:medal count of each countries 

# all_medals="gold"+"silver"+"bronze"
# def get_medals(med):
#     return med.get("all_medals")
# medal_data=[m.get("country") for m in olympic_medal_count if m.get(all_medals)]
# print(medal_data)





#Q3: country with least number of medals

# def get_gold(med):
#     return med.get("gold")
# most_gold_medal=max(olympic_medal_count,key=get_gold)
# gold_medal=[m.get("country")for m in olympic_medal_count if m.get("gold")==most_gold_medal.get("gold")]
# print(gold_medal)

# def get_medals(med):                Error
# #     medals=[m.get("gold")+m.get("silver")+m.get("bronze") for m in olympic_medal_count]
# #     print(medals)
# #     return med.get("medals")

# least_medal=min([m.get("gold")+m.get("silver")+m.get("bronze") for m in olympic_medal_count])
# least_medal_country=[m.get("country")for m in olympic_medal_count if m.get("medals")==min([m.get("gold")+m.get("silver")+m.get("bronze") for m in olympic_medal_count])]
# print(least_medal_country)





#Q5: sort countries with medal count



