#pragma once
#include <iostream>
//SFML
#include "SFML\Graphics.hpp"
#include "SFML\Audio.hpp"
#include "SFML\Main.hpp"
#include "SFML\Network.hpp"
#include "SFML\System.hpp"
#include "SFML\Window.hpp"
#include "Animation.h"

class Player
{
public:
	Player(sf::Texture* texture, sf::Vector2u imageCount, float switchTime, float speed);
	~Player();

	//void T();
	void Update(float deltaTime);
	void Draw(sf::RenderWindow& window);
	//หลอดเลือด
	sf::Texture gauge;
	sf::Sprite hpbar;
	int MyHP = 5000;	//เลือดเริ่มต้น
	sf::RectangleShape HP;//เซตขนาดของหลอดเลือดที่ เป็นรูปสี่เหลี่ยม
	
	sf::Vector2f GetPosition() { return body.getPosition(); }
	sf::Vector2f Gethalfsize() { return body.getSize() / 2.0f; }
	void SetPosition(float x, float y) { body.setPosition(x, y); }
	sf::RectangleShape body;

private:
	Animation animation;
	unsigned int row;
	float speed;
	bool faceRight;
};