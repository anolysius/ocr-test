import re
from typing import List

from .patterns import *


def extractAddress(paragraph: List[str]):
    replace_from = [' .', '.,', ' .,', ' ,', ',,', ';', ' ;', ':', ' :', '_', ' _']
    replace_to = '.'
    addr = None
    for i, p in reversed(list(enumerate(paragraph))):
        match = re.search(street_pattern, p)
        post_match = re.search(po_box_pattern, p)
        if match or post_match:
            addr = match.group(0) if match else post_match.group(0)
            addr = addr.rstrip()
            for r in replace_from:
                addr = addr.replace(r, replace_to)
            for s in street:
                addr = addr + '.' if addr.endswith(s) else addr

    return addr


def extractCityStateZipcode(name: str):
    state = None
    match = re.search(city_state_zip_pattern, name)
    if match:
        city = match.group('city')
        state = match.group('state')
        zip_code = match.group('zip')
        state = {'city': city, 'state': state, 'zip': zip_code}

    return state


def extractTotalAddress(paragraph: List[str]):
    total_address = {}
    from_index = -1
    to_index = -1

    to_target = 'Dear Peter'
    to_target_back = 'eter'

    for i, p in enumerate(paragraph):
        address_match = re.search(address_pattern, ''.join(p))
        po_box_match = re.search(po_box_pattern, p)
        if from_index == -1 and (po_box_match or address_match):
            from_index = i

        if to_index == -1 and (to_target in p or (i > 4 and to_target_back in p)):
            to_index = i

        if to_index != -1:
            break

    mail_code = None
    code = None
    address = None
    if to_index != -1:
        mail_code_index = to_index - 1
        mail_code = paragraph[mail_code_index]

        zip_code_index = mail_code_index - 1
        city_state_zipcode = paragraph[zip_code_index]
        check_before = paragraph[zip_code_index - 1]
        if re.search(digit_start_pattern, city_state_zipcode) or re.search(state_start_patter, city_state_zipcode):
            city_state_zipcode = check_before + ", " + city_state_zipcode
            zip_code_index = zip_code_index - 1

        replace_from = ['.', ' .', '.,', ' .,', ' ,', ',,', ';', ' ;', ':', ' :', '_', ' _']
        replace_to = ','
        for f in replace_from:
            city_state_zipcode = city_state_zipcode.replace(f, replace_to)

        # for s in states:
        #     city_state_zipcode = city_state_zipcode.replace(s + ",", s)
        #     city_state_zipcode = city_state_zipcode.replace(s + " ,", s)
        #     city_state_zipcode = city_state_zipcode.replace(s + ".", s)
        #     city_state_zipcode = city_state_zipcode.replace(s + " .", s)

        code = extractCityStateZipcode(city_state_zipcode)
        address = extractAddress(paragraph[:zip_code_index])

    if code is not None:
        total_address.update(code)
    if mail_code is not None:
        total_address['mail_code'] = mail_code
    if address is not None:
        total_address['address'] = address
    return total_address


def extractName(name: str):
    names = None
    match = re.search(name_pattern, name)
    if match:
        title = match.group('title') or ''
        firstname = match.group('firstname')
        middlename = match.group('middlename') or ''
        lastname = match.group('lastname')
        names = {'title': title, 'first_name': firstname, 'middle_name': middlename, 'last_name': lastname}

    return names


def refineName(paragraph: List[str]):
    _from = 'From'

    from_index = -1
    to_index = -1

    replace_from = [' .', ',', ' ,', ';', ' ;', ':', ' :', '_', ' _']
    replace_to = '.'
    for i, p in enumerate(paragraph):
        if from_index == -1 and _from in p:
            from_index = i

        address_match = re.search(address_pattern, ''.join(p))
        po_box_match = re.search(po_box_pattern, p)

        if to_index == -1 and (po_box_match or address_match):
            to_index = i

        if to_index != -1:
            break

    if from_index != -1 and to_index == -1:
        to_index = from_index + 2

    if from_index == -1 or to_index == -1:
        return None

    joined_name = " ".join(paragraph[from_index + 1:to_index])

    for t in replace_from:
        joined_name = joined_name.replace(t, replace_to)

    return joined_name


def extractNames(paragraph: List[str]):
    refined_name = refineName(paragraph)
    if refined_name is None:
        return None
    return extractName(refined_name)


def isCommonForm(paragraph: List[str]):
    if len(paragraph) < 3:
        return False

    find_target = 'to Peter Flaherty'
    fine_target2 = 'eter Flaher'
    for i in range(3):
        if (find_target in paragraph[i]) or (fine_target2 in paragraph[i]):
            return True

    return False


def isMailForm(paragraph: List[str]):
    if len(paragraph) < 3:
        return False

    find_target = '22630'
    find_target2 = 'Box 486'
    for i, p in enumerate(paragraph):
        if (i > 6 and find_target in p) or (find_target2 in p):
            return True

    return False
