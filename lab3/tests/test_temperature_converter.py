import pytest
from src.temperature_converter import TemperatureConverter

def test_celsius_to_fahrenheit_conversions():
    assert TemperatureConverter.celsius_to_fahrenheit(0) == pytest.approx(32.0)
    assert TemperatureConverter.celsius_to_fahrenheit(100) == pytest.approx(212.0)

def test_fahrenheit_to_celsius_conversions():
    assert TemperatureConverter.fahrenheit_to_celsius(32) == pytest.approx(0.0)
    assert TemperatureConverter.fahrenheit_to_celsius(212) == pytest.approx(100.0)

def test_invalid_temperature_type_raises_type_error():
    with pytest.raises(TypeError, match="Temperature must be a number"):
        TemperatureConverter.celsius_to_fahrenheit("25")
    with pytest.raises(TypeError, match="Temperature must be a number"):
        TemperatureConverter.celsius_to_fahrenheit(True)

def test_celsius_below_absolute_zero_raises_value_error():
    with pytest.raises(ValueError, match="Temperature is below absolute zero"):
        TemperatureConverter.celsius_to_fahrenheit(-280)

def test_fahrenheit_below_absolute_zero_raises_value_error():
    with pytest.raises(ValueError, match="Temperature is below absolute zero"):
        TemperatureConverter.fahrenheit_to_celsius(-460)