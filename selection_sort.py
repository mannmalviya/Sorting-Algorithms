
def selection_sort(ilist):
	i = 0
	while(i <= len(ilist)-1):
		smallest = i
		j = i
		while(j <= len(ilist)-1):	
			if ilist[j] < ilist[smallest]:
				smallest = j
			j+= 1
		tmp = ilist[i]
		ilist[i] = ilist[smallest]
		ilist[smallest] = tmp
		i += 1	

	return ilist
