# Напоминание: вам понадобится материал лекций:
# 3 - Списки и кортежи
# 4 - Словари и множества
# 7 и 8 - Классы
# 9 - Работа с файлами

# =====================================
# ЗАДАНИЕ 1: Работа с файлами
# =====================================
# TODO 1-1
#  Прочитайте данные из файла pilot_path.json (лекция 9)
import json

with open('pilot_path.json', 'r+') as f:
	data: dict = json.load(f)

# =====================================
# ЗАДАНИЕ 2: Расчет статистик
# =====================================
# TODO 2-1) Подсчитайте, сколько миссий налетал каждый пилот. Выведите результат в порядке убывания миссий
# ИНФОРМАЦИЯ:
# структура данных в файле: {"имя_пилота": "список_миссий":[миссия1, ...]]
# структура одной миссии: {"drone":"модель_дрона", "mission":[список точек миссии]}
# у пилотов неодинаковое количество миссий (и миссии могут быть разной длины). у каждой миссии - произвольная модель дрона

# РЕЗУЛЬТАТ:
# Пилоты в порядке убывания количества миссий: {'pilot3': 6, 'pilot8': 6, 'pilot6': 5, 'pilot2': 5, 'pilot7': 4, 'pilot9': 3, 'pilot5': 3, 'pilot4': 2, 'pilot1': 1}

# ВАШ КОД:
from typing import Dict

missions_info: Dict[str, int] = dict(
	{item[0], item[1]} 
	for item in sorted(
		[(item, len(data[item]['missions'])) for item in data], key=lambda item: item[1], reverse=True
	)
)

print(missions_info, end='\n\n')

# подсказка: готовый код нужной вам сортировки есть здесь (Sample Solution-1:): https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php
#print(f"Пилоты в порядке убывания количества миссий: {dict(sorted(pilot_mission_dict.items(), key=lambda item: item[1], reverse=True))}")

# TODO 2-2) Получите и выведите список всех моделей дронов, которые были в файле pilot_path.json
# Подсказка: внутри print используйте str.join(), чтобы соединить элементы списка (множества)

# РЕЗУЛЬТАТ:
# Полеты совершались на дронах следующих моделей: DJI Mavic 2 Pro, DJI Mavic 3, DJI Inspire 2, DJI Mavic 2 Zoom, DJI Mavic 2 Enterprise Advanced

# ВАШ КОД:
from typing import Set

unique_dron_names: Set[str] = set()

for pilot_name in data:
	for mission in data[pilot_name]['missions']:
		unique_dron_names.add(mission['drone'])

print(', '.join(unique_dron_names), end='\n\n')


# вывод результата (допишите код)
#print(f'Полеты совершались на дронах следующих моделей: {", ".join(...)}')

# TODO 2-3) Получите список миссий для каждой модели дронов, которые были в файле pilot_path.json,
# и выведите на экран модель дрона и количество миссий, которые он отлетал

# РЕЗУЛЬТАТ:
# Дрон DJI Inspire 2 отлетал 6 миссий
# Дрон DJI Mavic 2 Pro отлетал 6 миссий
# Дрон DJI Mavic 2 Enterprise Advanced отлетал 10 миссий
# Дрон DJI Mavic 3 отлетал 4 миссий
# Дрон DJI Mavic 2 Zoom отлетал 9 миссий

# ВАШ КОД:
from collections import defaultdict


drones_mission_counter: Dict[str, int] = defaultdict(int)

for pilot_name in data:
	for mission in data[pilot_name]['missions']:
		drones_mission_counter[mission['drone']] += 1

print('\n'.join([f'Дрон {name} отлетал {count} миссий' for name, count in drones_mission_counter.items()]), end='\n\n')

# вывод результата (допишите код)
#print(f'Дрон {...} отлетал {...} миссий')

# =====================================
# ЗАДАНИЕ 3: Создание классов
# =====================================
# Для вас уже написаны заготовки классов Aircraft и UAV
# TODO 3-1) Добавьте в класс UAV защищенный атрибут _=_missions (тип - список списков [[], []]), куда вы будете сохранять все миссии, которые отлетал беспилотник
# TODO 3-2) При помощи декоратора @property сделайте возможность чтения и записи миссий в этот атрибут (лекция 8)
# TODO 3-3) Создайте в классе UAV публичный метод count_missions, который возвращает количество миссий (лекция 7)
# TODO 3-4) Создайте класс MultirotorUAV - наследник классов Aircraft и UAV (лекция 7)

