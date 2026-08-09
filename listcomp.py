# a comprise way to create lists in oython compact and easier to read than traditional loops
double=[]
for i in range(1,11):
    double.append(i*2)
#insted we can write 
doubles=[i*2 for i in range(1,11)]
squares=[y*y for y in range(1,11)]
fruits=["apple","banana","cherry"]
fruits=[fruit.upper() for fruit in fruits]
fruits=[fruit[0] for fruit in fruits]
numbers=[1,-2,-3,4]
pos_num=[num for num in numbers if num>0]
neg_nums=[num for num in numbers if num <0]
grades=[85,42,79,90,56,61,30]
passing_grades=[grade for grade in grades if grade>=60]
# dict comprehension
cities_in_f={"ny":32,"la":75,"chicago":28}
cities_in_c={key:round((value-32)*5/9) for (key,value) in cities_in_f.items()}
weather={city:conditions for (city, conditions) in [("ny", "sunny"), ("la", "sunny"), ("chicago", "cloudy")]}
sunny_weather={key for (key,value) in weather.items() if value=="sunny"}
desc_cities={key: ("WARM"if value>=40 else "COLD") for (key,value) in cities_in_c.items()}
def check_temp(temp):
    if(temp>=70):
        return "HOT"
    elif(temp>=40):
        return "WARM"
    else:
        return "COLD"
des_cities={key:check_temp(key) for (key,value) in cities_in_c.items()}
#tuple comprehension
TC=tuple((i*2 for i in range(1,11)))
TSC=tuple((language for language in languages if language.startswith("Python")))