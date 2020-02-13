def mergeSort(arr): 
	if len(arr) > 1: 
		middle = len(arr)//2
		leftArr = arr[:middle]
		rightArr = arr[middle:]

		mergeSort(leftArr)
		mergeSort(rightArr)

		i = j = k = 0
		
		while i < len(leftArr) and j < len(rightArr): 
			if leftArr[i] < rightArr[j]: 
				arr[k] = leftArr[i] 
				i+=1
			else: 
				arr[k] = rightArr[j] 
				j+=1
			k+=1
		
		while i < len(leftArr): 
			arr[k] = leftArr[i] 
			i+=1
			k+=1
		
		while j < len(rightArr): 
			arr[k] = rightArr[j] 
			j+=1
			k+=1


arr = [12, 11, 13, 5, 6, 7, 25, 1, 19, 15] 
mergeSort(arr) 
print(arr)