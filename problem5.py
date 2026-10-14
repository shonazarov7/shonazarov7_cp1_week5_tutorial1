n=int(input("Enter the number of days: "))
measures=[]
for i in range(n):
    m=int(input("Enter the measuement for the next day: "))
    measures.append(m)
for i in range(n):
    print(f"Day {i+1}: {measures[i]} cm")
print(f"First height: {measures[0]} cm")
print(f"Last height: {measures[-1]} cm")
print(f"Change: {measures[-1] - measures[0]} cm")