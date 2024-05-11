import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--A', required=True, type=str)
parser.add_argument('--B', required=True, type=str)
args = parser.parse_args()
print("Before Swapping Variables")
A = args.A
B = args.B
print("A:", A)
print("B:", B)
A, B = B, A
print("After swapping Variables")
print("A:", A)
print("B:", B)



 