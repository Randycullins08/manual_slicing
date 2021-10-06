nums = list(range(21))

def slice(iter_obj, start=0, stop=None, step=1):

    result = []
    end = stop
    if start < 0:
      begin = len(iter_obj) + start  
    else:
      begin = start
    if stop is None:
       if start >= 0:
          end = len(iter_obj)  
       else:
          end = -1
    elif stop < 0:
        end = len(iter_obj) + stop

    for i in range(begin,end, step):
        result.append(iter_obj[i])

    return result

print(slice(nums, 9, 20, 5))
print(nums[9:20:5])