# ВАШ КОД (дополните то, что нужно в классах):
from typing import List


class Aircraft:
	def __init__(self, weight):
		self._weight = weight

class UAV(object):
	def __init__(self):
		self._has_autopilot = True

	# напишите код для декоратора атрибута _missions
	@property
	def missions(self) -> List[List[str]]:
		return self._missions
	
	@missions.setter
	def missions(self, mission: List[List[List[str]]]) -> None:
		if not hasattr(self, "missions"):
			self._missions: List[List[str]] = []
			
		if mission is not None:
			self._missions.extend(mission)

	@missions.deleter
	def missions(self) -> None:
		self._missions.clear()

	# напишите публичный метод count_missions
	def count_missions(self) -> int:
		return len(self.missions)


class MultirotorUAV(Aircraft, UAV):
	def __init__(self, weight, model, brand):
		super().__init__(weight)
		UAV.__init__(self)
		self.__model = model
		self.__brand = brand

	# напишите публичный метод get_info
	def get_info(self) -> None:
		print(f'Информация о дроне {self.__model}: масса {self._weight}, производитель {self.__brand}, количество миссий {self.count_missions()}')

	# напишите публичный метод get_model
	def get_model(self) -> None:
		return self.__model

# =====================================
# ЗАДАНИЕ 4: Работа с экземплярами классов
# =====================================
# TODO 4-1) Создайте экземпляры класса MultirotorUAV для всех моделей дронов, которые были в файле pilot_path.json
# Подсказка: созданные экземпляры класса MultirotorUAV сохраните в список для последующего использования
# TODO 4-2) При создании каждого экземпляра задайте ему как приватные атрибуты массу и производителя из справочника дронов drone_catalog в соответствии с моделью дрона
# TODO 4-3) А также добавьте ему миссии, найденные для этой модели дрона на шаге 2-3
# Напоминание: миссии находятся в атрибуте missions (с декоратором, и поэтому он публично доступен) в классе UAV

# каталог дронов уже готов для вас:
drone_catalog = {
	"DJI Mavic 2 Pro": {"weight":903, "brand":"DJI"},
	"DJI Mavic 2 Zoom": {"weight":900, "brand":"DJI"},
	"DJI Mavic 2 Enterprise Advanced": {"weight":920, "brand":"DJI"},
	"DJI Inspire 2": {"weight":1500, "brand":"DJI"},
	"DJI Mavic 3": {"weight":1000, "brand":"DJI"}
}

# ВАШ КОД:
drones_list: List[MultirotorUAV] = list()

for drone, info in drone_catalog.items():
	drones_list.append(MultirotorUAV(info['weight'], drone, info['brand']))


def get_missions_by_drone_name(data: dict, name: str) -> List[List[List[str]]]:
	missions: List[List[List[str]]] = list()

	for pilot_name in data:
		for mission in data[pilot_name]['missions']:
			if mission['drone'] == name:
				missions.append(mission['mission'])
	
	return missions


for index, drone in enumerate(drones_list):
	drones_list[index].missions = get_missions_by_drone_name(data, drone.get_model())


# TODO 4-4
# Напишите код, который выводит информацию по заданной модели дрона. Состав информации: масса, производитель, количество отлетанных миссий
# (название модели пользователь вводит с клавиатуры в любом регистре, но без опечаток)
# Подсказка: для этого вам необходимо вернуться в ЗАДАНИЕ 3 и добавить в класс два публичных метода: get_info(), который выводит нужную информацию,
# и get_model, который позволит получить название модели дрона

# РЕЗУЛЬТАТ:
# Информация о дроне DJI Mavic 2 Pro: масса 903, производитель DJI, количество миссий 6

# ВАШ КОД:
user_unput = input("Введите модель дрона (полностью) в любом регистре\n")

for drone in drones_list:
	if user_unput.lower() == drone.get_model().lower():
		drone.get_info()
