# POSIX shell script kit

The POSIX shell script kit is one file of helper functions and constants.

These work for bash, zsh, ksh, dash, sh, and any other modern POSIX shell.

You can include this file in your own scripts, or copy anything you want.

This file is free libre open source software, created by SixArm.

Constructive feedback is welcome and appreciated.

To download this file:

```sh
curl -O "https://raw.githubusercontent.com/SixArm/posix-shell-script-kit/main/posix-shell-script-kit"
```

To include this file in your own script, in the same directory:

```sh
# Include https://github.com/SixArm/posix-shell-script-kit
. "$(dirname "$(readlink -f "$0")")/posix-shell-script-kit"
```

## Tracking

* Package: posix-shell-script-kit
* Version: 11.1.0
* Created: 2017-08-22T00:00:00Z
* Updated: 2023-03-28T14:01:52Z
* Website: https://github.com/sixarm/posix-shell-script-kit
* License: GPL-2.0 or GPL-3.0 or contact us for more
* Contact: Joel Parker Henderson (joel@sixarm.com)

## Input/output helpers

### out

Print output message to stdout.

```sh
out "my message"
STDOUT=> my message
```

### err

Print error message to stderr.

```sh
err "my message"
STDERR=> my message
```

### die

Print error message to stderr, then exit with an error code.

```sh
die 1 "my message"
STDERR=> my message
=> exit 1
```

### big

Print a big banner to stdout, good for human readability.

```sh
big "my message"
=>
###
#
# my message
#
###
```

### log

Print a datestamp, unique random id, hostname, process id, and message.

```sh
log "my message"
=> 2021-05-04T22:57:54.000000000+00:00 7e7151dc24bd511098ebb248771d8ffb abc.example.com 1234 my message
```

### zid

Generate a 32-bit secure random lowercase hex identifier.

```sh
zid
=> 78577554e967951388b5907854b4c337
```

### ask

Prompt the user for a line of input, then return a trimmed string.

```sh
ask
=> prompt
```

## Date & time helpers

### now

Get a datetime using our preferred ISO format.

```sh
now
=> 2021-05-04T22:59:28.769653000+00:00
```

Example with a custom datetime:

```sh
now -d "2021-01-01"
=> 2021-01-01T00:00:00.000000000+00:00
```

### now_date

Get a date using our preferred ISO format.

```sh
now_date
=> 2021-05-04
```

Example with a custom date, if your date command offers option -d:

```sh
now_date -d "January 1, 2021"
=> 2021-01-01
```

### sec

Get the current time in POSIX seconds.

```sh
sec
=> 1620169178
```

### age

Get the age of a given time in POSIX seconds.

```sh
age 1620169178
=> 19
```

### newer

Is the age of a given time newer than a given number of seconds?

```sh
newer 2000000000 && echo "true" || echo "false
=> true
```

### older

Is the age of a given time older than a given number of seconds?

```sh
older 1000000000 && echo "true" || echo "false"
=> true
```

## Validation helpers

### command_exists

Does a command exist?

```sh
command_exists grep
=> true

command_exists curl
=> false
```

### command_exists_or_die

Ensure a command exists, otherwise die with a help message.

```sh
command_exists_or_die grep
=> true

command_exists_or_die loremipsum
STDERR=> Command needed: loremipsum
=> exit 1
```

### command_version_exists_or_die

Ensure a command exists and version is sufficient, otherwise die with a help message.

```sh
command_version_exists_or_die grep 1.1 2.2
=> true

command_version_exists_or_die grep 3.3 2.2
STDERR=> Command version needed: grep >= 3.3 (not 2.2)
=> exit 1
```

### var_exists

Does a variable exist?

```sh
var_exists HOME
=> true

var_exists FOO
=> false
```

### var_exists_or_die

Ensure a variable exists, otherwise die with a help message.

```sh
var_exists_or_die HOME
=> true

var_exists_or_die FOO
STDERR=> Variable needed: FOO
=> exit 1
```

### version

Is a version sufficient?

```sh
version 1.1 2.2
=> true

version 3.3 2.2
=> false
```

### version_or_die

Ensure a version is sufficient, otherwise die with a help message.

```sh
version_or_die 1.1 2.2
=> true

version_or_die 3.3 2.2
STDERR=> Version needed: >= 3.3 (not 2.2)
```

## Number helpers

### int

Convert a number string to an integer number string.

```sh
int 1.23
=> 1
```

### sum

Print the sum of numbers.

```sh
sum 1 2 3
=> 6
```

## Comparison helpers

### cmp_alnums

Compare alnums as groups, such as for word version strings.

```sh
cmp_alnums "a.b.c" "a.b.d"
# => -1 (negative one means left < right)
```

### cmp_digits

Compare digits as groups, such as for number version strings.

