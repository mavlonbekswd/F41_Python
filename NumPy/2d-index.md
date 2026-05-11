Albatta. 2D array’ni jadval deb tasavvur qil.

import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

Bu jadval:

        col0 col1 col2
row0     10   20   30
row1     40   50   60
row2     70   80   90
1. Bitta element olish

Formula:

arr[row, column]

Masalan:

arr[0, 0]   # 10
arr[0, 1]   # 20
arr[1, 2]   # 60
arr[2, 1]   # 80

Eng muhim qoida:

birinchi son = row
ikkinchi son = column
2. Bitta row olish
arr[0]

Natija:

[10 20 30]

Yana:

arr[1]   # [40 50 60]
arr[2]   # [70 80 90]
3. Bitta column olish

Column olish uchun : kerak.

arr[:, 0]

Bu degani:

hamma row, 0-column

Natija:

[10 40 70]

Yana:

arr[:, 1]   # [20 50 80]
arr[:, 2]   # [30 60 90]
4. Kesib olish: row + column slicing
arr[0:2, 1:3]

Bu degani:

row 0 dan row 2 gacha, lekin row 2 kirmaydi
column 1 dan column 3 gacha, lekin column 3 kirmaydi

Natija:

[[20 30]
 [50 60]]

Chunki tanlangan joy:

row0: col1, col2 → 20, 30
row1: col1, col2 → 50, 60
5. Eng ko‘p ishlatiladigan patternlar
arr[1, 2]      # row 1, col 2 → 60

arr[1, :]      # row 1 hamma column → [40 50 60]

arr[:, 1]      # hamma row, col 1 → [20 50 80]

arr[0:2, :]    # row 0 va row 1, hamma column

arr[:, 0:2]    # hamma row, col 0 va col 1

arr[1:, 1:]    # row 1 dan oxirigacha, col 1 dan oxirigacha
Juda sodda qoida

2D array’da doim shunday o‘qi:

arr[row_part, column_part]

Masalan:

arr[1:, 1:]

O‘qilishi:

row 1 dan oxirigacha
column 1 dan oxirigacha

Natija:

[[50 60]
 [80 90]]