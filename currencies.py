import pandas as pd
import xmltodict
import requests


def get_currency(file_name):
    """Возвращает список валют, с частотностью в более чем 5000 вакансий
    Args:
        file_name (str): Название файла для обработки
    Returns:
        Dict: key - валюта, value - количество раз
    """

    df = pd.read_csv(file_name)
    currency_dict = df['salary_currency'].value_counts().to_dict()
    print(currency_dict)
    currency_dict = {k: v for k, v in currency_dict.items() if v >= 5000}
    return currency_dict


def get_years_currency(file_name):
    """Собирает курсы валют за диапазон между самой старой и новой вакансией с частотностью раз в месяц,
     сохранет полученный результат в csv
    Args:
        file_name (str): Название файла для обработки
    """
    df = pd.read_csv(file_name)
    df = df[df["salary_currency"].isin(list(get_currency(file_name).keys()))]
    range_date = [df["published_at"].min().split("-")[:2], df["published_at"].max().split("-")[:2]]
    dict = {}
    url = r"http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/"
    result_data = pd.DataFrame()
    for year in range(int(range_date[0][0]), int(range_date[1][0]) + 1):
        for month in range(int(range_date[0][1]), 13):
            try:
                response = requests.get(fr"{url}{str(month).zfill(2)}/{year}")
            except:
                continue

            response = xmltodict.parse(response.text)
            for i in response['ValCurs']['Valute']:
                if i['CharCode'] in list(get_currency(file_name).keys()):
                    dict["date"] = f"{year}-{month}".zfill(2)
                    dict[i['CharCode']] = round(float(i["Value"].replace(",", ".")) / int(i["Nominal"]), 7)
            result_data = pd.concat([result_data, pd.DataFrame([dict])])
            if year == int(range_date[1][0]) and month == int(range_date[1][1]) or month == 12: break

    result_data.to_csv("currency.csv", index=False)


def get_info_by_year(file_name):
    """
    Группирует по годам
    Args:
        file_name (str): Название csv-файла для обработки
    """
    applier = lambda x: x[:4]
    df = pd.read_csv(file_name)
    df["year"] = df["published_at"].apply(applier)
    df = df.groupby("year")
    for year, info in df:
        info[["name", "salary_from", "salary_to", "salary_currency", "area_name", "published_at"]].to_csv(
            rf"csv\new_csv\{year}_year.csv", index=False)


file = input("Введите название файла: ")
get_currency(file)
get_info_by_year(file)
get_years_currency(file)
