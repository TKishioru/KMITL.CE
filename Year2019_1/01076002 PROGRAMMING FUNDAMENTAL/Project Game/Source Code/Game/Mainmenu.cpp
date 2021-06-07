#include "Mainmenu.h"

void Mainmenu::T()
{
	this->bgmain.setPosition(-900.0f, 0.f);
	std::cout << "PP" << std::endl;
}

Mainmenu::Mainmenu(sf::RenderWindow& window)
{
	if (!this->font.loadFromFile("Fonts/Sarun_s.ttf")) std::cout << "Could not load fontTexture";
	if (!this->bgmainTexture.loadFromFile("Picture/B_mainBG.png")) std::cout << "Could not load bgmainTexture";
	if (!this->button.loadFromFile("Picture/B_button.png")) std::cout << "Could not load button";
	//Sound

	this->gotostate = 0;
	this->buttonState = BTN_IDLE;
	this->bgmain.setTexture(&this->bgmainTexture);
	this->bgmain.setSize(sf::Vector2f(window.getSize()));
	this->bgmain.setPosition(-760.0f, 0.f);
	//this->bgmain.setFillColor(sf::Color::Black);
	for (int i = 0; i < 5; i++)
	{
		this->menu[i].setCharacterSize(48);
		this->shape[i].setTexture(&this->button);
	}
	this->mousePosview = sf::Vector2f(0.0f, 0.0f);
	this->idleColor = sf::Color(100, 100, 100, 200);
	this->hoverColor = sf::Color(150, 150, 150, 255);
	this->activeColor = sf::Color(20, 20, 20, 200);

	this->shape[0].setPosition(sf::Vector2f(1200, 430));
	this->shape[0].setSize(sf::Vector2f(400, 100));
	//this->shape[0].setFillColor(this->idleColor);
	this->menu[0].setFont(this->font);
	this->menu[0].setString("Play");
	this->menu[0].setFillColor(sf::Color::Magenta);
	this->menu[0].setPosition(sf::Vector2f(
		this->shape[0].getPosition().x + (this->shape[0].getGlobalBounds().width / 2.f) - this->menu[0].getGlobalBounds().width / 2.f,
		this->shape[0].getPosition().y + (this->shape[0].getGlobalBounds().height / 2.f) - this->menu[0].getGlobalBounds().height / 2.f
	));

	this->shape[1].setPosition(sf::Vector2f(1200, 530));
	this->shape[1].setSize(sf::Vector2f(400, 100));
	//this->shape[1].setFillColor(this->idleColor);
	this->menu[1].setFont(this->font);
	this->menu[1].setString("How to play");
	this->menu[1].setFillColor(sf::Color::White);
	this->menu[1].setPosition(sf::Vector2f(
		this->shape[1].getPosition().x + (this->shape[1].getGlobalBounds().width / 2.f) - this->menu[1].getGlobalBounds().width / 2.f,
		this->shape[1].getPosition().y + (this->shape[1].getGlobalBounds().height / 2.f) - this->menu[1].getGlobalBounds().height / 2.f
	));

	this->shape[2].setPosition(sf::Vector2f(1200, 630));
	this->shape[2].setSize(sf::Vector2f(400, 100));
	//this->shape[2].setFillColor(this->idleColor);
	this->menu[2].setFont(this->font);
	this->menu[2].setString("High Score");
	this->menu[2].setFillColor(sf::Color::White);
	this->menu[2].setPosition(sf::Vector2f(
		this->shape[2].getPosition().x + (this->shape[2].getGlobalBounds().width / 2.f) - this->menu[2].getGlobalBounds().width / 2.f,
		this->shape[2].getPosition().y + (this->shape[2].getGlobalBounds().height / 2.f) - this->menu[2].getGlobalBounds().height / 2.f
	));

	this->shape[3].setPosition(sf::Vector2f(1200, 730));
	this->shape[3].setSize(sf::Vector2f(400, 100));
	//this->shape[3].setFillColor(this->idleColor);
	this->menu[3].setFont(this->font);
	this->menu[3].setString("Credit");
	this->menu[3].setFillColor(sf::Color::White);
	this->menu[3].setPosition(sf::Vector2f(
		this->shape[3].getPosition().x + (this->shape[3].getGlobalBounds().width / 2.f) - this->menu[3].getGlobalBounds().width / 2.f,
		this->shape[3].getPosition().y + (this->shape[3].getGlobalBounds().height / 2.f) - this->menu[3].getGlobalBounds().height / 2.f
	));

	this->shape[4].setPosition(sf::Vector2f(1200, 830));
	this->shape[4].setSize(sf::Vector2f(400, 100));
	//this->shape[4].setFillColor(this->idleColor);
	this->menu[4].setFont(this->font);
	this->menu[4].setString("Quit");
	this->menu[4].setFillColor(sf::Color::White);
	this->menu[4].setPosition(sf::Vector2f(
		this->shape[4].getPosition().x + (this->shape[4].getGlobalBounds().width / 2.f) - this->menu[4].getGlobalBounds().width / 2.f,
		this->shape[4].getPosition().y + (this->shape[4].getGlobalBounds().height / 2.f) - this->menu[4].getGlobalBounds().height / 2.f
	));
}

void Mainmenu::Update(sf::RenderWindow& window)
{
	this->mousePosview = window.mapPixelToCoords(sf::Mouse::getPosition(window));
	this->gotostate = 0;

	for (int i = 0; i < 5; i++)
	{
		this->shape[i].setFillColor(this->idleColor);
		if (this->shape[i].getGlobalBounds().contains(this->mousePosview))
		{
			this->shape[i].setFillColor(this->hoverColor);
			if (sf::Mouse::isButtonPressed(sf::Mouse::Left))
			{
				this->shape[i].setFillColor(this->activeColor);
				this->gotostate = i + 1;

			}
		}
	}

}

void Mainmenu::Draw(sf::RenderWindow& window)
{
//	T();
	this->bgmain.setPosition(0.f, 0.f);
	window.draw(this->bgmain);
	for (int i = 0; i < 5; i++)
	{
		window.draw(this->shape[i]);
		window.draw(this->menu[i]);
	}
}
