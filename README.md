# Программа реализует простую хеш-функцию по . Это алгоритм, который принимает на вход сообщение и превращает его в уникальный битовый массив фиксированного размера.
Пользователь вводит сообщение в поле ввода и программа вычисляет и отображает хеш-значение, используя пользовательскую функцию `hash_function`. Функция `hash_function` последовательно обрабатывает каждый символ сообщения, используя для вычисления промежуточных хешей линейную функцию `encryption_block` и операцию XOR. Результат — шестнадцатеричное представление хеша.
Выбранная формула: H_i=E_(H_(i-1) )(M_i ) + M_i
