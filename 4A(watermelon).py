# weight = int(input())
#
# i = 0
#
# while i <= weight:
#
#     i = i + 1
#     if (i / 2) % 2 == 0:
#         print("YES")
#     else:
#         print("NO")


def task():
    weight = int(input())
    if weight % 2 == 0 and weight > 2:
        print("YES")
    else:
        print("NO")


task()
