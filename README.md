# Medieval Tools

This is a place for me to store various, small coding projects that focus on medieval problems, 
such as converting money or distances.

I hope to grow these tools over time. If you have any projects that you think would be useful for you, 
please feel to request them. I am new to programming, but always up for a challenge.

## Money Conversion

The medieval system of money was complex and difficult to comprehend. Rather than being a decimal-based system, such as we are used to today, conversion between units was seemingly arbitrary. For example     There were:
* 12 denarii in a shilling.
* 160 denarii in a mark.
* 240 denarii in a pound.


The `money_conversion.py` program (and its accompanying `gui.py` user interface) give you the ability to easily convert between these various medieval monetary units.

To use the Money Converter:
* [Install python](https://realpython.com/installing-python/)
* Download the `money_conversion` directory
* Using your terminal (or command line) navigate to directory and the run `python gui.py`
* Enter the amount you want to convert into the "Enter Value" box. You may either press enter or the "Convert" button.
* The converted amounts will then display in the boxes below.
* You can convert as many times as you wish.
* Press exit or close the window when you are finished.

You can enter your amounts using either Roman or Arabic numerals. You may also use medieval Roman numeral notation (e.g. 'iiij' for 4).

It is important to note, however, that coin notations **must** come after the numbers (e.g. 'iiij l.' rather than '£4').


Here are some examples of valid inputs:

#### Valid Input

* iiij s. 4d
* 4m 6l
* VIJ m.
* 6 l. iij s xij d.


#### Invalid Input
*N.B.: The following will convert, they will simply ignore the pounds.*

* £6 iij s xij d.
* £.6 iij s xij d.