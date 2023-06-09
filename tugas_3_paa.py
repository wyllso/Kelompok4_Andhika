# -*- coding: utf-8 -*-
"""tugas 3 PAA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MjUO05DtiIMSsZFbqxGFRF0Y7Japn31t

# ***`algoritma bubble sort`***
"""

def bubble_sort(arr):
    n = len(arr)
    iterations = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            iterations += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr, iterations

# Contoh penggunaan:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr, iterations = bubble_sort(arr)
print("Hasil Bubble Sort:", sorted_arr)
print("Jumlah iterasi:", iterations)

"""# algoritma insertion sort"""

def insertion_sort(arr):
    iterations = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        iterations += 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            iterations += 1
        arr[j + 1] = key
    return arr, iterations

# Contoh penggunaan:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr, iterations = insertion_sort(arr)
print("Hasil Insertion Sort:", sorted_arr)
print("Jumlah iterasi:", iterations)

"""Kedua algoritma tersebut merupakan algoritma pengurutan yang sederhana. Namun, dari segi kecepatan dan kinerja, Insertion Sort cenderung lebih optimal dibandingkan dengan Bubble Sort. Bubble Sort memiliki kompleksitas waktu terburuk O(n^2), sedangkan Insertion Sort memiliki kompleksitas waktu terburuk O(n^2) juga, tetapi dengan kinerja yang lebih baik dalam kasus terbaik dan rata-rata. Hal ini disebabkan karena Insertion Sort hanya memerlukan sedikit perbandingan dan pertukaran elemen jika array hampir terurut, sedangkan Bubble Sort selalu melakukan pertukaran secara berpasangan, tidak peduli seberapa dekat array dengan urutan yang benar.

### Jadi, jika Anda memiliki pilihan antara Bubble Sort dan Insertion Sort, disarankan untuk menggunakan Insertion Sort karena lebih efisien.
"""