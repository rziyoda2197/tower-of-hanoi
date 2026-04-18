def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"1 diskni {from_rod} dan {to_rod} ga ko'chirish")
        return
    tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
    print(f"1 diskni {from_rod} dan {to_rod} ga ko'chirish")
    tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)

n = int(input("Disklar sonini kiriting: "))
tower_of_hanoi(n, 'A', 'C', 'B')
```

Kodni ishlatish uchun quyidagicha qo'llaniladi:

1. Dasturga disklar sonini kiritish uchun `input` funksiyasidan foydalanish kerak.
2. Dastur disklar sonini `n` deb tanlaydi.
3. `tower_of_hanoi` funksiyasiga `n`, `from_rod`, `to_rod` va `aux_rod` parametrini berish kerak.
4. Dastur disklarni `from_rod` dan `to_rod` ga ko'chiradi.

Masalan, agar disklar soni 3 bo'lsa, dastur quyidagicha ishlaydi:

1. 3 diskli Tower of Hanoi masalasini hal qilish uchun quyidagicha ishlaydi:
 * 2 diskli Tower of Hanoi masalasini hal qilish uchun quyidagicha ishlaydi:
 + 1 diskli Tower of Hanoi masalasini hal qilish uchun quyidagicha ishlaydi:
  1 diskni A dan C ga ko'chirish
 + 1 diskni A dan B ga ko'chirish
 + 1 diskni C dan B ga ko'chirish
 * 1 diskni A dan C ga ko'chirish
2. 1 diskni A dan B ga ko'chirish
3. 2 diskni B dan C ga ko'chirish