```sh
cmp_digits "1.2.3" "1.2.4"
# => -1 (negative one means left < right)
```

## Extensibility helpers

### dot_all

Source all the executable files in a given directory and subdirectories.

```sh
dot_all ~/temp
=> . ~/temp/a.sh
=> . ~/temp/b.pl
=> . ~/temp/c.js
```

### run_all

Run all the executable commands in a given directory and subdirectories.

```sh
run_all ~/temp
=> ~/temp/a.sh
=> ~/temp/b.pl
=> ~/temp/c.js
```

### sh_all

Shell all the executable commands in a given directory and subdirectories.

```sh
sh_all ~/temp
=> sh -c ~/temp/a.sh
=> sh -c ~/temp/b.pl
=> sh -c ~/temp/c.js
```

### rm_all

Remove all files in a given directory and subdirectories-- use with caution.

```sh
rm_all ~/temp
=> rm ~/temp/a.sh
=> rm ~/temp/b.pl
=> rm ~/temp/c.js
```

## Text helpers

### trim

Remove any space characters at the text's start or finish.

```sh
trim "  foo  "
=> foo
```

### slug

Convert a string from any characters to solely lowercase and single internal dash characters.

```sh
slug "**Foo** **Goo** **Hoo**"
=> foo-goo-hoo
```

### slugs

Convert a string from any characters to solely lowercase and single internal dash characters and slash characters.

```sh
slugs "**Foo** / **Goo** / **Hoo**"
=> foo/goo/hoo
```

### upper_format

Convert text from any lowercase letters to uppercase letters.

```sh
upper_format AbCdEf
=> ABCDEF
```

### lower_format

Convert text from any uppercase letters to lowercase letters.

```sh
lower_format AbCdEf
=> abcdef
```

### chain_format

Convert a string from any characters to solely alphanumeric and single internal dash characters.

```sh
chain_format "**Foo** **Goo** **Hoo**"
=> Foo-Goo-Hoo
```

### snake_format

Convert a string from any characters to solely alphanumeric and single internal underscore characters.

```sh
snake_format "**Foo** **Goo** **Hoo**"
=> Foo_Goo_Hoo
```

### space_format

Convert a string from any characters to solely alphanumeric and single internal space characters.

```sh
space_format "**Foo** **Goo** **Hoo**"
=> Foo Goo Hoo
```

### touch_format

Convert a string from any characters to solely a command "touch -t" timestamp format.

```sh
touch_format "Foo  2021-05-04 22:57:54 Goo"
=> 202105042257.54
```

### select_character_class

Get a string's characters that match a class, with optional offset and length.

Syntax: 

```sh
select_character_class <string> <class> [offset [length]]
```

Example with character class:

```sh
select_character_class foo123goo456 alpha
=> foogoo
```

Example with character class and substring offset:

```sh
select_character_class foo123goo456 alpha 3
=> goo
```

Example with character class and substring offset and length:

```sh
select_character_class foo123goo456 alpha 3 1
=> g
```

### reject_character_class

Get a string's characters that don't match a class, with optional offset and length.

Syntax: 

```sh
reject_character_class <string> <class> [offset [length]]
```

Exapmle with character class:

```sh
reject_character_class foo123goo456 alpha
=> 123456
```

Example with character class and substring offset:

```sh
reject_character_class foo123goo456 alpha 3
=> 456
```

Example with character class and substring offset and length:

```sh
reject_character_class foo123goo456 alpha 3 1
=> 4
```

## Random character helpers

### random_char

Generate random characters

Syntax:
```sh
random_char [characters [length]]
```

Example:
```sh
random_char ABCDEF 8
=> CBACBFDD
```

Example hexadecimal digit uppercase:
```sh
random_char 0-9A-F 8
=> FC56A95C
```

Example character class for uppercase letters:
```sh
random_char '[:upper:]' 8
=> ZMGIQBJB
```

POSiX character classes for ASCII characters:
```
Class       Pattern        Description
----------  -------------  -----------
[:upper:]   [A-Z]          uppercase letters
[:lower:]   [a-z]          lowercase letters
[:alpha:]   [A-Za-z]       uppercase letters and lowercase letters
[:alnum:]   [A-Za-z0-9]    uppercase letters and lowercase letters and digits
[:digit:]   [0-9]          digits
[:xdigit:]  [0-9A-Fa-f]    hexadecimal digits
[:punct:]                  punctuation (all graphic characters except letters and digits)
[:blank:]   [ \t]          space and TAB characters only
[:space:]   [ \t\n\r\f\v]  whitespace characters (space, tab, newline, return, feed, vtab)
[:cntrl:]                  control characters
[:graph:]   [^ [:cntrl:]]  graphic characters (all characters which have graphic representation)
[:print:]   [[:graph:] ]   graphic characters and space
```

