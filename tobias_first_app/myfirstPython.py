import random
#
# a = 1
# b = 2
#
# print(a+b)
#
# if b > a:
#     print('b is bigger({})'.format(b))
# else:
#     print('a is bigger')
#
# c = [10, 12, 8, 3]
#
# for i in c:
#     print(i)
#
# print(sum(c))
# print(len(c))
# c.append(22229)
# print(c)
#
# random.shuffle(c)
# print("new shuffle: ",c )
#
# d= random.choice(c)
# print(d)
# e = random.sample(c, 3)
# print(e)
#
# for i in e:
#     print("This {} is a random number".format(i))

# a = [4, 3, 5, 15, 22, 28, 7]
# #
# # b = [i for i in a if i >= 20]
# #
# # print(b)
# #
# # c = []
# # for i in a :
# #     if i % 2 == 1:
# #         c.append(i)
# # print(c)
# #
# # c = [random.randint(25, 100) for i in range(100)]
# # print(c)

# a = {'name': 'Tobias', 'surname':'Tomczak', 'height':184}
# #
# # a['city']='Zurich'
# # for i, v in a.items():
# #     print(i, ': ', v)
# #
# # for i in a.values():
# #     print(i)
# # for i in a.keys():
# #     print(i)
# #
# # print(a['surname'])

price_per_square = 100
garden_price = 2000

def house_price(length, width):
    space = length * width
    return space * price_per_square

def elite_house_price(length, width):
    # space = length*width
    # return space * price_per_square + garden_price
    return house_price(length, width) + garden_price

my_house_price = house_price(10, 25)
print(my_house_price)

trump_house_price = elite_house_price(100,200)
print(trump_house_price)

a = [(10, 20), (23,22), (99,88)]
b = []
for i in a:
    print(house_price(i[0], i[1]))
    b.append(house_price(i[0], i[1]))
print(b)

c = [house_price(i[0],i[1]) for i in a]
print('das ist c: ', c)