numbers=[45,87,96,65,43,23,12,54]
odds=[]

for num in numbers:
    if num%2==1:
        odds.append(num)

print(odds)  

#shortcut
#listcomprehention
odd_num=[num for num in numbers if num%2==1]
#1st num ta holo select er num oitai list a rakhbo
#num jeta for er agea acea
print(odd_num)

odd_num=[num for num in numbers if num%2==1 if num%5==0]
# 2 ta condition
print(odd_num)


#age_comb=[(player,age) for player in players for age in ages]
#nested loop shortcut
#(player,age) dile tuple
#[player,age] dile list
