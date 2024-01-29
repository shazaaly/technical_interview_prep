def binary_search(ordered_list, search_value):
  first = 0
  last = len(ordered_list) - 1

  while first <= last:
    middle = (first + last)//2
    # Check whether the search value equals the value in the middle
    if ordered_list[middle] == search_value:
      return True
    # Check whether the search value is smaller than the value in the middle
    elif search_value < ordered_list[middle]:
      # Set last to the value of middle minus one
     last = middle - 1
    else:
      first = middle + 1
  return False

print(binary_search([1,5,8,9,15,20,70,72], 5))