//this is the header file declaring the class and its features.


#ifndef LED_H
#define LED_H
class led{
public:
	led();
	led(int pin1, int pin2);
	~led();
	bool flashOn();
	bool flashOff();
private:
int pin1_;
int pin2_;
};


#endif
