# Probability Theory

A summary of probability theory based on the lecture notes of the course "Principles of Statistical Modelling" by Herbert Jaeger: https://www.ai.rug.nl/minds/teaching/courses/t2019psm/.

## Introduction

- Probability theory is the scientific foundation of data engineering.
- Statistics and machine learning share the same mathematical roots in probability theory, but they pursue different goals and have developed different tools and techniques.

## Components of data collection scenarios

Terms as used by (and only by) Jaeger.

| Component | Definition                                                                                                                                                                                                               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| RSOI      | The _Reality Segment Of Interest_. A reality segment of interest is a circumscribed portion of reality, in which one has specified a set of opportunities for making observations. Commonly referred to as _population_. |
| OO        | _Observation Opportunities_. A set of objects or events within the RSOI from which observation data _could_ be collected.                                                                                                |
| OP        | _Observation Procedure._ An apparatus or procedure that enables one to actually get data in the RSOI at every OO. Examples are a measurement device in a lab or a questionnaire that is send out.                        |
| OA        | _Observation Acts._ A finite subset of the OO where the observation procedure is actually set to action and data are recorded.                                                                                           |
| DVS       | _Data Value Space._ The set of all possible results that the OP could deliver. Should be defined so that it is guaranteed to contain all possible values.                                                                |

## Randomness

Randomness appears when an observation procedure is executed repeatedly. The data value that comes out of a particular observation act is "random".

## Linking the informal components of data collection with math:

- **RSOI:** Modelled by a set that goes by multiple names in the literature. We will use "universe", and denote it by $\Omega$.
- The elements $\omega \in \Omega$ are referred to as _elementary events_. They are the observation opportunities, so the individual events where observations _could_ be made. An elementary event is an occasion in space-time where _some_, or _any_, measurements can be made — _which_ measurements are made, i.e. which particular recording procedure is carried out at the occasion $\omega$, is not part of $\omega$.
- The data value space (**DVS**) is a set _S_ that contains all the possible outcomes of a particular recording procedure. It is commonly referred to as the _sample space_.
- A particular observation procedure (**OP**) is always connected to a specific data value space. If one adds another OP, the DVS is extended by the new DVS of the new OP. Mathematically, this is done using _cross-products_ of the sample space sets S: S1 X S2. In mathematical abstraction, an OP is a _function_ which turns elementary events $\omega \in \Omega$ into data values $s \in S$. Such functions are called **random variables (RVs)**. Below is an example of random variable X.
  - $X_{i} : \Omega -> S_{i}$ (i $\in$ I).

**Important note on random variables (RVs):** Random variables are arguably the most misleadingly named mathematical objects that we have to live with. A random variable X is neither a variable (it is a function!), nor is it random (it is reliably and deterministically returning the result X( $\omega$ ) $\in$ S when applied to the argument $\omega$). The randomness in our big picture and its mathematical abstraction is not created or modelled by the random variables. It
resides in the universe $\Omega$ which has the property that different elementary events $\omega \in \Omega$ will lead to different data values when the (deterministic!) function X is applied.

## Basic operations on RVs

### Elementary mathematical structure-forming operations (Appendix A)

#### Pairs, tuples, and indexed families

- A pair $\(\omicron_{1}, \omicron_{2}\)$ is ordered.
- A set ${\omicron_{1}, \omicron_{2}}$ is unordered.
