# висновки

Алгоритм Боєра-Мура виявився найшвидшим у всіх випадках.

```bash
File: стаття 1.txt
	Pattern: integers.length
		Кнута-Морріса-Пратта     : 0.004242 seconds
		Боєра-Мура               : 0.000986 seconds
		Рабіна-Карпа             : 0.010369 seconds

	Pattern: Ключі вузла
		Кнута-Морріса-Пратта     : 0.009714 seconds
		Боєра-Мура               : 0.004375 seconds
		Рабіна-Карпа             : 0.026769 seconds


File: стаття 2.txt
	Pattern: integers.length
		Кнута-Морріса-Пратта     : 0.016003 seconds
		Боєра-Мура               : 0.004653 seconds
		Рабіна-Карпа             : 0.041273 seconds

	Pattern: Ключі вузла
		Кнута-Морріса-Пратта     : 0.010184 seconds
		Боєра-Мура               : 0.002482 seconds
		Рабіна-Карпа             : 0.015876 seconds

```