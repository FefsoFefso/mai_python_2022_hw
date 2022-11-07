drone_list = ["DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", "DJI Mavic 2 Enterprise Advanced", "AUTEL Evo II Pro", "DJI Mini 2", "Autel Evo Nano", "Autel Evo Lite Plus", "Parrot Anafi", "Dji Inspire 2", "DJI Mavic 3", "DJI Mavic Air2s", "Ryze Tello", "Eachine Trashcan"]

drone_weight_list = [903, 900, 920, 980, 249, 249, 600, 540, 1500, 1000, 570, 130, 110]

#в drone по очереди попадает каждый дрон из списка drone_list
#for drone in drone_list:
#	print(drone)

#TODO1
#выведите все дроны производителя, название которого введет пользователь через input, и подсчитайте их количество. 
#учтите, что:
#1) DJI и Dji - это один и тот же производитель! такие случаи тоже должны обрабатываться
#2) при выводе исправьте название производителя, если допущена ошибка. правильный вариант названия: DJI, Autel
print('1', '---' * 10)

from typing import List, Tuple, Dict

true_drone_manufacturer_names: Tuple[str] = ("DJI", "Autel", "Parrot", "Ryze", "Eachine")

try:
	while manufacturer_name := input().strip():
		company_drones_list: List[str] = list()

		for drone in drone_list:
			if manufacturer_name.lower() in drone.split()[0].lower():
				company_drones_list.append(
					' '.join([
						w if w.lower() not in [
							drone_name.lower() for drone_name in true_drone_manufacturer_names
						]
						else true_drone_manufacturer_names[
							[
								drone_name.lower() for drone_name in true_drone_manufacturer_names
							].index(w.lower())
						]
						for w in drone.split()
					])
				)
		
		print(f'By {manufacturer_name} found {len(company_drones_list)}:')
		
		if len(company_drones_list):
			print(*company_drones_list, sep='\n')
except (EOFError):
	print('2', '---' * 10)

#TODO2
#подсчитайте количество моделей дронов каждого производителя из списка drone_list. производители: DJI, Autel, Parrot, Ryze, Eachine
def count_value_by_name(manufacturer_name: str, drone_list: List[str]) -> int:
	return len(
		[	
			drone_name 
			for drone_name in drone_list 
			if manufacturer_name.lower() == drone_name.split()[0].lower()
		]
	)


manufacturer_stats: Dict[str, int] = dict()

for manufacturer_name in true_drone_manufacturer_names:
	manufacturer_stats[manufacturer_name] = count_value_by_name(manufacturer_name, drone_list)

print(manufacturer_stats)

#TODO3
#выведите все дроны из списка, которые нужно регистрировать (масса больше 150 г), и подсчитайте их количество. 
#сделайте то же самое для всех дронов, которые не нужно регистрировать
#для этого вам нужно параллельно обрабатывать два списка: drone_list и drone_weight_list:
#как работает zip, мы разберем на лекции про списки. пока что просто пользуйтесь
print('3', '---' * 10)

need_to_register: List[str] = list()
no_need_to_register: List[str] = list()

for drone, weight in zip(drone_list,  drone_weight_list):
	if weight > 150:
		need_to_register.append(drone)
	else:
		no_need_to_register.append(drone)

print(f'Need to registed ({len(need_to_register)}): {need_to_register}')
print(f'No need to registed ({len(no_need_to_register)}): {no_need_to_register}')

#TODO4
#для каждого дрона из списка выведите, нудно ли согласовывать полет при следующих условиях:
#высота 100 м, полет над населенным пунктом, вне закрытых зон, в прямой видимости
#помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!
print('4', '---' * 10)

class SupInfo:
	HEIGHT: int = 321
	IS_OVER_POPULATED_AREA: bool = True
	IS_INSIDE_OF_CLOSEST_AREA: bool = False
	IS_IN_LINE_OF_SIGHT: bool = True


for drone, weight in zip(drone_list, drone_weight_list):
	if SupInfo.HEIGHT > 150 or \
			(SupInfo.IS_OVER_POPULATED_AREA and weight > 150) or \
			SupInfo.IS_INSIDE_OF_CLOSEST_AREA or \
			not SupInfo.IS_IN_LINE_OF_SIGHT:
		print(f'Need to approve for {drone}')
	else:
		print(f'No need to approve for {drone}')

#TODO5*
#модифицируйте решение задания TODO1:
#теперь для введенного пользователем производителя вы должны вывести строку, содержащую перечисление моделей и БЕЗ названия производителя.
#например, пользователь ввел "Autel". ваша программа должна вывести вот такой результат: "Evo II Pro, Evo Nano, Evo Lite Plus". для этого вам понадобится несколько функций работы со строками. решить эту задачу можно несколькими разными способами
#производители те же: DJI, Autel, Parrot, Ryze, Eachine
print('5', '---' * 10)

import sys

for line in sys.stdin:
	manufacturer_name = line.strip(' |\n|\t')

	company_drones_list: List[str] = list()

	for drone in drone_list:
		if manufacturer_name.lower() in drone.split()[0].lower():
			company_drones_list.append(
				' '.join([
					w for w in drone.split() 
					if w.lower() not in [
						drone_name.lower() for drone_name in true_drone_manufacturer_names
					]
				])
			)
		
	print(f'By {manufacturer_name} found {len(company_drones_list)}:')
		
	if len(company_drones_list):
		print(*company_drones_list, sep='\n')