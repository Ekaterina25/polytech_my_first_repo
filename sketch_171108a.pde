int[] array = new int[15];
void setup() {
    size(400, 500);
    for (int i = 0; i < array.length; i++) {
        array[i] = (int) random(40);
    }
    frameRate(3);
}
int i = 0;
void draw() {
    background(0);

    for (int j = 0; j < array.length; j++) {
        if (array[i] > array[j]) {
            int temp = array[j];
            array[j] = array[i];
            array[i] = temp;
        }
        fill(200);
        text(array[j], 40, 30 + 20 * j);
        stroke(#D514AF);
        strokeWeight(2);
        line(80, 25 + 20 * j, 90 + 5 * array[j], 25 + 20 * j);
    }
    i++;
    if (i > array.length - 1)
        noLoop();
}