import Functions

# r is read, a is append, and w is overwrite
# can do a+ and w+ to read and write

new_list = []
with open("test_file", "r") as f:
    for line in f:
        new_list.append(float(line.rstrip("\n")))

    print(new_list)
    print("Max value of list is " + str(Functions.max_val(new_list)))
    print("Average of list is " + str(Functions.compute_list_avg(new_list)))

city_list = []

with open("unordered_cities.txt", "r") as f:
    for line in f:
        city_list.append(line.rstrip("\n"))

sorted_citylist = sorted(city_list)

with open("ordered_list", "w") as f:
    for city in sorted_citylist:
        f.write(city + "\n")
