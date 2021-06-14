# Base "library" with:
# Defenition of screen array (Beeld[])
# Two character arrays:
#   TxTs = small 8x8 characters
#   TxTl = large 16x16 characters (same as small, but Horizontal and Vertical multiplied by 2)
# Several routines to draw lines (H and V), double lines (H and V)
# Rectangles (single and double lines)
# Print Small and Large text on screen
#
# PLUS...ofcourse the original E-Paper routines#

Beeld = [0XFF] * 4000

#Text small rotated
#GA=([0xF0,0x03,0xC0,0x00,0xC0,0xFC,0xCC,0x3C,0xCF,0x0C,0xC0,0x00,0xF0,0x03,0xFF,0xFF], #0
TxTs=([0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],     #(space)
[0xFF,0xFF,0xF9,0xA0,0xA0,0xF9,0xFF,0xFF],     #(!)
[0xFF,0xFC,0xFC,0xFF,0xFC,0xFC,0xFF,0xFF],     #(")
[0xEB,0x80,0x80,0xEB,0x80,0x80,0xEB,0xFF],     #(#)
[0xDB,0xD1,0x94,0x94,0xC5,0xED,0xFF,0xFF],     #($)
[0xB9,0x99,0xCF,0xE7,0xF3,0x99,0x9D,0xFF],     #(%)
[0xCF,0x85,0xB0,0xA2,0xC8,0x85,0xB7,0xFF],     #(&)
[0xFB,0xF8,0xFC,0xFF,0xFF,0xFF,0xFF,0xFF],     #(')
[0xFF,0xE3,0xC1,0x9C,0xBE,0xFF,0xFF,0xFF],     #(()
[0xFF,0xBE,0x9C,0xC1,0xE3,0xFF,0xFF,0xFF],     #())
[0xF7,0xD5,0xC1,0xE3,0xE3,0xC1,0xD5,0xF7],     #(*)
[0xF7,0xF7,0xC1,0xC1,0xF7,0xF7,0xFF,0xFF],     #(+)
[0xFF,0x7F,0x1F,0x9F,0xFF,0xFF,0xFF,0xFF],     #(
[0xF7,0xF7,0xF7,0xF7,0xF7,0xF7,0xFF,0xFF],     #(-)
[0xFF,0xFF,0x9F,0x9F,0xFF,0xFF,0xFF,0xFF],     #(.)
[0x9F,0xCF,0xE7,0xF3,0xF9,0xFC,0xFE,0xFF],     #(/)
[0xC1,0x80,0x8E,0xA6,0xB2,0x80,0xC1,0xFF],     #(0)
[0xBF,0xBD,0x80,0x80,0xBF,0xBF,0xFF,0xFF],     #(1)
[0x9D,0x8C,0xA6,0xB6,0x90,0x99,0xFF,0xFF],     #(2)
[0xDD,0x9C,0xB6,0xB6,0x80,0xC9,0xFF,0xFF],     #(3)
[0xE7,0xE3,0xE9,0xAC,0x80,0x80,0xAF,0xFF],     #(4)
[0xD8,0x98,0xBA,0xBA,0x82,0xC6,0xFF,0xFF],     #(5)
[0xC3,0x81,0xB4,0xB6,0x86,0xCF,0xFF,0xFF],     #(6)
[0xFC,0xFC,0x8E,0x86,0xF0,0xF8,0xFF,0xFF],     #(7)
[0xC9,0x80,0xB6,0xB6,0x80,0xC9,0xFF,0xFF],     #(8)
[0xF9,0xB0,0xB6,0x96,0xC0,0xE1,0xFF,0xFF],     #(9)
[0xFF,0xFF,0x99,0x99,0xFF,0xFF,0xFF,0xFF],     #(:)
[0xFF,0x7F,0x19,0x99,0xFF,0xFF,0xFF,0xFF],     #(
[0xF7,0xE3,0xC9,0x9C,0xBE,0xFF,0xFF,0xFF],     #(<)
[0xDB,0xDB,0xDB,0xDB,0xDB,0xDB,0xFF,0xFF],     #(=)
[0xFF,0xBE,0x9C,0xC9,0xE3,0xF7,0xFF,0xFF],     #(>)
[0xFD,0xFC,0xAE,0xA6,0xF0,0xF9,0xFF,0xFF],     #(?)
[0xC1,0x80,0xBE,0xA2,0xA2,0xE0,0xE1,0xFF],     #(@)
[0x83,0x81,0xEC,0xEC,0x81,0x83,0xFF,0xFF],     #(A)
[0xBE,0x80,0x80,0xB6,0xB6,0x80,0xC9,0xFF],     #(B)
[0xE3,0xC1,0x9C,0xBE,0xBE,0x9C,0xDD,0xFF],     #(C)
[0xBE,0x80,0x80,0xBE,0x9C,0xC1,0xE3,0xFF],     #(D)
[0xBE,0x80,0x80,0xB6,0xA2,0xBE,0x9C,0xFF],     #(E)
[0xBE,0x80,0x80,0xB6,0xE2,0xFE,0xFC,0xFF],     #(F)
[0xE3,0xC1,0x9C,0xBE,0xAE,0x8C,0x8D,0xFF],     #(G)
[0x80,0x80,0xF7,0xF7,0x80,0x80,0xFF,0xFF],     #(H)
[0xFF,0xBE,0x80,0x80,0xBE,0xFF,0xFF,0xFF],     #(I)
[0xCF,0x8F,0xBF,0xBE,0x80,0xC0,0xFE,0xFF],     #(J)
[0xBE,0x80,0x80,0xF7,0xE3,0x88,0x9C,0xFF],     #(K)
[0xBE,0x80,0x80,0xBE,0xBF,0x9F,0x8F,0xFF],     #(L)
[0x80,0x80,0xF1,0xE3,0xF1,0x80,0x80,0xFF],     #(M)
[0x80,0x80,0xF9,0xF3,0xE7,0x80,0x80,0xFF],     #(N)
[0xE3,0xC1,0x9C,0xBE,0x9C,0xC1,0xE3,0xFF],     #(O)
[0xBE,0x80,0x80,0xB6,0xF6,0xF0,0xF9,0xFF],     #(P)
[0xE1,0xC0,0xDE,0x8E,0x80,0xA1,0xFF,0xFF],     #(Q)
[0xBE,0x80,0x80,0xF6,0xE6,0x80,0x99,0xFF],     #(R)
[0xD9,0x90,0xB2,0xA6,0x8C,0xCD,0xFF,0xFF],     #(S)
[0xFC,0xBE,0x80,0x80,0xBE,0xFC,0xFF,0xFF],     #(T)
[0x80,0x80,0xBF,0xBF,0x80,0x80,0xFF,0xFF],     #(U)
[0xE0,0xC0,0x9F,0x9F,0xC0,0xE0,0xFF,0xFF],     #(V)
[0x80,0x80,0xCF,0xE7,0xCF,0x80,0x80,0xFF],     #(W)
[0xBC,0x98,0xC3,0xE7,0xC3,0x98,0xBC,0xFF],     #(X)
[0xF8,0xB0,0x87,0x87,0xB0,0xF8,0xFF,0xFF],     #(Y)
[0xB8,0x9C,0x8E,0xA6,0xB2,0x98,0x8C,0xFF],     #(Z)
[0xFF,0x80,0x80,0xBE,0xBE,0xFF,0xFF,0xFF],     #([)
[0xFE,0xFC,0xF9,0xF3,0xE7,0xCF,0x9F,0xFF],     #(\)
[0xFF,0xBE,0xBE,0x80,0x80,0xFF,0xFF,0xFF],     #(])
[0xF7,0xF3,0xF9,0xFC,0xF9,0xF3,0xF7,0xFF],     #(^)
[0x7F,0x7F,0x7F,0x7F,0x7F,0x7F,0x7F,0x7F],     #(_)
[0xFF,0xFF,0xFC,0xF8,0xFB,0xFF,0xFF,0xFF],     #(`)
[0xDF,0x8B,0xAB,0xAB,0xC3,0x87,0xBF,0xFF],     #(a)
[0xBE,0x80,0xC0,0xB7,0xB7,0x87,0xCF,0xFF],     #(b)
[0xC7,0x83,0xBB,0xBB,0x93,0xD7,0xFF,0xFF],     #(c)
[0xCF,0x87,0xB7,0xB6,0xC0,0x80,0xBF,0xFF],     #(d)
[0xC7,0x83,0xAB,0xAB,0xA3,0xE7,0xFF,0xFF],     #(e)
[0xB7,0x81,0x80,0xB6,0xFC,0xFD,0xFF,0xFF],     #(f)
[0x67,0x43,0x5B,0x5B,0x07,0x83,0xFB,0xFF],     #(g)
[0xBE,0x80,0x80,0xF7,0xFB,0x83,0x87,0xFF],     #(h)
[0xFF,0xBB,0x82,0x82,0xBF,0xFF,0xFF,0xFF],     #(i)
[0x9F,0x1F,0x7F,0x7F,0x02,0x82,0xFF,0xFF],     #(j)
[0xBE,0x80,0x80,0xEF,0xC7,0x93,0xBB,0xFF],     #(k)
[0xFF,0xBE,0x80,0x80,0xBF,0xFF,0xFF,0xFF],     #(l)
[0x83,0x83,0xE7,0xC7,0xE3,0x83,0x87,0xFF],     #(m)
[0x83,0x83,0xFB,0xFB,0x83,0x87,0xFF,0xFF],     #(n)
[0xC7,0x83,0xBB,0xBB,0x83,0xC7,0xFF,0xFF],     #(o)
[0x7B,0x03,0x07,0x5B,0xDB,0xC3,0xE7,0xFF],     #(p)
[0xE7,0xC3,0xDB,0x5B,0x07,0x03,0x7B,0xFF],     #(q)
[0xBB,0x83,0x87,0xB3,0xFB,0xE3,0xE7,0xFF],     #(r)
[0xB7,0xA3,0xAB,0xAB,0x8B,0xDB,0xFF,0xFF],     #(s)
[0xFF,0xFB,0xC1,0x80,0xBB,0xDB,0xFF,0xFF],     #(t)
[0xC3,0x83,0xBF,0xBF,0xC3,0x83,0xBF,0xFF],     #(u)
[0xE3,0xC3,0x9F,0x9F,0xC3,0xE3,0xFF,0xFF],     #(v)
[0xC3,0x83,0x8F,0xC7,0x8F,0x83,0xC3,0xFF],     #(w)
[0xBB,0x93,0xC7,0xEF,0xC7,0x93,0xBB,0xFF],     #(x)
[0x63,0x43,0x5F,0x5F,0x03,0x83,0xFF,0xFF],     #(y)
[0xB3,0x9B,0x8B,0xA3,0xB3,0x9B,0xFF,0xFF],     #(z)
[0xF7,0xF7,0xC1,0x88,0xBE,0xBE,0xFF,0xFF],     #()
[0xFF,0xFF,0xFF,0x88,0x88,0xFF,0xFF,0xFF],     #(|)
[0xBE,0xBE,0x88,0xC1,0xF7,0xF7,0xFF,0xFF],     #()
[0xFD,0xFC,0xFE,0xFC,0xFD,0xFC,0xFE,0xFF],     #(~)
)

