int relay = 2;

void setup() {
  // put your setup code here, to run once:
  pinMode(relay, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int lectura = analogRead(A0);

  Serial.println(lectura);

  if (lectura >= 600) {
    digitalWrite(relay, HIGH);
    delay(5000);
    digitalWrite(relay, LOW);
    delay(25000);
  }
  else {
    delay(30000);
  }
}
