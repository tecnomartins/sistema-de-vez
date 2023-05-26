int uni = 0;
int dez = 0;
//portuguese
int buttonPushCounter1 = 0; 
int buttonState1 = 0;
int lastButtonState1 = 0;
//english
int buttonPushCounter2 = 0; 
int buttonState2 = 0;
int lastButtonState2 = 0;
//french
int buttonPushCounter3 = 0; 
int buttonState3 = 0;
int lastButtonState3 = 0;

void setup()
{
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  Serial.begin(9600);
}

void write1()
{
  //print number
  Serial.print("a");
  Serial.print(dez);
  Serial.print(uni);
  Serial.print("\n");
}

void write2()
{
  //print number
  Serial.print("b");
  Serial.print(dez);
  Serial.print(uni);
  Serial.print("\n");
}

void write3()
{
  //print number
  Serial.print("c");
  Serial.print(dez);
  Serial.print(uni);
  Serial.print("\n");
}


void loop()
{
  //go up
  buttonState1 = digitalRead(8);
  if (buttonState1 != lastButtonState1) {
    if (buttonState1 == HIGH) {
      //go from 88 to 89
      if (uni<9){
        uni++;
        write1();
      }
      else{
        //go from 89 to 90
        if (dez<9){
          dez++;
          uni=0;
          write1();
        }
        //go from 99 to 00 (loop around)
        else{
          dez=0;
          uni=0;
          write1();
        }
      }
    }
    delay(500);
  }
  lastButtonState1 = buttonState1;

  //go up
  buttonState2 = digitalRead(9);
  if (buttonState2 != lastButtonState2) {
    if (buttonState2 == HIGH) {
      //go from 88 to 89
      if (uni<9){
        uni++;
        write2();
      }
      else{
        //go from 89 to 90
        if (dez<9){
          dez++;
          uni=0;
          write2();
        }
        //go from 99 to 00 (loop around)
        else{
          dez=0;
          uni=0;
          write2();
        }
      }
    }
    delay(500);
  }
  lastButtonState2 = buttonState2;

  //go up
  buttonState3 = digitalRead(10);
  if (buttonState3 != lastButtonState3) {
    if (buttonState3 == HIGH) {
      //go from 88 to 89
      if (uni<9){
        uni++;
        write3();
      }
      else{
        //go from 89 to 90
        if (dez<9){
          dez++;
          uni=0;
          write3();
        }
        //go from 99 to 00 (loop around)
        else{
          dez=0;
          uni=0;
          write3();
        }
      }
    }
    delay(500);
  }
  lastButtonState3 = buttonState3;
}