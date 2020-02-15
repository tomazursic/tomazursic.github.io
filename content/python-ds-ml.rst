:title: Python Data Analysis and ML
:date: 2019-11-06
:category: blog
:tags: python, ds, ml, ai
:summary: Learning notes for Data Science and Machine Learning using Python


>> **This post is under heavy development and with constant updates, following the learning curve.**

.. code-block:: text

  DRAFT VERSION,
  contains Typos
  contains <°-(-(-(-<
  contains no ( o ) ( o )
  also, no 8====D
  also, tl;dr

Basic Machine Learning with Python
===================================

About basic concepts of Data Analysis, Machine Learning and the basics of
building ML models with Scikit-Learn and TensorFlow for humans.


ML Terminology
--------------

Machine Learning is the process of building models from data, either to gain
insight into the data or to make predictions for new data (generalization).

There are two main categories:

- **SUPERVISED** learning, in which the data (training data) is labeled with an
  known outcome (this is the supervision part), and the aim is to predict new
  outcomes from new data; if the outcome is a category this is classification
  while if the outcome is a continuous quantity this is regression

- **UNSUPERVISED** learning, in which the data is analyzed for underlying
  patterns to gain insight; common examples are clustering (finding similar
  cases), outlier detection (finding unusual cases), and dimensionality
  reduction (reducing the number of variables needed to represent the data,
  essentially a form of lossy compression)

**"A technique for implementing ML"**

DL in the context of **deep neural networks (DNNs)** is the code
structures you write **are arranged in layers that loosely mimic the human
brain, learning patterns of patterns**.

Simple explanation is "when we have more than 2 layers we are talking about deep leaning"

From bottom up is:

- DL is subset of ML and ML is subset of AI
- DL drives ML which than can enable AI


.. code-block:: text

    +-------------------------+
    |AI                       |
    |  +--------------------+ |
    |  |ML                  | |
    |  |   +--------------+ | |
    |  |   |DL            | | |
    |  |   |              | | |
    |  |   |              | | |
    |  |   |              | | |
    |  |   |              | | |
    |  |   +--------------+ | |
    |  +--------------------+ |
    +-------------------------+

* The data used in ML is typically tabular. 
* The **columns** are called `features` while the **rows** are `instances or observations`.
* For supervised learning, we call the output the target or label. 
* Often refer to the vector if features as `X` and the output (label) as `y`, and say that we're trying to find a function that approximates `f(X)=y`; this
  function is our model and is characterized by some model parameters. 
* We choose the type or class of model, and then use ML techniques to learn the
  model parameters that minimize the error (the difference between the
  predicted and actual output)

ML Workflow
-----------

A typical machine learning workflow begins with:

- **GETTING THE DATA** 

  Collecting data, creating datasets

- **EXPLORING AND CLEANING** 

  Known as "exploratory data analysis" (EDA) which consist of (handling missing
  values, normalizing values, removing bad data and outliers, encoding data in
  appropriate representations, and more) 

- **TRAINING THE MODEL**

  Evaluating the results adjusting the model type or the hyperparameters if the
  results are not yet satisfactory


How to choose data to train ML system
-------------------------------------

Features / Attributes
~~~~~~~~~~~~~~~~~~~~~

Features (aka attributes) are used to train ML system.
This are the proprieties of the things you are trying to learn about

.. code-block:: text

          ,--./,-.      
         / #      \    <-- color
        |          |
         \        /    <-- size
          `._,._,'

    
Features of the apple might be size and color.

2 features, would mean there are 2D (two dimensions)

The 2D system my be plotted on a graph if features are represented in a numerical way.

The ML system can learn to split the data up with a line to separate apples from oranges.

.. code-block:: text

        ^
        |
        |                           X
        |           O             X
        |                       X
        |          O          X
      S |            OO     X
      I |    O            X
      Z |        O      X    A
      E |           O X     A
        |           X  A
        |     OO  X                           A = Apples
        |       X   A A                       O = Oranges
        |     X           A                   X = Line
        |   X  A
        | X
        +------------------------------->
                      COLOR

Example: Plotting apple and oranges size and colors

Choosing useful inputs features can have big impact on the quality of the ML
system. Some features my not be useful enough to separate the data points.
