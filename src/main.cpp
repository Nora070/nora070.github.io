// Filename: Shapes CPP HW1
// Description: Practice creating simple classes using cpp
// Author: Nora Humfeld
// Date Modified: Oct 18, 2024

#include <iostream>
using namespace std;

#include "CCircle.h"
#include "CTriangle.h"
#include "CSquare.h" // point, color included in shape, which is in polygon, which is in rectangle: don't need to re-include
// is vs has. Polygon is a shape. Shape has a point. Very different

int main()      // "entry point"
{
    cout << "Welcome to Shapes CPP!" << endl;
   
    CShape *shapes[10]; // Array of pointers to shape objects - still need to instantiate each one
    // Allowed to be array of different data type because theyre all inherited from Shape
    shapes[0] = new CCircle();
    // shapes[0].radius() won't work because it's still being treated as a shape not a circle yet
    ((CCircle*)shapes[0])->radius(3.0); // forced typecasting
    cout << "Area of my circle: " <<  ((CCircle*)shapes[0])->calcArea() << endl;

    shapes[1] = new CSquare();
    ((CSquare*)shapes[1])->setDimension(3.0, 5.0);
    cout << "Area of my square: " << ((CSquare*)shapes[1])->calcArea() << endl;
    
    shapes[2] = new CEllipse();
    ((CEllipse*)shapes[2])->radius(3.0, 5.0);
    cout << "Area of my ellipse: " << ((CEllipse*)shapes[2])->calcArea() << endl;

    shapes[3] = new CRectangle();
    ((CRectangle*)shapes[3])->setDimension(6.0, 8.0);
    cout << "Area of my rectangle: " << ((CRectangle*)shapes[3])->calcArea() << endl;

    shapes[4] = new CTriangle();
    ((CTriangle*)shapes[4])->set(0, 0, 6, 7, -3, 5);
    cout << "Area of my triangle: " << ((CTriangle*)shapes[4])->calcArea() << endl;

    shapes[5] = new CLine();
    ((CLine*)shapes[5])->set(1.0, 1.0, 5.0, 6.0);
    cout << "Length of my line: " << ((CLine*)shapes[5])->calcArea() << endl;


    cout << "Still running Shapes CPP..." << endl;

    delete ((CCircle*)shapes[0]);
    delete ((CSquare*)shapes[1]);
    delete ((CEllipse*)shapes[2]);
    delete ((CRectangle*)shapes[3]);
    delete ((CTriangle*)shapes[4]);
    delete ((CLine*)shapes[5]);
    // could let program automatically delete at the end

    return 0; // destructor classes run here, at the close of the function
}