Car[] cars;
RaceTrack track;
boolean raceend;
float r;
float g;
float b;


void setup() {
  size(1000, 600);
  cars = new Car[5];
  track = new RaceTrack();
  for (int i = 0; i < cars.length; i++) {
    r = random(0, 255);
    b = random(0, 255);
    g = random(0, 255);
    

    cars[i] = new Car(track.getStartPosition(), (i+1)*100, 60, color(r, b, g));
  }
  raceend = false;
}

void draw() {
  background(70);
  track.display();
  for (int i = 0; i < cars.length; i++) {
    cars[i].display();
  }
  if (!raceend) {
    for (int i = 0; i < cars.length; i++) {
      if (cars[i].getPosition() >= track.getFinishPosition()) {
        raceend = true;
        cars[i].increaseScore();
        cars[i].detectOneWinner(cars[i]);
        println("Press 's' to restart");
      } else {
        cars[i].move();
}
 }
 }
}
void keyPressed() {
  if (key == 's' && raceend) {
    float startLine = track.getStartPosition();
    for (int i = 0; i < cars.length; i++) {
      cars[i].setPosition(startLine);
      raceend = false;
    }
  }
}
