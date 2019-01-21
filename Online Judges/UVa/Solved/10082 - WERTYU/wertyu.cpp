#include <iostream>
#include <map>

using namespace std;

int main() {

    map<char,char> replaces;
    replaces['1'] = '`'; 
    replaces['2'] = '1';//"2" : "1", 
    replaces['3'] = '2';//"3" : "2", 
    replaces['4'] = '3';//"4" : "3", 
    replaces['5'] = '4';//"5" : "4", 
    replaces['6'] = '5';//"6" : "5", 
    replaces['7'] = '6';//"7" : "6", 
    replaces['8'] = '7';//"8" : "7", 
    replaces['9'] = '8';//"9" : "8", 
    replaces['0'] = '9';//"0" : "9", 
    replaces['-'] = '0';//"-" : "0", 
    replaces['='] = '-';//"=" : "-", 
    replaces['W'] = 'Q';//"W" : "Q", 
    replaces['E'] = 'W';//"E" : "W", 
    replaces['R'] = 'E';//"R" : "E", 
    replaces['T'] = 'R';//"T" : "R", 
    replaces['Y'] = 'T';//"Y" : "T", 
    replaces['U'] = 'Y';//"U" : "Y", 
    replaces['I'] = 'U';//"I" : "U", 
    replaces['O'] = 'I';//"O" : "I", 
    replaces['P'] = 'O';//"P" : "O", 
    replaces['['] = 'P';//"[" : "P", 
    replaces[']'] = '[';//"]" : "[", 
    replaces['\\'] = ']';//"\\" : "]", 
    replaces['S'] = 'A';//"S" : "A", 
    replaces['D'] = 'S';//"D" : "S", 
    replaces['F'] = 'D';//"F" : "D", 
    replaces['G'] = 'F';//"G" : "F", 
    replaces['H'] = 'G';//"H" : "G", 
    replaces['J'] = 'H';//"J" : "H", 
    replaces['K'] = 'J';//"K" : "J", 
    replaces['L'] = 'K';//"L" : "K", 
    replaces[';'] = 'L';//";" : "L", 
    replaces['\''] = ';';//"'" : ";", 
    replaces['X'] = 'Z';//"X" : "Z", 
    replaces['C'] = 'X';//"C" : "X", 
    replaces['V'] = 'C';//"V" : "C", 
    replaces['B'] = 'V';//"B" : "V", 
    replaces['N'] = 'B';//"N" : "B", 
    replaces['M'] = 'N';//"M" : "N", 
    replaces[','] = 'M';//"," : "M", 
    replaces['.'] = ',';//"." : ",", 
    replaces['/'] = '.';//"/" : ".",
    replaces[' '] = ' ';//" " : " "}

    char c;
    while (cin.get(c)) {
        if (replaces.count(c)) {
            c = replaces[c];
        }
        putchar(c);
    }
    return 0;
}