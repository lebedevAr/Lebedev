from unittest import TestCase, main
from main import Vacancy, DataSet, Report

vacancy_dct = {'name': 'Программист', 'salary_from': "10", 'salary_to': '20', 'salary_currency': 'RUR',
               'area_name': "Екатеринбург", 'published_at': '2007-12-03T17:40:09+0300'}

filename = "vacancies_by_year.csv"
vacancyname = "Аналитик"
stats = [{2020: 15000}, {2020: 1000}, {"Екатеринбург": 30000}, {2020: 100}, {2020: 35000}, {"Москва": 0.23}]
avg_dict = {2020: [1, 2, 3], 2019: [2, 4]}
avg_true = {2020: 2, 2019: 3}


class VacancyTest(TestCase):
    def test_vacancy_type(self):
        self.assertEqual(type(Vacancy(vacancy_dct)).__name__, 'Vacancy')

    def test_vacancy_name(self):
        self.assertEqual(Vacancy(vacancy_dct).name, 'Программист')

    def test_year(self):
        self.assertEqual(type(Vacancy(vacancy_dct).year), int)

    def test_salary(self):
        self.assertEqual(type(Vacancy(vacancy_dct).salary_average), float)

    def test_area(self):
        self.assertEqual(type(Vacancy(vacancy_dct).area_name), str)


class DataSetTest(TestCase):
    def test_dataset_type(self):
        self.assertEqual(type(DataSet(file_name=filename, vacancy_name=vacancyname)).__name__, "DataSet")

    def test_dataset_filename(self):
        self.assertEqual(DataSet(file_name=filename, vacancy_name=vacancyname).file_name, 'vacancies_by_year.csv')

    def test_dataset_vacancyname(self):
        self.assertEqual(DataSet(file_name=filename, vacancy_name=vacancyname).vacancy_name, 'Аналитик')

    def test_dataset_avg_method(self):
        ds = DataSet(file_name=filename, vacancy_name=vacancyname)
        dic = ds.avg(avg_dict)
        self.assertEqual(dic[2020], avg_true[2020])
        self.assertEqual(dic[2019], avg_true[2019])

    def test_dataset_stats_method1(self):
        ds = DataSet(file_name=filename, vacancy_name=vacancyname)
        s1, s2, s3, s4, s5, s6 = ds.get_stats()
        self.assertEqual(type(s1), type(stats[0]))

    def test_dataset_stats_method2(self):
        ds = DataSet(file_name=filename, vacancy_name=vacancyname)
        s1, s2, s3, s4, s5, s6 = ds.get_stats()
        self.assertEqual(type(s2), type(stats[1]))

    def test_dataset_stats_method3(self):
        ds = DataSet(file_name=filename, vacancy_name=vacancyname)
        s1, s2, s3, s4, s5, s6 = ds.get_stats()
        self.assertEqual(type(s3), type(stats[2]))

    def test_dataset_stats_method4(self):
        ds = DataSet(file_name=filename, vacancy_name=vacancyname)
        s1, s2, s3, s4, s5, s6 = ds.get_stats()
        self.assertEqual(type(s4), type(stats[3]))

    def test_dataset_stats_method5(self):
        ds = DataSet(file_name=filename, vacancy_name=vacancyname)
        s1, s2, s3, s4, s5, s6 = ds.get_stats()
        self.assertEqual(type(s5), type(stats[4]))

    def test_dataset_stats_method6(self):
        ds = DataSet(file_name=filename, vacancy_name=vacancyname)
        s1, s2, s3, s4, s5, s6 = ds.get_stats()
        self.assertEqual(type(s6), type(stats[5]))


class ReportTest(TestCase):
    def test_report_type(self):
        self.assertEqual(type(Report(vacancy_name=vacancyname, stats1=stats[0], stats2=stats[1], stats3=stats[2],
                                     stats4=stats[3], stats5=stats[4], stats6=stats[5])).__name__, "Report")

    def test_report_vacancyname(self):
        self.assertEqual(Report(vacancy_name=vacancyname, stats1=stats[0], stats2=stats[1], stats3=stats[2],
                                stats4=stats[3], stats5=stats[4], stats6=stats[5]).vacancy_name, "Аналитик")

    def test_stats1(self):
        self.assertEqual(type(Report(vacancy_name=vacancyname, stats1=stats[0], stats2=stats[1], stats3=stats[2],
                                     stats4=stats[3], stats5=stats[4], stats6=stats[5]).stats1).__name__, "dict")

    def test_stats2(self):
        self.assertEqual(type(Report(vacancy_name=vacancyname, stats1=stats[0], stats2=stats[1], stats3=stats[2],
                                     stats4=stats[3], stats5=stats[4], stats6=stats[5]).stats2).__name__, "dict")

    def test_stats3(self):
        self.assertEqual(type(Report(vacancy_name=vacancyname, stats1=stats[0], stats2=stats[1], stats3=stats[2],
                                     stats4=stats[3], stats5=stats[4], stats6=stats[5]).stats3).__name__, "dict")

    def test_stats4(self):
        self.assertEqual(type(Report(vacancy_name=vacancyname, stats1=stats[0], stats2=stats[1], stats3=stats[2],
                                     stats4=stats[3], stats5=stats[4], stats6=stats[5]).stats4).__name__, "dict")

    def test_stats5(self):
        self.assertEqual(type(Report(vacancy_name=vacancyname, stats1=stats[0], stats2=stats[1], stats3=stats[2],
                                     stats4=stats[3], stats5=stats[4], stats6=stats[5]).stats5).__name__, "dict")


if __name__ == '__main__':
    main()
