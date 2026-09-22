'''

Redistributing Chocolates
Alice, Bob, and Charlie have 
X
,
Y
,
X,Y, and 
Z
Z chocolates respectively.
Find whether you can redistribute the chocolates such that:

Each person has at least one chocolate;
No two people have same number of chocolates;
No chocolate is left after redistribution.
Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
The first and only line of each test case contains three space-separated integers 
X
,
Y
,
X,Y, and 
Z
Z — the number of chocolates Alice, Bob, and Charlie have initially.
Output Format
For each test case, output on a new line YES, if you can redistribute all the chocolates such that all the given conditions are met, and NO otherwise.

You may print each character in uppercase or lowercase. For example, NO, no, No and nO, are all considered identical.

Constraints
1
≤
T
≤
1000
1≤T≤1000
1
≤
X
,
Y
,
Z
≤
100
1≤X,Y,Z≤100


'''



import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx]); idx += 1
    out = []
    for _ in range(t):
        x = int(input_data[idx]); y = int(input_data[idx+1]); z = int(input_data[idx+2])
        idx += 3
        s = x + y + z
        out.append("YES" if s >= 6 else "NO")
    print("\n".join(out))

main()