from os import read

def bubble(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def selection(arr):
    for i in range(len(arr) - 1):
        min_ = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_]:
                min_ = j
        arr[i], arr[min_] = arr[min_], arr[i]
    return arr

def inserttion(arr):
    for i in range(1, len(arr)):
        key = arr[i];
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j];
            j-=1
        arr[j+1] = key
    return arr

def cocktail(arr):
    lo,hi = 0, len(arr) - 1
    while lo < hi:
        for j in range(lo,hi):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        hi -= 1
        for j in range(hi, lo, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

def gnome(arr):
    pos = 0
    while pos < len(arr):
        if pos == 0 or arr[pos] >= arr[pos - 1]:
            pos +=1
        else:
            arr[pos], arr[pos-1] = arr[pos-1],arr[pos]
            pos -= 1
    return arr

def comb(arr):
    gap = len(arr)
    shrink = 1.3
    while gap > 1:
        gap = max(1, int(gap/shrink))
        for i in range(len(arr) - gap):
            if arr[i] > arr[i+gap]:
                arr[i],arr[i+gap] = arr[i+gap], arr[i]
    return arr

def pancake(arr):
    for size in range(len(arr), 1, -1):
        max_ = arr.index(max(arr[:size]))
        if max_ != size -1:
            arr[:max_ + 1] = reversed(arr[:max_ + 1])
            arr[:size] = reversed(arr[:size])
    return arr

def shell(arr):
    gap = len(arr) //2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr

def quick(arr, lo, hi):
    if(lo< hi):
        p = partition(arr,lo,hi)
        quick(arr,lo,p-1)
        quick(arr,p+1,hi)
    return arr
def partition(arr,lo,hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo,hi):
        if arr[j] < pivot:
            i += 1
            arr[i] , arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1

def merge_(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = merge_(leftHalf)
  sortedRight = merge_(rightHalf)

  return merge(sortedLeft, sortedRight)
def merge(l, r):
  new_arr = []
  i = j = 0

  while i < len(l) and j < len(r):
    if l[i] < r[j]:
      new_arr.append(l[i])
      i += 1
    else:
      new_arr.append(r[j])
      j += 1
  new_arr.extend(l[i:])
  new_arr.extend(r[j:])

  return new_arr

def heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
def heapify(arr, n, i):
    largest = i    
    l = 2 * i + 1    
    r = 2 * i + 2  

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def radix_bucket(arr):
    max_ = max(arr)
    exp = 1
    while max_ // exp > 0:
        buckets = [[] for _ in range(10)]
        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)
        arr = [num for bucket in buckets for num in bucket]
        exp *= 10
    return arr

def count(arr):
    max_ = max(arr)
    count_ = [0] * (max_ + 1)
    output = [0] * len(arr)

    for num in arr:
        count_[num] += 1

    for i in range(1, len(count_)):
        count_[i] += count_[i - 1]

    for num in reversed(arr):
        output[count_[num] - 1] = num
        count_[num] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

    return arr

def bitonic_(arr):
    bitonic(arr, 0, len(arr), 1)
    return arr
def bitonic(arr, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        bitonic(arr, low, k, 1)   
        bitonic(arr, low + k, k, 0)  
        bitonicMerge(arr, low, cnt, dire)
    return arr
def bitonicMerge(arr, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            if (dire == 1 and arr[i] > arr[i + k]) or (dire == 0 and arr[i] < arr[i + k]):
                arr[i], arr[i + k] = arr[i + k], arr[i]
        bitonicMerge(arr, low, k, dire)
        bitonicMerge(arr, low + k, k, dire)

