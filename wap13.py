raw_data = "  mAtThEw , sArAh,   bOb, jEnNiFeR ,AlIcE  "

clean_data = raw_data.strip()

names = clean_data.split(",")

names = [name.strip().title() for name in names]

if "Bob" in names:
    names.remove("Bob")

names.append("Charlie")

names.sort()

index = names.index("Jennifer")

print("Final List:", names)
print("Jennifer Index:", index)