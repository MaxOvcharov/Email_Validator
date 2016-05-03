"""  Check e-mail for compliance with the following rules:
1. e-mail consists of a name and a domain part, the parts are separated by a "@";
2. The domain part is not shorter than three characters and no longer than 256, is a
set of non-empty strings of characters a-z 0-9_- and separated by a point;
3. Each domain component part can not begin or end with a "-";
4. The name (before the @) does not exceed 128 characters, consists of the characters
a-z0-9 "._-;
5. in the name are not allowed two consecutive points;
6. if the name has double quotes ", they must be paired;
7. The name may occur in the characters "!,:", but only between the paired double quotes.
"""

import re


def check_email(email):
    """ This function checks an e-mail on the following conditions:
        1) Check e-mail using a regular expression;
        2) Check two consecutive points in name;
        3) Check len of name > 128 and domain > 256;
        4) Check starts/ends "-" in domain;
        5) Check the paired double quotes;
        6) Check the prohibited symbol between double quotes;
    """
    res = re.match(
        r'^([a-z0-9"!:,._-]+)@([a-z0-9_-]+(\.[a-z0-9_-]+)*(\.[a-z0-9_-]+))$',
        email)

    # Check e-mail using a regular expression
    if res:
        # take e-mail name before @
        email_name = res.group(1)
        # take e-mail domain
        email_dom = res.group(2)
    else:
        raise ValueError("Bad Syntax or doesn't exist username/domain")
    # Check two consecutive points in name
    if '..' in email_name:
        raise ValueError("Two points in a row")

    # Check len of name > 128 and domain > 256
    if (len(email_name) > 128) or (len(email_dom) > 256):
        raise ValueError('E-mail len out of range')

    # Check starts/ends "-" in domain
    lst_dom = email_dom.split(".")
    for dom in lst_dom:
        if dom.startswith("-") or dom.endswith("-"):
            raise ValueError('Domain starts/ends on "-"')

    # Check the paired double quotes
    if email_name.count('"') % 2 != 0:
        raise ValueError("Unpaired quotes")

    # Check the prohibited symbol between double quotes
    lst_proh = ["!", ":", ","]
    stripped = ''.join([value for key, value in enumerate(
        email_name.split('"')) if key % 2 == 0])

    for prohibited in lst_proh:
        if prohibited in stripped:
            raise ValueError("Prohibited symbol %s in email" % prohibited)

    return True

if __name__ == '__main__':
    # Enter your e-mail
    put_email = raw_input('Enter email here ->')
    # Start checking e-mail
    if check_email(put_email):
        print "This is correct e-mail: ", put_email
