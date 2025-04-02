product = 1
for count in range (4):
    product = product * (count + 1) #count starts at 0. 
#     print(count, end=" ")
    print(product, end =" ")

print(f"\nProduct = {product}")

#Explanaton
#The product is 1, and the count is 0
# 1*0+1=1*1=1
#Then the product is 1, and the count is 1
# 1*1+1=1*2=2
#Then the product becomes 2, and the count becomes 2
# 2*2+1=2*3=6
#Then the product becomes 6, and the count become 3
# 6*3+1=6*4=24

print("\n===========================================\n")
product = 1
for count in range (1, 5): # same as above because it goes 1 2 3 4, ends at 4 
    product = product * count
    print(product, end=" ")
