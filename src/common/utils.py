
# apermindex should be a number between 0 and factorial(len(alist))
def perm_given_index(alist, apermindex):
    for i in range(len(alist)-1):
        apermindex, j = divmod(apermindex, len(alist)-i)
        alist[i], alist[i+j] = alist[i+j], alist[i]
    return alist
