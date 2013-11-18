# Alston Clark

def bsearch(list,search):




  top = len(list)

  bottom = 0

  
 

  if (top >= search >= bottom):
    return -1 

   
  while ( bottom != top):
    # when bottom == top then you have found the index

    mid = (top + bottom) / 2

    if (search < list[mid]):
      top = mid - 1


    elif ( search > list[mid]):
      bottom = mid + 1


    else:
      return mid

#Sarah Jones

def bsearch( lista, element):
    start = 0
    end = len(lista) - 1
    while (end >= start):
          mid = (start + end) / 2
          if (lista[mid] < element):
            start = mid + 1
          elif lista[mid] > element:
            end = mid - 1
          else:
            return mid
            
        
    return -1

bsearch([2, 6, 7, 9, 14, 17, 18, 20], 2)


    












