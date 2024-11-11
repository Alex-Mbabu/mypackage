def top_n(items, n):
    """ 
    Return top n items in an array in descending order.

    Args:
        items (list): Array-like object (e.g., a list of numbers).
        n (int): Number of items to return.

    Returns:
        list: The top n items in descending order.
    """
    # Bubble Sort-like approach
    for i in range(n):
        for j in range(len(items)-1-i):
            if items[j] < items[j+1]:
                # Swap if the element is smaller than the next one
                items[j], items[j+1] = items[j+1], items[j]

    return items[:n]
