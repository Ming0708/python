for i in range(1,5,1): #百位數 
    for j in range(1,5,1): #十位數
        for k in range(1,5,1): #個位數
            if (i!=k) & (i!=j) & (j!=k): #如果有任一位數數字相等時就不列印
                print(i,j,k)