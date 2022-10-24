---
title: 'What are the odds of a solo win in Mexican bingo? (Riddler 2022-10-21)'
date: 2022-10-23
permalink: /posts/2022/10/riddler-mexican-bingo/
tags: riddler, probability
---

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

My solution to [this week's riddler](https://fivethirtyeight.com/features/can-you-make-the-fidget-spinner-go-backwards/). (See more of [my Riddler solutions here](/riddlers).)

## The Problem
From Roberto Linares comes a puzzle that will have you shouting “Bingo!”:

>A thousand people are playing Lotería, also known as Mexican bingo. The game consists of a deck of 54 cards, each with a unique picture. Each player has a board with 16 of the 54 pictures, arranged in a 4-by-4 grid. The boards are randomly generated, such that each board has 16 distinct pictures that are equally likely to be any of the 54.
>
>During the game, one card from the deck is drawn at a time, and anyone whose board includes that card’s picture marks it on their board. A player wins by marking four pictures that form one of four patterns, as exemplified below: any entire row, any entire column, the four corners of the grid and any 2-by-2 square.
>![Winning bingo boards.](/images/bingo-boards.png)
>Four four-by-four grids are shown. In the first grid, the third row has four blue markers. In the second grid, the second column has four blue markers. In the third grid, the four corner squares are marked. And in the fourth grid, the two middle squares in the third and fourth columns are marked, forming a smaller two-by-two square.
>
>After the fourth card has been drawn, there are no winners. What is the probability that there will be exactly one winner when the fifth card is drawn?

## The Solution

For simplicity, we can label the distinct pictures with numbers 1 through 54 and assume without loss of generality that the numbers are drawn in order. A valid board therefore consists of a 4x4 grid of squares labelled with 16 distinct numbers in the range from 1 to 54. The number of distinct boards is therefore given by

$$
n = \binom{54}{16}16! = 164300848531852032000.
$$

It remains to count the number of distinct boards that win after 4 draws and the number of boards that win after 5 draws.

There are 18 distinct winning patterns:
 - 4 distinct columns
 - 4 distinct rows
 - 9 distinct 2x2 blocks
 - 1 set of all four corners

For a board to win after exactly 4 draws, the four squares composing the winning pattern must have the numbers 1, 2, 3, and 4 in some arrangement. The remaining 12 squares can have any choice of 12 out of the remaining 50, and those 12 numbers can be in any arrangement. The number of valid boards that win after exactly 4 draws is therefore given by

$$
a = 18\cdot4!\binom{50}{12}12! = 25121070914259640320000.
$$

The number of boards that win after exactly 5 draws is exactly 4 times the number of boards that win after exactly 4 draws. To see this, note that after 5 draws, any valid board can only have at most one of the 18 winning patterns completely filled in. One of the four numbers comprising the winning pattern must be the number 5, the other three must be selected from the first 4 numbers. After arranging those 4 numbers in any order, the remaining 12 squares can be filled with any of the remaining 50 numbers, which can then be in any arrangement. The number of valid boards that win after exactly 5 draws is therefore given by

$$
b = 18\cdot\binom{4}{3}\cdot4!\binom{50}{12}12! = 4a = 100484283657038561280000.
$$

Given that there are $N$ players, each with a valid board selected uniformly at random, the probability that there are exactly $k$ winners after 5 draws given that there were no winners after 4 draws is computed as

$$
\begin{align*}
\operatorname{Pr}&\big(\text{exactly }k\text{ winners after 5 draws }\big|\text{ no winners after 4 draws}\big)\\
&= \frac{\binom{N}{k}b^k(n-b)^{N-k}}{(n-a)^{N}}\\
&=\binom{N}{k}\left(\frac{b}{n-a}\right)^k \left(\frac{n-b}{n-a}\right)^{N-k}.
\end{align*}
$$

In the original problem statement, there are 1000 players. With $k=1$, the probability of exactly 1 winner after 5 draws given that there were no winners after 4 draws is approximately 18.1%.

As the number of players grows, this probability increases until $N=4293$, after which this probability starts to shrink as the probability of there being multiple winners begins to outstrip the probability of there being exactly one winner. The plot below shows the probabilities of having exactly $k$ winners after the fifth draw as the number $N$ of participants grows, given that there are no winners after the fourth draw.


![Probability of exactly k winners after 5 draws as a function of the number of participants, given that there are no winners after 4 draws.](/images/riddler-mexican-lottery.png)
