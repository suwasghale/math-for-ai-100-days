# 📅 Prépa L2 — Syllabus

**Goal:** be ready for **L2 Informatique** in France (Sept 2027): cover the French **L1 maths** that L2 assumes, then preview the L2 maths itself.
**Main book:** Pearson *Mathématiques L1* (Marco, Lazzarini et al.). **Duration:** 40 weeks, 23 Nov 2026 → 29 Aug 2027.
**Pace:** ~1 h/day, 6 days/week (~6 h/week).

## How each week works

| Day | What to do |
|---|---|
| Mon–Thu | Read the section(s), redo every worked example **on paper**, without looking |
| Fri–Sat | Exercises at the end of the chapter + the chapter's *Test*. Try each one for 20 min before opening the solution |
| Sun | Write the weekly log in French: `python prepa_week.py N "Topic" --chap "X"` (30–45 min) |

**Rules**
- Pen and paper first. NumPy only to *check* an answer, never to replace the hand calculation.
- Write the weekly log in **French**. The exams will be in French.
- Behind schedule? Use the buffer weeks (11, 20, 21, 22, 33). Don't skip the exercises to catch up.
- Each "Révision" week ends with a **2-hour mock exam** with no notes, like a real *partiel*.

## Skipped on purpose
Pearson ch. 9, 10, 11 (groups, symmetric group, rings), ch. 14 (rational fractions), ch. 22 §V–VIII, ch. 23, 24, and all *Compléments*. These are for the maths degree, not CS. Come back to them only if you have time.

### Phase 1 — Bases (raisonnement, ensembles, arithmétique, complexes, polynômes)

| Sem. | Week of | Topic | Source | What it covers |
|---|---|---|---|---|
| 01 | 23 Nov 2026 | Modes de raisonnement | Pearson L1 — *Quelques modes de raisonnement* (p. xvii–xxv) | Logic, implication, equivalence, proof by récurrence |
| 02 | 30 Nov 2026 | Ensembles et applications | Ch. 7 §I–II (p. 139–157) | Sets, injective / surjective / bijective maps |
| 03 | 07 Dec 2026 | Symboles Σ et Π | Ch. 6 (p. 115–133) | Sums, geometric series, binomial formula |
| 04 | 14 Dec 2026 | Relations binaires | Ch. 7 §IV–V (p. 160–169) + Ch. 1 quick review | Equivalence and order relations; plane geometry refresher |
| 05 | 21 Dec 2026 | Dénombrement | Ch. 8 (p. 179–199) | Counting, arrangements, combinations |
| 06 | 28 Dec 2026 | Arithmétique dans Z (1) | Ch. 12 §I–IV (p. 279–292) | Divisibility, congruences, PGCD/PPCM, primes |
| 07 | 04 Jan 2027 | Arithmétique dans Z (2) | Ch. 12 §V–VI (p. 293–296) | Bézout, Diophantine equations, Z/nZ |
| 08 | 11 Jan 2027 | Nombres complexes | Ch. 5 (p. 87–113) | Modulus, complex exponential, roots of unity |
| 09 | 18 Jan 2027 | Polynômes (1) | Ch. 13 §I–III (p. 301–324) | K[X], degree, Euclidean division |
| 10 | 25 Jan 2027 | Polynômes (2) | Ch. 13 §IV–V (p. 325–340) | Roots, multiplicity, factorisation over R and C |
| 11 | 01 Feb 2027 | Révision Bases | Pearson *Tests* for ch. 5–8, 12–13 | Buffer + mock exam (2 h, no notes) |

### Phase 2 — Algèbre linéaire

