# Snake Game
Developer :  Rudraksh Charhate

## Overview
This project is a classic implementation of the Snake game using Pygame. In this game, the player controls a snake that grows in length as it eats food. The goal is to achieve the highest score possible without the snake colliding with the walls or itself.

## Features
<ul>
  <li>Home Screen: A welcoming screen with instructions on how to start the game.</li>
  <li>Game Loop: The main game where the snake moves, eats food, and grows.</li>
  <li>Game Over Screen: Displays the player's score and an option to restart the game.</li>
  <li>Pause Functionality: The game can be paused by pressing the spacebar.</li>
  <li>High Score Management: The game keeps track of the highest score achieved.</li>
</ul>

## Controls
<ul>
  <li>Arrow Keys: Move the snake in the respective direction (up, down, left, right).</li>
  <li>Spacebar: Pause the game.</li>
  <li>Right Shift: Start the game from the home screen.</li>
  <li>Enter: Restart the game from the game over screen.</li>
</ul>

## Installation
1. Install Python from the official website.
2. Install Pygame by running the following command: pip install pygame

## How to run
1. Ensure all the required images (welcome.jpg and gameover.png) and sound files (crash.mp3, bite.mp3, eat.mp3) are in the same directory as the script.
2. Run the script: python main.py

## File Structure
<ul>
  <li>snake_game.py: Main script containing the game logic.</li>
  <li>welcome.jpg: Image for the home screen.</li>
  <li>gameover.png: Image for the game over screen.</li>
  <li>crash.mp3: Sound played when the snake collides with the wall.</li>
  <li>bite.mp3: Sound played when the snake collides with itself.</li>
  <li>eat.mp3: Sound played when the snake eats food.</li>
  <li>highscore.txt: File to store the high score.</li>
</ul>

## Future Improvements
<ul>
  <li>Add more levels with increasing difficulty.</li>
  <li>Implement a more sophisticated collision detection system.</li>
  <li>Add more sound effects and background music.</li>
  <li>Create a graphical interface for setting game preferences.</li>
</ul>

Feel free to customize and enhance the game as per your preferences. Enjoy coding and have fun playing the Snake game!
