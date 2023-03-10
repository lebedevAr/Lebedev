# Внимание! Коммиты 3.2.1 и 3.2.2 названы ошибочно, имелось ввиду 2.2.1 и 2.2.2!!!
# Lebedev
Скриншот прохождения Unit-тестов
![image](https://user-images.githubusercontent.com/105739082/208314334-a07bb490-8c13-446f-ad2f-fd8d127f70fa.png)

Скриншот прохождения doc-тестов
![image](https://user-images.githubusercontent.com/105739082/208315094-2dade12a-f5d6-4c0a-b849-e0fff56b9ff9.png)

# Profiling results
first func
![pr1](https://user-images.githubusercontent.com/105739082/208319041-d633d856-fa8d-4bff-b797-aa09a02936fc.png)

second func
![pr2](https://user-images.githubusercontent.com/105739082/208319055-0f7c1302-6e59-4369-80c5-d6fd47c95f61.png)

third func
![pr3](https://user-images.githubusercontent.com/105739082/208319059-1aa68eef-fba9-4be0-8c0c-065ac690ce8d.png)

thought func
![pr4](https://user-images.githubusercontent.com/105739082/208319065-db5460c9-e883-4580-8655-099bb4e7fd89.png)

По результатам профилирования самая быстрая функция получилась parse_det_with_slices

# Создана функция разделения на чанки:
![image](https://user-images.githubusercontent.com/105739082/209690103-3e7b9412-16ec-4555-a5ac-b965070528ad.png)

# Время выполнения без multiprocessing
![multi2](https://user-images.githubusercontent.com/105739082/210015406-7ad25453-9b78-4317-88cc-cd217a04e008.png)

# Время выполнения с multiprocessing (6 threads)
![multi1](https://user-images.githubusercontent.com/105739082/210015453-58ff6fc7-5e88-451e-9071-a54d6f0b421c.png)

# Время выполнения с concurrent.futures
(Получилось очень медленно, поэтому оставил с enable multiprocessin)
![multi3](https://user-images.githubusercontent.com/105739082/210016815-a3f4a09b-96db-45f0-ad6b-af819d717594.png)

# Частотность валют
![cur1](https://user-images.githubusercontent.com/105739082/210083101-3625f115-b0e4-4e09-a5d0-0d8743ab7f29.png)

$venv\Scripts\activate. bat
