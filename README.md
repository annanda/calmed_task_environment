# Task Environment System

A Flask web application of a task environment to be used during the experiments for dataset creation in the project *"Person-Independent Multimodal Emotion Detection System for Children with High-Functioning Autism"*.

The system includes: 

* 4 different tasks to elicit each emotional zone (i.e green, yellow, red and blue);
* 4 different calming content to help the child to calm down and relax between the tasks;
* A database to store the time each part of the system was requested to allow later recovering of which eliciting task the child was interacting with during a given moment in the session. 


## Config
The configuration of tasks contents and time in each of them can be configured by changing the variables values in a `.env` file. 
You can find a `example.env` file to check the format for the variables' format. 