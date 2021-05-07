def dutch_national_flag(arr):
   first,last = 0,len(arr)-1;
   i=0;
   while(i<=last):
       if arr[i] ==0:
           arr[i],arr[first] = arr[first],arr[i]
           i+=1
           first+=1
       elif arr[i]==1:
           i += 1
       else:
           arr[i],arr[last] = arr[last],arr[i];
           last -= 1 
