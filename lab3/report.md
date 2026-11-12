# Звіт до лабораторної роботи №3

**Тема:** Методи Assert, верифікація та валідація вхідних даних  
**Мета:** Навчитися перевіряти результат роботи Python-коду за допомогою pytest, тестувати правильні й неправильні вхідні дані та пройти практичні цикли TDD і BDD.

## Структура проєкту

```text
lab_3/
├── src/
│   ├── __init__.py
│   ├── bank_account.py
│   ├── temperature_converter.py
│   ├── user_registration_validator.py
│   └── discount_calculator.py
├── tests/
│   ├── test_bank_account.py
│   ├── test_temperature_converter.py
│   ├── test_user_registration.py
│   └── test_discount_calculator.py
├── features/
│   ├── user_registration.feature
│   └── discount.feature
├── .venv/
├── pytest.ini
├── requirements-dev.txt
└── report.md
```


## Реалізація TDD-класів та тестів
### BankAccount
Реалізував клас банківського рахунку із валідацією початкового балансу, суми поповнення та зняття грошей. Перевірив відсутність дублювання перевірок рефакторингом у приватний метод _validate_positive_amount.

### TemperatureConverter
Реалізував статичні методи конвертації температур між градусами Цельсія та Фаренгейта. Для тестування чисел з плаваючою крапкою застосував pytest.approx(), для обробки абсолютного нуля та неправильних типів - pytest.raises().

## Реалізація BDD-сценаріїв
### UserRegistrationValidator
Для опису поведінки валідатора створив сценарії у features/user_registration.feature.

### DiscountCalculator
Створив feature-файл features/discount.feature та відповідні step definitions у tests/test_discount_calculator.py із конвертацією типів через parsers.re та parsers.parse.

## Висновок
Під час виконання лабораторної роботи опанував методи верифікації результатів за допомогою assert та перевірки винятків pytest.raises(). Застосував цикл TDD для розробки класів BankAccount та TemperatureConverter. За допомогою pytest-bdd реалізував тестування поведінки програмного забезпечення на основі BDD-сценаріїв Given → When → Then для класів UserRegistrationValidator та DiscountCalculator.
