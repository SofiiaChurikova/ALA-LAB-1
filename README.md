# ALA-LAB-1
### Поексперементувати з різними матрицями трансформації, зробити висновки, які елементи матриці на що впливають.
1. **Елементи матриці обертання** утворюють ортогональну матрицю і визначають кут повороту(обертання).
2. **Елементи матриці масштабування** розтягують(стискають) матрицю по осях.
3. **Елементи матриці віддзеркалення** змінюють знак відносно осі.
4. **Елементи матриці нахилу** відповідають за зміщення (координат) однієї осі пропорційно до (координат) іншої.

### Що таке лінійні трансформації?

*Лінійні трансформації* - відображення вектора з одного лінійного простору на вектор в іншому лінійному просторі. Для лінійності повинні виконуватись такі умови:
1. Адитивність (лінійність за додаванням):

   $$
   T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})
   $$

2. Однорідність (лінійність за множенням на скаляр):
 
$$
   T(c\mathbf{v}) = cT(\mathbf{v})
   $$


### Як і в яких галузях застосовуються лінійні трансформації?
1. *Комп'ютерна графіка.*
   - Наприклад, для перетворення зображень, а саме масштабувань, зсуву.
2. *Машинне навчання та аналіз даних*
   - Лінійні трансформації виконуються для побудови регресійної моделі, зменшення розмірності даних.
3. *Медицина*
   - Лінійні трансформації допомагають оброблять та аналізувати зображення, отримані за допомогою мадичного обладнання.
4. *Економіка*
   - Моделювання доходів та ризиків у фінансових портфелях.


### Що таке матриця лінійної трансформації та як її можна інтерпретувати? 
*Матриця лінійної трансформації* - матриця-представлення лінійних перетворень над векторами у векторному просторі. Тобто за допомогою матриці можна подати будь-яке лінійне відображення.

Матрицю лінійної трансформації можна інтерпретувати як набір дій над координатами вектора. Кожна координата буде змінюватись під впливом трансформації і переходити в інші точки простору.

### Які особливості та властивості має матриця обертання?
1. Оскільки поворот — це перетворення координат, при якому зберігаються довжини векторів, то отже, матриця повороту є ортогональною матрицею: обернена матриця дорівнює транспонованій матриці.
2. Детермінант матриці обертання дорівнює 1. Це свідчить про те, що обертання зберігає орієнтацію простору.
3. Добутком матриць повороту є матриця повороту.
4. Матриця обертання зберігає скалярний добуток векторів.

### Чи залежить фінальний результат від порядку трансформацій? Провести експерименти з фігурами або зображеннями з частин 1-2.
Через те, що лінійні трансформації не є комутативними, то порядок впливає.
Наприклад:
1. Візьмемо фігуру і обернемо її на кут 45, далі відзеркалимо відносно осі х.
2. Візьмемо фігуру і відзеркалимо її відносно осі х, а потім обернемо на кут 45.
![Figure_1](https://github.com/SofiiaChurikova/ALA-LAB-1/assets/150338552/0f4113f0-8f10-4d1b-81b8-f2498257f6e9)
![Figure_2](https://github.com/SofiiaChurikova/ALA-LAB-1/assets/150338552/c8992a09-de32-46c6-8906-a3b7627a800f)

Отже, результати різні.

### Була здійснена якась довільна лінійна трансформація; як знайти матрицю лінійної трансформації, що поверне все до початкового вигляду? Чи завжди можна здійснити обернену трансформацію?
Щоб знайти матрицю лінійної трансформації, яка поверне все до початкового вигляду після лінійної трансформації, необхідно знайти обернену матрицю. 
Існує кілька методів:
   - Метод LU розкладу
   - Метод Гаусса-Жордана
   - Алгебраїчні перетворення

Детермінант матриці повинен бути ненульовим, якщо нульовий - матриця не має оберненої, отже й неможливо зробити обернену трансформацію.

### Модуль визначника матриці трансформації менше 1, які висновки можна зробити про дану трансформацію (як змінюється простір при даній трансформації)? А якщо більше 1? Дорівнює 1? Дорівнює 0? 
- Модуль визначника матриці менше 1, то трансформація стискає простір (розмір об'єктів у просторі)
- Модуль визначника матриці більше 1, то трансформація розширює/збільшує простір (розмір об'єктів у просторі)
- Модуль визначника матриці дорівнює 1, то трансформація залишається незмінною (розмір об'єктів у просторі)
- Модуль визначника матриці дорівнює 0, то вектори перетворюються на об'єкти меншої розмірності, матриця не є виродженою (не має оберненої)