### random_char_alnum

Get random characters using `[:alnum:]` class.

Syntax:
```sh
random_char_alnum [length]
```

Example:
```sh
random_char_alnum 8
=> 1Yp7M7wc
```

### random_char_alpha

Get random characters using `[:alpha:]` class.

Syntax:
```sh
random_char_alnum [length]
```

Example:
```sh
random_char_alpha 8
=> dDSmQlYD
```

### random_char_blank

Get random characters using `[:blank:]` class.

Syntax:
```sh
random_char_alnum [length]
```

Example:
```sh
random_char_blank 8
=> "  \t  \t  \t"
```

### random_char_cntrl

Get random characters using `[:cntrl:]` class.

Syntax:
```sh
random_char_alnum [length]
```

Example:
```sh
random_char_cntrl 8
=> "^c^m^r^z^a^e^p^u"
```

### random_char_digit

Get random characters using `[:digit:]` class.

Syntax:
```sh
random_char_alnum [length]
```

Example:
```sh
random_char_digit 8
=> 36415110
```

### random_char_graph

Get random characters using `[:graph:]` class.

Syntax:
```sh
random_char_alnum [length]
```

Example:
```sh
random_char_graph 8
=> e'2-3d+9
```

### random_char_lower

Get random characters using `[:lower:]` class.

Syntax:
```sh
random_char_alnum [length]
```

Example:
```sh
random_char_lower 8
=> pgfqrefo
```

### random_char_lower_digit

Get random characters using `[:lower:][:digit]` classes

Syntax:
```sh
random_char_alnum [length]
```

Example:
```sh
random_char_lower_digit 8
=> 69m7o83i
```

### random_char_upper

Get random characters using `[:upper:]` class.

Syntax:
```sh
random_char_alnum [length]
```

Example:
```sh
random_char_upper 8
=> EGXUHNIM
```

### random_char_upper_digit

Get random characters using `[:upper:][:digit:]` classes

Syntax:
```sh
random_char_alnum [length]
```

Example:
```sh
random_char_upper_digit 8
=> L2PT37H6
```

### random_char_print

Get random characters using `[:print:]` class.

Syntax:
```sh
random_char_alnum [length]
```

Example:
```sh
random_char_print 8
=> ),zN87K;
```

### random_char_space

Get random characters using `[:space:]` class.

Syntax:
```sh
random_char_alnum [length]
```

Example:
```sh
random_char_space 8
=> "\n \t\r \v \f"
```

### random_char_xdigit

Get random characters using `[:xdigit:]` class.

Syntax:
```sh
random_char_alnum [length]
```

Example:
```sh
random_char_xdigit 8
=> eC3Ce9eD
```

## Array helpers

### array_n

Get the array number of fields a.k.a. length a.k.a. size.

```sh
set -- a b c d
array_n "$@"
=> 4
```

### array_i

Get the array item at index `i` which is 1-based.

```sh
set -- a b c d
array_i  "$@" 3
=> c
```

### array_first

Get the array's first item.

```
set -- a b c d
array_first "$@"
=> a
```

### array_last

Get the array's last item.

```
set -- a b c d
array_last "$@"
=> d
```

### array_car

Get the array's car item a.k.a. first item.

```
set -- a b c d
array_car "$@"
=> a
```

### array_cdr

Get the array's cdr items a.k.a. everything after the first item.

```
set -- a b c d
array_car "$@"
=> b c d
```

## Assert helpers

### assert_test

Assert a test utility command succeeds.

```sh
assert_test -x program.sh
=> success i.e. no output

assert_test -x notes.txt
STDERR=> assert_test -x notes.txt
```

### assert_empty

Assert an item is empty i.e. null.

```sh
assert_empty ""
=> success i.e. no output

assert_empty foo
STDERR=> assert_empty foo
```

### assert_not_empty

Assert an item is not empty i.e. not null.

```sh
assert_not_empty foo
=> success i.e. no output

assert_not_empty ""
STDERR=> assert_not_empty
```

### assert_int_eq (eq|ne|ge|gt|le|lt)

Assert an integer comparison.

```sh
assert_int_eq 1 1
=> success i.e. no output

assert_int_eq 1 2
STDERR=> assert_int_eq 1 2
```

There are comparison assertions for integers:

* `assert_int_eq` is equal to
* `assert_int_ne` is not equal to
* `assert_int_ge` is greater than or equal to
* `assert_int_gt` is greater than
* `assert_int_le` is less than or equal to
* `assert_int_lt` is less than

### assert_str_eq (eq|ne|ge|gt|le|lt)

Assert a string comparison.

```sh
assert_str_eq foo foo
=> success i.e. no output

assert_str_eq foo bar
STDERR=> assert_str_eq foo bar
```

