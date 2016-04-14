# -- coding: utf8 --
#定义一个传递两个参数的函数 cheese_and_cracker 
def cheese_and_crackers(cheese_count, boxes_ofcrackers):
	print"You have %d cheese!" %cheese_count
	print "You have %d boxes of crackers!" % boxes_ofcrackers
	print "Man that's enough for a party"
	print "Get a blanket.\n"
	

# 直接传递参数 调用函数
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#定义两个变量并传入调用函数
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 +6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)