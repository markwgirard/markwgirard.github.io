---
title: 'Covering a square of overlapping disks (Riddler 2022-09-09)'
date: 2022-09-11
permalink: /posts/2022/09/riddler-overlapping-disks/
tags: mathematics, riddler
---

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

Here's my solution to this week's [Riddler](https://fivethirtyeight.com/features/can-you-cover-the-baking-sheet-with-cookies/). (See more of [my Riddler solutions here](/riddlers).)

## The Problem
Suppose you have a unit square (i.e., with side length 1). If you also have four identical circles that can overlap, they would need to have a radius of $\sqrt{2}/4$ to completely cover the square, as shown below:

![A square that is completely covered by four overlapping circles of the same size. The four circles are centered over the four respective quadrants of the square, and all overlap in the squares center.](/images/overlappingdisks.png)


Now suppose that, instead of four identical circles, you have five identical circles that can overlap. What is the minimum radius they would need to completely cover a unit square?

_Extra credit:_ Suppose you have _six_ identical circles that can overlap. What is the minimum radius they would need to completely cover a unit square?

## The Solution
Interestingly this problem appears to have been previously solved (more on that in a minute). But first, my solution:
### My solution
I guessed that the best solution would have a bit of reflectional symmetry. With the help of some amazing geometric drawing software ([Geogebra](https://www.geogebra.org/)), I was able to come up with a solution with $r\approx 0.326$ with the diagram below:

![A Geogebra drawing of 5 disks of minimal radius covering the unit square.](/images/geogebra-5disks.png)

Note that $0.326<.3535 \approx\frac{1}{2\sqrt{2}}$ so this solution is definitely an improvement over simply covering the square with 4 squares.

I wanted to come up with a more exact value. From this geometric picture, and doing a little bit of work, we can set up a system that the lengths must satisfy. With $e=\frac{1}{4}$, the lengths $a$, $b$, $c$, $d$, and $r$ in the above diagram satisfy:


$$\begin{align}r^2&=\left(\frac{1}{2}-a\right)^2+\frac{1}{16.}\\r^2&=\left(\frac{1}{2}-c\right)^2+\left(\frac{1}{2}-d\right)^2\\r^2&=a^2+\frac{d^2}{4}\\b&=\frac{1}{2}-a\\c&=\frac{1}{2}+r-2a\end{align}$$

This system of equations has only one positive solution for $r$ (assuming $a$, $b$, $c$, and $d$ are positive). This is approximately $r\approx0.32616058$.

I wanted to determine if there was a good way to express the *exact* value of this optimal radius. Unfortunately there does not appear to be a nice way to do this. The best I could do (with the help of Mathematica) was to say that the exact value of $r$ is expressed as

$$r=\frac{1373-2039 x+3927 x^2-4237 x^3+4112 x^4-832 x^5}{3104}
$$

where $x\approx0.41895454$ is the smallest real root of the polynomial defined by

$$p(x)=21-92 x+154 x^2-196 x^3+209 x^4-144 x^5+64 x^6.$$

### Previous work

After a bit of Googling, I was able to stumble upon a few papers that had investigated this and similar problems. By far the best one was [Covering a square with up to 30 equal circles.](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.30.3894&rep=rep1&type=pdf) by Nurmela and Östergård (2000). In that work, the authors developed a clever optimization algorithm to determine the smallest radius of circle such that $n$ circles of that size can be used to cover the unit square for $n$ up to 30. Here are the figures for $n=5$ and $n=6$.

![Minimal radius coverings with 5 and 6 disks.](/images/5-and-6-disk-covers.png)

The authors determined the optimal radii for $5$ and $6$ circles to be $r_5=0.32616058400398728086$ and $r_6=0.29872706223691915876$ respectively.
