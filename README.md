## Your Project Answers

### Project Description
TinyML Updates - TL;DR: Given a Pre-Trained basic n-Dimensional Perceptron model and some valid inputs [x_1, x_2, ... x_n], run Perceptron Algorithm locally to update the model in real time to adapt to specific situations.

Training Machine Learning models is expensive - whether it be in time or in computational power needed. Thus, there is a growing market of 'pre-trained' models - general purpose models that are very good at some set of tasks, like searching for objects in images. However, oftentimes use cases are 1.) more localized and 2.) deployed on much smaller computers. In example, Face ID is used in phones and security camera systems. One problem we run into with deployed models is that they are deployed as-is - thus, unless you spend a lot of training resources to create a very large model, it might not perform your specific task as well as you'd like. Hence, this project: a proof-of-concept exploration where we deploy a model on a small-scale device (FRDM-KL46Z board) and perform updates locally with (ideally) efficient uses of memory.


### Technical Approach
As a baseline, I will be using the Lab 4 and 5 lock and real-time job systems to simulate inputs from an external source to our locally loaded model and ensure that the model doesn't add two inputs at once. The bulk of the work will be developing efficient matrix math systems and doing such operations locally on the model itself (so more inputs can be handled). Ideally, no additional memory will be used except when new inputs are created. Clever uses of parallelization could also be interesting - e.g. adding inputs to each other if the model is currently locked. If time allows, I will look into reading PyTorch models into the C program.

## Feedback.

Good luck!

## Welcome team! Please edit me.
### You can use the 'main' branch for you code.
### The GitHub web-page should be in the 'gh-pages' branch
You can access the page adding a "pages" prefix to the url for the git repo e.g. if your browser currently shows https://github.coecis.cornell.edu/ece3140-sp22/ew423 then the GitHub page is at https://pages.github.coecis.cornell.edu/ece3140-sp22/ew423 . You can edit the source in the gh-pages branch or use the "automatic page generator" acessible via settings->options in the GitHub Pages Section toward the bottom. We recommend the latter approach since it is quick and easy. We made an initial wepage that you can edit and a description of the headings we expect to see.
