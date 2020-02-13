def merge(arr1, arr2):
	pointer1 = 0
	pointer2 = len(arr1)
	joinedlist = arr1 + arr2

	while pointer1 < len(arr1) and pointer2 < len(joinedlist):
		if joinedlist[pointer1] > joinedlist[pointer2]:
			temp = joinedlist[pointer1]
			joinedlist[pointer1] = joinedlist[pointer2]
			joinedlist[pointer2] = temp
			pointer1 += 1
			for x in range(pointer2, len(joinedlist)-1):
				if joinedlist[x] > joinedlist[x+1]:
					temp = joinedlist[x]
					joinedlist[x] = joinedlist[x+1]
					joinedlist[x+1] = temp
				else:
					break
		else:
			pointer2 += 1

	print(joinedlist)

arr1 = [1, 3, 5, 6, 9, 10]
arr2 = [0, 2, 4, 6, 8] 
merge(arr1, arr2) 