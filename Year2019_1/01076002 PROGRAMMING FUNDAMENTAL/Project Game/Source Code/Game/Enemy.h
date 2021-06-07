#pragma once
#include "Animation.h"
class Enemy
{
public:
	Enemy(sf::Texture* texture, sf::Vector2u imageCount, float switchTime, float speed);
	~Enemy();
	void Update(float deltaTime);
	void Draw(sf::RenderWindow& window);

	int BossHP = 50000;
	sf::RectangleShape B_HP;

	sf::Vector2f GetPosition() { return body.getPosition(); }
	sf::Vector2f Gethalfsize() { return body.getSize() / 2.0f; }
	void SetPosition() { body.setPosition(1920.0f, 1080.0f); }
	int random();
	sf::RectangleShape body;
	float speed;
private:
	
	Animation animation;
	unsigned int row;
	//float speed;
	bool faceRight;
};