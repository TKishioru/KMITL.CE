#pragma once
#include<SFML/Graphics.hpp>
#include "Animation.h"

class item
{
public:
	item(sf::Texture* texture, sf::Vector2u imageCount, float switchTime, float speed);
	~item();
	void Update(float deltaTime);
	void Draw(sf::RenderWindow& window);
	float random();

	sf::Vector2f GetPosition(int i) { return itemvector[i].getPosition(); }
	sf::Vector2f Gethalfsize(int i) { return itemvector[i].getSize() / 2.0f; }
	void SetPosition(int i) {
		itemvector[i].setPosition(random(), 550.0f);
		std::cout << "set new Position" << std::endl;
	}
	std::vector<sf::RectangleShape> itemvector;

private:
	sf::RectangleShape Item;
	
	Animation animation;
	unsigned int row;
	float speed;
	bool faceRight;
};