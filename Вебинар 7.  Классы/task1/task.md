<html>
<head>
  <meta charset="utf-8" />
  <style>
   .colortext {
    color: orange;
   }
  </style>
 </head>
<h2>Задача 1</h2>
Напишите класс <code><span class="colortext">Segment</span></code>.
Для его инициализации нужно два кортежа с координатами точек <code>(x1, y1), (x2, y2)</code>.
<br>
Реализуйте методы класса:
<ol>
<li><code>length</code>, который возвращает длину нашего отрезка с округлением до 2 знаков после запятой;</li>
<li><code>x_axis_intersection</code>, который возвращает <code>True</code>, 
если отрезок пересекает ось абцисс, иначе - <code>False</code>;</li>
<li><code>y_axis_intersection</code>, который возвращает <code>True</code>, 
если отрезок пересекает ось ординат, иначе - <code>False</code></li>
</ol>
<p><b>Пример:</b> (Ввод --> Вывод)
<ol>
  <li><code>Segment((2, 3), (4, 5)).length() --> 2.83</code></li>
<li><code>Segment((-2, -3), (4, 5)).x_axis_intersection() --> True</code></li>
<li><code>Segment((-2, -3), (-4, -5)).y_axis_intersection() --> False</code></li>
</ol>
<br>
<p><b>Подсказки:</b>
<div class="hint">
<div>Вспомните формулу вычисления длины отрезка по координатам двух точек.</div>
</div>
<div class="hint">
<div>С помощью конструкций <code>if/else</code> запрограммируйте 
условия пересечения отрезка с осями координат.</div>
</div>
<br>
  <p><b>Материалы:</b>
  <a href="https://n.sbis.ru/shared/disk/6584c96b-9259-4609-b400-9502b8424d3c">Вебинар 7</a>
<br>
<br>
</html>