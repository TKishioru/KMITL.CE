#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <sstream>
#include <math.h>
#include <fstream>
//SFML
#include "SFML\Graphics.hpp"
#include "SFML\Audio.hpp"
#include "SFML\Main.hpp"
#include "SFML\Network.hpp"
#include "SFML\System.hpp"
#include "SFML\Window.hpp"
//Class Make
#include "Mainmenu.h"
#include "Player.h"
#include "item.h"
#include "Collision.h"
#include "Enemy.h"
static const float VIEW_HEIGHT = 1080.0f;
const int State_mainmenu = 0;
const int State_play = 1;
const int State_howtoplay = 2;
const int State_score = 3;
const int State_credit = 4;
const int State_quit = 5;
const int State_Input = 6;
const int State_End = 7;
int State = State_mainmenu;
int Pastcheck = 0;

//แถบค่าพลัง
int MyHP = 5000;
int GHP = 5000;
int PHP = 0;
int BHP = 0;
int GameScore = 0;
int bossblood = 50000;
void ResizeView(const sf::RenderWindow& window, sf::View& view)
{
	float aspectRatio = float(window.getSize().x) / float(window.getSize().y);
	view.setSize(VIEW_HEIGHT * aspectRatio, VIEW_HEIGHT);

}
void mousePositionShow(sf::RenderWindow* window)
{
	sf::Vector2f mousePosition;
	std::stringstream position;
	sf::Text mousePosition_text;
	sf::Font fontP;
	fontP.loadFromFile("Fonts/arial.ttf"); //// <- Enter font here
	mousePosition_text.setCharacterSize(15);
	mousePosition_text.setFillColor(sf::Color::White);
	mousePosition_text.setFont(fontP);

	mousePosition = window->mapPixelToCoords(sf::Mouse::getPosition(*window));
	mousePosition_text.setPosition(mousePosition.x, mousePosition.y + 75);
	position << mousePosition.x << " , " << mousePosition.y;
	mousePosition_text.setString(position.str());

	window->draw(mousePosition_text);
}
class Flame
{
public:
	  sf::CircleShape shape;
	  sf::Vector2f currVelocity;
	  float maxSpeed;
	  Flame(float radius = 5.0f) :currVelocity(0.0f, 0.0f), maxSpeed(20.0f)
	  {
		  this->shape.setRadius(radius);
	  }
	  
};
void readTextFile(sf::RenderWindow& window)
{
	sf::Font font;
	font.loadFromFile("Fonts/Sarun_s.ttf");

	sf::Text scoreText;
	sf::Text rankText;
	sf::Text nameText;
	
	scoreText.setFont(font);
	rankText.setFont(font);
	nameText.setFont(font);

	scoreText.setCharacterSize(40.0f);
	rankText.setCharacterSize(40.0f);
	nameText.setCharacterSize(40.0f);
	std::ifstream file("HighScore.ini");
	if (file)
	{
		std::string rank = "";
		std::string name = "";
		std::string score = "";
		while (file >> rank >> name >> score)
		{
			int r = stoi(rank);

			rankText.setString(rank);
			nameText.setString(name);
			scoreText.setString(score);

			/*setPosition */
			rankText.setPosition(600.0f,250.0f+(80*r));
			nameText.setPosition(750.0f, 250.0f + (80 * r));
			scoreText.setPosition(1250.0f, 250.0f + (80 * r));

			window.draw(rankText);
			window.draw(nameText);
			window.draw(scoreText);
		}
	}
	else
	{
		std::cout << "can't open FileText" << std::endl;
	}
	file.close();

}
void sort(std::string input,int Sscore)
{
	std::ifstream file("HighScore.ini");

	std::vector<int> RANK;
	std::vector<std::string> NAME;
	std::vector<int> SCORE;
	
	if (file)
	{
		std::string rank = "";
		std::string name = "";
		std::string score = "";

		while (file >> rank >> name >> score)
		{
			int r = stoi(rank);
			int s = stoi(score);
			
			RANK.push_back(r);
			NAME.push_back(name);
			SCORE.push_back(s);
		}
		std::cout << "step 1 " << std::endl;
	}
	else  		        
		std::cout << "Can open file" << std::endl;
	file.close();

	for (int i = 0; i < SCORE.size(); i++)
	{
		if (Sscore > SCORE[i])
		{
			SCORE.insert(SCORE.begin() + i, Sscore);
			NAME.insert(NAME.begin() + i, input);
			break;
		}
		else if(Sscore == SCORE[i])
		{
			SCORE.insert(SCORE.begin() + 1+i, Sscore);
			NAME.insert(NAME.begin() + 1+i, input);
			break;
		}
		else if (i + 1 == SCORE.size())
		{
			break;
		}
	}
	
	if (SCORE.size() == 6)
	{
		SCORE.erase(SCORE.end() - 1);
		NAME.erase(NAME.end() - 1);
	}

	std::ofstream of("HighScore.ini");
	if (of)
	{
		for (int i = 0; i < SCORE.size(); i++)
		{
			of << RANK[i] << " " << NAME[i] << " " << SCORE[i] << std::endl;
		}
		std::cout << "step 2 " << std::endl;
	}
	else	std::cout << "can't Open file";
	
	of.close();
	RANK.clear();
	NAME.clear();
	SCORE.clear();
}

