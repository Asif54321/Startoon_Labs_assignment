def can_form_weight(W, weights):
    if W == 0:
        return True
    
    n = len(weights)
    if n == 0:
        return False
    
    # Check if any single weight equals W
    if W in weights:
        return True
    
    # Sort the weights in descending order
    weights.sort(reverse=True)
    
    # Check if it's possible to form the weight W using a combination of smaller weights
    for i in range(1, 2**n):
        current_sum = 0
        for j in range(n):
            if (i >> j) & 1:
                current_sum += weights[j]
                if current_sum == W:
                    return True
    
    return False

# Example usage:
W = 15
weights = [4, 3, 5, 6, 4]
print(can_form_weight(W, weights))  # Output: True

W = 9
weights = [4, 1, 3, 7]
print(can_form_weight(W, weights))  # Output: False
