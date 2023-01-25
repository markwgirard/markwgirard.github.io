---
title: 'Random infinite graphs: They are all the same!'
date: 2022-01-03
permalink: /posts/2022/01/random-infinite-graphs/
tags: mathematics, combinitorics
---

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

I picked up a book at a used book store recently: *(Probabilistic Methods in Combinitorics)[https://www.amazon.ca/Probabilistic-Methods-Combinatorics-Paul-Erdos/dp/0122409604]* (1974) by Paul Erdős and Joel Spencer. Always a sucker for neat-looking old math books, I picked it up and browse through it ocassionally.

As with most of Erdős' writing, I found the statements and proofs in the book rather obtuse. To help me understand some of the contents, I wanted to write some blog posts as I read through it.

The first topic I wanted to look at was a simple one: random infinite graphs. Here, Spencer and Erdős consider randomly generated graphs whose sets of vertices are the natural numbers. Something interesting happens with the graphs generated this way. Namely, they are almost always the same! Up to isomorphism, at least.


## Background

Recall that a *graph* $G$ is an ordered pair $(V,E)$ consisting of a set $V$ of vertices and a set of edges

$$
E\subseteq\binom{V}{2}
$$

(where we recall that given a set $S$ and an integer $k$, the notation $\binom{S}{k}$ is used to denote the collection of all subsets of $S$ containing exactly $k$ elements).  We may write $\operatorname{Vertices}(G)=V$ and $\operatorname{Edges}(G)=E$. Two distinct vertices $a,b\in \operatorname{Vertices}(G)$ are said to be *adjacent* in $G$ if it holds that

$$
\{a,b\}\in \operatorname{Edges}(G)
$$

and not adjacent otherwise.

Two graphs $G$ and $H$ are said to be *isomorphic* if there exists a bijection

$$
f:\operatorname{Vertices}(G)\to\operatorname{Vertices}(H)
$$

with the property that, for every choice of distinct pairs of vertices $a,b\in\operatorname{Vertices}(G)$, we have the equivalence

$$
\{a,b\}\in \operatorname{Edges}(G)\iff\{f(a),f(b)\}\in \operatorname{Edges}(H).
$$

Graph isomorphism defines an equivalence relation on a collection of graphs.

## Infinite graphs and universality

The set of vertices in a graph is usually taken to be finite, but there is no reason we can't consider graphs to have infinite sets of vertices. In this note in particular, we will consider graphs whose sets of vertices are the natural numbers $\mathbb{N}$.

> **Definition.** A graph $G$ with $\operatorname{Vertices}(G)=\mathbb{N}$ is said to be *universal* if, for every pair of finite disjoint subsets $S,T\subseteq\mathbb{N}$ there exists a choice of vertex $a\in\mathbb{N}\setminus(S\cup T)$ that is adjacent to every vertex in $S$ and not adjacent to every vertex in $T$.

Symbolically, a graph $G$ is universal if the following statement holds:

$$
\forall n,k\in \mathbb{N},\,\forall S\in\binom{\mathbb{N}}{n},\,\forall T\in\binom{\mathbb{N}\setminus S}{k},\, \exists a\in \mathbb{N}\setminus(S\cup T), \,\forall s\in S\cup T, \bigg(s\in S \iff \{a,s\}\in\operatorname{Edges}(G)\bigg)
$$

Fascinatingly, it turns out that all universal graphs are isomorphic!

>**Proposition.** All universal graphs on $\mathbb{N}$ are isomorphic.

*Proof.* Suppose $G$ and $H$ are universal graphs on the natural numbers. Define a sequence of finite subsets $A_1,A_2,\dots$ of $\mathbb{N}$ and functions $f_1,f_2,\dots$, where

$$
f_n:A_n\to\mathbb{N}
$$

for each $n\in\mathbb{N}$ recursively as follows.

Define $A_1=\{1\}$ and $f_1(1)=1$. Note that $f_1$ is injective and trivially satisfies the relations $\{1\}\subseteq A_1$ and $\{1\}\subseteq f_1(A_1)$.

Given a number $n\in\mathbb{N}$, suppose we have defined $A_n$ and $f_n$ such that $f_n$ is injective and satisfies the properties that

$$
\{1,2,\dots n\}\subseteq A_n \quad\text{and}\quad \{1,2,\dots n\}\subseteq f_n(A_n).
$$

Consider two cases concerning whether $n+1\in f_n(A_n)$.
- Suppose that $n+1\in f_n(A_n)$. In this case, let $a\in A_n$ such that $f_n(a)=n+1$.
- Conversely, if $n+1\notin f_n(A_n)$, by universality of $G$, there exists a choice of vertex $a\in\mathbb{N}\setminus A_n$ such that, for all $s\in A_n$, the equivalence

$$
\{a,s\}\in \operatorname{Edges}(G) \iff \{n+1,f_n(s)\}\in\operatorname{Edges}(H)
$$

  holds.

Similarly, consider the following cases:
- If $n+1\in A_n$, let $b=f_n(n+1)$.
- If $a=n+1$, where $a$ is the number chosen above, also let $b=n+1$.
- Otherwise, analogous to the step above, by universality of $H$ there exists a choice of vertex $b\in\mathbb{N}\setminus f_n(A_n)$ such that, for all $s\in A_n$, the equivalence

$$
\{n+1,s\}\in \operatorname{Edges}(G) \iff \{b,f_n(s)\}\in\operatorname{Edges}(H)
$$

   holds.

Regardless of which of the cases above were used, define

$$
A_{n+1} = A_n\cup\{n+1, a\}
$$

and $f_{n+1}:A_{n+1}\to\mathbb{N}$ as $f_{n+1}(s)= f_n(s)$ for every $s\in A_n\setminus\{n+1,a\}$, and

$$
f_{n+1}(n+1) = b \quad\text{and}\quad f_{n+1}(a) = n+1.
$$
It is evident that $f_{n+1}$ is injective, and that $\{1,\dots,n+1\}\subseteq A_{n+1}\cap f_{n+1}(A_{n+1})$.

With the subsets $A_1,A_2,\dots$ and functions $f_1,f_2,\dots$ defined this way, note that we have the chain of inclusions

$$
A_1\subseteq A_2\subseteq \cdots.
$$

Moreover, for every $n\in\mathbb{N}$, it holds that $f_{n+1}|_{A_n} = f_n$ and for pair of distinct numbers $a,b\in A_n$ we have the equivalence

$$
\{a,b\}\in \operatorname{Edges}(G) \iff \{f_n(a),f_n(b)\}\in \operatorname{Edges}(H).
$$

We may now define the desired graph isomorphism $f:\mathbb{N}\to\mathbb{N}$ as

$$
f(n) = f_n(n)
$$

for every $n\in\mathbb{N}$.
$\square$


## Random infinite graphs are almost always the same

We now get to the main point of this post: random infinite graphs.

We can randomly construct a graph on a set of vertices as follows. Given a set of vertices $V$, for each pair of distinct vertices in $V$, a biased coin is flipped with a probability of $p$ of landing on heads. If the coin lands on heads, an edge is created between those two vertices. This process is repeated for all pairs of distinct vertices in $V$, and the events of whether an edge is created between two vertices are independent of one another. Essentially, the graph is constructed by randomly deciding, with a certain probability, whether or not to add an edge between each pair of distinct vertices.

This process induces a probability measure on the set $\operatorname{Graph}(V)$ of all graphs having vertex set $V$, which is

$$
\operatorname{Graph}(V) = \mathcal{P}\left(\binom{V}{2}\right),
$$

where $\mathcal{P}(S)$ denotes the power set of a set $S$. For each pair of distinct elements $a,b\in V$, define

$$
A_{\{a,b\}} = \big\{G\in \operatorname{Graph}(V)\,:\, \{a,b\}\in\operatorname{Edges}(G)\big\}
$$

to be the event that the randomly generated graph contains the edge connecting $a$ and $b$ such that

$$
\operatorname{Pr}\big(\{a,b\}\in\operatorname{Edges}(G)\big) = \operatorname{Pr}(A_{\{a,b\}}) = p,
$$
and these events are all independent of each other.

We now turn our attention to infinite graphs. It turns out that random graphs constructed this way are almost always all isomorphic to each other. This is because a graph constructed this way is almost always universal!

>*Theorem.* Let $G$ be a random graph with $\operatorname{Vertices}(G)=\mathbb{N}$ constructed as above. The ranom graph $G$ is universal with probability $1$.

*Proof.* We prove that the set of graphs that are not universal is a set of measure zero. Given disjoint finite sets $S,T\subseteq\mathbb{N}$ and a number $a\in\mathbb{N}\setminus (S\cup T)$, let $A(S,T,a)$ denote the event that in the graph $G$, the vertex $a$ is adjacent to every vertex in $S$ and not adjacent to every vertex in $T$. That is,

$$
A(S,T,a) = \Bigg(\bigcup_{s\in S} A_{\{a,t\}}\Bigg)\cup\Bigg(\bigcup_{t\in T} (A_{\{a,t\}})^c\Bigg).
$$

Note that the probability of this event is given by

$$
\operatorname{Pr}\big(A(S,T,a)\big) = p^{|S|}(1-p)^{|T|}.
$$

Given finite disjoint subsets $S,T\subseteq\mathbb{N}$ that are not both nonempty, note that the events $A(S,T,a)$ and $A(S,T,b)$ are independent from one another for each choice of $a,b\in\mathbb{N}\setminus (S\cup T)$ and thus

$$
\begin{align*}
\operatorname{Pr}\Bigg(\bigcap_{a\in\mathbb{N}\setminus(S\cup T)}A(S,T,a)^c\Bigg)
&= \prod_{a\in\mathbb{N}\setminus(S\cup T)}\left(1-p^{|S|}(1-p)^{|T|}\right)\\
&=\lim_{k\to\infty}\left(1-p^{|S|}(1-p)^{|T|}\right)^k\\
 & =0,
\end{align*}
$$

as $0<p^{|S|}(1-p)^{|T|} < 1$. Now, the event that the random graph is *not* universal is

$$
\bigcup_{n\in\mathbb{N}}\bigcup_{S\in\binom{\mathbb{N}}{k}}\bigcup_{n\in\mathbb{N}}\bigcup_{T\in\binom{\mathbb{N}\setminus S}{k}}\Bigg(\bigcap_{a\in\mathbb{N}\setminus(S\cup T)}A(S,T,a)^c\Bigg),
$$

which is a countable union of a measure-zero sets, and thus also has zero measure.
$\square$

We conclude that there is a graph $H$ on $\mathbb{N}$ such that a randomly generated graph $G$ is almost always isomorphic to $H$.

>**Corollary.** With probability one, random graphs on $\mathbb{N}$ are all isomorphic to one another.
