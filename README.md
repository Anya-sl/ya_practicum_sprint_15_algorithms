# ya_practicum_sprint_15_algoritms
Задачи по алгоритмам из курса Яндекс Практикум, 15 спринт

<details>
<summary> ## [A. Ближайший ноль](https://github.com/Anya-sl/ya_practicum_sprint_15_algorithms/blob/main/a_nearest_zero.py)</summary>

Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить, имеет длину n, то есть состоит из n одинаковых идущих подряд участков. Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице. Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка. Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.

**Формат ввода**

В первой строке дана длина улицы —– n (1 ≤ n ≤ 10^6). В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули). Гарантируется, что в последовательности есть хотя бы один ноль. Номера домов (положительные числа) уникальны и не превосходят 10^9.

**Формат вывода**

Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.

![sample](https://github.com/Anya-sl/ya_practicum_sprint_15_algorithms/blob/main/pictures/a_nearest_zero.PNG)
</details>

<details>
<summary> ## [B. Ловкость рук](https://github.com/Anya-sl/ya_practicum_sprint_15_algorithms/blob/main/b_sleight_of_hand.py)</summary>
Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4. В нём на каждом раунде появляется конфигурация цифр и точек. На клавише написана либо точка, либо цифра от 1 до 9.

В момент времени t игрок должен одновременно нажать на все клавиши, на которых написана цифра t. Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый. Если в момент времени t нажаты все нужные клавиши, то игроки получают 1 балл.

Найдите число баллов, которое смогут заработать Гоша и Тимофей, если будут нажимать на клавиши вдвоём.

![sample_keyboard](https://github.com/Anya-sl/ya_practicum_sprint_15_algorithms/blob/main/pictures/b_sleight_of_hand_0.PNG)

**Формат ввода**

В первой строке дано целое число k (1 ≤ k ≤ 5).
В четырёх следующих строках задан вид тренажёра -— по 4 символа в каждой строке. Каждый символ – либо точка, либо цифра от 1 до 9. Символы одной строки идут подряд и не разделены пробелами.

**Формат вывода**

Выведите единственное число -— максимальное количество баллов, которое смогут набрать Гоша и Тимофей.
![sample_1_2](https://github.com/Anya-sl/ya_practicum_sprint_15_algorithms/blob/main/pictures/b_sleight_of_hand_1.PNG)
![sample_3](https://github.com/Anya-sl/ya_practicum_sprint_15_algorithms/blob/main/pictures/b_sleight_of_hand_2.PNG)
</details>
