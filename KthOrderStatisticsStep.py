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
    N=ArrayChunk(array,low,high)
    res=[]
    if K==N:
        res.append(low)
        res.append(high)
        return res
    elif N<K:
        res.append(N+1)
        res.append(high)
        return res
    elif N>K:
        res.append(low)
        res.append(N-1)
        return res

    

