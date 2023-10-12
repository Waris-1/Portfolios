class Car {
  private float x;
  private float y;
  private color clr;
  private float theSize;
  private int score = 0;

  public Car(float xcr, float ycr, float size, color cl) {
    theSize = size;
    setPosition(xcr);
    y = ycr;
    clr = cl;
  }

  public void display() {
    float wheelOffset = theSize / 4;
    rectMode(CENTER);
    stroke(0);
    fill(clr);
    rect(x, y, theSize, theSize/2);
    fill(0);
    textSize(20);
    text(score, x-3, y+5);

    rect(x - wheelOffset, y - wheelOffset, wheelOffset, wheelOffset/2);
    rect(x + wheelOffset, y - wheelOffset, wheelOffset, wheelOffset/2);
    rect(x + wheelOffset, y + wheelOffset, wheelOffset, wheelOffset/2);
    rect(x - wheelOffset, y + wheelOffset, wheelOffset, wheelOffset/2);
    
  }

  public void move() {
    x = x + random(0, 10);
  }

  public float getPosition() {
    return x + theSize/2;
  }

  public void setPosition(float newPos) {
    x = newPos - theSize/2;
  }

  private void increaseScore() {
    score++;
    println(score);
  }

  private void detectOneWinner(Car c) {
    if   (x > c.getPosition()) {
      increaseScore();
    }
  }
}
