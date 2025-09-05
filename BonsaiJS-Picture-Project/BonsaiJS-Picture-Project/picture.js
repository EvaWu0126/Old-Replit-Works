/* 
documentation for simple shapes using BonsaiJS:
http://docs.bonsaijs.org/overview/SimpleShapes.html
*/

//synta: var variableName
//declares a variable and the name should be dscriptive
//

//new Rect() creats a rectangle object
//the "=" assigns that rectangle object
//to tje variable myShape

/*
//Rect is a class--a blueprint that defines how all rectangles behave
//the blueprint says that all rectangles should remember their position and their dimensions

var myShape = new Rect(10, 300, 100, 100)

//once a variable is declared, you can refre to that varible and call methods on it
//varName.methodName(arguments)

myShape.fill('lightblue');
myShape.stroke('#6495ED', 1);
myShape.addTo(stage);
*/

//Happy Face//

//camelCase is when you make each new word a capital letter
var face = new Circle(178, 170, 150);
face.fill("#FDF5E6");
face.stroke("#FFDEAD", 1);
face.addTo(stage);

var leftEye = new Ellipse(100, 100, 20, 25);
leftEye.fill('#00BFFF');
leftEye.stroke('#1E90FF', 2);
leftEye.addTo(stage);
var leftEyeDark = new Ellipse(107, 108, 11, 12);
leftEyeDark.fill('#6495ED');
leftEyeDark.addTo(stage);
var leftEyeLight = new Ellipse(98, 98, 7, 8);
leftEyeLight.fill('#F0F8FF');
leftEyeLight.addTo(stage);

var rightEye = new Ellipse(250, 100, 20, 25);
rightEye.fill('#00BFFF');
rightEye.stroke('#1E90FF', 2);
rightEye.addTo(stage);
var rightEyeDark = new Ellipse(257, 108, 11, 12);
rightEyeDark.fill('#6495ED');
rightEyeDark.addTo(stage);
var rightEyeLight = new Ellipse(246, 98, 7, 8);
rightEyeLight.fill('#F0F8FF');
rightEyeLight.addTo(stage);

var nose = new Star(180, 170, 10, 4, 5)
nose.fill('#FFFACD');
nose.stroke('#F0E68C', 2);
nose.addTo(stage);

var mouth = new Arc(180, 190, 70, Math.PI, 0, true);
mouth.stroke('#1E90FF', 2);
mouth.addTo(stage);

var leftFace = new Ellipse(70, 180, 20, 15);
leftFace.fill('#FFB6C1');
leftFace.stroke('#F08080', 2);
leftFace.addTo(stage);
var rightFace = new Ellipse(290, 180, 20, 15);
rightFace.fill('#FFB6C1');
rightFace.stroke('#F08080', 2);
rightFace.addTo(stage);