#숫자가 연속으로 증가하는 알고리즘
#for i in range(0, 4):
#    for j in range (1, 5):
#        seat_no = i * 4 + j
#        if seat_no > 15:
#            break
#        print(seat_no, end = " ")
#    print()

#자리 배치도
col_no = 4
cust_no = int(input("No. of customers: "))

if cust_no % col_no == 0:
    row = cust_no // col_no
else:
    row = cust_no // col_no + 1

for i in range(0, row):
    for j in range(1, col_no + 1):
        num = i * col_no + j
        if num > cust_no:
            break
        print(num, end = " ")
    print()