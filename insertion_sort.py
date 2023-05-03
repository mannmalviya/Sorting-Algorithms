
def insertion_sort(ilist):
	i = 1
	
	while(i <= len(ilist)-1):	
		j = i - 1
		t = i
		while(j >= 0):
			if(ilist[t] < ilist[j]):
				tmp = ilist[j]
				ilist[j] = ilist[t]
				ilist[t] = tmp
				t -= 1
				j -= 1	
			else:
				break
		i += 1
	
	return(ilist)

