def luhn_algorithm(card_number):
    """Функція для виконання алгоритму Луна для перевірки валідності номера картки."""
    # Конвертуємо рядок у список цифр
    digits = [int(digit) for digit in card_number if digit.isdigit()]

    # Перевертаємо список
    digits.reverse()

    # Подвоюємо кожен другий розряд
    for i in range(1, len(digits), 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    # Сумуємо всі цифри
    total = sum(digits)

    # Перевіряємо, чи сума кратна 10
    return total % 10 == 0

def validate_card(card_number):
    """Функція для перевірки валідності номера картки."""
    if luhn_algorithm(card_number):
        return "Карта правильна"
    else:
        return "Карта не правильна"

# Перевірка валідності номера картки
card_number = input("Введіть номер картки: ")
print(validate_card(card_number))
