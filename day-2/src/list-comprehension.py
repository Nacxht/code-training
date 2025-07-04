print("=" * 4 + " LIST COMPREHENSION PYHTON VOKAL " + "=" * 4)

def cari_vokal(kalimat):
  vokal = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E','O']
  ketemu_vokal = [X for X in kalimat if X in vokal]
  return ketemu_vokal

kalimat = input("\nMasukkan kalimat: ")
print(f"Hasil array setelah difilter: {cari_vokal(kalimat)}")