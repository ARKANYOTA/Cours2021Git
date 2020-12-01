---
title: DM Segond degré
tags: [Maths/DM]
created: '2020-10-28T22:47:29.268Z'
modified: '2020-10-28T22:48:17.393Z'
---

# DM Segond degré

Enoncé:

Nous considérons le polynôme P d’expression $P(x) = 6x^4 - 35x^3+62x^2 -35x+6$

Le but de cet exercice est de trouver les solutions de l’équation $(E) P(x) = 0$.

### 1. Calculer $P(0)$

$$P(0) = 6*0^4 - 35*0^3+62*0^2 -35*0+6\\
P(0) = 0 - 0+0-0+6 = 6
$$

## 2. Montrer que si un nombre a, différent de zéro, vérifie $P(a) = 0$ alors   $P(1/a) = 0$

On prend pour exemple 2:

$$P(a) = 0\; et \;P(\frac{1}{a}) = 0\\
\text{alors nous en déduisons que pour un nombre a, } P(a)=P(\frac{1}{a}) \; où\; a \neq 0\\
\text{Cela fonctione pour a = 2 puis }a = P(\frac{1}{2})

$$

## 3. Nous posons $u = x+\frac{1}{x}$.Calculer $u^2$

$$u = x+\frac{1}{x}
\\u^2 = (x+\frac{1}{x})^2\\
\\u^2 = x^2+2*x*\frac{1}{x}+ (\frac{1}{x})^2
\\u^2 = x^2+2+ \frac{1}{x^2}
\\u^2 = x^2+2+ x^{-2}$$

## 4. Après avoir mis $x^2$ en facteur dans (E), montrer que $u$ est solution d’une équation du second degré (E’) que vous donnerez

$$6x^4 - 35x^3+62x^2 -35x+6\\
6x^4 - 35x^3+50x^2+2*6x^2 -35x+6\\
$$

si on prend pour valeur a= 6, b = -35 et c = 50

$$ax^4 + bx^3 + cx^2 + 2ax^2 + bx+a\\
ax^4 + 2ax^2 +a + bx^3 + bx + cx^2\\
x^2(ax^2+2a+ax^{-2}) + bx^3 + \frac{1}{x}bx^2 + cx^2\\
x^2(a(x^2+2x\frac{1}{x}+x^{-2})) + x^2*(bx+\frac{1}{x}b) + cx^2\\
x^2(a(x+\frac{1}{x})^2) + x^2*b(x+\frac{1}{x}) + c*x^2\\
x^2(a(x+\frac{1}{x})^2 + b(x+\frac{1}{x}) + c)\\

$$

## 5. Résoudre l'équation $6X^2 − 35X + 50 = 0$

$$6X^2 − 35X + 50 = 0\\
\Delta = b^2 - 4ac = 35^2 - 4*6*50 = 25 \\
\Delta > 0 \text{ donc la fonction est factorisable}\\
6X^2 − 35X + 50 = 0 =
a(x-x_1)(x-x_b)\\
$$

$$x_1 = \frac{-b-\sqrt{\Delta}}{2a}=  \frac{35-\sqrt{25}}{2*6}= \frac{35-5}{12}= \frac{30}{12} = \frac{5}{2}\\
x_2 = \frac{-b+\sqrt{\Delta}}{2a} = \frac{35+\sqrt{25}}{12} =\frac{40}{12}=\frac{10}{3}\\
S = \{\frac{5}{2}; \frac{10}{3}\}$$

## 6. En déduire les solutions de l’équation (E).

$$6x^4 -35x^3+62x^2-35x+6 = 0\\
6x^4 +12x^2 +6 -35x^3 - 35x - 12x^2 + 62x^2 = 0\\
6(x^2+1)^2 -35x(x^2+1) + 50x^2 = 0\\
[3(x^2+1) - 10x][2(x^2+1) - 5x] = 0\\
[3x^2-10x+3][2x^2- 5x+2] = 0\\
(3x-1)(x-3)(2x-1)(x-2)= 0\\
x_1 = \frac{1}{3}\\
x_2 = 3\\
x_3 = \frac{1}{2}\\
x_4 = 2\\
S=\{\frac{1}{3},\frac{1}{2}, 2,3\}$$

## 7. La propriété de la question 2 est-elle vérifiée?

$$P(\frac{1}{x_1}) = 3\\
P(\frac{1}{x_2}) = \frac{1}{3}\\
P(\frac{1}{x_3}) = 2\\
P(\frac{1}{x_4}) = \frac{1}{2}\\
$$

La propriété de la question 2 est juste.
