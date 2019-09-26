#recursive
def flatten(arr):
	res = []
	for item in arr:
		if type(item) == int:
			res.append(item)
		else:
			res.extend(flatten(item))
	return res

#test
print (flatten([1,[2,[4,5],6]]))
print (flatten([]))