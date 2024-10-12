ka = {"name" : "Muhammad kaif" , "education" : "under bachlaor" , "res_matric" : "76%" , 
      "res_inter" : "85%" , "Roll_num_inter" : 111731 , "Roll_num_matric" : 12232 }
print(ka["Roll_num_inter"])
# dict_keys = they use print name , education , res_matric
print(ka.keys())
# dict_values = they use print Muhammad kaif, under bachlaor , 76%
print(ka.values())


# use loop in
for key in ka.keys():
    print(f"The value of {key} is {ka[key]}")

print("\n \n")


for key,value in ka.items():
    print(f"the value of {key} is {value}")