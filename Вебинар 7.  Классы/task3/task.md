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
<h4>Реализовать три класса.</h4>
<p><b>I.</b> Напишите класс <code><span class="colortext">PublicTransport</span></code>.
<br>
Экземпляр класса создается из следующих атрибутов:
<ol>
<li><code>brand</code> - Марка транспорта;</li>
<li>ЗАЩИЩЕННЫЙ (<code>protected</code>) атрибут <code>engine_power</code> - Мощность двигателя;</li>
<li><code>year</code> - Год выпуска;</li>
<li><code>color</code> - Цвет;</li>
<li><code>max_speed</code> - Максимальная скорость.</li>
</ol>
<p>У класса должно быть <b>свойство</b> <code>info</code>, которое выводит на печать 
информацию о марке, цвете, годе выпуска и мощности двигателя.


<b>II.</b> Напишите класс <code><span class="colortext">Bus</span></code>, 
<i>унаследованный</i> от <code><span class="colortext">PublicTransport</span></code>.
<br>
Дополнительными атрибутами будут:
<ol>
<li><code>passengers</code> - количество пассажиров;</li>
<li>ПРИВАТНЫЙ (<code>private</code>) атрибут <code>park</code> - Парк приписки автобуса;</li>
<li>ЗАЩИЩЕННЫЙ (<code>protected</code>) атрибут <code>fare</code> - Стоимость проезда.</li>
</ol>
<p>Добавить <b>свойство</b> <code>park</code>, которое будет возвращать значение <code>park</code>,
а при присвоении проверять номер парка, что он в диапазоне от 1000 до 9999.
Если номер парка не попадает в диапазон, то выдавать ошибку.


<b>III.</b> Напишите класс <code><span class="colortext">Tram</span></code>, 
<i>унаследованный</i> от <code><span class="colortext">PublicTransport</span></code>.
<br>
Дополнительными атрибутами будут:
<ol>
<li>ПРИВАТНЫЙ (<code>private</code>) атрибут <code>route</code> - маршрут трамвая;</li>
<li><code>path</code> - длина маршрута;</li>
<li>ЗАЩИЩЕННЫЙ (<code>protected</code>) атрибут <code>fare</code> - Стоимость проезда.</li>
</ol>
<p>У класса должно быть <b>свойство</b> <code>how_long</code>, 
которое вычисляет время прохождения маршрута по формуле <code>max_speed/(4*path)</code>
<br>
<br>
<p><b>Подсказки:</b>
<div class="hint">
<div>Для создания <code>protected</code> атрибута 
используйте нижнее подчеркивание в начале имени.</div>
</div>
<div class="hint">
<div>Для создания <code>private</code> атрибута 
используйте два нижних подчеркивания в начале имени.</div>
</div>
<div class="hint">
<div>Свойство можно создать с помощью декоратора <code>@property</code>.</div>
</div>
<div class="hint">
<div>Для присвоения номера парка используйте <code>setter</code> 
с проверкой условия на диапазон.</div>
</div>
<div class="hint">
<div>Для проверки номера парка на диапазон используйте <a href="https://pythonru.com/uroki/35-instrukcija-assert-dlja-nachinajushhih">assert</a>.</div>
</div>
<br>
  <p><b>Материалы:</b>
  <a href="https://n.sbis.ru/shared/disk/6584c96b-9259-4609-b400-9502b8424d3c">Вебинар 7</a>
<br>
<br>
</html>