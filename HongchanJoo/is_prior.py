def is_prior(left, right):
    idx_left = idx_right = 17
    while idx_left > 0 and idx_right > 0:
        if bool(left & 1 << idx_left) == bool(right & 1 << idx_right):
            idx_left -= 1
            idx_right -= 1
        else:
            if left & 1 << idx_left:
                idx_right -= 1
            elif right & 1 << idx_right:
                idx_left -= 1
    return True if idx_left <= idx_right else False

print(is_prior(2,4))
print(is_prior(4,4))
print(is_prior(4,2))
print(is_prior(14,26))
print(is_prior(26,14))
