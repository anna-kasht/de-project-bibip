# привет, ревьюр!) хочу прокомментировать свое решение:
# 1 - нам была предоставлена возможность использовать все знания, 
# # не только полученные на курсе
# 2 - по организационным сложностям я не смогла получить
# от преподавателя ответы на свои вопросы, поэтому 
# решила все с использованием пандас.

# В целом я планирую еще для себя доделать это задание
# без использования пандас. Согласна с твоим комментом на все 100, что полезно)
# По поводу инициализации путей к файлам, спасибо за коммент. поняла, учту.
# И да, про более оптимальное решение при добавление каждой сущности 
# прям на все 100 согласна. После отправки уже сама поняла что нагородила

from models import Car, CarFullInfo, CarStatus, Model, ModelSaleStats, Sale
import os
from datetime import datetime
from decimal import Decimal
import pandas as pd


class CarService:
    def __init__(self, root_directory_path: str) -> None:
        self.root_directory_path = root_directory_path

    # Задание 1. Сохранение автомобилей и моделей
    def add_model(self, model: Model) -> Model:
        # зададим путь к файлу models.txt
        path_models = os.path.join(self.root_directory_path, 'models.txt')
        # путь к файлу models_index.txt
        path_idx_models = os.path.join(self.root_directory_path, 'models_index.txt')

        # Создаем пустые файлы, если их еще нет
        if not os.path.exists(path_models):
            data_mod = pd.DataFrame(
                {'id': [model.id],
                 'name': [model.name],
                 'brand': [model.brand]})
            data_idx = pd.DataFrame(
                {'idx': [model.id],
                 'line': [1]})
            data_mod.to_csv(path_models, sep=';', index=False, header=False)
            data_idx.to_csv(path_idx_models, sep=';',
                            index=False, header=False)
        # если файлы уже есть, добавим новые строки
        else:
            # строки в файл с моделями
            data_mod = pd.read_csv(path_models,
                                   sep=';',
                                   names=['id', 'name', 'brand']
                                   )
            new_line_mod = pd.DataFrame(
                {'id': [model.id],
                 'name': [model.name],
                 'brand': [model.brand]})
            data_mod = pd.concat([data_mod, new_line_mod], ignore_index=True)
            number_line = int(data_mod.shape[0])
            # строки в файл с индексами
            data_idx = pd.read_csv(path_idx_models,
                                   sep=';',
                                   names=['id', 'line'],
                                   dtype=int
                                   )
            new_line_idx = pd.DataFrame(
                {'id': [model.id],
                 'line': [number_line]})
            data_idx = pd.concat([data_idx, new_line_idx], ignore_index=True)
            data_idx.sort_values(by='id', inplace=True)
            data_mod.to_csv(path_models, sep=';', index=False, header=False)
            data_idx.to_csv(path_idx_models, sep=';',
                            index=False, header=False)
        return model
        
    # Задание 1. Сохранение автомобилей и моделей
    def add_car(self, car: Car) -> Car:
        # зададим путь к файлу cars.txt
        path_cars = os.path.join(self.root_directory_path, 'cars.txt')
        # путь к файлу cars_index.txt
        path_idx_cars = os.path.join(self.root_directory_path, 'cars_index.txt')

        # Создаем пустые файлы, если их еще нет
        if not os.path.exists(path_cars):
            data_car = pd.DataFrame(
                {'vin': [car.vin],
                 'model': [car.model],
                 'price': [car.price],
                 'date_start': [car.date_start],
                 'status': [car.status]})
            data_idx_car = pd.DataFrame(
                {'vin': [car.vin],
                 'line': [1]})
            data_car.to_csv(path_cars, sep=';', index=False, header=False)
            data_idx_car.to_csv(path_idx_cars, sep=';',
                                index=False, header=False)
        # если файлы уже есть, добавим новые строки
        else:
            # строки в файл с авто
            data_car = pd.read_csv(path_cars,
                                   sep=';',
                                   names=['vin', 'model', 'price', 'date_start', 'status']
                                   )
            new_line_car = pd.DataFrame(
                {'vin': [car.vin],
                 'model': [car.model],
                 'price': [car.price],
                 'date_start': [car.date_start],
                 'status': [car.status]})
            data_car = pd.concat([data_car, new_line_car], ignore_index=True)
            number_line_mod = int(data_car.shape[0])                      
            
            # строки в файл с индексами
            data_idx_car = pd.read_csv(path_idx_cars,
                                       sep=';',
                                       names=['vin', 'line']
                                       )
            new_line_idx_car = pd.DataFrame(
                {'vin': [car.vin],
                 'line': [number_line_mod]})
            data_idx_car = pd.concat([data_idx_car, new_line_idx_car],
                                     ignore_index=True)
            data_idx_car.sort_values(by='vin', inplace=True)
            data_car.to_csv(path_cars, sep=';', index=False, header=False)
            data_idx_car.to_csv(path_idx_cars, sep=';',
                                index=False, header=False)
        return car

    # Задание 2. Сохранение продаж.
    def sell_car(self, sale: Sale) -> Car:
        # зададим путь к файлу sales.txt
        path_sales = os.path.join(self.root_directory_path, 'sales.txt')
        # путь к файлу sales_index.txt
        path_idx_sales = os.path.join(self.root_directory_path, 
                                      'sales_index.txt')

        # Создаем пустые файлы, если их еще нет
        if not os.path.exists(path_sales):
            data_sale = pd.DataFrame(
                {'sales_number': [sale.sales_number],
                 'car_vin': [sale.car_vin],
                 'cost': [sale.cost],
                 'sales_date': [sale.sales_date]})
            data_idx_sale = pd.DataFrame(
                {'car_vin': [sale.car_vin],
                 'line': [1]})
            data_sale.to_csv(path_sales, sep=';', index=False, header=False)
            data_idx_sale.to_csv(path_idx_sales, 
                                 sep=';', index=False, header=False)
        else:
            # строки в файл с продажами
            data_sale = pd.read_csv(path_sales,
                                    sep=';',
                                    names=['sales_number', 'car_vin', 'cost', 'sales_date']
                                    )
            new_line_sale = pd.DataFrame(
                {'sales_number': [sale.sales_number],
                 'car_vin': [sale.car_vin],
                 'cost': [sale.cost],
                 'sales_date': [sale.sales_date]})
            data_sale = pd.concat([data_sale, new_line_sale], ignore_index=True)
            number_line_sale = int(data_sale.shape[0])
            
            # строки в файл с индексами
            data_idx_sale = pd.read_csv(path_idx_sales,
                                        sep=';',
                                        names=['vin', 'line']
                                        )
            new_line_idx_sale = pd.DataFrame(
                {'car_vin': [sale.car_vin],
                 'line': [number_line_sale]})
            data_idx_sale = pd.concat([data_idx_sale, new_line_idx_sale], ignore_index=True)
            data_idx_sale.sort_values(by='car_vin', inplace=True)
            data_sale.to_csv(path_sales, sep=';', index=False, header=False)
            data_idx_sale.to_csv(path_idx_sales, sep=';',
                                 index=False, header=False)

        # обновим данные с файле cars
        path_cars = os.path.join(self.root_directory_path, 'cars.txt')
        data_car = pd.read_csv(path_cars,
                               sep=';',
                               names=['vin', 'model', 'price', 'date_start', 'status']
                               )
        data_car.loc[data_car['vin'] == sale.car_vin, 'status'] = 'sold'
        data_car.to_csv(path_cars, sep=';', index=False, header=False)
        
        # Возвращаем объект Car, соответствующий проданной машине
        updated_car_data = data_car.loc[data_car['vin'] == sale.car_vin].iloc[0]
                   
        updated_car = Car(vin=updated_car_data['vin'],
                          model=int(updated_car_data['model']),
                          price=Decimal(str(updated_car_data['price'])),
                          date_start=updated_car_data['date_start'],
                          status=CarStatus(updated_car_data['status']))
        return updated_car
        
    # Задание 3. Доступные к продаже
    def get_cars(self, status: CarStatus) -> list[Car]:
        path_cars = os.path.join(self.root_directory_path, 'cars.txt')
        data_car = pd.read_csv(path_cars,
                               sep=';',
                               names=['vin', 'model', 'price', 'date_start', 'status'],
                               dtype={'price': str}
                               )
        data_car_filt = data_car.loc[data_car['status'] == status.value]
        # Преобразуем каждую строку в объект Car
        result = []
        if data_car_filt.shape[0] != 0:
            for _, row in data_car_filt.iterrows():
                price_car = Decimal(row['price']).quantize(Decimal('.01'))
                try:
                    st_date = datetime.strptime(row['date_start'], '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    st_date = datetime.strptime(row['date_start'], '%Y-%m-%d')
                car = Car(vin=row['vin'],
                          model=int(row['model']),
                          price=price_car,
                          date_start=st_date,
                          status=CarStatus(row['status'])) 
                result.append(car)
        return result
    
    # Задание 4. Детальная информация
    def get_car_info(self, vin: str) -> CarFullInfo | None:
        # зададим пути к файлам
        path_models = os.path.join(self.root_directory_path, 'models.txt')
        path_cars = os.path.join(self.root_directory_path, 'cars.txt')
        path_sales = os.path.join(self.root_directory_path, 'sales.txt')
        
        if not os.path.exists(path_sales):
            data_sales = pd.DataFrame(columns=['sales_number',
                                               'car_vin',
                                               'cost',
                                               'sales_date'])
        else:
            data_sales = pd.read_csv(path_sales, sep=';',
                                 names=['sales_number', 'car_vin', 'cost', 'sales_date'],
                                 dtype={'cost': str})

        # загрузим данные
        data_car = pd.read_csv(path_cars, sep=';',
                               names=['vin', 'model', 'price', 'date_start', 'status'],
                               dtype={'price': str}
                               )
        data_model = pd.read_csv(path_models, sep=';',
                                 names=['id', 'name', 'brand']
                                 )
        
        # отфильруем таблицу с по вин-номеру
        data_car = data_car.loc[data_car['vin'] == vin]
        
        if data_car.shape[0] != 0:
            # объединим таблицы
            data_join_1 = pd.merge(data_car, data_model, left_on='model',
                                   right_on='id',
                                   how='left')
            data_join_2 = pd.merge(data_join_1, data_sales, left_on='vin',
                                   right_on='car_vin',
                                   how='left')
            data_car_full = data_join_2[
                ['vin', 'name', 'brand', 'price',
                 'date_start', 'status', 'sales_date', 'cost']
                ]
            data_car_full = data_car_full.copy()
            data_car_full.fillna({'sales_date': 'None', 'cost': 'None'},
                                 inplace=True)
            full_data_list = data_car_full.values.tolist()[0]
            if full_data_list[7] == 'None':
                sl_cost = None
            else:
                sl_cost = Decimal(str(full_data_list[7]))
            if full_data_list[6] == 'None':
                sl_date = None
            else:
                try:
                    sl_date = datetime.strptime(full_data_list[6], '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    sl_date = datetime.strptime(full_data_list[6], '%Y-%m-%d')

            full_info_car = CarFullInfo(vin=full_data_list[0],
                                        car_model_name=full_data_list[1],
                                        car_model_brand=full_data_list[2],
                                        price=Decimal(str(full_data_list[3])),
                                        date_start=full_data_list[4],
                                        status=CarStatus(full_data_list[5]),
                                        sales_date=sl_date,
                                        sales_cost=sl_cost)
        else:
            full_info_car = None
        return full_info_car
    
    # Задание 5. Обновление ключевого поля
    def update_vin(self, vin: str, new_vin: str) -> Car:
        # зададим путь к файлу cars.txt
        path_cars = os.path.join(self.root_directory_path, 'cars.txt')
        # путь к файлу cars_index.txt
        path_idx_cars = os.path.join(self.root_directory_path, 'cars_index.txt')
        
        # загрузим данные
        data_car = pd.read_csv(path_cars,
                               sep=';',
                               names=['vin', 'model', 'price', 'date_start', 'status']
                               )
        # строки в файл с индексами
        data_idx_car = pd.read_csv(path_idx_cars,
                                   sep=';',
                                   names=['vin', 'line']
                                   )
        data_car.loc[data_car['vin'] == vin, 'vin'] = new_vin
        data_idx_car.loc[data_idx_car['vin'] == vin, 'vin'] = new_vin
        data_idx_car.sort_values(by='vin', inplace=True)
        data_car.to_csv(path_cars, sep=';', index=False, header=False)
        data_idx_car.to_csv(path_idx_cars, sep=';',
                            index=False, header=False)
        # Возвращаем объект Car, соответствующий проданной машине
        updated_vin_car = data_car.loc[data_car['vin'] == new_vin].iloc[0]
                   
        updated_vin_car = Car(vin=updated_vin_car['vin'],
                              model=int(updated_vin_car['model']),
                              price=Decimal(str(updated_vin_car['price'])),
                              date_start=updated_vin_car['date_start'],
                              status=CarStatus(updated_vin_car['status']))
        return updated_vin_car

    # Задание 6. Удаление продажи
    def revert_sale(self, sales_number: str) -> Car:
        # зададим пути к файлам 
        path_cars = os.path.join(self.root_directory_path, 'cars.txt')
        path_sales = os.path.join(self.root_directory_path, 'sales.txt')
        path_idx_sales = os.path.join(self.root_directory_path, 
                                      'sales_index.txt')
        
        # загрузим данные
        data_car = pd.read_csv(path_cars, sep=';', 
                               names=['vin', 'model', 'price', 'date_start', 'status'],
                               dtype={'price': str}
                               )
        data_sales = pd.read_csv(path_sales, sep=';',
                                 names=['sales_number', 'car_vin', 'cost', 'sales_date'],
                                 dtype={'cost': str})
        data_idx_sale = pd.read_csv(path_idx_sales,
                                    sep=';',
                                    names=['vin', 'line']
                                    )
                                       
        # запишем вин номер по удаляемой продаже, чтобы потом поменять статус
        vin_to_change = sales_number.split('#')[1]
        row_to_delete = data_sales.loc[data_sales['sales_number'] == sales_number]
        
        # Удаляем запись о продаже
        data_sales = data_sales.drop(index=row_to_delete.index)
        data_sales.reset_index(inplace=True, drop=True)
        data_car.loc[data_car['vin'] == vin_to_change, 'status'] = 'available'
        number_model_car = data_car.loc[data_car['vin'] == vin_to_change, 'model'].iloc[0]
        price_car = data_car.loc[data_car['vin'] == vin_to_change, 'price'].iloc[0]
        date_st = data_car.loc[data_car['vin'] == vin_to_change, 'date_start'].iloc[0]
        car_st = data_car.loc[data_car['vin'] == vin_to_change, 'status'].iloc[0]
        if data_sales.shape[0] != 0:
            data_join_1 = pd.merge(data_sales, data_idx_sale, left_on='car_vin',
                                   right_on='vin',
                                   how='left')
            data_join_1['line'] = data_join_1.index + 1
            data_idx_sale = data_join_1[['vin', 'line']]
            data_idx_sale.sort_values(by='car_vin', inplace=True)
        else:
            data_idx_sale = data_idx_sale.head(0)
        data_sales.to_csv(path_sales, sep=';', index=False, header=False)
        data_idx_sale.to_csv(path_idx_sales, sep=';',
                                 index=False, header=False)
        data_car.to_csv(path_cars, sep=';', index=False, header=False)
        # Возвращаем объект Car, соответствующий удаленной продаже
        delete_car = Car(vin=vin_to_change,
                         model=int(number_model_car),
                         price=Decimal(str(price_car)),
                         date_start=date_st,
                         status=CarStatus(car_st))
        return delete_car
    
    # Задание 7. Самые продаваемые модели
    def top_models_by_sales(self) -> list[ModelSaleStats]:
        # зададим пути к файлам models.txt
        path_models = os.path.join(self.root_directory_path, 'models.txt')
        path_cars = os.path.join(self.root_directory_path, 'cars.txt')
        path_sales = os.path.join(self.root_directory_path, 'sales.txt')
        # загрузим данные
        data_car = pd.read_csv(path_cars, sep=';', 
                               names=['vin', 'model', 'price', 'date_start', 'status']
                               )
        data_model = pd.read_csv(path_models, sep=';',
                                 names=['id', 'name', 'brand']
                                 )
        data_sales = pd.read_csv(path_sales, sep=';',
                                 names=['sales_number', 'car_vin', 'cost', 'sales_date'])
        # объединим таблицы
        data_join_1 = pd.merge(data_car, data_model, left_on='model',
                               right_on='id',
                               how='left')
        data_join_2 = pd.merge(data_join_1, data_sales, left_on='vin',
                               right_on='car_vin',
                               how='left')
        data_filt = data_join_2.loc[data_join_2['status'] == 'sold']
        grouped_df = data_filt.groupby(
            ['name', 'brand'], 
            as_index=False)['cost'].count()
        # Добавляем среднюю цену по каждой модели
        grouped_df['avg_price'] = data_filt.groupby(['name', 'brand'])['price'].mean().values
        # Сортируем по количеству продаж, а затем по средней цене
        sorted_df = grouped_df.sort_values(
            by=['cost', 'avg_price'], ascending=[False, False]
            )
        # Выбираем топ-3 модели
        top_3_models = sorted_df.head(3)
        # преобразуем DataFrame в список объектов ModelSaleStats
        result = []
        for index, row in top_3_models.iterrows():
            model_stats = ModelSaleStats(
                car_model_name=row['name'],
                brand=row['brand'],
                sales_number=int(row['cost']),
            )
            result.append(model_stats)
        return result
