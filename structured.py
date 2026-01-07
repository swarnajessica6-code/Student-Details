import sys

# Check arguments
if len(sys.argv) != 5:
    print("Usage: python structured.py <name> <mark1> <mark2> <mark3>")
    sys.exit(1)

name = sys.argv[1]
mark1 = int(sys.argv[2])
mark2 = int(sys.argv[3])
mark3 = int(sys.argv[4])

total = mark1 + mark2 + mark3
average = total / 3

print("Student Name:", name)
print("Marks:", mark1, mark2, mark3)
print("Total:", total)
print("Average:", average)
