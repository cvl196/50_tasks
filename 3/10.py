def coiner(coins):
    if (len(coins)) % 3 == 0:
        return True
    else:
        return False


print(coiner([32, 32, 32, 32, 33]))