| Sem. | Week of | Topic | Source | What it covers |
|---|---|---|---|---|
| 12 | 08 Feb 2027 | Calcul vectoriel dans Kn | Ch. 15 (p. 383–401) | Familles libres/liées — redo Days 1–7 by hand |
| 13 | 15 Feb 2027 | Matrices et rang | Ch. 16 §I–II (p. 403–415) | Matrix operations, rank — redo Days 8–13 by hand |
| 14 | 22 Feb 2027 | Pivot de Gauss et systèmes | Ch. 16 §III–V (p. 416–437) | Row reduction by hand, linear systems — redo Day 14 |
| 15 | 01 Mar 2027 | Noyau image et théorème du rang | Ch. 17 (p. 439–452) | Kernel, image, rank theorem — redo Days 15, 17, 18 |
| 16 | 08 Mar 2027 | Espaces vectoriels | Ch. 18 §I–II (p. 453–471) | Abstract vector spaces, linear maps |
| 17 | 15 Mar 2027 | Bases et dimension | Ch. 18 §III (p. 472–488) | Bases, dimension, supplementary subspaces |
| 18 | 22 Mar 2027 | Matrice d'une application linéaire | Ch. 19 §I–II (p. 489–503) | Coordinates, change of basis, similar matrices |
| 19 | 29 Mar 2027 | Déterminants | Ch. 20 (p. 529–548) | Cofactor expansion, properties — redo Day 16 |
| 20 | 05 Apr 2027 | Sommes directes (léger) | Ch. 19 §III–IV (p. 504–523) | LIGHT WEEK — DALF C1 prep |
| 21 | 12 Apr 2027 | Pause DALF | — | BUFFER — DALF C1 exam (move this week to match your exam date) |
| 22 | 19 Apr 2027 | Révision Algèbre linéaire | Pearson *Tests* for ch. 15–20 | Mock exam: Gauss pivot, rank, determinant, change of basis |

### Phase 3 — Analyse

| Sem. | Week of | Topic | Source | What it covers |
|---|---|---|---|---|
| 23 | 26 Apr 2027 | Fonctions usuelles | Ch. 2, 3, 4 quick review (p. 29–86) | Continuity/derivative intuition, trig, log/exp |
| 24 | 03 May 2027 | Suites (1) | Ch. 21 quick + Ch. 22 §I–II (p. 563–590) | Sup/inf, bounded and convergent sequences |
| 25 | 10 May 2027 | Suites (2) | Ch. 22 §III–IV (p. 590–600) | Limit operations, monotone and adjacent sequences |
| 26 | 17 May 2027 | Limites et continuité | Ch. 25 §I–II (p. 681–700) | Limit of a function, continuity |
| 27 | 24 May 2027 | Fonctions continues | Ch. 25 §III–IV (p. 701–718) | Intermediate value theorem, o / O / équivalents |
| 28 | 31 May 2027 | Dérivation | Ch. 26 §I–II (p. 721–737) | Derivatives, Rolle, accroissements finis |
| 29 | 07 Jun 2027 | Suites récurrentes et convexité | Ch. 26 §IV + Ch. 29 §I–II (p. 740–753, 841–852) | u(n+1) = f(u(n)), higher derivatives, convexity |
| 30 | 14 Jun 2027 | Taylor et développements limités | Ch. 29 §III–IV (p. 853–875) | Taylor formulas, DL and their uses |
| 31 | 21 Jun 2027 | Intégration | Ch. 27 §III, IV, VI (p. 774–790) | Primitives, intégration par parties, changement de variable |
| 32 | 28 Jun 2027 | Équations différentielles | Ch. 31 (p. 943–967) | Linear ODEs of order 1 and 2 |
| 33 | 05 Jul 2027 | Plusieurs variables + révision | Ch. 30 §IV–V (p. 917–941) + *Tests* | Partial derivatives, gradient; mock exam on analysis |

### Phase 4 — Topics from L2 itself (beyond the Pearson L1 book)

| Sem. | Week of | Topic | Source | What it covers |
|---|---|---|---|---|
| 34 | 12 Jul 2027 | Valeurs propres et diagonalisation | Pearson *Mathématiques L2* or Exo7 (Réduction des endomorphismes) | Characteristic polynomial, diagonalisation — resume Days 22–24 |
| 35 | 19 Jul 2027 | Orthogonalité et moindres carrés | Pearson L2 or Exo7 (Espaces euclidiens) | Scalar product, projection, Gram-Schmidt, QR, least squares — Days 19–21, 28 |
| 36 | 26 Jul 2027 | Théorème spectral et SVD | Pearson L2 or Exo7 | Symmetric matrices, spectral theorem, SVD, PCA — Days 25–27, 29–30 |
| 37 | 02 Aug 2027 | Probabilités discrètes | Pearson L2 or Exo7 (Probabilités) | Probability spaces, conditioning, Bayes, independence |
| 38 | 09 Aug 2027 | Variables aléatoires discrètes | Pearson L2 or Exo7 | Expectation, variance, Bernoulli, binomial, geometric, Poisson |
| 39 | 16 Aug 2027 | Introduction aux graphes | Your SQA discrete-maths notes + any French L2 *introduction aux graphes* course | Vocabulary, paths, trees, BFS/DFS |
| 40 | 23 Aug 2027 | Analyse numérique et bilan | Any L2 *analyse numérique* course notes | Interpolation, trapezoid/Simpson, Euler method; final review |