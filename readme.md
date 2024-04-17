# Clicker Game

## Developers :
Owen Cupps, Parker Gonzaga, Ahmed Malik, Alex Nguyen, Ethan Scott


## API(s) used
Pygame:
https://www.pygame.org/docs/

## Sprint 2 Report

In this iteration of our Clicker Project, we implemented two more use cases. Our first use case was to allow users to click the upgrade points per click button to increase the amount of points they get each time they click the icon. Our second use case was the feature where the user passively gains points every second. 

We created the two following test cases for the use cases that were implemented:

Points-Per-Click Upgrade Test Case:
Action:  Click upgrade points per click icon when player has 25 points.
Expected Result:  The player’s points per click is increased by 10, and their total points is decreased by 25.

Idle Point Clicker Test Case:
Action:  Wait 1 second.
Expected Result:  The player’s points should increase by 1.

We had a few difficulties when implementing these features. In order to implement the points per click upgrade feature, we had to go back and change the internal variable name for points. Previously it was named “timesClicked,” which is inaccurate considering points would also be able to be increased passively. We went back and renamed every occurrence of this variable. Another difficulty encountered was synchronization of program versions. To ensure that group members’ work wasn’t overwritten, each member communicated when they were making changes to the code. Finally, our previous game clock did not have the ability to perform an action each second, so we had to adapt it in order to add a timer in order to track when each point gain should occur.



## Sprint 2 Goals: 
-Implement points per click upgrade system

-Allow the player to get points every second when idle



