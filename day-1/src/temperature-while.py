print("=" * 4 + " KONVERSI SUHU " + "=" * 4)
c = float(input("\nMasukkan suhu (dalam satuan celcius): "))

while True:
  kv = (input("Konversi ke satuan apa? (fahrenheit/kelvin): "))

  if kv == 'fahrenheit':
    fahrenheit = (c * 9/5) + 32
    print(f"Hasil konversi Celcius => Fahrenheit: {fahrenheit}")
    break

  elif kv == 'kelvin':
    kelvin = c + 273,15
    print(f"Hasil konversi Celcius => kelvin: {kelvin}")
    break

  else:
    print("satuan yang dipilih tidak valid! pilih satuan ulang!")