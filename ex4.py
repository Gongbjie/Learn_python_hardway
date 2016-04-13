# -- coding: utf-8 --
# 定义一个常量存放车的数量
cars = 100 
# 定义每辆车乘坐人数
space_in_a_car = 4
# 司机数量
drivers = 30
# 乘客数量
passengers = 90 
# 没有使用的车辆数量
cars_not_driven = cars - drivers 
# 已经使用的车
cars_driven = drivers 
# 意义承载乘客的容量
carpool_capacity = cars_driven * space_in_a_car 
# 平均每辆车可承载的乘客
average_passengers_per_car = passengers / cars_driven 


print "There are", cars, "cars available."
print "There are only, drivers", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."