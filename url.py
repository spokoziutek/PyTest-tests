# Walidacja poprawności adresu URL
# Stworzyć funkcję sprawdzającą poprawność adresu URL (protokół http) podanego w parametrze url. Funkcja zwraca True,
# jeśli adres ma poprawny format, False w przeciwnym wypadku. 
# Należy przygotować testy sprawdzające poprawność rezultatu zwracanego przez funkcję. Przykład poprawnego adresu: http://usz.edu.pl


def isUrlValid(url):

    if not url.startswith("http://"):
        return False
    

    url = url[7:]
    

    if not url:
        return False
    

    parts = url.split("/", 1)
    domain_port = parts[0]
    

    if not domain_port:
        return False
    

    domain_parts = domain_port.split(":")
    domain = domain_parts[0]
    

    if not domain:
        return False
    

    if "." not in domain:
        return False
    

    domain_labels = domain.split(".")
    if any(not label or len(label) > 63 for label in domain_labels):
        return False
    

    if len(domain_parts) == 2:
        port = domain_parts[1]
        if not port.isdigit() or not (1 <= int(port) <= 65535):
            return False
    elif len(domain_parts) > 2:
        return False
    
    return True


def testIsUrlValid():
    assert isUrlValid("http://example.com") == True
    assert isUrlValid("http://example.com/path") == True
    assert isUrlValid("http://example.com:8080") == True
    assert isUrlValid("http://example.com:8080/path") == True
    assert isUrlValid("https://example.com") == False
    assert isUrlValid("ftp://example.com") == False
    assert isUrlValid("http://example") == False
    assert isUrlValid("http://.com") == False
    assert isUrlValid("example.com") == False
    assert isUrlValid("http://example.toolongtld") == False
    assert isUrlValid("http://example..com") == False

