#include "Enemy.h"

Enemy::Enemy(sf::Texture* texture, sf::Vector2u imageCount, float switchTime, float speed)
	:animation(texture, imageCount, switchTime)
{
	this->speed = speed;
	row = 0;
	faceRight = true;
	body.setSize(sf::Vector2f(200.0f, 300.0f));
	body.setOrigin(body.getSize() / 2.0f);
	body.setPosition(1200.f,600.f);
	body.setTexture(texture);
	body.setOrigin(25.0f, 25.0f);
}

Enemy::~Enemy()
{
}

void Enemy::Update(float deltaTime)
{
	sf::Vector2f movement(0.0f, 0.0f);
	switch (random())
	{
	case 1: if(GetPosition().x > 50)
			movement.x -= speed * deltaTime;
			faceRight = false;
		break;
	case 2:if (GetPosition().y > 50)
			movement.y -= speed  * deltaTime;
		break;
	case 3:if (GetPosition().x < 1850)
			movement.x += speed * deltaTime;
			faceRight = true;
		break;
	case 4:if (GetPosition().y < 950)
			movement.y += speed * deltaTime;
		break;
	}
	/*
	if (movement.x == 0.0f && movement.y == 0.0f)
	{
		row = 0;
	}
	else
	{
		row = 1;
		if (movement.x > 0.0f)
			faceRight = true;
		else
			faceRight = false;
		if (movement.y != 0.0f) faceRight = true;
	}
	*/
	B_HP.setPosition(sf::Vector2f(body.getPosition().x + 10, body.getPosition().y - 50));//เซตตำแหน่งของหลอดเลือด
	B_HP.setFillColor(sf::Color::Color(255, 145, 0));//เซตสีของเลือด
	B_HP.setSize(sf::Vector2f(BossHP / 500, 10));//กำหนด size
	
	animation.Update(row, deltaTime, faceRight);
	body.setTextureRect(animation.uvRect);
	body.move(movement);
}

void Enemy::Draw(sf::RenderWindow& window)
{
	window.draw(B_HP);
	window.draw(body);
}

int Enemy::random()
{
	int random[4] = {1,2,3,4};
	int x;
	srand(time(NULL));
	x = rand() % 4;
	return random[x];
}
