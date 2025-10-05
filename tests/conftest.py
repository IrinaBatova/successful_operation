import pytest


#Фикстуры для тестирования функции get_mask_card_number в модуле masks.py

@pytest.fixture
def card_number():
    return 7000792289606361

@pytest.fixture
def mask_card_number():
    return "7000 79** **** 6361"