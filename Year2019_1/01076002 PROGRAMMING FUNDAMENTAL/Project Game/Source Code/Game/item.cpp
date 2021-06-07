#include<SFML/Graphics.hpp>
#include "item.h"

item::item(sf::Texture* texture, sf::Vector2u imageCount, float switchTime, float speed)
	:animation(texture, imageCount, switchTime)
{
	this->speed = speed;
	row = 0;
	faceRight = true;

	Item.setSize(sf::Vector2f(50.f, 60.f));
	Item.setTexture(texture);
	
	itemvector.push_back(sf::RectangleShape(Item));
	for (int i = 0; i < itemvector.size(); i++)
	{
		itemvector[i].setPosition(random(), 550.0f);
	}
}

item::~item()
{
}

void item::Update(float deltaTime)
{
	animation.Update(row, deltaTime, faceRight);
	for (int i = 0; i < itemvector.size(); i++)
	{
		itemvector[i].setTextureRect(animation.uvRect);
	}
}

void item::Draw(sf::RenderWindow& window)
{
	for (int i = 0; i < itemvector.size(); i++)
	{
		window.draw(itemvector[i]);
	}
}

float item::random()
{
	float random[7] = { 12,152,559,956,489,879,618 };
	int x;
	srand(time(NULL));
	x = rand() % 7;
	return random[x];
}
