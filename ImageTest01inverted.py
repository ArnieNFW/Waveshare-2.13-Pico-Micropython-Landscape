# *****************************************************************************
# * | File        :	  Pico_ePaper-2.13.py
# * | Author      :   Waveshare team
# * | Function    :   Electronic paper driver
# * | Info        :
# *----------------
# * | This version:   V1.0
# * | Date        :   2021-03-16
# # | Info        :   python demo
# -----------------------------------------------------------------------------
# Changed by:   Arnoud van Leijden
# Function:     Display a picture on e-paper, picture is used by Waveshare in other examples.
#               The display is inverted.

from machine import Pin, SPI
import framebuf
import utime

Beeld = [0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XC7,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XF0,0XFF,0XFF,0X87,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XE0,0X7F,0XFF,0X07,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0X00,0X3F,0XFC,0X07,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFE,0XFF,0XFF,0XFF,0XFF,0XFE,0X00,0X1F,0XE0,0X07,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0X3F,0XFF,0XFF,0XFF,0XFC,0X00,0X8F,0XE0,0X0F,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0X81,0XFF,0XFF,0XFF,0XFC,0X00,0X87,0XC7,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XC0,0XFF,0XFF,0XFF,0XFC,0X00,0X07,0X0F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XF0,0X3F,0XFF,0XFF,0XFC,0X0F,0X07,0X3E,0X07,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFC,0X0F,0XFF,0XFF,0XFC,0X0C,0X0C,0X70,0X01,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFE,0X07,0XFF,0XFF,0XFC,0X00,0X0C,0X40,0X00,0X3F,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XC1,0XFF,0XFF,0XFC,0X00,0X05,0X80,0X00,0X0F,0XFF,0XFF,
0XFF,0XF0,0XFF,0XFF,0XFF,0XC0,0X1F,0XFF,0XFF,0X18,0X04,0X00,0X00,0X0F,0XFF,0XFF,
0XFF,0XF8,0XFF,0XFF,0XFF,0XC0,0X0F,0XFF,0XFF,0X18,0X04,0X00,0X00,0X1F,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XE0,0X03,0XFF,0XFF,0X00,0X04,0X00,0X00,0X1F,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XF0,0X01,0XFF,0XFF,0X80,0X04,0X30,0X00,0X1F,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFC,0X01,0XFF,0XFF,0XC0,0X06,0X30,0X00,0X1F,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFE,0X00,0X7F,0XFF,0XF0,0X0E,0X00,0X00,0X1F,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0X00,0X3F,0XFF,0XFF,0XC2,0X10,0X00,0X1F,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0X80,0X1F,0XFF,0XFC,0X00,0X08,0X00,0X3F,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XC0,0X1F,0XFF,0XC0,0X00,0X00,0X00,0X7F,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XE0,0X1F,0XFF,0X81,0X00,0X00,0X00,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,0XC1,0X00,0X0E,0X00,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XF0,0X1F,0XFF,0XC0,0X00,0X40,0X03,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0XC1,0X80,0XC0,0X07,0XC7,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0X81,0X80,0X3F,0XFF,0X83,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0X81,0XC0,0X3F,0XFE,0X01,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XF8,0X0F,0XFF,0X80,0XE0,0X20,0X00,0X00,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XFC,0X0F,0XFF,0X80,0X78,0X10,0X00,0X00,0X7F,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XFC,0X0F,0XFF,0X80,0X1C,0X0E,0X00,0X00,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XFC,0X0F,0XFE,0X78,0X03,0X87,0X01,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XFC,0X0F,0XFC,0XFE,0X07,0X00,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XFC,0X0F,0XF1,0XFF,0XFE,0X00,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XFC,0X0F,0XF3,0XFF,0XFC,0X00,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XFC,0X0F,0XE3,0XFF,0XF0,0X67,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XFC,0X0F,0XC7,0XFF,0X80,0X63,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XFF,0XFF,0XFC,0X0F,0XCF,0XFF,0XC0,0X23,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XF8,0X01,0XF8,0X1F,0XCF,0XFF,0XE0,0X01,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XF0,0X00,0X78,0X0F,0X8F,0XFF,0XE0,0X03,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XE0,0X00,0X38,0X0F,0XFF,0XFF,0XF0,0X01,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XC0,0X00,0X18,0X1F,0XFF,0XFF,0XF0,0X0F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0X80,0X00,0X0C,0X1F,0X80,0X00,0X10,0X1F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0X00,0X60,0X04,0X30,0X00,0X00,0X39,0XE7,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFC,0X00,0X30,0X06,0X20,0X00,0X00,0X3F,0XF7,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XF1,0X00,0X20,0X02,0X00,0X00,0X01,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFE,0X0F,0X00,0X00,0X02,0X00,0X01,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFC,0X07,0X00,0X00,0X02,0X00,0X03,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XF8,0X03,0X00,0X20,0X02,0X00,0X07,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XF0,0X01,0X38,0X20,0X02,0X00,0X7F,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XC1,0X80,0X08,0X20,0X00,0X01,0XCF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XC1,0X80,0X08,0X20,0X30,0X0F,0XC7,0XFF,0XF9,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0X81,0X80,0X00,0X00,0X60,0X1F,0XC7,0XFF,0XE0,0X3F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0X80,0XE0,0X00,0X01,0XC1,0XFF,0XC3,0XFF,0XC4,0X1F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0X80,0X70,0X00,0X01,0X83,0XFF,0XC3,0XFF,0XC4,0X1F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0X80,0X78,0X01,0XC0,0X07,0XFF,0XC3,0XFF,0X80,0X0F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0X80,0X5E,0X07,0XE0,0X03,0XFF,0XE3,0XFF,0X83,0X0F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XC0,0X00,0X0F,0XF0,0X03,0XFF,0XF3,0XFF,0X81,0X83,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XC0,0X00,0X0F,0XF0,0X01,0XFF,0XF3,0XFF,0X80,0XC3,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XE0,0X00,0X0F,0XF0,0X00,0XFF,0XF3,0XFF,0XC0,0X7F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XF0,0X00,0X0F,0XF1,0X80,0X7F,0XF3,0XFF,0XC0,0X3F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XF8,0X00,0X07,0XF1,0XC0,0X3F,0XF3,0XFF,0XE0,0X0F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFC,0X00,0X07,0XE1,0XE0,0X1F,0XF3,0XFF,0XF0,0X0F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XC0,0X01,0XC0,0X78,0X1F,0XC3,0XFF,0XF0,0X41,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XB8,0X00,0X00,0X0F,0X9F,0XC3,0XFF,0XF0,0X40,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XCE,0X00,0X00,0X07,0X1F,0XC7,0XFF,0XF0,0X40,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFC,0XF9,0XEE,0X00,0X02,0X00,0X1F,0XC7,0XFF,0XF0,0XE0,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFC,0XF1,0XEC,0X00,0X06,0X00,0X1F,0XCF,0XFF,0XF1,0XF8,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFC,0XC3,0X28,0X02,0X02,0X00,0X1F,0XCF,0XFF,0XE3,0X38,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFC,0XC6,0X10,0X04,0X00,0X00,0X1F,0XCF,0XFF,0XC2,0X00,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFC,0X8C,0X10,0X04,0X00,0X00,0X1F,0X9F,0XFF,0XC2,0X00,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFC,0X98,0X10,0X04,0X00,0X00,0X3F,0X3F,0XFF,0XC0,0X00,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFC,0X70,0X08,0X1C,0X00,0X00,0X7F,0X1F,0XFF,0XE4,0X00,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFC,0X60,0X0C,0X1E,0X00,0X1F,0XFE,0X3F,0XFF,0XC4,0X00,0X3F,0XFF,0XFF,0XFF,
0XFF,0XFC,0XC0,0X0E,0X06,0X00,0X3F,0XFC,0X7F,0XFF,0X80,0X00,0X1F,0XFF,0XFF,0XFF,
0XFF,0XFC,0X80,0X0E,0X02,0X00,0X7F,0XF8,0XFF,0XFF,0XE0,0X00,0X07,0XFF,0XFF,0XFF,
0XFF,0XFC,0X00,0X0E,0X00,0X00,0X7F,0XF0,0XFF,0XFF,0XC0,0X00,0X03,0XFF,0XFF,0XFF,
0XFF,0XFC,0X00,0X1F,0X00,0X00,0XFF,0XF1,0XFF,0XFF,0XC0,0X00,0X63,0XFF,0XFF,0XFF,
0XFF,0XFC,0X00,0X7F,0XF0,0X00,0XFF,0XF9,0XFF,0XFF,0XFC,0X09,0X83,0XFF,0XFF,0XFF,
0XFF,0XFC,0X00,0XFF,0XE0,0X83,0XFF,0X07,0XFF,0XFF,0XF6,0X0F,0XC3,0XFF,0XFF,0XFF,
0XFF,0XFC,0X01,0XFF,0XC0,0XC7,0XFE,0X03,0XFF,0XFF,0XE3,0X07,0XE3,0XFF,0XFF,0XFF,
0XFF,0XFC,0X03,0XFF,0X00,0X6F,0XFC,0X01,0XFF,0XFF,0XC2,0X00,0X63,0XFF,0XFF,0XFF,
0XFF,0XFC,0X07,0XFF,0X00,0X3F,0XF0,0X00,0XFF,0XFF,0X8C,0X00,0X33,0XFF,0XFF,0XFF,
0XFF,0XFC,0X0F,0XFF,0X00,0X1F,0XF0,0X00,0XFF,0XFF,0X9E,0X00,0X03,0X9F,0XFF,0XFF,
0XFF,0XFC,0X0F,0XFE,0X00,0X0F,0XE0,0X00,0XFF,0XFF,0X3F,0X00,0X00,0X0F,0XFF,0XFF,
0XFF,0XF8,0X1F,0XFE,0X00,0X40,0X00,0X00,0X7F,0XFF,0X1F,0XFF,0X80,0X0F,0XFF,0XFF,
0XFF,0XFC,0X3F,0XFE,0X00,0XC0,0X00,0X00,0X7F,0XFF,0X3F,0XFF,0XC0,0X07,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFE,0X01,0X80,0X00,0X00,0X7F,0XFF,0X7F,0XFF,0XE0,0X03,0XFF,0XFF,
0XFF,0XF8,0XFF,0XFF,0X01,0X80,0X00,0X00,0X7F,0XFF,0X7F,0XFF,0XF3,0X03,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0X0F,0X80,0X00,0X00,0XFF,0XFF,0X7F,0XFF,0XFB,0X83,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0X81,0XC0,0X00,0X03,0XFF,0XFE,0X7F,0XFF,0XFC,0X03,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0X81,0XC0,0X00,0X01,0XFF,0XFE,0X7F,0XFF,0XFE,0X0F,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XC0,0X20,0X40,0X00,0X7F,0XFE,0X7F,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0XC0,0X30,0X40,0X00,0X3F,0XFE,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0X80,0X30,0X00,0X00,0X1F,0XFE,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XFF,0X00,0X30,0X30,0X00,0X3F,0XFE,0X7F,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFF,0XE1,0X00,0X10,0X38,0X00,0X3F,0XFE,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XFE,0X03,0X00,0X18,0X0F,0X80,0X7F,0XFC,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XF8,0XF8,0X3F,0X00,0X0C,0X07,0X00,0XFF,0XF0,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFC,0XF0,0X7F,0X80,0X0C,0X06,0X01,0XFF,0XF1,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0XE0,0XFF,0XC0,0X0C,0X04,0X01,0XFF,0XF3,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0XC7,0XFF,0XFC,0X06,0X04,0X0C,0X1F,0XE7,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X0F,0XFF,0XC3,0X06,0X04,0X10,0X0F,0XCF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X3F,0XFF,0X82,0X06,0X04,0X30,0X0F,0X8F,0XFF,0XFF,0XE7,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0X00,0X07,0X04,0X30,0X03,0X3F,0XFF,0XFC,0X07,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0X00,0X03,0X04,0X00,0X03,0XFF,0XFF,0XF8,0X07,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0X00,0X21,0X04,0X00,0X83,0XFF,0XFF,0XC0,0X03,0XFF,0XFF,0XFF,
0XFF,0XFE,0XFF,0XFF,0X00,0X21,0X0C,0X00,0XC3,0XFF,0XFF,0X80,0X01,0XFF,0XFF,0XFF,
0XFF,0XFE,0XFF,0XFF,0X00,0X3D,0X0C,0X00,0XE3,0XFF,0XFF,0X00,0X01,0XFF,0XFF,0XFF,
0XFF,0XFE,0XFF,0XFF,0X04,0X1C,0X00,0X00,0XC3,0XFF,0XFF,0X00,0X00,0XFF,0XFF,0XFF,
0XFF,0XFE,0XFF,0XFF,0X06,0X10,0X00,0X01,0XC3,0XFF,0XFF,0X00,0X00,0XFF,0XFF,0XFF,
0XFF,0XFE,0XFF,0XFF,0X03,0X00,0X00,0X06,0X03,0XFF,0XFF,0X23,0X80,0XFF,0XFF,0XFF,
0XFF,0XFE,0XFF,0XFE,0X01,0X80,0X00,0X1C,0X01,0XFF,0XFF,0X00,0X40,0XFF,0XFF,0XFF,
0XFF,0XFE,0XFF,0XFE,0X01,0XC0,0X00,0X38,0X01,0XFF,0XFF,0X00,0X60,0XFF,0XFF,0XFF,
0XFF,0XFE,0XFF,0XFC,0X00,0XC0,0X00,0X30,0X00,0XFF,0XFF,0X00,0X40,0XFF,0XFF,0XFF,
0XFF,0XFE,0XFF,0X00,0X00,0X30,0X00,0X00,0X00,0X7F,0XFF,0X00,0X01,0XFF,0XFF,0XFF,
0XFF,0XFE,0XF0,0X1F,0X80,0X00,0X78,0X00,0X00,0X7F,0XFF,0X00,0X3F,0XFF,0XFF,0XFF,
0XFF,0XFE,0XE0,0X7F,0XC0,0X00,0XFC,0X00,0X31,0XFF,0XFF,0X00,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X0F,0XFF,0XF0,0X01,0XFE,0X03,0XE1,0XFF,0XFF,0X0F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X1F,0X80,0X38,0X03,0XFE,0X03,0XC1,0XFF,0XFF,0X3E,0X00,0X1F,0XFF,0XFF,
0XFF,0XFE,0X3E,0X00,0X08,0X07,0XFE,0X00,0X03,0XFF,0XFE,0X72,0X00,0X0F,0XFF,0XFF,
0XFF,0XFE,0X78,0X00,0X04,0X03,0XFE,0X00,0X07,0XFF,0XF0,0XE1,0X00,0X07,0XFF,0XFF,
0XFF,0XFE,0XC0,0X7F,0XFC,0X03,0XFE,0X00,0X0F,0XFF,0XF1,0X81,0X80,0X01,0XFF,0XFF,
0XFF,0XFE,0X07,0XFF,0XF8,0X01,0XFE,0X00,0X1D,0XFF,0XE1,0X80,0XC0,0X03,0XFF,0XFF,
0XFF,0XFE,0X1F,0X00,0X60,0X20,0XFC,0X00,0X39,0X9F,0XE3,0X00,0X70,0X01,0XFF,0XFF,
0XFF,0XFE,0X70,0X3F,0X00,0XC0,0X38,0X10,0X1C,0X87,0XC1,0XE0,0X30,0X00,0XFF,0XFF,
0XFF,0XFE,0X20,0X7F,0X01,0X80,0X10,0X18,0X0E,0X43,0X80,0XF0,0X30,0X00,0X3F,0XFF,
0XFF,0XFE,0X03,0XFF,0X02,0X00,0X00,0X1C,0X0E,0X61,0XC0,0X3C,0X18,0X00,0XFF,0XFF,
0XFF,0XFE,0X07,0XFE,0X0E,0X06,0X00,0X0E,0X02,0X30,0X60,0X1E,0X00,0X00,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFE,0X0C,0X0E,0X00,0X06,0X02,0X3E,0X60,0X07,0X00,0X1F,0XFF,0XFF,
0XFF,0XFE,0XFF,0XFE,0X00,0X1C,0X02,0X01,0X00,0X3F,0XC0,0X0F,0XFF,0XFC,0X7F,0XFF,
0XFF,0XFE,0XFF,0XFF,0X00,0X1C,0X02,0X00,0X80,0X3F,0X80,0X3F,0XFF,0XF8,0X7F,0XFF,
0XFF,0XFE,0XFF,0XFF,0X00,0X18,0X03,0X00,0XF8,0X7F,0X00,0X30,0X00,0X00,0XFF,0XFF,
0XFF,0XFE,0XFF,0XFF,0X00,0X10,0X31,0X80,0XF8,0XFF,0X81,0X80,0X00,0X01,0XFF,0XFF,
0XFF,0XFE,0XE0,0X01,0X00,0X00,0X31,0X80,0XC1,0XFF,0XC1,0X80,0X00,0X03,0XFF,0XFF,
0XFF,0XFE,0X00,0X00,0X00,0X0E,0X31,0XC0,0XC1,0XFF,0XC0,0X03,0XF8,0X07,0XFF,0XFF,
0XFF,0XFE,0X00,0X00,0XC0,0X1E,0X71,0XC0,0XC1,0XFF,0XE0,0X03,0XF8,0X0F,0XFF,0XFF,
0XFF,0XFE,0X1F,0XFF,0XF1,0XFC,0X71,0XC0,0XC1,0XFF,0XF0,0X00,0X07,0XFF,0XFF,0XFF,
0XFF,0XFE,0X00,0X00,0X78,0X00,0X71,0XC0,0XE1,0XFF,0XFB,0X01,0XC1,0XFF,0XFF,0XFF,
0XFF,0XFE,0X00,0X00,0X38,0X00,0X70,0XC0,0X41,0XFF,0XFF,0X01,0XE1,0XFF,0XFF,0XFF,
0XFF,0XFE,0X00,0X00,0X38,0X00,0X70,0X60,0X01,0XFF,0XFF,0X03,0XC0,0X7F,0XFF,0XFF,
0XFF,0XFE,0X78,0X00,0X70,0X00,0X70,0X60,0X01,0XFF,0XFF,0X86,0X00,0X3F,0XFF,0XFF,
0XFF,0XFE,0XFF,0XF9,0XC0,0X00,0X70,0X20,0X01,0XFF,0XFF,0X80,0X00,0X3F,0XFF,0XFF,
0XFF,0XFE,0XFF,0XFF,0X80,0X00,0X70,0X70,0X03,0XFF,0XFF,0XE0,0X00,0X1F,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0X00,0X00,0X70,0XE0,0XFF,0XFF,0XFF,0XF0,0X00,0X0F,0XFF,0XFF,
0XFF,0XFE,0X3F,0XFE,0X00,0X00,0X71,0XC0,0X7E,0XFF,0XFF,0XFE,0X00,0X1F,0XFF,0XFF,
0XFF,0XFE,0X1F,0XFE,0X00,0X00,0X71,0X80,0X3C,0X7F,0XFF,0XFF,0X00,0X7F,0XFF,0XFF,
0XFF,0XFE,0X07,0XFF,0X00,0X0C,0X71,0X80,0X18,0X3F,0XFF,0XFF,0X80,0XFF,0XFF,0XFF,
0XFF,0XFE,0X00,0X7F,0X00,0X18,0X70,0X00,0X3B,0X1F,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X78,0X1E,0X00,0X20,0X70,0X00,0X31,0XE3,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X0E,0X07,0X00,0X00,0X70,0X00,0X30,0X30,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X01,0XE3,0X00,0X41,0XBC,0X1F,0XE0,0X0C,0X7F,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X00,0XF9,0X80,0XC1,0X9C,0X3E,0XC0,0X0E,0X1F,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X00,0X7C,0XC1,0XC3,0X0C,0X7E,0XE0,0X07,0X0F,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X00,0X1E,0X7F,0XC6,0X00,0XFF,0XF8,0X01,0X87,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X00,0X01,0X9F,0XE0,0X01,0XE3,0XFC,0X00,0XE3,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0XF0,0X00,0XC3,0XE0,0X01,0X9F,0XFE,0X00,0X71,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0XFE,0X00,0X61,0XF0,0X00,0X3F,0XFF,0XC0,0X3C,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0XFF,0X80,0X3C,0X70,0X02,0X7F,0XFF,0XC0,0X1C,0X7F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0XFF,0XC0,0X1E,0X38,0X03,0XFF,0XFF,0XC0,0X0E,0X3F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0XFF,0XE0,0X0E,0X1C,0X07,0XFF,0XFF,0XF8,0X0F,0X9F,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XF0,0X0E,0X1E,0X0F,0XFF,0XFF,0XFC,0X07,0XCF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFE,0X07,0XCF,0XFF,0XFF,0XFF,0XFE,0X03,0XC3,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0X07,0XE7,0XFF,0XFF,0XFF,0XFF,0X03,0XF1,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0X03,0XF3,0XFF,0XFF,0XFF,0XFF,0X01,0XF0,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0X83,0XF3,0XFF,0XFF,0XFF,0XFF,0X81,0XF8,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0X83,0XF9,0XFF,0XFF,0XFF,0XFF,0XC0,0XFC,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0X81,0XF9,0XFF,0XFF,0XFF,0XFF,0XE0,0X7E,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XE1,0XFC,0XFF,0XFF,0XFF,0XFF,0XF0,0X7F,0X3F,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XF1,0XFE,0XFF,0XFF,0XFF,0XFF,0XF8,0X7F,0X9F,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XF0,0XFE,0X7F,0XFF,0XFF,0XFF,0XFC,0X3F,0XCF,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XF8,0X7E,0X3F,0XFF,0XFF,0XFF,0XFE,0X3F,0XC7,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XF8,0X7E,0X3F,0XFF,0XFF,0XFF,0XFF,0X3F,0XE7,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XF8,0X3F,0X1F,0XFF,0XFF,0XFF,0XFF,0XBF,0XF7,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFC,0X3F,0X0F,0XFF,0XFF,0XFF,0XFF,0XFF,0XFB,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFC,0X3F,0X8F,0XFF,0XFF,0XFF,0XFF,0XFF,0XF9,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFE,0X3F,0X8F,0XFF,0X07,0XFF,0XFF,0XFF,0XFD,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFC,0X3F,0XCF,0XFF,0X00,0X0F,0XFF,0XFF,0XF8,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFC,0X3F,0XCF,0XFE,0X00,0X07,0XFF,0XFF,0XFC,0X7F,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFE,0X3F,0XCF,0XFE,0X00,0X03,0XFF,0XFF,0XFC,0X7F,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFE,0X3F,0XE7,0XFE,0X00,0X01,0XFF,0XFF,0XFC,0X7F,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFE,0X3F,0XF7,0XFF,0X00,0X00,0XFF,0XFF,0XFE,0X3F,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFE,0X3F,0XF7,0XFF,0X98,0X00,0XFF,0XFF,0XFE,0X3F,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFE,0X3F,0XF7,0XFF,0X00,0X00,0XFF,0XFF,0XFF,0X3F,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFE,0X7F,0XF7,0XFC,0X00,0X40,0X7F,0XFF,0XFF,0XBF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XF8,0X00,0XC0,0X7F,0XFF,0XFF,0XBF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XFC,0X00,0X40,0X3F,0XFF,0XFF,0XBF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XFC,0X00,0XC0,0X3F,0XFF,0XFF,0XBF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XFC,0X0F,0XE0,0X3F,0XFF,0XFF,0XBF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XFC,0X00,0X30,0X0F,0XFF,0XFF,0XBF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XFE,0X00,0X18,0X03,0XFF,0XFF,0X3F,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XFE,0X00,0X0C,0X00,0X0F,0XFE,0X3F,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XFE,0X00,0X07,0X00,0X07,0XFE,0X7F,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XFF,0X80,0X03,0X80,0X00,0XFC,0X7F,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XFF,0XE0,0X00,0XFF,0X80,0X7C,0X7F,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XFF,0XC0,0X00,0X7F,0XE0,0X38,0X7F,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XFF,0XC0,0X00,0X00,0X00,0X3C,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XFF,0XC0,0X00,0X00,0X00,0X3B,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XFF,0XC0,0X00,0X00,0X00,0X3B,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XE7,0XFF,0XE0,0X00,0X00,0X00,0X3B,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XC7,0XFF,0XF0,0X00,0X00,0X00,0X3F,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0X87,0XFF,0XFC,0X00,0X00,0X00,0X3F,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0X07,0XFF,0XFF,0X80,0X00,0X00,0X03,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFE,0X07,0XFF,0XFF,0XC0,0X00,0X00,0X03,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XC7,0XFF,0XFF,0XC0,0X00,0X06,0X03,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XE7,0XFF,0XFF,0XC0,0X00,0X0C,0X03,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XFF,0XFF,0XC0,0X00,0X18,0X03,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0XF7,0XFF,0XFF,0XC3,0X03,0XE0,0X07,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0XFF,0X73,0XFF,0XFF,0X81,0XFF,0X80,0X67,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0X86,0X73,0XFF,0XF8,0X00,0XF0,0X00,0X63,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFF,0X03,0X39,0XFF,0XF0,0X00,0X80,0X00,0X87,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFE,0X07,0XB9,0XFF,0XF0,0X00,0X80,0X01,0X87,0XFF,0XFF,0XFF,
0XFF,0XFE,0X7F,0XFF,0XFC,0X03,0XF8,0XFF,0XF0,0X00,0X80,0X01,0X87,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XFF,0XF8,0X01,0XF8,0X3F,0XF0,0X00,0X80,0X01,0X9F,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XFF,0XF8,0X06,0X18,0X1F,0XF8,0X00,0X80,0X07,0X3F,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XFF,0XFC,0X1C,0X0C,0X0F,0XFC,0X00,0X00,0X0E,0X3F,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XFF,0X80,0X3C,0X0C,0XC7,0XFE,0X00,0X00,0X0E,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XFF,0X00,0X20,0X0C,0XE3,0XFF,0X80,0X00,0X1C,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XFF,0X00,0X60,0X0C,0X71,0XFF,0XC0,0X00,0X18,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XFF,0X01,0XCC,0X04,0X30,0XFF,0XE0,0X00,0X30,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XFE,0X01,0XC0,0X0E,0X30,0XFF,0XF0,0X00,0X30,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XFF,0XF3,0X80,0X32,0X1C,0X7F,0XF0,0X00,0X20,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XFE,0XFE,0X03,0X71,0X80,0X7F,0XF0,0X00,0X60,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XF0,0X06,0X03,0XE1,0XC0,0X7F,0XF0,0X0C,0X40,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XF0,0X02,0X03,0XC1,0XC0,0X7F,0XF0,0X1E,0X40,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XF0,0X03,0X03,0XC0,0XC0,0X7F,0XF0,0X3E,0XC0,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XE0,0X1A,0X07,0XC4,0X60,0X7F,0XF0,0X3D,0XC0,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XE0,0X30,0X0F,0XCC,0X20,0X3F,0XFC,0X63,0XF0,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XFF,0XF1,0XFF,0XC6,0X26,0X3F,0XFF,0XC7,0X9C,0X3F,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XF0,0X01,0XFF,0XF0,0X11,0X0F,0XFF,0X00,0X0C,0X0F,0XFF,0XFF,0XFF,
0XFF,0XFF,0X7F,0XE0,0X01,0XFF,0XF8,0X11,0X87,0XFE,0X00,0X00,0X0F,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XE0,0X01,0XFF,0XF8,0X11,0XC3,0XFE,0X00,0X00,0X0F,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XE0,0X01,0XFF,0XF8,0X10,0XC3,0XFE,0X00,0X00,0X0F,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XE0,0X83,0XFF,0XFF,0X10,0X03,0XFE,0X00,0X00,0X0F,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XE1,0XE3,0XFF,0XFF,0X90,0X03,0XFE,0X00,0X00,0X3F,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XCC,0X01,0XFF,0X00,0X00,0X3F,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFC,0X01,0XFF,0X00,0X00,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XF8,0X01,0XFF,0XC0,0X00,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XF8,0X01,0XFF,0XE0,0X00,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFC,0X03,0XFF,0XFC,0X00,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFE,0X01,0XFF,0XFC,0X00,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0X81,0XFF,0XFC,0X00,0X7F,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFC,0X00,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFE,0X01,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0X87,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XCF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,0XFF,
]


