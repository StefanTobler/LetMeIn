# LetMeIn
LetMeIn is a facial recognition door security system that utilizes the Microsoft Vision API to handle facial recognition based on people groups. Once the user is authenticated a motor is actuated on the inside of the door unlocking the deadbolt. After two minutes the deadbolt is then set back in place by the motor.

# Target Audience
LetMeIn is targeted at elderly people with depth perception issues or motor neurone disorders such as parkinsons. This device will allow for the ease of access and security of a traditional lock, but without the hastle of keeping up with or using a key. 

LetMeIn can also be used in households with children who are not yet responsible enough to keep up with a key.

# Hardware
In this project we used an Adruino UNO to actuate a stepper motor to unlock the door. In the future we will add a transistor so that power running to the stepper can be switched on and off.

# Improvements
Eventually we will want to switch out the Arduino for a Raspberry Pi 3 and some sort of NFC activation for the camera being used. We are also encouraged to look for ways that the power consumption of the stepper and the UNO can be reduced when not in use. 

Create a user interface for quick and easy setup.

*This project was created for HackGT*