TxTl=([0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #(space)
[0xFF,0xFF,0xFF,0xFF,0xFF,0xC3,0xCC,0x00,0xCC,0x00,0xFF,0xC3,0xFF,0xFF,0xFF,0xFF],  #(!)
[0xFF,0xFF,0xFF,0xF0,0xFF,0xF0,0xFF,0xFF,0xFF,0xF0,0xFF,0xF0,0xFF,0xFF,0xFF,0xFF],  #(")
[0xFC,0xCF,0xC0,0x00,0xC0,0x00,0xFC,0xCF,0xC0,0x00,0xC0,0x00,0xFC,0xCF,0xFF,0xFF],  #(#)
[0xF3,0xCF,0xF3,0x03,0xC3,0x30,0xC3,0x30,0xF0,0x33,0xFC,0xF3,0xFF,0xFF,0xFF,0xFF],  #($)
[0xCF,0xC3,0xC3,0xC3,0xF0,0xFF,0xFC,0x3F,0xFF,0x0F,0xC3,0xC3,0xC3,0xF3,0xFF,0xFF],  #(%)
[0xF0,0xFF,0xC0,0x33,0xCF,0x00,0xCC,0x0C,0xF0,0xC0,0xC0,0x33,0xCF,0x3F,0xFF,0xFF],  #(&)
[0xFF,0xCF,0xFF,0xC0,0xFF,0xF0,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #(')
[0xFF,0xFF,0xFC,0x0F,0xF0,0x03,0xC3,0xF0,0xCF,0xFC,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #(()
[0xFF,0xFF,0xCF,0xFC,0xC3,0xF0,0xF0,0x03,0xFC,0x0F,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #())
[0xFF,0x3F,0xF3,0x33,0xF0,0x03,0xFC,0x0F,0xFC,0x0F,0xF0,0x03,0xF3,0x33,0xFF,0x3F],  #(*)
[0xFF,0x3F,0xFF,0x3F,0xF0,0x03,0xF0,0x03,0xFF,0x3F,0xFF,0x3F,0xFF,0xFF,0xFF,0xFF],  #(+)
[0xFF,0xFF,0x3F,0xFF,0x03,0xFF,0xC3,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #(
[0xFF,0x3F,0xFF,0x3F,0xFF,0x3F,0xFF,0x3F,0xFF,0x3F,0xFF,0x3F,0xFF,0xFF,0xFF,0xFF],  #(-)
[0xFF,0xFF,0xFF,0xFF,0xC3,0xFF,0xC3,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #(.)
[0xC3,0xFF,0xF0,0xFF,0xFC,0x3F,0xFF,0x0F,0xFF,0xC3,0xFF,0xF0,0xFF,0xFC,0xFF,0xFF],  #(/)
[0xF0,0x03,0xC0,0x00,0xC0,0xFC,0xCC,0x3C,0xCF,0x0C,0xC0,0x00,0xF0,0x03,0xFF,0xFF],  #(0)
[0xCF,0xFF,0xCF,0xF3,0xC0,0x00,0xC0,0x00,0xCF,0xFF,0xCF,0xFF,0xFF,0xFF,0xFF,0xFF],  #(1)
[0xC3,0xF3,0xC0,0xF0,0xCC,0x3C,0xCF,0x3C,0xC3,0x00,0xC3,0xC3,0xFF,0xFF,0xFF,0xFF],  #(2)
[0xF3,0xF3,0xC3,0xF0,0xCF,0x3C,0xCF,0x3C,0xC0,0x00,0xF0,0xC3,0xFF,0xFF,0xFF,0xFF],  #(3)
[0xFC,0x3F,0xFC,0x0F,0xFC,0xC3,0xCC,0xF0,0xC0,0x00,0xC0,0x00,0xCC,0xFF,0xFF,0xFF],  #(4)
[0xF3,0xC0,0xC3,0xC0,0xCF,0xCC,0xCF,0xCC,0xC0,0x0C,0xF0,0x3C,0xFF,0xFF,0xFF,0xFF],  #(5)
[0xF0,0x0F,0xC0,0x03,0xCF,0x30,0xCF,0x3C,0xC0,0x3C,0xF0,0xFF,0xFF,0xFF,0xFF,0xFF],  #(6)
[0xFF,0xF0,0xFF,0xF0,0xC0,0xFC,0xC0,0x3C,0xFF,0x00,0xFF,0xC0,0xFF,0xFF,0xFF,0xFF],  #(7)
[0xF0,0xC3,0xC0,0x00,0xCF,0x3C,0xCF,0x3C,0xC0,0x00,0xF0,0xC3,0xFF,0xFF,0xFF,0xFF],  #(8)
[0xFF,0xC3,0xCF,0x00,0xCF,0x3C,0xC3,0x3C,0xF0,0x00,0xFC,0x03,0xFF,0xFF,0xFF,0xFF],  #(9)
[0xFF,0xFF,0xFF,0xFF,0xC3,0xC3,0xC3,0xC3,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #(:)
[0xFF,0xFF,0x3F,0xFF,0x03,0xC3,0xC3,0xC3,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #(
[0xFF,0x3F,0xFC,0x0F,0xF0,0xC3,0xC3,0xF0,0xCF,0xFC,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #(<)
[0xF3,0xCF,0xF3,0xCF,0xF3,0xCF,0xF3,0xCF,0xF3,0xCF,0xF3,0xCF,0xFF,0xFF,0xFF,0xFF],  #(=)
[0xFF,0xFF,0xCF,0xFC,0xC3,0xF0,0xF0,0xC3,0xFC,0x0F,0xFF,0x3F,0xFF,0xFF,0xFF,0xFF],  #(>)
[0xFF,0xF3,0xFF,0xF0,0xCC,0xFC,0xCC,0x3C,0xFF,0x00,0xFF,0xC3,0xFF,0xFF,0xFF,0xFF],  #(?)
[0xF0,0x03,0xC0,0x00,0xCF,0xFC,0xCC,0x0C,0xCC,0x0C,0xFC,0x00,0xFC,0x03,0xFF,0xFF],  #(@)
[0xC0,0x0F,0xC0,0x03,0xFC,0xF0,0xFC,0xF0,0xC0,0x03,0xC0,0x0F,0xFF,0xFF,0xFF,0xFF],  #(A)
[0xCF,0xFC,0xC0,0x00,0xC0,0x00,0xCF,0x3C,0xCF,0x3C,0xC0,0x00,0xF0,0xC3,0xFF,0xFF],  #(B)
[0xFC,0x0F,0xF0,0x03,0xC3,0xF0,0xCF,0xFC,0xCF,0xFC,0xC3,0xF0,0xF3,0xF3,0xFF,0xFF],  #(C)
[0xCF,0xFC,0xC0,0x00,0xC0,0x00,0xCF,0xFC,0xC3,0xF0,0xF0,0x03,0xFC,0x0F,0xFF,0xFF],  #(D)
[0xCF,0xFC,0xC0,0x00,0xC0,0x00,0xCF,0x3C,0xCC,0x0C,0xCF,0xFC,0xC3,0xF0,0xFF,0xFF],  #(E)
[0xCF,0xFC,0xC0,0x00,0xC0,0x00,0xCF,0x3C,0xFC,0x0C,0xFF,0xFC,0xFF,0xF0,0xFF,0xFF],  #(F)
[0xFC,0x0F,0xF0,0x03,0xC3,0xF0,0xCF,0xFC,0xCC,0xFC,0xC0,0xF0,0xC0,0xF3,0xFF,0xFF],  #(G)
[0xC0,0x00,0xC0,0x00,0xFF,0x3F,0xFF,0x3F,0xC0,0x00,0xC0,0x00,0xFF,0xFF,0xFF,0xFF],  #(H)
[0xFF,0xFF,0xCF,0xFC,0xC0,0x00,0xC0,0x00,0xCF,0xFC,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #(I)
[0xF0,0xFF,0xC0,0xFF,0xCF,0xFF,0xCF,0xFC,0xC0,0x00,0xF0,0x00,0xFF,0xFC,0xFF,0xFF],  #(J)
[0xCF,0xFC,0xC0,0x00,0xC0,0x00,0xFF,0x3F,0xFC,0x0F,0xC0,0xC0,0xC3,0xF0,0xFF,0xFF],  #(K)
[0xCF,0xFC,0xC0,0x00,0xC0,0x00,0xCF,0xFC,0xCF,0xFF,0xC3,0xFF,0xC0,0xFF,0xFF,0xFF],  #(L)
[0xC0,0x00,0xC0,0x00,0xFF,0x03,0xFC,0x0F,0xFF,0x03,0xC0,0x00,0xC0,0x00,0xFF,0xFF],  #(M)
[0xC0,0x00,0xC0,0x00,0xFF,0xC3,0xFF,0x0F,0xFC,0x3F,0xC0,0x00,0xC0,0x00,0xFF,0xFF],  #(N)
[0xFC,0x0F,0xF0,0x03,0xC3,0xF0,0xCF,0xFC,0xC3,0xF0,0xF0,0x03,0xFC,0x0F,0xFF,0xFF],  #(O)
[0xCF,0xFC,0xC0,0x00,0xC0,0x00,0xCF,0x3C,0xFF,0x3C,0xFF,0x00,0xFF,0xC3,0xFF,0xFF],  #(P)
[0xFC,0x03,0xF0,0x00,0xF3,0xFC,0xC0,0xFC,0xC0,0x00,0xCC,0x03,0xFF,0xFF,0xFF,0xFF],  #(Q)
[0xCF,0xFC,0xC0,0x00,0xC0,0x00,0xFF,0x3C,0xFC,0x3C,0xC0,0x00,0xC3,0xC3,0xFF,0xFF],  #(R)
[0xF3,0xC3,0xC3,0x00,0xCF,0x0C,0xCC,0x3C,0xC0,0xF0,0xF0,0xF3,0xFF,0xFF,0xFF,0xFF],  #(S)
[0xFF,0xF0,0xCF,0xFC,0xC0,0x00,0xC0,0x00,0xCF,0xFC,0xFF,0xF0,0xFF,0xFF,0xFF,0xFF],  #(T)
[0xC0,0x00,0xC0,0x00,0xCF,0xFF,0xCF,0xFF,0xC0,0x00,0xC0,0x00,0xFF,0xFF,0xFF,0xFF],  #(U)
[0xFC,0x00,0xF0,0x00,0xC3,0xFF,0xC3,0xFF,0xF0,0x00,0xFC,0x00,0xFF,0xFF,0xFF,0xFF],  #(V)
[0xC0,0x00,0xC0,0x00,0xF0,0xFF,0xFC,0x3F,0xF0,0xFF,0xC0,0x00,0xC0,0x00,0xFF,0xFF],  #(W)
[0xCF,0xF0,0xC3,0xC0,0xF0,0x0F,0xFC,0x3F,0xF0,0x0F,0xC3,0xC0,0xCF,0xF0,0xFF,0xFF],  #(X)
[0xFF,0xC0,0xCF,0x00,0xC0,0x3F,0xC0,0x3F,0xCF,0x00,0xFF,0xC0,0xFF,0xFF,0xFF,0xFF],  #(Y)
[0xCF,0xC0,0xC3,0xF0,0xC0,0xFC,0xCC,0x3C,0xCF,0x0C,0xC3,0xC0,0xC0,0xF0,0xFF,0xFF],  #(Z)
[0xFF,0xFF,0xC0,0x00,0xC0,0x00,0xCF,0xFC,0xCF,0xFC,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #([)
[0xFF,0xFC,0xFF,0xF0,0xFF,0xC3,0xFF,0x0F,0xFC,0x3F,0xF0,0xFF,0xC3,0xFF,0xFF,0xFF],  #(\)
[0xFF,0xFF,0xCF,0xFC,0xCF,0xFC,0xC0,0x00,0xC0,0x00,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #(])
[0xFF,0x3F,0xFF,0x0F,0xFF,0xC3,0xFF,0xF0,0xFF,0xC3,0xFF,0x0F,0xFF,0x3F,0xFF,0xFF],  #(^)
[0x3F,0xFF,0x3F,0xFF,0x3F,0xFF,0x3F,0xFF,0x3F,0xFF,0x3F,0xFF,0x3F,0xFF,0x3F,0xFF],  #(_)
[0xFF,0xFF,0xFF,0xFF,0xFF,0xF0,0xFF,0xC0,0xFF,0xCF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #(`)
[0xF3,0xFF,0xC0,0xCF,0xCC,0xCF,0xCC,0xCF,0xF0,0x0F,0xC0,0x3F,0xCF,0xFF,0xFF,0xFF],  #(a)
[0xCF,0xFC,0xC0,0x00,0xF0,0x00,0xCF,0x3F,0xCF,0x3F,0xC0,0x3F,0xF0,0xFF,0xFF,0xFF],  #(b)
[0xF0,0x3F,0xC0,0x0F,0xCF,0xCF,0xCF,0xCF,0xC3,0x0F,0xF3,0x3F,0xFF,0xFF,0xFF,0xFF],  #(c)
[0xF0,0xFF,0xC0,0x3F,0xCF,0x3F,0xCF,0x3C,0xF0,0x00,0xC0,0x00,0xCF,0xFF,0xFF,0xFF],  #(d)
[0xF0,0x3F,0xC0,0x0F,0xCC,0xCF,0xCC,0xCF,0xCC,0x0F,0xFC,0x3F,0xFF,0xFF,0xFF,0xFF],  #(e)
[0xCF,0x3F,0xC0,0x03,0xC0,0x00,0xCF,0x3C,0xFF,0xF0,0xFF,0xF3,0xFF,0xFF,0xFF,0xFF],  #(f)
[0x3C,0x3F,0x30,0x0F,0x33,0xCF,0x33,0xCF,0x00,0x3F,0xC0,0x0F,0xFF,0xCF,0xFF,0xFF],  #(g)
[0xCF,0xFC,0xC0,0x00,0xC0,0x00,0xFF,0x3F,0xFF,0xCF,0xC0,0x0F,0xC0,0x3F,0xFF,0xFF],  #(h)
[0xFF,0xFF,0xCF,0xCF,0xC0,0x0C,0xC0,0x0C,0xCF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #(i)
[0xC3,0xFF,0x03,0xFF,0x3F,0xFF,0x3F,0xFF,0x00,0x0C,0xC0,0x0C,0xFF,0xFF,0xFF,0xFF],  #(j)
[0xCF,0xFC,0xC0,0x00,0xC0,0x00,0xFC,0xFF,0xF0,0x3F,0xC3,0x0F,0xCF,0xCF,0xFF,0xFF],  #(k)
[0xFF,0xFF,0xCF,0xFC,0xC0,0x00,0xC0,0x00,0xCF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #(l)
[0xC0,0x0F,0xC0,0x0F,0xFC,0x3F,0xF0,0x3F,0xFC,0x0F,0xC0,0x0F,0xC0,0x3F,0xFF,0xFF],  #(m)
[0xC0,0x0F,0xC0,0x0F,0xFF,0xCF,0xFF,0xCF,0xC0,0x0F,0xC0,0x3F,0xFF,0xFF,0xFF,0xFF],  #(n)
[0xF0,0x3F,0xC0,0x0F,0xCF,0xCF,0xCF,0xCF,0xC0,0x0F,0xF0,0x3F,0xFF,0xFF,0xFF,0xFF],  #(o)
[0x3F,0xCF,0x00,0x0F,0x00,0x3F,0x33,0xCF,0xF3,0xCF,0xF0,0x0F,0xFC,0x3F,0xFF,0xFF],  #(p)
[0xFC,0x3F,0xF0,0x0F,0xF3,0xCF,0x33,0xCF,0x00,0x3F,0x00,0x0F,0x3F,0xCF,0xFF,0xFF],  #(q)
[0xCF,0xCF,0xC0,0x0F,0xC0,0x3F,0xCF,0x0F,0xFF,0xCF,0xFC,0x0F,0xFC,0x3F,0xFF,0xFF],  #(r)
[0xCF,0x3F,0xCC,0x0F,0xCC,0xCF,0xCC,0xCF,0xC0,0xCF,0xF3,0xCF,0xFF,0xFF,0xFF,0xFF],  #(s)
[0xFF,0xFF,0xFF,0xCF,0xF0,0x03,0xC0,0x00,0xCF,0xCF,0xF3,0xCF,0xFF,0xFF,0xFF,0xFF],  #(t)
[0xF0,0x0F,0xC0,0x0F,0xCF,0xFF,0xCF,0xFF,0xF0,0x0F,0xC0,0x0F,0xCF,0xFF,0xFF,0xFF],  #(u)
[0xFC,0x0F,0xF0,0x0F,0xC3,0xFF,0xC3,0xFF,0xF0,0x0F,0xFC,0x0F,0xFF,0xFF,0xFF,0xFF],  #(v)
[0xF0,0x0F,0xC0,0x0F,0xC0,0xFF,0xF0,0x3F,0xC0,0xFF,0xC0,0x0F,0xF0,0x0F,0xFF,0xFF],  #(w)
[0xCF,0xCF,0xC3,0x0F,0xF0,0x3F,0xFC,0xFF,0xF0,0x3F,0xC3,0x0F,0xCF,0xCF,0xFF,0xFF],  #(x)
[0x3C,0x0F,0x30,0x0F,0x33,0xFF,0x33,0xFF,0x00,0x0F,0xC0,0x0F,0xFF,0xFF,0xFF,0xFF],  #(y)
[0xCF,0x0F,0xC3,0xCF,0xC0,0xCF,0xCC,0x0F,0xCF,0x0F,0xC3,0xCF,0xFF,0xFF,0xFF,0xFF],  #(z)
[0xFF,0x3F,0xFF,0x3F,0xF0,0x03,0xC0,0xC0,0xCF,0xFC,0xCF,0xFC,0xFF,0xFF,0xFF,0xFF],  #()
[0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xC0,0xC0,0xC0,0xC0,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF],  #(|)
[0xCF,0xFC,0xCF,0xFC,0xC0,0xC0,0xF0,0x03,0xFF,0x3F,0xFF,0x3F,0xFF,0xFF,0xFF,0xFF],  #()
[0xFF,0xF3,0xFF,0xF0,0xFF,0xFC,0xFF,0xF0,0xFF,0xF3,0xFF,0xF0,0xFF,0xFC,0xFF,0xFF],  #(~)
)



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
  
#Draw Horizontal Lines - coordinates are absolute values
def LineHor(xs, ys, xe):
    #Only horizontal lines
    #xs=xpos start, ys=ypos, xe=xpos end 
    for n in range(0, (xe-xs+1), 1):
        #now pixel for pixel. Every x-step = 16 bytes!
        xpos = int((xs + n) * 16)
        #ypos is constructed:
        #  - //8 to calculate the byte
        #  - then calculate which bit
        yp_byte = ys // 8
        yp_bit = (ys - yp_byte * 8)
        #in array is de offset xpos+yp_byte
        xypos = xpos + yp_byte
        #pixel is 0, dus een bitwise AND met 1111011111 (0 op plek pixel)
        Beeld[xypos] = Beeld[xypos] & (~(128>>yp_bit))
    return 0
#Draw Vertical Lines - coordinates are absolute values
def LineVer(xs, ys, ye):
    #Only horizontal lines
    #xs=xpos, ys=ypos start, ye=epos end
    xpos = xs * 16
    for n in range(ys, ye + 1,1):
        #determine start byte y pos
        yp_byte = n // 8
        #determine bit(=pixel)
        yp_bit = (n - yp_byte * 8)
        #in array is de offset xpos+yp_byte
        xypos = xpos + yp_byte
        Beeld[xypos] = Beeld[xypos] & (~(128>>yp_bit))
    return 0
#Rectangle: absolute(x,y) and relative x (to the right) and y (upwards)
def Rect(xs, ys, xre, yre):
    LineHor(xs, ys, xs+xre)
    LineHor(xs, ys+yre, xs+xre)
    LineVer(xs, ys, ys+yre)
    LineVer(xs+xre, ys, ys+yre)
    return 0    
#DoubleLines Horizontal - 2nd goes 1 pixel above
def DLineH(xs, ys, xe):
    LineHor(xs, ys, xe)
    LineHor(xs, ys+1, xe)
    return 0
#DoubleLines Vertical - 2nd line goes 1 pixel to the right
def DLineV(xs, ys, ye):
    LineVer(xs, ys, ye)
    LineVer(xs+1, ys, ye)
    return 0
#Double-line rectangle
def DRect(xs, ys, xre, yre):
    DLineH(xs, ys, xs+xre)
    DLineH(xs, ys+yre, xs+xre)
    DLineV(xs, ys, ys+yre)
    DLineV(xs+xre, ys, ys+yre)
    return 0

#Print Small Text on screen: Txt, xpos, ypos (ypos per byte, so 0-15 lines, 0=below)    
#Mind you: the Y-position is in bytes, which goes from 0-15 !! (so not pixels)
#Thru is if text is deleting pixels in background or not. 0=empty it, <>0 keep background
def PrtStxt(txt, xs, ybs, thru):
    #Loop per character in text
    for xchar in range(0, len(txt), 1):
        #offset(os) in character-array equals ascii code minus 32, <space>=0 not 32
        os = ord(txt[xchar])-32
        #each character has 8 bytes with pixels, loop through them
        for charline in range(0, 8, 1):
            #position in screen array =
            #x-start PLUS (Character-in-Text + byteNr-in-character*8)*16 + y-offset
            #Mind you: one pixel row to right is + 16 bytes 
            pos = (xs + xchar*8 + charline) * 16 + ybs
            #character pattern bits
            charbits = TxTs[os][charline]
            if (thru==0):
                Beeld[pos] = charbits
            else:
                Beeld[pos] = ~(~Beeld[pos] | ~charbits)    
    return 0
def PrtLtxt(txt, xs, ybs, thru):
    #per character
    for xchar in range(0, len(txt), 1):
        os = ord(txt[xchar])-32
        for charline in range(0, 16, 2):
            pos = (xs + xchar*16 + charline) * 16 + ybs
            charbits = TxTl[os][charline]
            if (thru==0):
                Beeld[pos] = charbits
                Beeld[pos+16] = charbits    #Large character is twice the same byte (horizontal)
            else:
                Beeld[pos] = ~(~Beeld[pos] | ~charbits)
                Beeld[pos+16] = ~(~Beeld[pos+16] | ~charbits)
            #twice as big
            pos = (xs + xchar*16 + charline) * 16 + ybs + 1
            charbits = TxTl[os][charline+1]
            if (thru==0):
                Beeld[pos] = charbits
                Beeld[pos+16] = charbits    #Large character is twice the same byte (horizontal)
            else:
                Beeld[pos] = ~(~Beeld[pos] | ~charbits)
                Beeld[pos+16] = ~(~Beeld[pos+16] | ~charbits)           
    return 0
