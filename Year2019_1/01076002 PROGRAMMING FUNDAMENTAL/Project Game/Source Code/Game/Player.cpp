#include<SFML\Graphics.hpp>
#include<iostream>
#include "Player.h"

Player::Player(sf::Texture* texture, sf::Vector2u imageCount, float switchTime, float speed):
animation(texture, imageCount, switchTime)
{
	this->speed = speed;
	row = 0;
	faceRight = true;

	body.setSize(sf::Vector2f(200.0f, 300.0f));
	body.setOrigin(body.getSize() / 2.0f);
	body.setPosition(206.0f, 600.0f);
	//body.setPosition(0.0f, 0.0f);
	body.setTexture(texture);
}
Player::~Player()
{

}
/*
void Player::T()
{
	body.setPosition(206.0f, 600.0f);
}*/

void Player::Update(float deltaTime)
{
	if (!this->gauge.loadFromFile("Picture/P_HP.png")) std::cout << "Could not load fontTexture";
	hpbar.setTexture(gauge);
	hpbar.setPosition(body.getPosition().x-900, 800);//เซตตำแหน่งของรูปภาพ
	sf::Vector2f movement(0.0f, 0.0f);
	//Input Keyboard
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::A) || sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
	{
		if (GetPosition().x > 0)
		{
			movement.x -= speed * deltaTime;
			faceRight = true;
		}
	}
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::D) || sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
	{
		if (GetPosition().x < 1920)
		{
			movement.x += speed * deltaTime;
			faceRight = false;
		}
	}
	/*
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::W))
	{
		if (GetPosition().y > 0)
		{
			movement.y -= speed * deltaTime;
			faceRight = false;
		}
	}
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::S))
	{
		if (GetPosition().x < 720)
		{
			movement.y += speed * deltaTime;
			faceRight = false;
		}
	}
	
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Space))
	{
		movement.y = -1.0f;	//กระโดดแต่ยังไม่มีการลง
	}*/
	/* ถ้าใส่โค้ดนี้จะทำให้ภาพกระตุก เนื่องจากมีรูปแถวเดียว
	if (movement.x == 0.0f)
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
	}
	*/

	/*
	HP.setPosition(sf::Vector2f(body.getPosition().x - 675, 895));//เซตตำแหน่งของหลอดเลือด
	HP.setFillColor(sf::Color::Color(153, 255, 153));//เซตสีของเลือด
	HP.setSize(sf::Vector2f(MyHP / 200, 20));//กำหนด size
	
	MP.setPosition(sf::Vector2f(body.getPosition().x - 675, 935));
	MP.setFillColor(sf::Color::Color(153, 230, 255));
	MP.setSize(sf::Vector2f(MyMP / 200, 20));
	*/
	HP.setPosition(sf::Vector2f(body.getPosition().x - 675, 920));//เซตตำแหน่งของหลอดเลือด
	HP.setFillColor(sf::Color::Color(153, 255, 153));//เซตสีของเลือด
	HP.setSize(sf::Vector2f(MyHP / 20, 20));//กำหนด size
	animation.Update(row, deltaTime, faceRight);
	body.setTextureRect(animation.uvRect);
	body.move(movement);
}

void Player::Draw(sf::RenderWindow& window)
{
	window.draw(hpbar);
	window.draw(HP);
	//window.draw(MP);
	window.draw(body);
}