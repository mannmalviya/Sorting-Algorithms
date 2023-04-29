
def selection_sort(ilist):
	i = 0
	smallest = 0
	while(i <= len(ilist)-1):
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


l = [5,4,3,2,1]
print(selection_sort(l))

