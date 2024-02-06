# Task Environment System

A Flask web application of a task environment to be used during the data collection experiments for dataset creation in
the project "Ethically-driven Multimodal Emotion Detection for Children with Autism".

The system includes:

- Four different tasks to elicit each emotional zone (i.e green, yellow, red and blue);
    - The yellow zone elicitation task includes two versions, one for each session.
- Four different calming content to help the child to calm and regulate their emotions between the tasks;
- The system automatically change activities based on set time per activity.
- The systems also record into a local database the accessed time of each task to allow later recovering of which
  eliciting task the child was interacting with during a given moment in the study session.

The Task Environment system can be accessed at http://task-environment.datascienceinstitute.ie/

## User Manual

### Development

1. Prepare the virtual environment (Create and activate virtual environment with venv).

`python -m venv ./venv`

`source ./venv/bin/activate`

2. Run the script

`python app.py`

### Deployment with Docker

1. Build the images

`docker compose build`

2. Start the services

`docker compose up -d`

A user can configure each task's content and time by adding/changing the variables values in
a `.env` file.

The `example.env` file contains examples of variable and values format.

## Licence

This repository is released under the [GPL-3.0 License](LICENSE.md).


### Copyright Content Used in This Project

- Youtube Videos:
    - [Calming Video 1](https://www.youtube.com/embed/POP5BzZLOKk?controls=0&start=21&autoplay=1)
    - [Calming Video 2](https://www.youtube.com/embed/qUJ6nGK7wrw?controls=0&amp;start=17&autoplay=1)
    - [Calming Video 3](https://www.youtube.com/embed/y4BLQW1lCDE?controls=0&amp;start=14&autoplay=1)
    - [Calming Video 4](https://www.youtube.com/embed/TlQ1EEbBlcI?controls=0&amp;start=21&autoplay=1)
    - [Green Zone Video](https://youtu.be/VB4CCHHYOqY?si=KldC4g2z7MJOWQcr)
    - [Blue Zone Video](https://youtu.be/lVrYV0odeFY?si=lUk1S8TDQOlgqUca)

- Games:
    - [Pacman](https://pacman.com/en/history/)
    - [Clumsy Bird](https://github.com/ellisonleao/clumsy-bird) by Ellison Leao

## Citation

If you use any of the resources provided on this repository in any of your publications we ask you to cite the following
work:

Sousa, Annanda, et al. "**Introducing CALMED: Multimodal Annotated Dataset for Emotion Detection in Children with
Autism**."
International Conference on Human-Computer Interaction. Cham: Springer Nature Switzerland, 2023.

----

Author: Annanda Sousa

Author's contact: [annanda.sousa@gmail.com](mailto:annanda.sousa@gmail.com)

----
