# Clicker Game

## Developers :
Owen Cupps, Parker Gonzaga, Ahmed Malik, Alex Nguyen, Ethan Scott


## API(s) used
Pygame:
https://www.pygame.org/docs/

## Sprint 3 Report

Link to full report (UML diagrams, videos):
https://docs.google.com/document/d/1qcI0fPElFwICL8WyJvkWyKaALD-E73XwjE_YWLhzFVo/edit?usp=sharing

In this iteration of our Clicker Project, we implemented one last use case. This use case consisted of adding sound to the clicker button once clicked.

We created one test case for the use case that was implemented:

Sound Test Case:
- Action: Click on the Clicker button
- Expected Result: A sound emits from the player’s machine that signifies the button being clicked.

 

We had difficulties implementing some of the features described in the use cases as well as some general new features that were added. First, the UI was changed so that instead of using pygame made shapes, a new design would be used instead (in the form of a png). This was difficult to implement because of the unprecedented nature of using a png to click on instead of a pygame designed shape. This was solved by using pygame documentation and other source code where users had similar problems that were solved in different ways. The next minor problem would be the use of sound files and the paths used to access assets (specifically how they were organized). This was quickly solved using common filepath organization practices. 
One additional feature that was gonna be added was a victory screen once the player reached a certain amount of points. Due to time constraints and some difficulties this was not added, instead of prompt of how many points are needed for a “goal” was added. Additionally, this goal value changes as the player reaches the previous goal value. 




## Sprint 3 Goals: 
- Incorporate sounds (music, sound effects).

- Implement goal systems



