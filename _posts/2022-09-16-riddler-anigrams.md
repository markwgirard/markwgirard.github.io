---
title: 'Can You Build The Biggest ‘Anigram’? (Riddler 2022-09-16)'
date: 2022-09-19
permalink: /posts/2022/09/riddler-anigrams/
tags: programming, riddler
---

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

My solution to [this week's riddler](https://fivethirtyeight.com/features/can-you-build-the-biggest-anigram/). (See more of [my Riddler solutions here](/riddlers).)

## The Problem
From Michael Branicky comes a word puzzle that is the G.O.A.T.:

If you like [Wordle](https://www.nytimes.com/games/wordle/index.html), then you might also enjoy [Anigrams](https://anigrams.us/), a game created by Friend-of-the-Riddler™ Adam Wagner.

In the game of Anigrams, you unscramble successively larger, nested collections of letters to create a valid “chain” of six English words between four and nine letters in length.

For example, a chain of five words (sadly, less than the six needed for a valid game of Anigrams) can be constructed using the following sequence, with each term after the first including one additional letter than the previous term:

-   DEIR (which unscrambles to make the words DIRE, IRED or RIDE)
-   DEIRD (DRIED or REDID)
-   DEIRDL (DIRLED, DREIDL or RIDDLE)
-   DEIRDLR (RIDDLER)
-   DEIRDLRS (RIDDLERS)

What is the longest chain of such nested anagrams you can create, starting with four letters?

For specificity, all valid words must come from Peter Norvig’s [word list](https://norvig.com/ngrams/enable1.txt) (a list we’ve used [previously](https://fivethirtyeight.com/features/can-you-solve-the-vexing-vexillology/) here at The Riddler).

_Extra credit:_ How many possible games of Anigrams games are there? That is, how many valid sets are there of four initial letters, and then five more letters added one at a time in an ordered sequence, that result in a sequence of valid anagrams? (Note: Swapping the order of the first four letters does not result in a distinct game.)

## The Solution
It turns out that the longest such chain of anagrams has length 13. While there are numerous such chains, one possible chain of length 13 is given by:
- aeno
- aenos
- aenost
- aeinost
- aeimnost
- aeimnnost
- aeiimnnost
- aeiimnnorst
- aeiimnnorstt
- adeiimnnorstt
- adeeiimnnorstt
- adeeiiimnnorstt
- adeeiiimnnnorstt

With one possible solution being:
- aeon
- aeons
- atones
- atonies
- amniotes
- nominates
- antimonies
- inseminator
- terminations
- antimodernist
- determinations
- intermediations
- indeterminations

(Interstingly, every anigram chain of lenth 13 ends in the same 6 words: inseminator, terminations, antimodernist, determinations, intermediations, indeterminations.)

Extra credit:
Assuming a valid anigram game starts with 4 letters and ends with 10 letters, there are 8,660,949 distinct anigram games.

I wrote up some code to compute my answer which you can see below:

```python
from urllib.request import urlopen
from collections import defaultdict
from functools import lru_cache


url = "https://norvig.com/ngrams/enable1.txt"
file = urlopen(url)
words = [line.decode("utf-8").strip() for line in file]

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def main():
    anagrams = defaultdict(list)
    for word in words:
        # Ignore words of length less than 4
        # (short words are not used in this problem)
        if len(word) >= 4:
            anagrams[''.join(sorted(word))].append(word)

    # An anagram is a child of another anagram if one letter can be added to
    # the parent anagram to produce the child anagram.
    graph = defaultdict(list)
    for anagram in anagrams:
        for letter in alphabet:
            child = ''.join(sorted(anagram + letter))
            if child in anagrams:
                graph[anagram].append(child)

    @lru_cache(maxsize=None)
    def get_longest_chain(anagram):
        if len(graph[anagram]) == 0:
            return (anagram,)
        anigrams = [get_longest_chain(child) for child in graph[anagram]]
        return (anagram,) + max(anigrams, key=len)

    start_anagrams = [anagram for anagram in anagrams if len(anagram) == 4]

    longest_chain = (
        max(
            (get_longest_chain(anagram) for anagram in start_anagrams),
            key=len
        )
    )

    print(f"The longest chain has length {len(longest_chain)}")

    outstring = """
There are numerous ways to construct an anigram chain with this length, but
one such chain is given by:
"""
    print(outstring)
    for anagram in longest_chain:
        print("- " + anagram)

    print("With one possible solution being:")
    for anagram in longest_chain:
        print("- " + anagrams[anagram][0])

    def count_anigram_games():
        @lru_cache(maxsize=None)
        def count_anigrams(anagram):
            if len(anagram) == 10:
                return 1
            return sum(count_anigrams(child) for child in graph[anagram])

        ans = (
            sum(count_anigrams(anagram)
                for anagram in anagrams if len(anagram) == 4)
        )
        return ans

    num_anigram_games = count_anigram_games()

    print("""
Extra credit:
Assuming a valid anigram game starts with 4 letters and ends with 10 letters:
there are {num_anigram_games} distinct anigram games.
""".format(num_anigram_games=num_anigram_games)
)


if __name__ == '__main__':
    main()
```
