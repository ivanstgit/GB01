import requests as rq
import datetime as dt
import decimal as dec


def currency_rates(currency: str):
    """
    Return last currency rate from CBR
    :param currency: currency code, for instance 'USD'
    :return: tuple(datetime.date date, decimal rate)
    """
    curr = currency.upper()

    cbr_url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    cbr_request = rq.get(cbr_url)

    # parse xml on main tag <Valute> and tags <Valcurs>
    xml = cbr_request.text
    valute_list_trash = xml.split('<Valute')
    date_str = valute_list_trash[0].split('<ValCurs Date="')[1][0:10]
    date_day, date_mon, date_year = date_str.split('.')
    res_date = dt.date(day=int(date_day), month=int(date_mon), year=int(date_year))

    nominal_str = ''
    value_str = ''
    for trash in valute_list_trash[1:]:
        curr_str = trash.split('<CharCode>')[1][0:3]
        if curr_str == curr:
            nominal_str = trash.split('<Nominal>')[1].split('</Nominal>')[0].replace(',', '.')
            value_str = trash.split('<Value>')[1].split('</Value>')[0].replace(',', '.')
            break

    if value_str != '' and nominal_str != '':
        result = (res_date, dec.Decimal(value_str) / dec.Decimal(nominal_str))
    else:
        result = None
    return result


if __name__ == '__main__':
    for currency in ['USD', 'EUR', 'UZS', 'RUB']:
        rate = currency_rates(currency)
        if rate:
            print(f'{currency}: {rate[1]} on {rate[0]}')
        else:
            print(f'{currency}: {rate}')
