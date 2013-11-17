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
      
# Hannah's new update 
def search(item,numbers):
        searchend=len(numbers)                                          # end of search
        search=0                                                                        # start of search
        found=False
        while(found==False):
                scope=(search+searchend)/2                              # scope to hold span of search
                if(item<numbers[scope]):
                        searchend=scope-1
                elif(item>numbers[scope]):
                        search=scope+1
                else:                                                                   # if its is not greater or less than it is equal to
                        found=True
                        return scope                                            # return correct index

      
      
#Hannah's bsearch

def search(item,numbers):
        searchend=len(numbers)                                          # end of search
        search=0                                                                        # start of search
        found=False
        while(found==False):
                scope=(search+searchend)/2                              # scope to hold span of search
                if(item<numbers[scope]):
                        searchend=scope-1
                elif(item>numbers[scope]):
                        search=scope+1
                else:                                                                   # if its is not greater or less than it is equal to
                        found=True
                        return scope                                            # return correct index


    
#Lena's bsearch 
def bsearch(list, element):              #bsearch function definition 
    if len(list) != 0:                     #condition checking for emptiness 
        first = 0                   
        last = len(list)-1                #declaration of last index variable 
        found = False                        #bool found variable defined 
        while not found:                  #while loops until element is found 
            midpoint = (first + last)/2         #updates midpoint checking
            if (first==last) and (element != list[first]):      #when one element is left to be searched and that element is not the desired value   
                print 'Element is not in list.'     
                return -1                                   #ends function 
            elif element < list[midpoint]:              #if element is less than element at current list position 
                last = midpoint - 1                     #updates last index value 
            elif element > list[midpoint]:              #if element is greater than element at current list positon 
                first = midpoint + 1                    #updates first index value 
            else:                                       #else element equals element at current list positon 
                found = True                        #ends while loop 
                return midpoint     #returns index of searched element 
    else:                           #list is empty 
        print 'Element cannot be found. List is empty.'
        return -1


#Attiyah's bsearch
#bsearch: binary search function of sorted list 
def bsearch (searchList, element):
    first = 0 #variable used to manuvear through list
    last = len(searchList) - 1    #variable used to manuvar through list
    midPoint = (first + last) / 2       #variable used to split list in half
    found = False    #variable to mark whether the element has been found in the list 
    
    #print "My first element is ", searchList[first]
    #print "My last element is ", searchList[last]
    #print "My midpoint is ", searchList[midPoint]

    while found == False and first <= last:    #while loop used to look through entire list once
        
        if element > searchList[midPoint]:      #conditional used to determine whether to search the upper or lower half of the list
            first = midPoint + 1                #changes the first position to the midpoint + 1
            midPoint = (first + last) /2        #updates the midpoint 
            found = False                       #updates the value of found

        elif element < searchList[midPoint]:    #used to determine whether to search the lower or upper half of the list
            last = midPoint - 1                 #changed the last poistion to midpoint - 1
            midPoint = (first + last) / 2       #updates the midpoint
            found = False                       #updates the value of found

        elif element == searchList[midPoint]:   #if the element is found
            found = True                        #found is set to True, exiting the loop

    if found == False:                          #if statement to return false if element is not found
        return -1

    
    return midPoint                             #if statement to return the index of the element if found

#myList = [22,33,44,55,66,77,88,99]              #declaration and assignment of myList 
#print bsearch(myList,9)                         #function call to bsearch passing the variable myList

# Cesa Salaam bsearch
def bSearch (List, element):  # defining function
    bottom = 0                
    top = len(List) #Variabl
    middle = 0 #Variable to split list in half
    if element < List[len(List)- 1] and element >= List[0]: # checks to see if the element is within the range of the List.
        if top != 0: #Makes sure the List isnt empty.
            while top >= bottom : # While loop to repeat the Binary search
                middle = (bottom+top)//2
                if List[middle] == element: #if statement to check if the element has been found
                    return middle
                elif List[middle] < element:
                    bottom = middle + 1
                else:
                    top = middle - 1
        else:
            return str(-1)+  " Your element was not found in the list,sorry try again." #This statement is printed when the element is not found.
    else:
        return str(-1) + " Your element was not found in the list, sorry try again." #This statement is printed when the element is not found.
#This is the test list: myList = [9,10,12,14]
#Call of the function using myList and the element 9: print bSearch(myList,9)












