# Clicker Game

## Developers :
Owen Cupps, Parker Gonzaga, Ahmed Malik, Alex Nguyen, Ethan Scott


## API(s) used
Pygame:
https://www.pygame.org/docs/

## Sprint 1 Report

In this current iteration for our Clicker Game project, the developers were able to implement two use cases to fulfill the project requirements for this sprint. A majority of this project was completed using the Pygame API; this API allows for a majority of coding actions (such as key inputs, screen display, etc.) to be abstracted and encapsulated in a way that allows the programmer to code without worrying about more complex implementations. The API documentation can be seen in a link in the readme. Using this API, we were able to implement two use cases with two test cases, with each test case corresponding to one use case. 

The two test cases we implemented were the click button and the game’s initial UI. 

The click button should allow the user to click an icon and increment a counter. Test Cases:
-Action:  Click icon.
 -Expected Result:  Counter increments (by 1?)
-Action:  Do not click icon for a period of time (1min)
 -Expected Result:  Counter remains at the same value.
-Action:  Click icon 10 times.
 -Expected result:  Counter increments by 10 (if we don’t have upgrades implemented)

The clicker game’s user interface should load once the program is run, allowing the user to view the click icon, point counter, and upgrade buttons. Test cases:
-Action:  Run program.	 
 -Expected Result:  Clicker icon, point counter, and upgrade buttons are drawn to the screen.
-Action:  Program runs for a period of time (1 minute)
 -Expected result:  If clicker button is clicked during this time, UI updates to display newly incremented counter

We encountered difficulties through the production of the Clicker Game project. The first problem was figuring out a language and API to use to begin this project. Due to our various backgrounds, we decided to use a language that would be suitable for the time range of this project, which was Python. Additionally the APIs used in Python for video games are plentiful and some members had past experience with these APIs. The Pygame API the developers ended up using was chosen due to the resources online that support this API and some developers having past experience with this API. Thankfully, there wasn’t too much difficulty in designing and implementing the UI, as some of the developers had prior experience with Pygame. Additionally, all test cases did pass with the current iteration of use cases. 



### remove sections below before final submission
## Sprint 1 Goals: 
-Get basic UI up for players to see

-Get click functionality working and be able to display clicks(?)

## Tasks : 
-Set up basics of main Game class (Ahmed) (started)

-Gather/ design Assets for UI to display on game window

-Code UI so that the displays can be clicked on (testing for now) (main goal) (alex has set up the barebones displays in the UI, which DO detect mouse click events)

-Establish a clicker counter (started, let me know what you guys think -Owen)
  -Get the clicker counter to be incremented when the whatever needs to get clicked is clicked(main goal)

