count = int(raw_input(''))

total = 1000 - count 
coin = 0

if(total >= 500): 
    coin = coin + total / 500
    total = total % 500



if(total >= 100):   
    coin = coin + total / 100
    total = total % 100

if(total >= 50): 
   
    coin = coin + total / 50
    total = total % 50

if(total >= 10): 
    
    coin = coin + total / 10
    total = total % 10

if(total >= 5): 
    coin = coin + total / 5
    total = total % 5 


if(total >= 1): 
     
    coin = coin + total / 1
    total = total % 1


print(coin)

