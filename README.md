# Task Environment System

A Flask web application of a task environment to be used during the data collection experiments for dataset creation in
the project "Ethically-driven Multimodal Emotion Detection for Children with Autism".

The system includes:

- Four different tasks to elicit each emotional zone (i.e green, yellow, red and blue);
    - The yellow zone elicitation task includes two versions, one for each session.
- Four different calming content to help the child to calm and regulate their emotions between the tasks;
- The systems also record into a local database the accessed time of each task to allow later recovering of which
  eliciting task the child was interacting with during a given moment in the study session.

## User Manual

A user can configure each task's content and time by adding/changing the variables values in
a `.env` file.

The `example.env` file contains examples of variable and values format.

### Copyright Content Used

- Youtube Videos:
  - [Calming Video 1]()
  - [Calming Video 2]()
  - [Calming Video 3]()
  - [Calming Video 4]()
  - [Green Video]()
  - [Blue Video]()

- Games:
  - Pacman 
  - [Clumsy Bird](https://github.com/ellisonleao/clumsy-bird) by Ellison Leao
