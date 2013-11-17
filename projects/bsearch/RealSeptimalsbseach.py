#Sarah Jones
def bsearch( lista, element):
    start = 0
    end = len(lista) - 1                #end equal index 
    while (end >= start):               
          mid = (start + end) / 2       #find mid of list
          if (lista[mid] < element):    #when the element in index of mid is less than the element searched for
            start = mid + 1             #make start equal old mid plus 1, cutting the list in half
          elif lista[mid] > element:    #when the element in the index of the mid is greater than the element being searched for
            end = mid - 1               #make end equal old mid minus 1
          else:
            return mid                  #if mid is equal to the element, the item is found
        
    return -1                           #if the list is searched and the element is not found, the end will eventually be
                                        #greater than the start and will return -1

bsearch([2, 6, 7, 9, 14, 17, 18, 20], 19) #test case

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


    












