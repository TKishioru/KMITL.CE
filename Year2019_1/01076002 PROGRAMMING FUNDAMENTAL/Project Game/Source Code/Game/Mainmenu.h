#pragma once
#ifndef  MAINMENU_H
#define MAINMENU_H
#include <iostream>
//SFML
#include "SFML\Graphics.hpp"
#include "SFML\Audio.hpp"
#include "SFML\Main.hpp"
#include "SFML\Network.hpp"
#include "SFML\System.hpp"
#include "SFML\Window.hpp"

enum button_states { BTN_IDLE = 0, BTN_HOVER, BTN_PRESSED, BTN_ACTIVE };
class Mainmenu
{
public:

	void T();
	short unsigned buttonState;
	sf::RectangleShape bgmain;
	sf::Texture bgmainTexture;
	sf::Texture button;

	sf::Vector2f mousePosview;
	sf::Color idleColor;
	sf::Color hoverColor;
	sf::Color activeColor;

	sf::RectangleShape shape[5];
	sf::Font font;
	sf::Text menu[5];

	int gotostate;
	//Constructor
	Mainmenu(sf::RenderWindow& window);
	//Fuctions
	void Update(sf::RenderWindow& window);
	void Draw(sf::RenderWindow& window);
};
#endif;