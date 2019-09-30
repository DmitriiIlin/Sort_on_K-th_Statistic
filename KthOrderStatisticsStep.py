def ArrayChunk(array,left,right):
#Метод сортирует массив на вокруг опорного элемента
    if len(array)==0:
        return None
    else:
        while len(array)>0:
            middle=(left+right)//2
            middle_value=array[middle]
            start=left
            finish=right
            while len(array)>0:
                for istart in range(left,right+1):
                    if array[middle]>array[start]:
                        start+=1
                    else:
                        istart=left
                        break 
                for ifinish in range(left,right+1):
                    if array[middle]<array[finish]:
                        finish-=1
                    else:
                        ifinish=left
                        break
                if start==(finish-1) and array[start]>array[finish]:
                    array[start],array[finish]=array[finish],array[start]
                    break
                if start==finish or (start==(finish-1) and array[start]>array[finish]):
                    for imiddle in range(0,len(array)):
                        if array[imiddle]==middle_value:
                            return imiddle
                array[start], array[finish]=array[finish], array[start]
                #print(array)

def KthOrderStatisticsStep(array,low,high,K):
#Основная ф-ция
    i=ArrayChunk(array,low,high)
    res=[]
    if K==i:
        res.append(low)
        res.append(high)
        return res
    elif i<K:
        return KthOrderStatisticsStep(array,i+1,high,K)
    elif i>K:
        return KthOrderStatisticsStep(array,low,i-1,K)

    

"""
a=[102,10,44,35,1,90,5]
print(KthOrderStatisticsStep(a,0,6,3))
print(a)
"""