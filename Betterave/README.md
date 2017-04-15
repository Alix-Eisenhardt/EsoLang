# A simple python interpreter for [Betterave](https://esolangs.org/wiki/Betterave)

Betterave is a functionnal esoteric programming language.  
As the Ruby interpreter linked in the Esolangs article did not work for me, I decided to make my own interpreter.

### Please note that this interpreter is not complete

__TODO:__

* `:` Input an integer and return its value.
* `;` Input a string, add it to the string list, return the index of the string. 
* `&` Append to the string designed by the index returned by the next function the ASCII character returned by the function after.
* `#` Same as `&` but appends a number.
* `\` Return the ASCII code of the first character of a string and delete it from the string.
* `_` Delete a string and return the index of the string deleted
