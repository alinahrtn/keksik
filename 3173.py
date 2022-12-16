def most_frequent(List):
   return max(set(List), key = List.count)
print(most_frequent(input().split()))