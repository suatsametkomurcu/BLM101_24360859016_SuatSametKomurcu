# -*- coding: utf-8 -*-
"""
BLM101 Dönem Projesi - RLE (Run-Length Encoding) Sıkıştırıcı

Encode örneği:
    AAAAABBBCCDAA -> 5A3B2C1D2A

Decode örneği:
    5A3B2C1D2A -> AAAAABBBCCDAA
"""

from __future__ import annotations


def rle_encode(text: str) -> str:
    """Metni RLE ile sıkıştırır (encode).

    Biçim: <sayı><karakter> tekrarları
    Örn: 'AAAAA' -> '5A'
    """
    if text == "":
        return ""

    out: list[str] = []
    count = 1
    # count: aynı karakterin ardışık tekrar sayısı

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            out.append(f"{count}{text[i - 1]}")
            count = 1

    out.append(f"{count}{text[-1]}")
    return "".join(out)


def rle_decode(encoded: str) -> str:
    """RLE ile sıkıştırılmış metni açar (decode).

    Örn: '5A3B' -> 'AAAAABBB'

    Hata kontrolleri:
    - Karakter gelmeden önce sayı gelmeli (örn: 'A3B' hatalı)
    - Metin sayı ile bitemez (örn: '12A3' hatalı)
    """
    if encoded == "":
        return ""

    out: list[str] = []
    num = ""

    for ch in encoded:
        if ch.isdigit():
            num += ch
        else:
            if num == "":
                raise ValueError("Geçersiz RLE: sayı olmadan karakter geldi.")
            out.append(ch * int(num))
            num = ""

    if num != "":
        raise ValueError("Geçersiz RLE: sonda karakter yok (sayı ile bitti).")

    return "".join(out)


def compression_ratio_percent(original: str, encoded: str) -> float:
    """Sıkıştırma oranını yüzde olarak hesaplar.

    Oran(%) = (1 - encoded_len / original_len) * 100
    Pozitif: küçülme, negatif: büyüme
    """
    if original == "":
        return 0.0
    return (1.0 - (len(encoded) / len(original))) * 100.0


def main() -> None:
    while True:
        print("\n=== RLE Sıkıştırıcı ===")
        print("1) Encode (Sıkıştır)")
        print("2) Decode (Aç)")
        print("3) Çıkış")

        choice = input("Seçim: ").strip()

        if choice == "1":
            text = input("Metin girin (örn: AAAAABBBCCDAA): ")
            encoded = rle_encode(text)
            ratio = compression_ratio_percent(text, encoded)
            print(f"Encoded: {encoded}")
            print(f"Sıkıştırma oranı: {ratio:.2f}%")

        elif choice == "2":
            encoded = input("Encoded metin girin (örn: 5A3B2C1D2A): ").strip()
            try:
                decoded = rle_decode(encoded)
                print(f"Decoded: {decoded}")
            except ValueError as e:
                print(f"Hata: {e}")

        elif choice == "3":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()