#!/usr/bin/evn python3

import sys

Zero = [
  '  ***  ',
  ' *   * ',
  '*     *',
  '*     *',
  '*     *',
  ' *   * ',
  '  ***  ']

One = [
  '   *   ',
  '  **   ',
  '   *   ',
  '   *   ',
  '   *   ',
  '   *   ',
  '  ***  ']

Two = [  
  '  ***  ',
  ' *   * ',
  '     * ',
  '    *  ',
  '   *   ',
  '  *    ',
  ' ***** ']

Three = [ 
  ' ***** ',
  '      *',
  '      *',
  '  **** ',
  '      *',
  '      *', 
  ' ***** ']

Four = [
  '    *  ',
  '   **  ',
  '  * *  ',
  ' *  *  ',
  '*   *  ',
  '*******',
  '    *  ']

Five = [
  ' ***** ',
  '*      ',
  '*      ',
  ' ***** ',
  '      *',
  '      *',
  ' ***** ']

Six = [
  ' ***** ',
  '*      ',
  '*      ',
  '* **** ',
  '*     *',
  '*     *',
  ' ***** ']

Seven = [
  '*******',
  '      *',
  '     * ',
  '    *  ',
  '   *   ',
  '  *    ',
  ' *     ']

Eight = [
  ' ***** ',
  '*     *',
  '*     *',
  ' ***** ',
  '*     *',
  '*     *',
  ' ***** ']
     
Nine = [
  ' ***** ',
  '*     *',
  '*     *',
  ' ***** ',
  '    *  ',
  '   *   ',
  '  *    ']

digits = [Zero, One, Two, Three, Four,
   Five, Six, Seven, Eight, Nine]


def disp_big_digits(digits_str):
    try:
        row = 0
        while(row < 7):
            line = ''
            col = 0
            while(col < len(digits_str)):
                line += digits[int(digits_str[col])][row] + ' '
                col += 1
            print(line)
            row += 1
    except IndexError:
        print("usage: bigdigits.py <number>")
    except ValueError as err:
        print(err, "in", digits)


a = sys.argv[1]
disp_big_digits(a)





 