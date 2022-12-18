import datetime
import cProfile


def profile(func):
    """Decorator for run function profile"""
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.print_stats(0)
        return result
    return wrapper

@profile
def parse_date_with_strptime_function(self):
    result_date = datetime.datetime.strptime(self[:10], '%Y-%m-%d').date()
    return '{0.day}.{0.month}.{0.year}'.format(result_date)


def parse_date_with_split(self):
    date = self.split("T")
    splited = date[0].split("-")
    day = splited[2].replace("0", "")
    return day + "." + splited[1] + "." + splited[0]


def parse_date_with_format(date):
    return '{0[2]}.{0[1]}.{0[0]}'.format(date[:10].split('-'))


def parse_det_with_slices(date):
    return f'{date[8:10].replace("0", "")}.{date[5:7]}.{date[:4]}'


print(parse_date_with_strptime_function('2020-11-03T17:11:35+0300'))
print(parse_date_with_split('2020-11-13T17:11:35+0300'))
print(parse_date_with_format('2020-11-13T17:11:35+0300'))
print(parse_det_with_slices('2020-11-03T17:11:35+0300'))
