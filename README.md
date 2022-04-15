<div align="center">
  <h3 align="center">SIMON SAYS</h3>
  <p align="center">
    INTERACTIVE JAVASCRIPT GAME
  <br />
  <br />
    <a href="https://annahabanna.github.io/Simon-Says/">View Demo</a>
  <br />
  </p>
</div>
<br />

![Screenshot](/assets/img/readme-img/ami.responsive.jpeg)


## About The Project

The project idea was inspired by the childhood memory game Simon Says. Simon was released by Milton-Bradley in 1978 with much fanfare, including a midnight release party at Studio 54, the elite disco in New York City. An instant success, the game reached its peak during the 1980s and continued to sell for decades thereafter [learn more](https://en.wikipedia.org/wiki/Simon_Says)

The game goal is to repeat a series of random computer clicks. After each round, the sequence becomes longer by one click which makes it harder to remember. 

The key project goal is to produce a simple memory game that can be used on all devices, stimulate memory and increase both auditory and visual attention. The target audience is users who consciously seek to improve attention, focus, concentration, and musical hearing.

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#ux-and-ui">UX and UI</a></li>
    <li><a href="#design">Design</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#deployment">Deployment</a></li>
    <li><a href="#testing">Testing</a></li>
    <li><a href="#credits">Credits</a></li>
  </ol>
</details>


## Built With

The project was built using the following tools:

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://www.javascript.com/)
* [JQuery](https://jquery.com)



## UX and UI

**User Story**
    
1. To play the game on any chosen device

2. To understand the rules of the game 

3. To be able to easily navigate the different parts of the game 

4. To be able to use all the interactive elements of the game

 **Game Flow**

The game flow schema was created using Figma and shows the simple logic of the game. The user is required to navigate from the game start window by pressing the continue button. On the next page, the user is required to press the start game button. Then the game begins and  computer activates a colored button with sound and animated press. The user is required to repeat what was 'played' by the computer and the user input is then verified as being true or false. If the user input correctly replicates what the computer 'played' a moment ago, the game then moves to the second level. The computer activates another colored button. This time the user input has to include the previous input and the newly generated button. If the user makes a mistake the game is over and instruction is given to reset the game by pressing the reset button that redirects to the game rules window.

![game flow](assets/img/readme-img/game-flow.jpeg)

**Wireframe**

The wireframe for the game was created using Figma and each page was drawn separately for desktop and mobile view. The tablet version of the website was designed to repeat the desktop view.

<details> 
  <summary> ** Wireframe ** </summary>
  <img src= "assets/img/readme-img/game-wireframe.jpeg">
</details>


<p align="right">(<a href="#about-the-project">back to top</a>)</p>



## Design

**Colors**

The game colors were chosen to compliment the four colors of the Simon Says game, ie. red, blue, green, and yellow.  As my game design is small-scale and compact, the two distinctively different background colors were picked to make game navigation memorable and easily distinguishable for the user. The main accent color of Celadon Green (#1E847F) was picked for the game rules window with the additional accent color of Medium Turquoise (#4FD1C5) for the continue button design. The chosen font color Dark Charcoal (#333) is well accessible with a great contrast ratio against the chosen background colors.
    
<details> 
  <summary> ** Game rules window palette ** </summary>
  <img src= "assets/img/readme-img/game-palette.png">
</details>

The background color of the main game section is Peach Crayola (#ECC19C) which provides a soft and subtle effect for the user's eye. The four colors of the Simon Says game act as accent colors and make it easier for the user to focus while offering a good accessibility rating against the chosen background color of Peach Crayola (#ECC19C). 

<details> 
  <summary>** Color pallette continued **</summary>
  <img src= "assets/img/readme-img/four-colors.png">
</details>

**Fonts**

The font Goudy Bookletter Lora was chosen from the Google Fonts database. The Sans Serif font style was added as a browser-safe font style.

<p align="right">(<a href="#about-the-project">back to top</a>)</p>


## Features

**Game Rules**

The game rules page is displayed first and contains the game discription that the user can learn. The brief and clear explanation offers a quick review of the game concept and its goal. The continue button below the game rules is designed to call for action and navigate the user to the game section. 

<details> 
  <summary> ** Game rules ** </summary>
  <img src="assets/img/readme-img/game-rules.jpeg"> 
</details>

**Game Section**

The game section visually mimics the classic look of the game with four buttons colored in red, blue, yellow, and green. The start button is placed on the top of the screen allowing the user to control the start of the game. The level indicator is set to 0 and located in the middle between the start button and the grid of four colored buttons.

<details> 
  <summary> ** Game section ** </summary>
  <img src= "assets/img/readme-img/game-section.jpeg">
</details>

**Playing Game**

The game starts after the user clicks the start button which gets replaced by a text message notifying the user to start repeating after Simon. The level indicator changes to level one. The turn is then passed to the user who has to repeat what Simon 'played' a moment ago. If the user clicks the required button, the game then moves to the next level. Starting from level two Simon continues to 'play' one button, however, the user has to first produce the level one button and then add the current level button. The game becomes more difficult with each level as more colors have to be memorized.

<details> 
  <summary> ** Playing game ** </summary>
  <img src= "assets/img/readme-img/playing-game.jpeg">
</details>

**Game Over**

The game is finished when the user clicks the wrong color button. The user is then notified that the game is over and the reset button appears for the user navigation back to the game rules page.

<details> 
  <summary> ** Game over ** </summary>
  <img src= "assets/img/readme-img/game-over.jpeg">
</details>

**Future Features**

I would like to improve usability by directing the user throughout a game cycle and providing extra guidance by the means of additional text, ie. identifying when it is Simon's turn and when it is time for user to step in; identifying how many clicks are left to complete the sequence.
I would like to implement a computer sequence replay for the user's turn.

**Responsiveness**

The Flexbox model was used to make the website responsive on all devices.

<p align="right">(<a href="#about-the-project">back to top</a>)</p>


## Deployment

This project was developed using GitPod, pushed to GitHub, and deployed to GitHub Pages using the following steps:
1. Log in to GitHub and locate the website creator GitHub Repository ANNAhabANNA/Simon-Says
2. At the top on the right-click Settings, scroll down to GitHub Pages and click to select
3. The website then gets built from the Main branch by default
4. The deployed website link [https://annahabanna.github.io/Simon-Says/](https://annahabanna.github.io/Simon-Says/) is then displayed on the top of the page.

<p align="right">(<a href="#about-the-project">back to top</a>)</p>


## Testing

**Validator Testing**

The game was tested using the tools of the World Wide Web Consortium (also known as W3C). The above-mentioned tools are the Markup Validation Service and the CSS Validation Service. No errors were returned for submitted HTML and CSS code.
Continuous testing was run using Lighthouse within Google Chrome to verify performance and accessibility standards were met and to ensure best practices were followed.
Javascript code was tested by using JShint Validator and no error or warnings were detected.

<details> 
  <summary> ** Lighthouse testing result ** </summary>
  <img src= "assets/img/readme-img/lighthouse-front.jpeg">
  <img src= "assets/img/readme-img/lighthouse-back.jpeg">
</details>


<details> 
  <summary> ** HTML validator result ** </summary>
  <img src= "assets/img/readme-img/html-validator.jpeg">
</details>

<details> 
  <summary> ** CSS validator result ** </summary>
  <img src= "assets/img/readme-img/css-validator.jpeg">
</details>

<details> 
  <summary> ** JShint validator result ** </summary>
  <img src= "assets/img/readme-img/jshint-validator.jpeg">
</details>

<p align="right">(<a href="#about-the-project">back to top</a>)</p>

**Manual Testing**

The game was tested manually across a range of devices to ensure all links and styling work correctly and to ensure responsiveness across a range of devices. All features on the page were tested to ensure functionality was not impacted. Testing was carried out on multiple browsers such as Google Chrome, Microsoft Edge, Mozilla Firefox, Safari, and Opera. Testing was carried out on an Apple iPhone, Apple iPhone 13, Samsung Galaxy S20 FE, Samsung Galaxy A51, Apple iPad Pro & Windows 10 Desktops. 

* Game Rules
    1. When the continue button is clicked it brings to the game section.
    2. The continue button is displayed fully for screen sizes smaller than 500px.
    3. Tested on various browsers and mobiles.

 * Playing Game
    1. The start game button initiates the game.
    2. The buttons are activated by clicking and audio accompanies each click.
    3. The level indicator changes accordingly to the successfully achieved level.
    4. Tested on various browsers and mobiles.
    
  * Game Over
    1. The game stops after the wrong color click.
    2. The reset button appears and navigates to the game rules page. 
    3. The level indicator displays the final level achieved.
    4. The text message changes to notify that the game is over.
 
**Bugs**

* The audio files did not play after buttons were clicked. The console displayed an unidentified audio path. My initial research focused on the javascript file path rules, but the issue was related to the audio function not being passed to nextSequence function.
* Chrome devtools identified a favicon error and reserch resulted in inserting
  ``` <link rel="icon" href="data:;base64,iVBORw0KGgo="> ```
  This solved the issue in Chrome, but the CSS validator produced a favicon warning. This was solved by inserting 
  ```   <link rel="shortcut icon" href="assets/img/favicon"> ```
* HTML validator identified an error with aria-label for divs. This was solved by applying aria-labelledby instead.
* JShint issued the following warnings: "template literal syntax' is only available in ES6 (use 'esversion: 6')" and "$ undefined variable". This was solved by inserting ``` /*jshint esversion: 6 */
/*globals $:false */```

<p align="right">(<a href="#about-the-project">back to top</a>)</p>

## Credits

**Frameworks, Libraries, and Tools**

* Am I Responsive - used to verify responsiveness of website on different devices.
* Figma - used to generate wireframe images.
* Chrome Dev Tools - used for overall development and tweaking, including testing responsiveness and performance.
* Font Awesome - used for social media and contact details icons in the footer and on the contact page.
* GitHub - used for version control and hosting.
* Google Fonts - used to import and alter website typography.
* Slack - used for support and advice from the Code Insitute Community.
* Coolors - used to create color palettes
* GitPod - used for automated dev environment
* W3C - Used for HTML & CSS Validation.
* Lighthouse - used for testing performance, accessibility, and search engine optimization.
* Color Safe - used for testing color contrast for better accessibility.
* jQuery - used for easier manipulation of HTML, event handling, animation.
 
**Audio**

* Audio effects for Simon Says buttons were downloaded at https://freesound.org/ from user Leszek Szary.

**Code/Content**

The following Youtube tutorials were used to assist my learning of game logic and coding solutions:

* [Recreating childhood: Simon Game](https://www.youtube.com/watch?v=ahGDFFAgKII)
* [Simon Game JavaScript Tutorial for Beginners](https://www.youtube.com/watch?v=n_ec3eowFLQ&t=2051s)
* [JavaScript Workshop: Simon Game](https://www.youtube.com/watch?v=FEL8gKaIm1Y)
* [Live Coding a Simon Game: HTML, CSS, Javascript](https://www.youtube.com/watch?v=W0MxUHlZo6U)

**Acknowledgment**

 * My Mentor Chris Quinn.
 * Code Institute team and community.

<p align="right">(<a href="#about-the-project">back to top</a>)</p>
