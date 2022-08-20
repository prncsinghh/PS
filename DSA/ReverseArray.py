def reverseArray(arr, m):
    def helper(l, r):
        if l >= r:
            return False
        
        arr[l], arr[r] = arr[r], arr[l]

        return helper(l+1, r-1)
    return helper(m+1, len(arr)-1)

reverseArray('apple', 12)

