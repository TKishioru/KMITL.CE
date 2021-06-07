#include "Collision.h"


Collision::Collision()
{
	if (!this->llbuffer.loadFromFile("Sound/FX_pick.wav")) std::cout << "Error";
	this->ll.setBuffer(llbuffer);
	if (!this->mmbuffer.loadFromFile("Sound/witch.wav")) std::cout << "Error";
	this->mm.setBuffer(mmbuffer);
}

Collision::~Collision()
{
}

bool Collision::collisitem(Player* P, item* c)
{
	/*
	for (int i = 0; i < c->itemvector.size(); i++)
	{
		
		if ((abs(P->GetPosition().x - c->GetPosition(i).x) <= P->Gethalfsize().x + c->Gethalfsize(i).x)
			&& (abs(P->GetPosition().y - c->GetPosition(i).y) <= P->Gethalfsize().y + c->Gethalfsize(i).y))
		{
			std::cout << "colis item" << std::endl;
			c->SetPosition(i);//set
			this->ll.play();
		}
	}
	return 1;*/
	for (int i = 0; i < c->itemvector.size(); i++)
	if ((abs(P->GetPosition().x - c->GetPosition(i).x) <= P->Gethalfsize().x + c->Gethalfsize(i).x)
		&& (abs(P->GetPosition().y - c->GetPosition(i).y) <= P->Gethalfsize().y + c->Gethalfsize(i).y))
	{
		//std::cout << "colis item" << std::endl;
		c->SetPosition(i);//set
		this->ll.play();
		return 1;
	}
	else return 0;
}

bool Collision::collisboss(Player* P, Enemy* e)
{
	if ((abs(P->GetPosition().x - e->GetPosition().x) <= P->Gethalfsize().x + e->Gethalfsize().x)
		&& (abs(P->GetPosition().y - e->GetPosition().y) <= P->Gethalfsize().y + e->Gethalfsize().y))
	{
		//std::cout << "colis enemy" << std::endl;
		this->mm.play();
		return 1;
	}
	
	else return 0;
}

