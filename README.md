## Paleo Hebrew

### torahs

- **torah2.csv** Koren: https://users.cecs.anu.edu.au/~bdm/dilugim/StatSci/data.html 
- **torah3.csv** Leningrad: https://github.com/TorahBibleCodes/Sefaria-Export/ 
### Usage

    $ python3 -m venv env
    $ source env/bin/activate
    $ pip install pandas
    $ python main.py

### 11QpaleoLev extract

**Leviticus Chapter:25**
1. (29) ... tnc mt do ftlag etief emfh rio bcfm tib rkmi ik ciaf
2. (30) ... tibe mqf emimt enc fl talm do lagi al maf. (29) ftlag eiet ...
3. (30) ... lbib asi al fitrdl fta enql ttimsl emh. (31) mirshe itbf
4. (31) asi lbibf fl eiet elag bchi srae edc lo bibx emh mel nia rca
5. (33) ... asif mifle nm lagi rcaf (32) mifll eiet mlfo tlag mtzha iro itb ...
6. (33) larci inb kftb mtzha afe mifle iro itb ik lbib ftzha
7. (34) ... mlfo tzha ik rkmi al ...
8. (36) ... kielam tarif tibrtf kcn ftam hqt la (35) kmo ihf bcftf rg fb ...

### Michigan-Clairmont transliteration scheme (modified)

- https://github.com/TorahBibleCodes/TorahBibleCodes
- https://users.cecs.anu.edu.au/~bdm/dilugim/StatSci/data.html

```
 A = Alef  B = Beit  G = Gimmel D = Dalet H = Hey  W = Waw
 Z = Zain  X = Chet  + = Tet    Y = Yud   K = Kaf  L = Lamed
 M = Mem   N = Nun   S = Samech @ = Ayin  P = Pey  C = Tzadi
 Q = Kuf   R = Reish $ = Shin   T = Tav

 PLETTERS = "abgdefzhjiklmnxopsqrct"
 KOREN = 'ABGDHWZX+YKLMNS@PCQR$T'
```
The standard characters for Alef and Ayin are ) and (, but we
have found they are a major source of transliteration error.

My | Koren | Def 
-- | -- | --
a | A | Alef
b | B | Beit
g | G | Gimmel
d | D | Dalet
e | H | Hey
f | W | Waw
z | Z | Zain
h | X | Chet
j | + | Tet
i | Y | Yud
k | K | Kaf
l | L | Lamed
m | M | Mem
n | N | Nun
x | S | Samech
o | @ | Ayin
p | P | Pey
s | C | Tzadi
q | Q | Kuf
r | R | Reish
c | $ | Shin
t | T | Tav


