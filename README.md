# Estimating Pi: The Monte Carlo Method

Initial completion date: Apr 18, 2021\
Last update: Oct 2, 2021\
Owner: Alison Zhang\
Credit: A simulation of the Monte Carlo method, developed by Stanislaw Ulam (1940s)\

## The Math Behind Approximating Pi

Let U<sub>1</sub> and U<sub>2</sub> be independent U(-1,1) random variables.

The probability that (U<sub>1</sub>, U<sub>2</sub>) is in the unit circle C = { (x<sub>1</sub>, x<sub>2</sub>): x_1<sup>2</sup> + x_2<sup>2</sup> ≤ 1 } is around the value of Pi! The more samples you draw from the uniform distribution, the more accurate this estimate will be. Below is a graph visualization of 100,000 drawings of uniform RVs.

![Graph visualization of Pi](sim_graph.png)

For more statistics and mathematical proof, see https://blogs.sas.com/content/iml/2016/03/14/monte-carlo-estimates-of-pi.html.