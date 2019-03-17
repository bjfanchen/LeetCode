def validMountainArray(A):
    """
    :type A: List[int]
    :rtype: bool
    """
    if len(A) < 3:
        return False
    for i in range(1, len(A)):
        if A[i] < A[i - 1]:
            # a = A[:i]
            # b = sorted(A[:i])
            # C = A[i:]
            # d = A[i:].sort(reverse=True)
            if sorted(A[:i]) == A[:i] and sorted(A[i:])[::-1] == A[i:]:
                return True
    return False


print(validMountainArray([1, 3, 2, 1]))