lut_full_update= [
    0x80,0x60,0x40,0x00,0x00,0x00,0x00,             #LUT0: BB:     VS 0 ~7
    0x10,0x60,0x20,0x00,0x00,0x00,0x00,             #LUT1: BW:     VS 0 ~7
    0x80,0x60,0x40,0x00,0x00,0x00,0x00,             #LUT2: WB:     VS 0 ~7
    0x10,0x60,0x20,0x00,0x00,0x00,0x00,             #LUT3: WW:     VS 0 ~7
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,             #LUT4: VCOM:   VS 0 ~7

    0x03,0x03,0x00,0x00,0x02,                       # TP0 A~D RP0
    0x09,0x09,0x00,0x00,0x02,                       # TP1 A~D RP1
    0x03,0x03,0x00,0x00,0x02,                       # TP2 A~D RP2
    0x00,0x00,0x00,0x00,0x00,                       # TP3 A~D RP3
    0x00,0x00,0x00,0x00,0x00,                       # TP4 A~D RP4
    0x00,0x00,0x00,0x00,0x00,                       # TP5 A~D RP5
    0x00,0x00,0x00,0x00,0x00,                       # TP6 A~D RP6

    0x15,0x41,0xA8,0x32,0x30,0x0A,
]

lut_partial_update = [ #20 bytes
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,             #LUT0: BB:     VS 0 ~7
    0x80,0x00,0x00,0x00,0x00,0x00,0x00,             #LUT1: BW:     VS 0 ~7
    0x40,0x00,0x00,0x00,0x00,0x00,0x00,             #LUT2: WB:     VS 0 ~7
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,             #LUT3: WW:     VS 0 ~7
    0x00,0x00,0x00,0x00,0x00,0x00,0x00,             #LUT4: VCOM:   VS 0 ~7

    0x0A,0x00,0x00,0x00,0x00,                       # TP0 A~D RP0
    0x00,0x00,0x00,0x00,0x00,                       # TP1 A~D RP1
    0x00,0x00,0x00,0x00,0x00,                       # TP2 A~D RP2
    0x00,0x00,0x00,0x00,0x00,                       # TP3 A~D RP3
    0x00,0x00,0x00,0x00,0x00,                       # TP4 A~D RP4
    0x00,0x00,0x00,0x00,0x00,                       # TP5 A~D RP5
    0x00,0x00,0x00,0x00,0x00,                       # TP6 A~D RP6

    0x15,0x41,0xA8,0x32,0x30,0x0A,
]

