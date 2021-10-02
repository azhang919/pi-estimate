# Estimating Pi: The Monte Carlo Method

![Graph visualization of Pi](sim_graph.png)

Initial completion date: April 18, 2021\
Last update: October 2, 2021\
Owner: Alison Zhang\
Credit: A simulation of the Monte Carlo method, developed by Stanislaw Ulam (1940s)\

## The Math Behind Approximating Pi

Let U<sub>1</sub> and U<sub>2</sub> be independent U(-1,1) random variables.

The probability that (U<sub>1</sub>, U<sub>2</sub>) is in the unit circle `C = { (x_1, x_2): x_1^2 + x_2^2 ≤ 1 }` is, you guessed it, around the value of Pi! The more samples you draw from the uniform distribution, the more accurate this estimate will be.

For more statistics and mathematical proof, see https://blogs.sas.com/content/iml/2016/03/14/monte-carlo-estimates-of-pi.html.