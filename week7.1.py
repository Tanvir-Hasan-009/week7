def chop(lst):
    """Remove the first and last elements from the input list."""
    if len(lst) >= 2:
        del lst[0]
        del lst[-1]
    else:
        lst.clear()

def middle(lst):
    """Return a new list containing all elements except the first and last elements."""
    if len(lst) >= 2:
        return lst[1:-1]
    else:
        return []

if __name__ == "__main__":
    my_list = [1, 2, 3, 4]
    print("My list before call chop function =>", my_list)
    chop(my_list)
    print("My list after call chop function =>", my_list)

    original_list = [1, 2, 3, 4]
    print("\nMy list before call middle function =>", original_list)
    new_list = middle(original_list.copy()) 
    print("My list after call middle function =>", original_list)
    print("New list after call middle function =>", new_list)
