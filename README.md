# OS_labs
Labs for course "OS for mobile platforms". Mostly related to threding in python

Lab 1
Задача «про філософів». За круглим столом сидять 8 філософів. Кожному
філософу подали по тарілці спагеті. Біля кожного філософа зліва та справа поклали по
одні виделці, тобто між сусідніми філософами лежить по одній виделці.
Філософи або розмовляють (виделки покладені на стіл), або їдять спагеті (звичайно
двома виделками).
Реалізуйте філософів як потоки (під задачі). В стандартний вивод направте
повідомлення філософів:
- Філософ хх їсть спагеті;
- Філософ хх очікує на вільні виделки;
- Філософ хх розмовляє.
Коректно реалізована задача не приведе до тупика, стану, коли всі філософи
чекають на виделки (нових повідомлень не буде).

Також зробив візуалізацію всього процесу 

Lab 2

Програми (процеси, потоки – згідно варіанту задачі), що реалізують функції f(x) і g(x),
займаються тільки обчисленням значення над вхідним аргументом, вони не обробляють
ніяких інших запитів (у тому числі – про завершення обчислень) і не взаємодіють з
іншими процесами та потоками ні в який інший спосіб, окрім викликів обчислень f(x) і
g(x) (тобто запуску функції на обчислення) та повернення результату (коли обчислення
результату завершено) – див. малюнок нижче.
 Зауважити, що функції f та g – можуть бути частково визначені (тобто «зациклюватись»
і ніколи не повертати результат). Потрібно коректно опрацювати таку ситуацію і
запитати користувача: «продовжити обчислення, припинити або продовжити, не
запитуючи більше» наприклад, кожні 10 секунд.
 Увага! Скористатись правилами булевих обчислень:
x && false = false && x = false

Взаємодія потоків. Паралелізм. Обчислити f(x) &amp;&amp; g(x), використовуючи 2
допоміжні потоки (threads): один обчислює f(x), а інший – g(x). Основна програма виконує
ввод-вивід та операцію &amp;&amp;.
