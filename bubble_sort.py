

def bubble_sort(ilist):
	
	last = len(ilist)-1
	
	while(last >= 1):
		i = 0
		j = 1
		while(j <= last):
			if(ilist[i] > ilist[j]):
				tmp = ilist[i]
				ilist[i] = ilist[j]
				ilist[j] = tmp
			i += 1
			j += 1

		last -= 1			

	return(ilist)

