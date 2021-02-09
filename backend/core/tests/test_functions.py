import pytest

from core.functions import get_valid_domain_name, get_valid_domain_name_without_suffix


@pytest.mark.parametrize(
    ["value", "value_expected"],
    (
        ("https://test_domain.pl/2139", "test_domain.pl"),
        ("https://test_domain.de?x=test", "test_domain.de"),
        ("http://forums.test_domain.co.uk", "test_domain.co.uk"),
        ("http://www.test_domain.org.kg/", "test_domain.org.kg"),
        ("test_domain.pl", "test_domain.pl"),
    ),
)
def test_get_valid_domain_name(value, value_expected):
    domain_name = get_valid_domain_name(value)
    assert domain_name == value_expected


@pytest.mark.parametrize(
    ["value", "value_expected"],
    (
        ("https://test_domain.pl/2139", "test_domain"),
        ("https://test_domain.de?x=test", "test_domain"),
        ("http://forums.test_domain.co.uk", "test_domain"),
        ("http://www.test_domain.org.kg/", "test_domain"),
        ("test_domain.pl", "test_domain"),
    ),
)
def test_get_valid_domain_name_without_suffix(value, value_expected):
    domain_name = get_valid_domain_name_without_suffix(value)
    assert domain_name == value_expected
