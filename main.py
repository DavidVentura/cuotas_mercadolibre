#!/usr/bin/env python3
import requests
import re
import sys
from bs4 import BeautifulSoup, NavigableString
from pprint import pprint
URL = "https://www.mercadolibre.com.ar/gz/promociones-bancos"
INSTALLMENT_TO_N = re.compile(r'(?P<number>\d+) cuotas sin interés')
my_banks = {
            'Emitida por American Express': 6,
            'HSBC': 6
            }

def fetch():
    r = requests.get(URL)
    response = r.text
    r.close()
    return response


def parse(data):
    soup = BeautifulSoup(data, 'html.parser')
    ret = []
    for li in soup.select('li[name="promociones"]'):
        # print(li)
        bank = ''
        for bank_elem in li.select('.banklogoContainer span[alt]'):
            bank = bank_elem['alt']
        span = li.find('span', class_='installments')
        installments = span.text
        match = INSTALLMENT_TO_N.match(installments)
        if match is not None:
            installments = int(match.group('number'))

        card = elem_to_inner_text(span.parent)[0]
        # print(bank)
        # print(installments)
        # print(card)
        ret.append((bank, installments, card))
    return ret


def main():
    data = fetch()
    # open("dump", "w").write(data)
    # data = open("dump", "r").read()
    curr_promo = parse(data)
    all_banks = list(map(lambda x: x[0], curr_promo))
    # pprint(all_banks)
    filtered = list(filter(lambda x: x[0] in my_banks.keys(), curr_promo))
    matched = False
    for elems in filtered:
        if elems[1] >= my_banks[elems[0]]:
            matched = True
            print(elems[2], elems[0], elems[1], "installments!")

    if not matched:
        sys.exit(1)



def elem_to_inner_text(outer):
    ret = []
    for element in outer:
        if isinstance(element, NavigableString):
            text = element.strip()
            if len(text) > 0:
                ret.append(text)
    return ret 


if __name__ == '__main__':
    main()
