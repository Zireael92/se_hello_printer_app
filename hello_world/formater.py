
PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"
XML = "xml"
#JSON
SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, XML]


def get_formatted(msg, imie, format):
    result = ""
    if format == PLAIN:
        result = plain_text(msg, imie)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(msg, imie)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(msg, imie)
    elif format == JSON:
        result = format_to_json(msg, imie)
    elif format == XML:
        result = format_to_xml(msg, imie)
    return result


def format_to_json(msg, imie):
#    f = open('data.json',)
#    data = json.load(f)
#    for i in data['msg','moje_imie']:
#        print(i)
#    f.close()
    return ('{ "imie":"' + imie + '", "mgs":"' +
            msg + '"}')

def format_to_xml(msg, imie):
    return ('<greetings>\n'+ '<name> ' + imie + ' </name>\n'  + '<msg>' + msg + '</msg>\n' +'</greetings>\n')

def plain_text(msg, imie):
    return imie + ' ' + msg


def plain_text_upper_case(msg, imie):
    return plain_text(msg.upper(), imie.upper())


def plain_text_lower_case(msg, imie):
    return plain_text(msg.lower(), imie.lower())
