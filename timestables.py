result = []
for i in range(1, 13):
    row = []
    for j in range(1, 13):
        row.append("{:^3}".format(i * j))
    result.append(" ".join(row))
print("\n".join(result))

