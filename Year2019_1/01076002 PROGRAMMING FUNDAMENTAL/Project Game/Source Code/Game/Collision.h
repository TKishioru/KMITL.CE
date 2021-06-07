#pragma once
#include<SFML/Graphics.hpp>
#include "Player.h"
#include "Item.h"
#include "Enemy.h"
#include <vector>

class Collision
{
public:
	sf::Sound ll;
	sf::SoundBuffer llbuffer;
	sf::Sound mm;
	sf::SoundBuffer mmbuffer;

	Collision();
	~Collision();
	bool collisitem(Player* P, item* c);
	bool collisboss(Player* P, Enemy* e);

private:


};