EPD_WIDTH       = 128 # 122
EPD_HEIGHT      = 250


RST_PIN         = 12
DC_PIN          = 8
CS_PIN          = 9
BUSY_PIN        = 13

FULL_UPDATE = 0
PART_UPDATE = 1

class EPD_2in13(framebuf.FrameBuffer):
    def __init__(self):
        self.reset_pin = Pin(RST_PIN, Pin.OUT)
        self.dc_pin = Pin(DC_PIN, Pin.OUT)
        self.busy_pin = Pin(BUSY_PIN, Pin.IN, Pin.PULL_UP)
        self.cs_pin = Pin(CS_PIN, Pin.OUT)
        self.width = EPD_WIDTH
        self.height = EPD_HEIGHT
        
        self.full_lut = lut_full_update
        self.partial_lut = lut_partial_update
        
        self.full_update = FULL_UPDATE
        self.part_update = PART_UPDATE
        
        self.spi = SPI(1)
        self.spi.init(baudrate=4000_000)

        self.buffer = bytearray(self.height * self.width // 8)
        super().__init__(self.buffer, self.width, self.height, framebuf.MONO_HLSB)
        self.init(FULL_UPDATE)

    def digital_write(self, pin, value):
        pin.value(value)

    def digital_read(self, pin):
        return pin.value()

    def delay_ms(self, delaytime):
        utime.sleep(delaytime / 1000.0)

    def spi_writebyte(self, data):
        self.spi.write(bytearray(data))

    def module_exit(self):
        self.digital_write(self.reset_pin, 0)

    # Hardware reset
    def reset(self):
        self.digital_write(self.reset_pin, 1)
        self.delay_ms(50)
        self.digital_write(self.reset_pin, 0)
        self.delay_ms(2)
        self.digital_write(self.reset_pin, 1)
        self.delay_ms(50)   


    def send_command(self, command):
        self.digital_write(self.dc_pin, 0)
        self.digital_write(self.cs_pin, 0)
        self.spi_writebyte([command])
        self.digital_write(self.cs_pin, 1)

    def send_data(self, data):
        self.digital_write(self.dc_pin, 1)
        self.digital_write(self.cs_pin, 0)
        self.spi_writebyte([data])
        self.digital_write(self.cs_pin, 1)
        
    def ReadBusy(self):
        print('busy')
        while(self.digital_read(self.busy_pin) == 1):      # 0: idle, 1: busy
            self.delay_ms(10)    
        print('busy release')
        
    def TurnOnDisplay(self):
        self.send_command(0x22)
        self.send_data(0xC7)
        self.send_command(0x20)        
        self.ReadBusy()

    def TurnOnDisplayPart(self):
        self.send_command(0x22)
        self.send_data(0x0c)
        self.send_command(0x20)        
        self.ReadBusy()

    def init(self, update):
        print('init')
        self.reset()
        if(update == self.full_update):
            self.ReadBusy()
            self.send_command(0x12) # soft reset
            self.ReadBusy()

            self.send_command(0x74) #set analog block control
            self.send_data(0x54)
            self.send_command(0x7E) #set digital block control
            self.send_data(0x3B)

            self.send_command(0x01) #Driver output control
            self.send_data(0x27)
            self.send_data(0x01)
            self.send_data(0x01)
            
            self.send_command(0x11) #data entry mode
            self.send_data(0x01)

            self.send_command(0x44) #set Ram-X address start/end position
            self.send_data(0x00)
            self.send_data(0x0F)    #0x0C-->(15+1)*8=128

            self.send_command(0x45) #set Ram-Y address start/end position
            self.send_data(0x27)   #0xF9-->(249+1)=250
            self.send_data(0x01)
            self.send_data(0x2e)
            self.send_data(0x00)
            
            self.send_command(0x3C) #BorderWavefrom
            self.send_data(0x03)

            self.send_command(0x2C)     #VCOM Voltage
            self.send_data(0x55)    #

            self.send_command(0x03)
            self.send_data(self.full_lut[70])

            self.send_command(0x04) #
            self.send_data(self.full_lut[71])
            self.send_data(self.full_lut[72])
            self.send_data(self.full_lut[73])

            self.send_command(0x3A)     #Dummy Line
            self.send_data(self.full_lut[74])
            self.send_command(0x3B)     #Gate time
            self.send_data(self.full_lut[75])

            self.send_command(0x32)
            for count in range(70):
                self.send_data(self.full_lut[count])

            self.send_command(0x4E)   # set RAM x address count to 0
            self.send_data(0x00)
            self.send_command(0x4F)   # set RAM y address count to 0X127
            self.send_data(0x0)
            self.send_data(0x00)
            self.ReadBusy()
        else:
            self.send_command(0x2C)     #VCOM Voltage
            self.send_data(0x26)

            self.ReadBusy()

            self.send_command(0x32)
            for count in range(70):
                self.send_data(self.partial_lut[count])

            self.send_command(0x37)
            self.send_data(0x00)
            self.send_data(0x00)
            self.send_data(0x00)
            self.send_data(0x00)
            self.send_data(0x40)
            self.send_data(0x00)
            self.send_data(0x00)

            self.send_command(0x22)
            self.send_data(0xC0)
            self.send_command(0x20)
            self.ReadBusy()

            self.send_command(0x3C) #BorderWavefrom
            self.send_data(0x01)
        return 0       
        
    def display(self, image):
        self.send_command(0x24)
        for j in range(0, self.height):
            for i in range(0, int(self.width / 8)):
                self.send_data(image[i + j * int(self.width / 8)])   
        self.TurnOnDisplay()
        
    def displayPartial(self, image):
        self.send_command(0x24)
        for j in range(0, self.height):
            for i in range(0, int(self.width / 8)):
                self.send_data(image[i + j * int(self.width / 8)])   
                
        self.send_command(0x26)
        for j in range(0, self.height):
            for i in range(0, int(self.width / 8)):
                self.send_data(~image[i + j * int(self.width / 8)])  
        self.TurnOnDisplayPart()

    def displayPartBaseImage(self, image):
        self.send_command(0x24)
        for j in range(0, self.height):
            for i in range(0, int(self.width / 8)):
                self.send_data(image[i + j * int(self.width / 8)])   
                
        self.send_command(0x26)
        for j in range(0, self.height):
            for i in range(0, int(self.width / 8)):
                self.send_data(image[i + j * int(self.width / 8)])  
        self.TurnOnDisplay()
    
    def Clear(self, color):
        self.send_command(0x24)
        for j in range(0, self.height):
            for i in range(0, int(self.width / 8)):
                self.send_data(color)
        self.send_command(0x26)
        for j in range(0, self.height):
            for i in range(0, int(self.width / 8)):
                self.send_data(color)
                                
        self.TurnOnDisplay()

    def sleep(self):
        self.send_command(0x10) #enter deep sleep
        self.send_data(0x03)
        self.delay_ms(2000)
        self.module_exit()
        
        
if __name__=='__main__':
    epd = EPD_2in13()
    epd.Clear(0xff)

#    epd.displayPartBaseImage(Beeld)
    epd.display(Beeld)
#    epd.display(epd.buffer)
    epd.delay_ms(10000)
    epd.init(epd.full_update)
    epd.Clear(0xff)
    epd.delay_ms(2000)
    epd.sleep()