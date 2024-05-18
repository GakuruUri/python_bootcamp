# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    # indent the b_list.append(new_item) to fix issue.
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])