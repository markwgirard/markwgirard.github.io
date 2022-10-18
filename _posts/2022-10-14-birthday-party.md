---
title: 'How big is your birthday surprise party? (Riddler 2022-10-14)'
date: 2022-10-14
permalink: /posts/2022/10/riddler-birthday-party/
tags: programming, riddler, probability
---

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

My solution to [this week's riddler](https://fivethirtyeight.com/features/can-you-salvage-your-rug/). (See more of [my Riddler solutions here](/riddlers).)

## The Problem
> Today I happen to be celebrating the birthday of a family member, which got me wondering about how likely it is for two people in a room to have the same birthday.
>
> Suppose people walk into a room, one at a time. Their birthdays happen to be randomly distributed throughout the 365 days of the year (and no one was born on a leap day). The moment two people in the room have the same birthday, no more people enter the room and everyone inside celebrates by eating cake, regardless of whether that common birthday happens to be today.
>
> On average, what is the expected number of people in the room when they eat cake?
>
> _Extra credit_: Suppose everyone eats cake the moment three people in the room have the same birthday. On average, what is this expected number of people?

## The Solution
At any given point during the party, right before a new guest arrives, we can describe the "state" of the party by the number $$n\in\{0,1,\dots,365\}$$ of currently present guests having unique birthdays. (Note that we cannot have $n>365$, as the pigeon-hole principle would guarantee that at least two guests share a birthday.) When the $(n+1)$th guest arrives, there are two possibilities:
 - With probability $n/365$, the new guest shares a birthday with one of the currently present guests. The cake is cut and the party is over.
 - With probability $1-n/365$, the new guests has a birthday that is distinct from everyone else's and the party continues.
Let $p_k$ denote the probability that there will be $k$ guests at some point in the night all having distinct birthdays. It is clear that $p_0=1$ and that

$$
p_{k+1}= \left(1-\frac{k}{365}\right)p_k
$$

holds for every $k\geq0$. For each $k\in\mathbb{N}$, define $X_k$ to be the random variable whose value is $1$ if there were at least $k$ people with distinct birthdays at some point in the night, and zero otherwise. The total number of guests that have arrived when the cake is cut is the random variable $X=X_0+X_1+\cdots+X_{365}$, and the expected value of this variable is given by

$$
\operatorname{E}(X) = \sum_{k=0}^{365}\operatorname{E}(X_k)  =\sum_{n=0}^{365}p_k.
$$

More explicitly,

$$
\operatorname{E}(X) = \sum_{k=0}^{365} \frac{1}{365^k}\frac{365!}{(365-k)!}.
$$

We can easily evaluate this on a computer to find that the expected number of guests at the end of the night is about 24.616585894598852.


## Extra credit---General solution with generating functions
Consider now the more general problem of computing the expected number of people that must arrive until there are $n$ people that share a birthday. The goal will be to construct a generating function

$$
G_n(x) = \sum_{k=0}^\infty \frac{p_{n,k}}{k!}x^k
$$

for which the coefficients $p_{n,k}$ are the probabilities that, after $k$ guests have arrived, there are no $n$ people who share a birthday. Note that we must have $p_{n,k} = 0$ whenever $k >365(n-1)$. As above, the desired expected value is the sum of these probabilities,

$$
\operatorname{E}(X) = \sum_{k=0}^{365(n-1)}p_{n,k}.
$$

Toward this end, for non-negative integers $a_1,a_2,\dots,a_{365}$, define

$$
f(a_1,a_2,\dots,a_{365}) = \frac{1}{365^{a_1+a_2+\cdots+a_{365}}} \frac{(a_1+a_2+\cdots+a_{365})!}{a_1!a_2!\cdots a_{365}!},
$$

which is the probability that, after $a_1+a_2+\cdots +a_{365}$ guests have arrived, there are:
 - $a_1$ individuals whose birthday is January 1,
 - $a_2$ individuals whose birthday is January 2,
 - $\cdots$
 - $a_{365}$ individuals whose birthday is December 31.

After $k$ people have arrived, the probability that no $n$ people share a birthday is

$$
\begin{align*}
p_{n,k}
&= \sum_{\substack{a_1+\cdots a_{365}=k\\a_1<n,\dots,a_{365}<n}} f(a_1,a_2,\dots,a_{365})\\
&=\sum_{\substack{a_1+\cdots a_{365}=k\\a_1<n,\dots,a_{365}<n}} \frac{1}{365^k}\frac{k!}{a_1!a_2!\cdots a_{365}!}.
\end{align*}
$$

We can now express the generating function as

$$
\begin{align*}
G_{n}(x)
&= \sum_{k=0}^\infty \frac{p_{n,k}}{k!}x^k \\
&=\sum_{k=0}^\infty \sum_{\substack{a_1+\cdots a_{365}=k\\a_1<n,\dots,a_{365}<n}} \frac{1}{365^k}\frac{1}{a_1!a_2!\cdots a_{365}!}x^k\\
& = \sum_{k=0}^\infty \sum_{\substack{a_1+\cdots a_{365}=k\\a_1<n,\dots,a_{365}<n}} \frac{(x/365)^{a_1}}{a_1!}\frac{(x/365)^{a_2}}{a_2!}\cdots \frac{(x/365)^{a_{365}}}{a_{365}!}\\
& = \left(\sum_{a_1=0}^{n-1}\frac{(x/365)^{a_1}}{a_1!}\right)
\cdots \left(\sum_{a_{365}=0}^{n-1}\frac{(x/365)^{a_{365}}}{a_{365}!}\right)\\
& = \left(\sum_{j=0}^{n-1}\frac{(x/365)^{j}}{j!}\right)^{365}.
\end{align*}
$$

Finally, making use of the fact that

$$
\int_{0}^\infty x^k e^{-x}\, \mathrm{d}x = k!
$$

for every positive integer $k$, it follows that

$$
\begin{align*}
\sum_{k=0}^\infty p_{n,k}
& = \sum_{k=0}^\infty \frac{p_{n,k}}{k!} \int_{0}^\infty x^k e^{-x}\, \mathrm{d}x \\
& = \int_{0}^\infty G_n(x)e^{-x}\, \mathrm{d}x\\
& = \int_0^\infty \left(\sum_{a=0}^{n-1}\frac{(x/365)^{a}}{a!}\right)^{365} e^{-x}\, \mathrm{d}x
\end{align*}
$$


Using this formula, we can now compute the expected numbers of guests that have arrived at the first instance when $n$ people share a birthday for different values of $n$, the first few values are shown in the table below.

| $n$ | $E(X_n)$|
|--|-------|
|1|1.0|
|2|24.6166|
|3|88.7389|
|4|187.0518|
|5|311.4494|
|6|456.0163|
|7|616.6169|
|8|790.2997|
|9|974.8939|
|10|1168.7567|
|11|1370.6135|
|12|1579.4531|
|13|1794.459|
|14|2014.9607|
|15|2240.3999|
|16|2470.3065|
|17|2704.2798|
|18|2941.9755|
|19|3183.095|
|20|3427.3773|
|21|3674.5931|
|22|3924.5391|
|23|4177.0347|
|24|4431.918|
|25|4689.0437|


Plotting these values, we see that the expected size of the party grows roughly linearly with $n$ as $n$ increases.

![Expected size of party the first time when there are n people who share a birthday.](/images/riddler-birthday-surprise.png)

```python
from scipy.integrate import quad
from scipy.special import factorial

def p(n, m=365):

    def integrand(x):
        out = (sum((x/m)**j / factorial(j) for j in range(n)) * np.exp(-x/m))** m
        return out

    return quad(integrand, 0, np.inf)
```
