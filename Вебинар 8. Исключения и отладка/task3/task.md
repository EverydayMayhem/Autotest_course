<html>
<head>
  <meta charset="utf-8" />
  <style>
   .colortext {
    color: orange;
   }
  </style>
 </head>
<h2>Задача 3</h2>
<p>Напишите функцию <code><span class="colortext">segment</span></code>.
<br>На вход подаются два кортежа с координатами точек <code>(x1, y1), (x2, y2)</code>.
<p><b><i>Входные данные:</i></b>
  <ul>
  <li>первый кортеж типа <code>tuple</code></li>
    <li>второй кортеж типа <code>tuple</code></li>
</ul>
В функции происходит проверка на корректность полученных данных.
С помощью инструкции <code>try/except as</code> отлавливается исключение <code>Exception</code>.
<ul>
<li>Если исключение поймано, то функция возвращает текст исключения наоборот.</li>
Например, исключение <code>"unsupported operand type(s) for +: 'int' and 'str'"</code> будет выглядеть
наоборот как <code>"'rts' dna 'tni' :+ rof )s(epyt dnarepo detroppusnu"</code>

<li>Если исключения не произошло, то функция возвращает сумму всех координат.</li>
</ul>
<br>
<p><b>Подсказки:</b>
<div class="hint">
<div>Чтобы получить текст исключения, 
нужно обратиться к атрибуту экземпляра класса <code>Exception</code>.</div>
</div>
<div class="hint">
<div>Опциональный блок <code>else</code> в конструкции <code>try/except</code> 
выполняется в том случае, если исключение не произошло.</div>
</div>

<br>
  <p><b>Материалы:</b>
  <a href="https://n.sbis.ru/shared/disk/d00cae89-ef87-4aa5-b600-ca889bddd132">Вебинар 8</a>
<br>
<br>
</html>