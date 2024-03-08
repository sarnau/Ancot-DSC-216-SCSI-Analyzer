# DSC-216 Display Board by Humusoft

Humusoft seems to do data acquisition and control boards. This board has a copyright 1992,1994 revision 1.30 with a date of 09/20/94 and prints a copyright "ELC 1.11 ROM 1.30"

The display board als is based around a 68008 CPU. It communicates with the main unit via a serial interface, which is VT100 based for the 80x25 screen and sends keyboard codes back for key-presses (low byte first, which is the ASCII code, the high byte is for cursor keys, etc). It looks like a very generic board, which could be used for other hardware, except the firmware has the keyboard matrix hardcoded.

4 Fonts are part of the ROM, which can be rendered via the `Font_Firmware_Renderer.py` as png.

## ICs on the board:

- 1x Motorola MC68008FN8
- 1x Motorola MC68681FN for the communication with the main unit
- 1x Motorola MC68B45P for the video display
- 1x Intel P8279-5 at the keyboard decoder
- 3x Cypress CY7C199-25vc (32K x 8 SRAM)

## Memory map

- 0x00000000 - 0x00007FFF 32KB ROM
- 0x00010000 - 0x0001FFFF 64KB SRAM
- 0x00030000 - 0x00030000 DIP Switches
- 0x00040000 - 0x00040003 Intel P8279 (2 registers on the even addresses)
- 0x00050000 - 0x00057FFF 32KB SRAM as video memory for the MC68B45P
- 0x00060000 - 0x00060003 MC6845 (2 registers on the even addresses)
- 0x00070000 - 0x0007001F MC68681 (16 registers on the even addresses)

## MC68681

Buffer A is used to communicate with the main unit.
Buffer B is used to read keys from an IBM AT compatible keyboard.

The parallel port is used for outputting some bits.

- 0 Signal beeper, used for the BEL sound
- 1 not written to
- 2 not written to
- 3 used for bit banging communicated with the IBM AT keyboard
- 4 not written to
- 5 Select Video RAM page 0/1
- 6 Set if Video RAM page 0 fails the memory test. System then switches to page 1.
- 7 Enable cursor keys

## DIP Switches

The DIP switches are not populated on my board, but they are read by the firmware.

- 0-2 Baudrate (0:300, 1:600, 2:1200, 3:2400, 4:4800, 5:9600, 6:19200, 7:19200, BRF off)
- 3 Enable XON/XOFF support for serial communication
- 4 0:With Parity, 1:No Parity (do not work, because of SW#6)
- 5 0:7N, 1:8N Bits with odd parity (do not work, because of SW#6)
- 6 0:8N 1:8O (This overwrites the changes from SW#4 and SW#5)
- 7 Echo any keypress to the display

## VT100 implementation

