import re
import csv
import os


def make_csv(filename: str):
    with open(filename, encoding='utf-8') as f:
        text = f.readlines()
    all_addressees_raw = []
    for i in text:
        raw_addressee = re.findall(r'^\*? ?\d{1,3}\..+', i)
        if len(raw_addressee) != 0:
            addr = raw_addressee[0].replace('*', '').strip()
            addr = ' '.join(addr.split()[1:])
            if addr.endswith('.'):
                all_addressees_raw.append(addr[:-1])
            else:
                all_addressees_raw.append(addr)

    all_addressees = []
    filename = filename.split('/')[-1][:-4]
    for addr in all_addressees_raw:
        addr = addr.lower()
        addr = addr.replace('неотправленное', '')
        addr = addr.replace('черновое', '')
        addr = re.sub(r'\(.+?\)', '', addr)
        addr = re.sub(r'\(.+', '', addr)
        addr = re.sub(r'\d+.*', '', addr)
        addr = addr.replace(',', '')
        addr = addr.replace(' от ', '')
        all_addressees.append(addr.strip())

    path = '/Users/mariabocharova/PycharmProjects/randomStuff/DH_Project_2/letters_csv'
    with open(f'{path}/{filename}.csv', 'a') as f:
        writer = csv.writer(f)
        for name in all_addressees:
            writer.writerow(('л. н. толстой', name))


path = '/Users/mariabocharova/PycharmProjects/randomStuff/DH_Project_2/letters_txt'
for i in os.listdir(path):
    make_csv(f'{path}/{i}')

