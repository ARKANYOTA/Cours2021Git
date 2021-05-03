---
tags: [Maths/4.Vecteurs, Maths/5.SN]
title: Suites Numerique
created: '2021-03-12T07:21:20.329Z'
modified: '2021-03-30T09:40:57.607Z'
---

# Suites Numerique

# SUITES NUMERIQUE:
  - Suites récurantes
    - u_{n+1} = 3u(n)+5 et u(0) = 42
  - Suites explicites
    - u_n = 3n
  - suite strictement croissante (ou décroissantes)
    - Métheode 1
      - u_{n+1}-u_n > 0 croissante
      - u_{n+1}-u_n < 0 décroissante
    - Methode 2:
      - Si $u_n > 0$; $\frac{u_{(n+1)}}{u_n} -1 > 0$ croissante
  - Limite de suites
    - lim u_n
    - Le trableau au dessus
    
## 3.
$$
h_0 = 3 = \sqrt{9} \\
h_1 = \sqrt{3² + 1²} = \sqrt{10} \\
h_2 = \sqrt{\sqrt{10}² + 1²} = \sqrt{11} \\
h_3 = \sqrt{\sqrt{11}² + 1²} = \sqrt{12} \\
h_4 = \sqrt{13}
$$
$$
Donc \;Pour \;n >= 0\\
h(n) = \sqrt{ n + 9 } \\
h(n+1) = \sqrt{1+h²_n}\\
\text{suite récurrente (retour en arrière)}
$$

## Croissante

### Méthode 2

Si $u_n > 0$ alors $u_{n_n+1}/u_n -1 > 0$
$u_n$ est strictement croissante

Preuve:
$$
u_n \text{est strictement croissante} \\
u_n+1 - u_n > 0 \\
u_n*(u_n+1/u_n-1) > 0\\
u_n+1/u_n - 1 > 0
$$

### Méthode 1:
$\frac{u_{n+1}}{2^n+1} - \frac{n}{2^n}$

---


| $u_n$ | $1/n$ | $1/n²$ | $1/n³$ | $1/\sqrt n$ |  $\sqrt n$ | $n$ |
|-----|-----|------|-----|----------|------|-----|
| $lim\;  u_n$ | 0 | 0    | 0   | 0    | $+\infin$ | $+\infin$ |

| $u_n$ | n² | n³ | 
|-----|-----|------|
| $lim \; u_n$ | $+\infin$ | $+\infin$    |






