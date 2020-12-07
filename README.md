# DND App

## Contents
* [Brief](#brief)
   * [Additional Requirements](#additional-requirements)
   * [My Approach](#my-approach)
* [Architecture](#architecture)
   * [Database Structure](#database-structure)
   * [CI Pipeline](#ci-pipeline)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
* [Testing](#testing)
* [Front-End Design](#front-end-design)

## Brief
The brief for this project was for us to create an app that uses 4 services and deploy it using docker swarm, nginx, gunicorn and jenkins.

### Additional Requirements
In addition to what has been set out in the brief, I am also required to include the following:
* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX

### My Approach
The app I decided to create was an app that creates a random DND character.

Service-1
service 1 was the frontend where the user will go and see a character class, race and stats.

![Service1][Service1]

Service-2
service 2 generates a random character class from the most popular DND classes, Wizard, Fighter, Rogue, Ranger and Cleric

![Service2][Service2]

Service-3 
service 3 generates a random race between Human, Dwarf, Half-Orc, Halfling and Elf

![Service3][Service3]

Service-4
service 4 generates a characters stats, after the generation it adds to the stats of the characcter based on the race.

![Service4][Service4]

## Architecture
### Database Structure
Below is an entity relationship diagram (ERD) showing the structure of the database that I plan to implement, I tried to get it done for the first release, however I couldn't make it work in time. As the database was only one table it is very basic.

![ERD][ERD]

### App Structure
Below is my app structure that shows how my services work tegether. 

![structure][structure]


### CI Pipeline
Pictured below is the continuous integration pipeline.

![ci][ci]

Here is the stage view

![stage][stage]

## Project Tracking
GITHUB was used to track the progress of this project

![projectboard][projectboard]

## Version control
For version control I have used github. This was used to develop the program whilst using branches. This is useful as you can change the code without it affecting your working branch.

![branch][branch]

## Risk Assessment
This is my risk assesment for this project, it shows the risks and mitigations, as well as a review at the end of the project. 

![riskass][riskass]

## Testing
PyTest is used to run unit tests on the app. This was used as it provides a coverage chart which allows the user to see how much of the program has been tested.

test service-1

![coverage1][coverage1]

test service-2

![coverage2][coverage2]

test service-3

![coverage3][coverage3]

test service-4

![coverage4][coverage4]

## Front-End Design
below is a screen grab of the page the user will see.

![home][home]


[Service1]: https://i.imgur.com/MRAZbKY.png
[Service2]: https://i.imgur.com/q8Nvpx1.png
[Service3]: https://i.imgur.com/fhGxC5E.png
[Service4]: https://i.imgur.com/DCVdz35.png
[ERD]: https://i.imgur.com/kkS2WDh.png
[risk]: https://i.imgur.com/1Xj9ArL.jpg
[ci]: https://i.imgur.com/LyliUtr.png
[structure]: https://i.imgur.com/cUEesp4.png
[projectboard]: https://i.imgur.com/kkS2WDh.png
[branch]: https://i.imgur.com/WvVpnQt.png
[riskass]: https://i.imgur.com/HeGg8AG.png
[coverage1]: https://i.imgur.com/O141mTn.png
[coverage2]: https://i.imgur.com/J94vsb6.png
[coverage3]: https://i.imgur.com/eNU9mvY.png
[coverage4]: https://i.imgur.com/Lylahwm.png
[home]: https://i.imgur.com/QOXG53W.png
[stage]: https://i.imgur.com/KTxdrkw.png
