def distinct(arr):
	disArr = dict()
	for i in arr:
		disArr[i] = i
	arr = list(disArr)
	return arr

arr = [1, 3, 5, 2, 1, 3, 7, 5, 4, 2, 1, 5, 3] 
arr = distinct(arr) 
print(arr)