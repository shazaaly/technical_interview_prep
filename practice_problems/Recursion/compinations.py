# Main function to generate combinations
def combine(n, k):
	# Initialize result list to store combinations
	result = []
	# Define a recursive function to generate combinations
	def bachrack(start, path):
     	# Base case: If the length of the path equals k
		if len(path) == k:  # If the length of current path is equal to 'k', add it to result and return
      	# Append the current path (combination) to the result
			result.append(list(path))
			return
	# Recursive case: Loop from the current start number to n
		for i in range(start, n + 1):
			path.append(i)
      	# Recursive call with the next start number and updated path
			bachrack(i + 1, path)
   	# Backtrack: Remove the last element to try another combination
			path.pop()

	bachrack(1, [])
	return result


# Example usage
print(combine(4, 2))  # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]




# Start the recursion with start = 1 and an empty path


# Return the result containing all combinations

