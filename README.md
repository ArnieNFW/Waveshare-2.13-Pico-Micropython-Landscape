# Waveshare-2.13-Pico-Micropython-Landscape
A way to display text horizontally on the 2.13 waveshare e-paper display for Raspberry Pico 

-------------------------------------------------------------------------------------------------
**Please mind: although I program, I am not a professional programmer (warning for bad coding).**
-------------------------------------------------------------------------------------------------

This project is for me a dive into Python (wow - how mistaken I was) in combination with the 2.13 inch Waveshare E-paper HAT for the Raspberry Pico. 
With this E-paper hat there is no (Micropython) example given to use it in Landscape mode. After consulting Waveshare they responded that it has not been made (yet).
The told me to look at the C/C++ examples. I could not make anything outof that.... 

What I did, briefly:
- found out how to display a picture (see example imagetest01inverted.py)
- build an empty picture and fill it with desired text/lines/rectangles. Rotated.
- build some basic routines for:
  + display 8x8 or 16x16 chars/text
  + draw lines, double lines
  + draw rectangles, double rectangles

All quite basic, but it defenitely works! You can either use:
- Landscape - all code included.py          Exactly as it says, 1 py program which contains all needed
- Landscape - minimum with library use.py   The same example, but all routines are put in EPB0.py and imported. So the actual program is quite small.
- EPB0.py                                   The library name (E-Paper Basic version 0.py) - only for use with the minimum example.

I will put more text in here when there is time available. 

Two small remarks:
- There are NO checks on coordinates. So if you specify them out-of-limits, you'll get an (hardware) error.
- for lines/rectangles size is 250x120. For text: horizontal 250, vertical 15 !! (0-15)
  this is because the characters have to be mapped into bytes.
