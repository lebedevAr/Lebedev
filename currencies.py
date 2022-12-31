import pandas as pd
import xmltodict
import requests

from math import isnan


class CSV_file:
    """Класс для обработки новых csv файлов.
            Attributes:
                file_name (str): название csv файла, расположенного в папке проекта
    """
    def __init__(self, file_name):
        """Инициализирует новый файл для обработки

            Args:
                file_name (str): название csv файла, расположенного в папке проекта
        """
        self.file_name = file_name

    def get_currency(self):
        """Возвращает список валют, с частотностью в более чем 5000 вакансий
        Returns:
            Dict: key - валюта, value - количество раз
        """

        df = pd.read_csv(self.file_name)
        currency_dict = df['salary_currency'].value_counts().to_dict()
        print(currency_dict)
        currency_dict = {k: v for k, v in currency_dict.items() if v >= 5000}
        return currency_dict

    def get_years_currency(self):
        """Собирает курсы валют за диапазон между самой старой и новой вакансией с частотностью раз в месяц,
         сохранет полученный результат в csv
        """
        df = pd.read_csv(self.file_name)
        df = df[df["salary_currency"].isin(list(self.get_currency().keys()))]
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
                    if i['CharCode'] in list(self.get_currency().keys()):
                        dict["date"] = f"{year}-{month}".zfill(2)
                        dict[i['CharCode']] = round(float(i["Value"].replace(",", ".")) / int(i["Nominal"]), 7)
                result_data = pd.concat([result_data, pd.DataFrame([dict])])
                if year == int(range_date[1][0]) and month == int(range_date[1][1]) or month == 12: break

        result_data.to_csv("currency.csv", index=False)

    def get_info_by_year(self):
        """Группирует по годам
        """
        applier = lambda x: x[:4]
        df = pd.read_csv(self.file_name)
        df["year"] = df["published_at"].apply(applier)
        df = df.groupby("year")
        for year, info in df:
            info[["name", "salary_from", "salary_to", "salary_currency", "area_name", "published_at"]].to_csv(
                rf"csv\new_csv\{year}_year.csv", index=False)

    @staticmethod
    def convert_salaries(row):
        """Переводит значение salary в рубли после сравнения даты появления вакансии
        с датой в файле currency.csv
        Args:
            row (Series): Строка в data_file
        Returns:
            float: Значение для ячейки 'salary' в рублях
        """
        converter = pd.read_csv("currency.csv")
        if row["salary_currency"] in converter.columns:
            answer = row["salary"] * float(converter[converter["date"] == row["published_at"][:7]][row["salary_currency"]])
            return round(answer, 2)
        return row["salary"]

    @staticmethod
    def get_avg_salary(row):
        """Возвращает значение для поля salary в зависимости от заполненности полей salary_from, salary_to
        Args:
            row (Series): Строка в data_file
        Returns:
            float: Значение для ячейки 'salary'
        """
        avg_values = []
        avg_values += [row["salary_from"]] if not isnan(row["salary_from"]) else []
        avg_values += [row["salary_to"]] if not isnan(row["salary_to"]) else []
        if len(avg_values) != 0:
            return sum(avg_values) / len(avg_values)
        return

    def get_conversion(self):
        """Объединяет в одну колонку данные из колонок salary_from, salary_to, salary_currency
        """
        data_file = pd.read_csv(self.file_name)
        result = data_file.loc[0:99].copy()
        result["salary"] = result.apply(lambda r: self.get_avg_salary(r), axis=1)
        result["salary"] = result.apply(lambda r: self.convert_salaries(r), axis=1)
        result.drop(labels=["salary_from", "salary_to", "salary_currency"], axis=1, inplace=True)
        result = result[["name", "salary", "area_name", "published_at"]]
        result.to_csv("new_vacancies.csv", index=False)
        print("cool")


new_csv = CSV_file("vacancies_dif_currencies.csv")
new_csv.get_conversion()
