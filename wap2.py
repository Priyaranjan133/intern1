previous = 0

for current in range(10):
    total = current + previous
    print("Current:", current, "Previous:", previous, "Sum:", total)
    previous = current