int main()
{
	sf::RenderWindow window(sf::VideoMode(1920, 1080), "MAOU GAME", sf::Style::Titlebar | sf::Style::Close | sf::Style::Resize);
	sf::View view(sf::Vector2f(0.0f, 0.0f), sf::Vector2f(VIEW_HEIGHT, VIEW_HEIGHT));
	view.setSize(1920, 1080);
	window.setFramerateLimit(60);

	sf::Texture playerTexture;
	playerTexture.loadFromFile("Picture/P_player.png");
	Player player(&playerTexture, sf::Vector2u(2, 1), 0.1f, 350.f);
	Collision colis;		//การชน

	//enemy
	sf::Texture moveAK;
	moveAK.loadFromFile("Picture/P_flame.png");
	sf::RectangleShape enemy;
	int enemyBlood = 50;
	std::vector<int> enemyBloodVector;
	std::vector<sf::RectangleShape> enemyVector;
	enemy.setSize(sf::Vector2f(90.0f, 90.0f));
	enemy.setTexture(&moveAK);
	int enemyCounter = 0;
	int enemySpawnTime = 40;
	std::vector<bool> setPosvector;
	setPosvector.push_back(bool());
	for (int i = 0; i < setPosvector.size(); i++)
	{
		setPosvector[i] = true;
	}
	
	Animation animation(&moveAK, sf::Vector2u(3, 1), 0.3f);
	
	sf::Texture BossTexture;
	BossTexture.loadFromFile("Picture/P_boss.png");
	Enemy Boss(&BossTexture, sf::Vector2u(2, 1), 0.1f, 50.f);
	//Item
	sf::Texture itemTexture;
	itemTexture.loadFromFile("Picture/P_item.png");	
    item Item(&itemTexture, sf::Vector2u(1, 1), 0.1f, 50.f);

	//แถบเมนู
	Mainmenu menu(window);
	sf::RectangleShape stateM1(sf::Vector2f(1920.f, 1080.f));
	sf::Texture M_howtoplay;
	M_howtoplay.loadFromFile("howtoplay.png");	//ชื่อไฟล์ภาพ
	stateM1.setPosition(0.0f, -80.f);
	stateM1.setTexture(&M_howtoplay);
	sf::RectangleShape stateM2(sf::Vector2f(1920.f, 1080.f));
	sf::Texture M_score;
	M_score.loadFromFile("score.png");	//ชื่อไฟล์ภาพ
	stateM2.setPosition(0.0f, -80.f);
	stateM2.setTexture(&M_score);
	sf::RectangleShape stateM3(sf::Vector2f(1920.f, 1080.f));
	sf::Texture M_credit;
	M_credit.loadFromFile("credit.png");	//ชื่อไฟล์ภาพ
	stateM3.setPosition(0.0f, -80.f);
	stateM3.setTexture(&M_credit);
	sf::RectangleShape stateM4(sf::Vector2f(1920.f, 1080.f));
	sf::Texture M_end;
	M_end.loadFromFile("gameover.png");	//ชื่อไฟล์ภาพ
	stateM4.setPosition(0.0f, -80.f);
	stateM4.setTexture(&M_end);
	/*
	//อาจจะ error ตอนตั้งพร้อมกับ cursor รอแก้ไข
	//Icon Window
	sf::Image Icon;
	Icon.loadFromFile("cursor2.png");
	window.setIcon(480, 480, Icon.getPixelsPtr());
	*/

	//ทำเคอเซอร์เป็นรูปภาพ
	sf::Cursor cursor;
	sf::Image image_cursor;
	image_cursor.loadFromFile("Picture/cursor.png");

	if (cursor.loadFromPixels(image_cursor.getPixelsPtr(), image_cursor.getSize(), { 1, 1 }))
	{
		window.setMouseCursor(cursor);
		std::cout << "Cursor complete" << std::endl;
	}
	else std::cout << "Cursor non-complete" << std::endl;

	//ติดตั้งพื้นหลัง (Not Loop)
	sf::Texture BG1;
	BG1.loadFromFile("Input.png");
	sf::RectangleShape Background1(sf::Vector2f(1920.0f, 1080.0f));
	Background1.setPosition(0,-80);
	Background1.setTexture(&BG1);

	//ติดตั้งพื้นหลัง (Loop)
	sf::Texture background_1texture, background_2texture, background_3texture, background_4texture;
	//สร้าง Texture โหลดไฟล์รูป ซึ่งเราจะนำทั้ง 3 รูปมาทับซ้อนกัน
	background_1texture.loadFromFile("Picture/B_moon.png");
	background_2texture.loadFromFile("Picture/B_Stars.png");
	background_3texture.loadFromFile("Picture/B_stateG.png");
	background_4texture.loadFromFile("Picture/B_BackG.png");
	sf::Sprite background_1, background_2, background_3, background_4;
	//สร้าง Sprite และ Set Texture ให้กับ Sprite 
	background_1.setTexture(background_1texture);
	background_2.setTexture(background_2texture);
	background_3.setTexture(background_3texture);
	background_4.setTexture(background_4texture);
	//Set Origin ให้ Background ให้อยู่ตรงกลางของ View;
	background_1.setOrigin(960.f, 540.f);
	background_2.setOrigin(960.f, 540.f);
	background_3.setOrigin(960.f, 540.f);
	background_4.setOrigin(960.f, 540.f);

	//Loop BG
	//view.setCenter(player.GetPosition()); //set View ตาม player
	view.setCenter(player.GetPosition().x, player.GetPosition().y);
	window.setView(view); //set View ให้
	//set background ให้ตาม player
	background_1.setPosition(player.GetPosition());
	background_2.setPosition(player.GetPosition());
	background_3.setPosition(player.GetPosition());
	background_4.setPosition(player.GetPosition());
	background_1.setTextureRect(sf::IntRect(view.getCenter().x * 1, 0, 1920, 1080));
	background_2.setTextureRect(sf::IntRect(view.getCenter().x * 0.5, 0, 1920, 1080));
	background_3.setTextureRect(sf::IntRect(view.getCenter().x * 0.2, 0, 1920, 1080));
	background_4.setTextureRect(sf::IntRect(view.getCenter().x * 0.8, 0, 1920, 1080));
	background_1texture.setRepeated(true);
	background_2texture.setRepeated(true);
	background_3texture.setRepeated(true);
	background_4texture.setRepeated(true);

	//snow
	sf::CircleShape whitecircle;
	whitecircle.setRadius(6);
	whitecircle.setFillColor(sf::Color::White);
	std::vector<sf::CircleShape> snow;
	srand(time(NULL));
	
	for (int i = 0; i < 50; i++) {
		snow.push_back(sf::CircleShape(whitecircle));
		snow.back().setPosition(rand() % 1920, rand() % 1080);
		snow.back().setFillColor(sf::Color(255, 255, 255, rand() % 100 + 150));
	}

	//ยิง
	sf::Texture bul;
	if (!bul.loadFromFile("Picture/P_Bullet.png"))
	{
		std::cout << "Can't load" << std::endl;
	}
	bul.setRepeated(true);
	sf::Vector2f playerCenter, mousePos, aimDir;
	Flame f;
	f.shape.setTexture(&bul);
	std::vector<Flame> flame;
	/*flame.push_back(Flame(f));*/

	//Input Text
	sf::RectangleShape object;
	object.setSize(sf::Vector2f(300.0f, 70.0f));
	object.setOrigin(sf::Vector2f(0.0f, 35.0f));
	object.setPosition(sf::Vector2f(800, 600.0f));

	sf::RectangleShape textcursor;
	textcursor.setSize(sf::Vector2f(5.0f, 64.0f));
	textcursor.setOrigin(sf::Vector2f(2.5f, 32.0f));
	textcursor.setPosition(sf::Vector2f(805, 600.0f));
	textcursor.setFillColor(sf::Color::Black);
	bool state = false;
	char last_char = ' ';
	
	std::string input;
	sf::Font font;
	
	font.loadFromFile("Fonts/2005_iannnnnHBO.ttf"); //// <- Enter font here
	sf::Text text, Outtext,Showtext,bloodtext;
	text.setFont(font);
	text.setCharacterSize(40);
	text.setFillColor(sf::Color::Black);
	text.setPosition(810, 570);
	//ติดตั้งเสียง BackgroudSound
	sf::Music music;
	if (!music.openFromFile("Sound/MagicForest.ogg")) std::cout << "could not load music" << std::endl;
	music.setLoop(true);
	music.setVolume(100);
	music.play();

	float totalTime = 0;
	bool Inputstate = false;
	
	//Time
	float deltaTime = 0.0f;
	sf::Clock clock;

	sf::Clock timegame;
	float runHpMp = 0.0f;

	while (window.isOpen())
	{
		deltaTime = clock.restart().asSeconds();
		runHpMp = timegame.restart().asSeconds();
		sf::Event event;

		while (window.pollEvent(event))
		{
			switch (event.type)
			{
			case sf::Event::Closed:	//ปิดหน้าต่าง
				window.close();
				break;
			}
		}

		if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Escape))
			window.close();	//ปิดหน้าต่าง
		
		//ทำหิมะตก
		for (int i = 0; i < 50; i++) {
			snow[i].move(0, 60 * deltaTime);
			if (snow[i].getPosition().y > 1080) {
				snow[i].setPosition(rand() % 1920, 0);
			}
		}

		//CHECK STATE
		

		if (State == State_play)
		{
			if (Pastcheck == 0)
			{
				window.clear(sf::Color(0, 0, 0, 50));
				totalTime += clock.restart().asSeconds();
				if (totalTime >= 0.5f)
				{
					totalTime = 0;
					Inputstate = !Inputstate;
				}
				if (Inputstate == true)
				{
					window.draw(textcursor);
				}
				if (event.type == sf::Event::EventType::TextEntered)
				{
					if (last_char != event.text.unicode && event.text.unicode == 8 &&
						input.length() > 0) // delete
					{
						last_char = event.text.unicode;
						input.erase(input.length() - 1);
						text.setString(input);
						textcursor.setPosition(960.0f + text.getGlobalBounds().width + 5, 600.0f);
						//std::cout << input << std::endl;
					}
					if (last_char != event.text.unicode &&
						(event.text.unicode >= 'a' && event.text.unicode <= 'z' ||
							event.text.unicode >= 'A' && event.text.unicode <= 'Z' ||
							event.text.unicode >= '0' && event.text.unicode <= '9'))
					{
						//std::cout << event.text.unicode << std::endl;
						last_char = event.text.unicode;
						input += event.text.unicode;
						text.setString(input);
						textcursor.setPosition(960.0f + text.getGlobalBounds().width + 5, 600.0f);
						std::cout << input << std::endl;
					}
				}
				if (event.type == sf::Event::EventType::KeyReleased && last_char != ' ')
				{
					last_char = ' ';
				}
				//Input Text
				window.draw(Background1);
				window.setView(window.getDefaultView());
				window.draw(object);
				if (Inputstate == true)
					window.draw(textcursor);				
				window.draw(text);
				window.display();
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Enter) && input.length() > 0)
					Pastcheck = 1;
			}

			if (Pastcheck == 1)
			{
				playerCenter = sf::Vector2f(player.GetPosition().x, player.GetPosition().y);
				mousePos = sf::Vector2f(sf::Mouse::getPosition(window));
				aimDir = mousePos - playerCenter;
				aimDir = aimDir / sqrt(pow(aimDir.x, 2) + pow(aimDir.y, 2));
				player.Update(deltaTime);
				Boss.Update(deltaTime);
				Item.Update(deltaTime);
				if ((runHpMp > 10000.f) == 0.f)
				{
					if (MyHP < 5000)
					{
						MyHP += 1;
						PHP -= 1;
					}
					runHpMp = timegame.restart().asSeconds();
				}
				//score
				std::string mytext,yourS,GaugeS;
				Outtext.setFont(font);
				Outtext.setFillColor(sf::Color::White);
				Outtext.setStyle(sf::Text::Bold);
				Outtext.setCharacterSize(60);
				Outtext.setPosition(player.GetPosition().x + 600, 900);
				mytext = "Score : " + std::to_string(GameScore);
				Outtext.setString(mytext);

				Showtext.setFont(font);
				Showtext.setFillColor(sf::Color::White);
				Showtext.setStyle(sf::Text::Bold);
				Showtext.setCharacterSize(60);
				Showtext.setPosition(950, 450);
				yourS = std::to_string(GameScore);
				Showtext.setString(yourS);
				
				bloodtext.setFont(font);
				bloodtext.setFillColor(sf::Color::White);
				bloodtext.setStyle(sf::Text::Bold);
				bloodtext.setCharacterSize(36);
				bloodtext.setPosition(player.GetPosition().x - 600.f, 930.f);
				GaugeS = std::to_string(MyHP) + " / 5000";
				bloodtext.setString(GaugeS);

				//Loop BG
				//view.setCenter(player.GetPosition()); //set View ตาม player
				window.setView(view); //set View ให้
				//set background ให้ตาม player
				background_1.setPosition(player.GetPosition());
				background_2.setPosition(player.GetPosition());
				background_3.setPosition(player.GetPosition());
				background_4.setPosition(player.GetPosition());
				background_1.setTextureRect(sf::IntRect(view.getCenter().x * 1, 0, 1920, 1080));
				background_2.setTextureRect(sf::IntRect(view.getCenter().x * 0.5, 0, 1920, 1080));
				background_3.setTextureRect(sf::IntRect(view.getCenter().x * 0.2, 0, 1920, 1080));
				background_4.setTextureRect(sf::IntRect(view.getCenter().x * 0.8, 0, 1920, 1080));
				background_1texture.setRepeated(true);
				background_2texture.setRepeated(true);
				background_3texture.setRepeated(true);
				background_4texture.setRepeated(true);

				if (enemySpawnTime < 40) enemySpawnTime++;
				if (enemySpawnTime >= 40 && enemyCounter < 20)
				{
					enemyVector.push_back(sf::RectangleShape(enemy));
					enemyBloodVector.push_back(int(enemyBlood));
					setPosvector.push_back(bool());
					enemyCounter++;
					
					enemySpawnTime = 0;
				}
				for (int i = 0; i < enemyVector.size(); i++)
				{
					if (setPosvector[i]) {
						enemyVector[i].setPosition(rand() % 1920, rand() % 1080);
						setPosvector[i] = false;
					}
				}
				
				//ยิง
				if (sf::Mouse::isButtonPressed(sf::Mouse::Left))
				{
					
					f.shape.setPosition(playerCenter);
					f.currVelocity = aimDir * f.maxSpeed;
					flame.push_back(Flame(f));
				}

				for (size_t i = 0; i < flame.size(); i++)
				{
					flame[i].shape.move(flame[i].currVelocity);
					if (flame[i].shape.getPosition().x > window.getSize().x
						|| flame[i].shape.getPosition().y > window.getSize().y
						|| flame[i].shape.getPosition().x < 0
						|| flame[i].shape.getPosition().y < 0)
					{
						flame.erase(flame.begin() + i);
						continue;
					}
					for (int j = 0; j < enemyVector.size(); j++) {
						if (flame[i].shape.getGlobalBounds().intersects(enemyVector[j].getGlobalBounds()))
						{
							GameScore += 1;
							enemyBloodVector[j] -= 10;
							//flame.erase(flame.begin() + i);

							if (enemyBloodVector[j] == 0) {
								enemyVector.erase(enemyVector.begin() + j);
								enemyBloodVector.erase(enemyBloodVector.begin() + j);
								setPosvector[j] = true;
								enemyCounter--;
							}
							continue;
						}
						//ถ้าลูกไฟ อยู่ติดกับตัวละครแล้วยิงจะเสียเลือด
						/*if (player.body.getGlobalBounds().intersects(enemyVector[j].getGlobalBounds()))
						{
							MyHP -= 20;
							PHP += 20;
							std::cout << "P-E collis" << std::endl;
							enemyBloodVector[j] -= 10;
							//flame.erase(flame.begin() + i);

							if (enemyBloodVector[j] == 0) {
								enemyVector.erase(enemyVector.begin() + j);
								enemyBloodVector.erase(enemyBloodVector.begin() + j);
								setPosvector[j] = true;
								enemyCounter--;
							}
							continue;
						}*/
					}
					
					if (flame[i].shape.getGlobalBounds().intersects(Boss.body.getGlobalBounds()))
					{
						bossblood -= 5;
						BHP += 5;
						if (bossblood <= 0)
						{
							GameScore += 1000;
							bossblood = 50000;
							BHP = 0;
							Boss.speed *= 2;
						}
					}
				}
				for (int j = 0; j < enemyVector.size(); j++) {
					if (player.body.getGlobalBounds().intersects(enemyVector[j].getGlobalBounds()))
					{
						MyHP -= 20;
						PHP += 20;
						std::cout << "P-E collis" << std::endl;
						enemyBloodVector[j] -= 10;
						//flame.erase(flame.begin() + i);

						if (enemyBloodVector[j] == 0) {
							enemyVector.erase(enemyVector.begin() + j);
							enemyBloodVector.erase(enemyBloodVector.begin() + j);
							setPosvector[j] = true;
							enemyCounter--;
						}
						continue;
					}
				}
				if (PHP <= 50000)
					Boss.B_HP.setSize(sf::Vector2f((100 - (BHP * 0.002)), 10));
				else if (PHP <= 0)
					Boss.B_HP.setSize(sf::Vector2f(0, 10));
				//std::cout << GameScore << std::endl;

				//enemy.movement		
				for (int i = 0; i < enemyVector.size(); i++) {
					if (enemyVector[i].getPosition().x > player.GetPosition().x-10) { enemyVector[i].move(-1.f, 0.f); }
					if (enemyVector[i].getPosition().x < player.GetPosition().x-10) { enemyVector[i].move(1.f, 0.f); }
					if (enemyVector[i].getPosition().y > player.GetPosition().y-10) { enemyVector[i].move(0.f, -1.f); }
					if (enemyVector[i].getPosition().y < player.GetPosition().y-10) { enemyVector[i].move(0.f, 1.f); }
				}
				if (colis.collisitem(&player, &Item))
				{
					GameScore += 10; 	//ระวังปัญหา
					MyHP -= 100;
					PHP += 100;
				}
				if (colis.collisboss(&player, &Boss))
				{
					MyHP -= 30;
					PHP += 30;
				}
				if(PHP<=5000)
					player.HP.setSize(sf::Vector2f(((GHP / 20) - (PHP * 0.0465)), 20));
				else if (PHP <= 0)
					player.HP.setSize(sf::Vector2f(0, 20));

				window.clear(sf::Color::Black);
				//พื้นหลัง
				window.draw(background_4);
				window.draw(background_1);
				window.draw(background_2);
				window.draw(background_3);
				//ตัวละคร + ไอเทม
				Item.Draw(window);
				for (size_t i = 0; i < flame.size(); i++)
				{
					window.draw(flame[i].shape);
				}
				player.Draw(window);
				Boss.Draw(window);
				animation.Update(0, deltaTime, false);
				for (int i = 0; i < enemyVector.size(); i++) {
					enemyVector[i].setTextureRect(animation.uvRect);
					window.draw(enemyVector[i]);
				}
				view.setCenter(player.GetPosition().x, player.GetPosition().y);
				mousePositionShow(&window);
				window.draw(Outtext);
				window.draw(bloodtext);
				
				
		

				window.display();
			}
			if (MyHP <= 0)
			{
				sort(input, GameScore);
				State = State_End;
			}
			if (sf::Keyboard::isKeyPressed(sf::Keyboard::BackSpace) && sf::Keyboard::isKeyPressed(sf::Keyboard::LControl))
			{
				Pastcheck = 0;
				input = ' ';
				State = State_mainmenu;
			}
		}
		if (State == State_howtoplay)
		{
			window.clear();
			window.setView(window.getDefaultView());
			window.draw(stateM1);
			window.display();
			if (sf::Keyboard::isKeyPressed(sf::Keyboard::BackSpace))
			{
				State = State_mainmenu;
			}
		}
		if (State == State_score)
		{
			window.clear();
			window.setView(window.getDefaultView());
			window.draw(stateM2);
			readTextFile(window);
			window.display();
			if (sf::Keyboard::isKeyPressed(sf::Keyboard::BackSpace))
			{
				State = State_mainmenu;
			}
		}
		if (State == State_credit)
		{
			window.clear();
			window.setView(window.getDefaultView());
			window.draw(stateM3);
			window.display();
			if (sf::Keyboard::isKeyPressed(sf::Keyboard::BackSpace))
			{
				State = State_mainmenu;
			}
		}
		if (State == State_End)
		{
			
			window.clear();
			window.setView(window.getDefaultView());
			window.draw(stateM4);
			window.draw(Showtext);
			window.display();
			MyHP = 5000;
			PHP = 0;
			GameScore = 0;
			Pastcheck = 0;
			input = ' ';
			if (sf::Keyboard::isKeyPressed(sf::Keyboard::BackSpace))
			{
				State = State_mainmenu;
			}
		}
		if (State == State_mainmenu)
		{
			window.clear();
			menu.Update(window);
			if (menu.gotostate == State_play)
				State = State_play;
			if (menu.gotostate == State_howtoplay)
				State = State_howtoplay;
			if (menu.gotostate == State_score)
				State = State_score;
			if (menu.gotostate == State_credit)
				State = State_credit;
			if (menu.gotostate == State_quit)
				window.close();
			//window.clear();
			//window.setView(view);
			//window.draw(Background);
			window.setView(window.getDefaultView());
			menu.Draw(window);
			for (int i = 0; i < 50; i++) {
				window.draw(snow[i]);
			}
			MyHP = 5000;
			PHP = 0;
			GameScore = 0;
			Pastcheck = 0;
			input = ' ';
			window.display();
		}
	}
	return 0;
}