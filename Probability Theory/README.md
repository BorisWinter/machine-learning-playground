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
