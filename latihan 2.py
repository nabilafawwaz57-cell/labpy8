nilai = [80, 90, 'A', 70, 100, 'B']

total = 0
count = 0

for n in nilai:
    try:
        angka = float(n)
        total += angka
        count += 1
    except:
        print(f"Data '{n}' dilewati (bukan angka)")

if count > 0:
    rata = total / count
    print("\nRata-rata nilai valid:", rata)
else:
    print("Tidak ada data angka yang valid.")