There are comparison assertions for strings:

* `assert_str_eq` is equal to
* `assert_str_ne` is not equal to
* `assert_str_ge` is greater than or equal to
* `assert_str_gt` is greater than
* `assert_str_le` is less than or equal to
* `assert_str_lt` is less than

### assert_str_starts_with

Assert a string starts with a substring.

```sh
assert_str_starts_with foobar foo
=> success i.e. no output

assert_str_starts_with foobar xxx
STDERR=> assert_str_starts_with foobar xxx
```

### assert_str_ends_with

Assert a string ends with with a substring.

```sh
assert_str_ends_with foobar foo
=> success i.e. no output

assert_str_ends_with foobar xxx
STDERR=> assert_str_ends_with foobar xxx
```

## Make temp helpers

### mktemp_dir

Make a temporary directory path.

```sh
mktemp_dir
=> /var/folders/4f7b65122b0fb65b0fdad568a65dc97d
```

### mktemp_file

Make a temporary file path.

```sh
mktemp_file
=> /var/folders/4f7b65122b0fb65b0fdad568a65dc97d/1d9aafac5373be95d8b4c2dece0b1197
```

## Media helpers

### file_media_type

Get a file's media type a.k.a. mime type such as "text/plain".

```sh
file_media_type notes.txt
=> text/plain
```

### file_media_type_supertype

Get a file's media type type a.k.a. mime type such as "text".

```sh
file_media_type_supertype notes.txt
=> text
```

### file_media_type_subtype

Get a file's media type subtype a.k.a. mime type such as "plain".

```sh
file_media_type_subtype notes.txt
=> plain
```

## Font helpers

### font_name_exists

Does a font name exist on this system?

```sh
font_name_exists Arial
=> true

font_name_exists Foo
=> false
```

### font_name_exists_or_die

Ensure a font name exists, otherwise die with a help message.

```sh
font_name_exists_or_die Arial
=> true

font_name_exists_or_die Foo
STDERR=> Font needed: Foo
=> exit 1
```

## Content helpers

### file_ends_with_newline

Does a file end with a newline?

```sh
file_ends_with_newline notes.txt
=> true
```

## Directory helpers

### user_dir

Get a user-specific directory via env var, or XDG setting, or HOME.

```sh
user_dir foo
=> $FOO_DIR || $FOO_HOME || $XDG_FOO_DIR || $XDG_FOO_HOME || $HOME/foo
```

Conventions:

  * `user_dir bin` => binary executable directory
  * `user_dir cache` => cache directory
  * `user_dir config` => configuration directory
  * `user_dir data` => data directory
  * `user_dir desktop` => desktop directory
  * `user_dir documents` => documents directory
  * `user_dir download` => download directory
  * `user_dir log` => logging directory
  * `user_dir music` => music directory
  * `user_dir pictures` => pictures directory
  * `user_dir publicshare` => public share directory
  * `user_dir runtime` => runtime directory
  * `user_dir state` => state directory
  * `user_dir temp` => temporary directory
  * `user_dir templates` => templates directory
  * `user_dir videos` => videos directory

Popular XDG conventions:

* `XDG_DESKTOP_DIR` => user-specific desktop, such as frequent apps and files.
* `XDG_DOCUMENTS_DIR` => user-specific documents, such as typical working files.
* `XDG_DOWNLOAD_DIR` => user-specific downloads, such as internet file downloads.
* `XDG_MUSIC_DIR` => user-specific music files, such as songs.
* `XDG_PICTURES_DIR` => user-specific pictures, such as photos.
* `XDG_PUBLICSHARE_DIR` => user-specific public share, such as file sharing.
* `XDG_TEMPLATES_DIR` => user-specific templates.
* `XDG_VIDEOS_DIR` => user-specific videos, such as movies.

POSIX XDG conventions:

* `XDG_BIN_HOME` => user-specific binaries, analogous to system /usr/bin or $HOME/.local/bin.
* `XDG_LOG_HOME` => user-specific log files, analogous to system /var/log or $HOME/.local/log.
* `XDG_TEMP_HOME` => user-specific temporary files, analogous to system /temp or $HOME/.temp.
* `XDG_DATA_HOME` => user-specific data files, analogous to system /usr/share or $HOME/.local/share.
* `XDG_CACHE_HOME` => user-specific cache files, analogous to system /var/cache or $HOME/.cache.
* `XDG_STATE_HOME` => user-specific cache files, analogous to system /var/state or $HOME/.local/state.
* `XDG_CONFIG_HOME` => user-specific configuration files, analogous to system /etc or $HOME/.config.
* `XDG_RUNTIME_HOME` => user-specific runtime files such as sockets, named pipes, etc. or $HOME/.runtime.
