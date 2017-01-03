def gcd(n1, n2):
    big = max(n1, n2)
    small = min(n1, n2)

    # Euclid's algorithm for finding the GCD
    if big % small == 0:
        return small
    else:
        return gcd(big % small, small)
