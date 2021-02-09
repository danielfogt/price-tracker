import tldextract


def get_valid_domain_name(url: str) -> str:
    """
    :param url: string that should be registered domain, url without or with protocol http(s)
    :return: valid domain name, e.g. example.com
    """
    ext = tldextract.extract(url)
    return f"{ext.registered_domain}"


def get_valid_domain_name_without_suffix(url: str) -> str:
    """
    :param url: string that should be registered domain, url without or with protocol http(s)
    :return: valid domain name without suffix, e.g. example (not example.com)
    """
    ext = tldextract.extract(url)
    return f"{ext.domain}"
