def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Lakukan perulangan dalam jumlah n-i-1 kali
        for j in range(0, n - i - 1):
            # Tukar elemen jika elemen saat ini lebih besar dari elemen berikutnya
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Contoh penggunaan
arr = [64, 34, 25, 12, 22, 11, 90]
print("Array sebelum diurutkan:")
print(arr)

bubble_sort(arr)

print("Array setelah diurutkan:")
print(arr)
