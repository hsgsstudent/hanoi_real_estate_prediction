# Ensemble methods
- Ensemble methods are techniques that aim at improving the accuracy of results in models by combining multiple models instead of using a single model. The combined models increase the accuracy of the results significantly. 

## Single weak learner problem
- It is important to pick an algorithm for solving a specific Machine Learning problem (classification or regression...), such as SVM, Decision Tree, Neural Network,..
- The process can be described as:
    1. Analyse data
    2. Try different models/algorithms to solve the problem
    3. For each model/algorithm, finetune to hyper parameters to obtain the best result

## Bias and variance tradeoff

- The bias error is an error from erroneous assumptions in the learning algorithm. High bias can cause an algorithm to miss the relevant relations between features and target outputs (underfitting).
- The variance is an error from sensitivity to small fluctuations in the training set. High variance may result from an algorithm modeling the random noise in the training data (overfitting).
- The tradeoff is unavoidable in single weak learner

## Ensemble method - Combine weak learners 
- We can aggregate different models in order to produce better results
- Main emsemble methods:
    1. Bagging
        + Bagging is mostly used for models whose bias is already low, but having high variance
        + The same model is trained multiple times on different subsamples (created using bootstrapping), resulting in multiple models
        + The models are then aggregated to produce the final result
    2. Boosting
        + Boosting is mostly used for models whose variance is low, but having high bias
        + A lot of models (of the same type) are trained, in which the latter model will learn by reducing errors of previous models
        + The last model is taken as the final result
    3. Stacking
        + Some models (of different types) are independently trained, and then a supervisor model will be trained to combined the child models in the best possible way.


## Gradient Boosting

### Idea
- The disadvantages of Bagging:
    + Bagging models are trained in parallel, thus independently. In a case when all models create bad results, bagging performance can be disappointing. In other words, we can not control the development of submodels added into bagging
    + Boosting improve consequent models by avoiding previous models' error, which is not available in bagging

- Boosting overview:
    + A sequential process, which can result in longer training time
    + After each epoch, the error can be reduced exponentially
    + Boosting can work well when the base model is not too complicated, and the error does not change very fast
    + Base model's bias can be reduced through boosting

## Adaptive Boosting

## References 
- https://viblo.asia/p/ensemble-learning-va-cac-bien-the-p1-WAyK80AkKxX
- https://viblo.asia/p/gradient-boosting-tat-tan-tat-ve-thuat-toan-manh-me-nhat-trong-machine-learning-YWOZrN7vZQ0
- https://www.ibm.com/think/topics/boosting