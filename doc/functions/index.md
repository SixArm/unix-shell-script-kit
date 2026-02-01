# Functions

## Input/output helpers

### color

Should the program use color?

Syntax:

```sh
color
=> true or false
```

The color logic heuristic in order of priority:

1. If NO_COLOR is set to non-empty, then no.
2. If CLICOLOR_FORCE is set to non-empty, then yes.
3. If the TERM is set to "dumb", then no.
4. If the output is on a terminal, then yes.
5. Otherwise, no.

### out

Print output message to stdout.

Syntax:

```sh
out <message>
=> message
```

Example:

```sh
out "my message"
STDOUT=> my message
```

We use `printf` instead of `echo` because `printf` is more consistent
on more systems, such a for escape sequence handling.

Compare:

  * Use the `out` function to print to STDOUT.

  * Use the `err` function to print to STDERR.

### err

Print error message to stderr.

Syntax:

```sh
err <message>
=> message
```

Example:

```sh
err "my message"
STDERR=> my message
````

We use `printf` instead of `echo` because `printf` is more consistent
on more systems, such a for escape sequence handling.

Compare:

  * Use the `out` function to print to STDOUT.

  * Use the `err` function to print to STDERR.

### die

Print error message to stderr, then exit with error code.

Syntax:

```sh
die <code> <message>
STDERR=> <message>
=> exit <code>
```

Example:

```sh
die 1 "my message"
STDERR=> my message
=> exit 1
```

Example with an exit code number and name:

```sh
die $EXIT_UNAVAILABLE EXIT_UNAVAILABLE
STDERR=> EXIT_UNAVAILABLE
=> exit 69
```

Example with more information:

```sh
false || die $? "Fatal error $? on line $LINENO of $0"
STDERR=> Fatal error 1 on line 2 of example.sh"
=> exit 1
```

### big

Print a big banner to stdout, good for human readability.

Syntax:

```sh
big <message>
=>
###
#
# <message>
#
###
```

Example:

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

Syntax:

```sh
log <message>
=> <datestamp> <unique random id> <hostname> <process id> <message>
```

Example:

```sh
log "my message"
=> 2021-05-04T22:57:54.000000000+00:00 7e7151dc24bd511098ebb248771d8ffb abc.example.com 1234 my message
```

We prefer this log file format for many of our scripts because we prefer
logging the additional diagnositc information that we use for our systems:
the datetime with nanosecond-friendly format and timezone-friendly format,
unique random id a.k.a. zid, hostname, and process number.

### zid

Generate a 32-bit secure random lowercase hex identifier.

Syntax:

```sh
zid
=> <32-bit secure random lowercase hex identifier>
```

Example:

```sh
zid
=> 78577554e967951388b5907854b4c337
```

### ask

Prompt the user for a line of input, then return a trimmed string.

Syntax:

```sh
ask
=> <prompt>
```

Example:

```sh
ask
=> prompt the user for a line of input
```

### utf8

Should the program print UTF-8 characters such as accents and emoji?

Syntax:

```sh
utf8
=> true or false
```

#
Example:

```sh
utf8
=> true
```

This implementation is a heuristic and subject to change as we learn more.
This checks the locale charmap. However, it's possible for the charmap to
be set to UTF-8, but the terminal is unable to render UTF-8 characters.

## Print messages with pretty formatting, colors, emojis, etc.

### Color settings

Set pretty display of messages for success, warning, failure.

If you wish to set these in your terminal, and your terminal supports
dollar strings with \E meaning escape, then you can use the following:

```sh
export PRINT_SUCCESS_START=$'\E[32m✅ Success: '
export PRINT_SUCCESS_START=$'\E[35m⚠️ Warning: '
export PRINT_FAILURE_START=$'\E[31m❌ Failure: '
```

### print_success

Print a success message to stdout.

Syntax:

```sh
print_success <message>
STDOUT=> <message>
```

Example:

```sh
print_success "This is a success message."
=> This is a success message.
```

The output can be customized by setting:

 * PRINT_SUCCESS_START
 * PRINT_SUCCESS_STOP

### print_warning

Print a warning message to stdout.

Syntax:

```sh
print_warning <message>
STDOUT=> <message>
```

Example:

```sh
print_warning "This is a warning message."
=> This is a warning message.
```

The output can be customized by setting:

 * PRINT_WARNING_START
 * PRINT_WARNING_STOP

### print_failure

Print a failure message to stdout.

Syntax:

```sh
print_failure <message>
STDOUT=> <message>
```

Example:

```sh
print_failure "This is a failure message."
=> This is a failure message.
```

The output can be customized by setting:

 * PRINT_FAILURE_START
 * PRINT_FAILURE_STOP

## Date & time helpers

### now

Get a datetime as our preferred ISO format.

Syntax:

```sh
now
=> <datetime as our preferred ISO format>
```

Example with the current datetime:

```sh
now
=> 2021-05-04T22:59:28.769653000+00:00
```

Example with a custom datetime, if your date command offers option -d:

```sh
now -d "January 1, 2021"
=> 2021-01-01T00:00:00.000000000+00:00
```

We prefer this date-time format for many of our scripts:

* We prefer ISO standard because it's well documented and supported.
  Specifically, we use ISO "YYYY-MM-DDTHH:MM:SS.NNNNNNNNN+00:00".

* We prefer nanosecond width because it aligns with high-speed systems.
  Specifically, we use GNU `date` and tools that print nanoseconds.

* We prefer timezone width because it aligns with localized systems.
  Specifically, we use some systems and tools that require timezones.

Note: the custom datetime capabilty relies on the system "date" command,
because this script sends the args along to the system "date" command.
For example Linux GNU "date" handles this, but macOS BSD "date" doesn't.

### now_date

Get a date as our preferred ISO format

Syntax:

```sh
now_date
=> <date as our preferred ISO format>
```

Example:

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

Syntax:

```sh
sec
=> <current time as posix sections>
```

Example:

```sh
sec
=> 1620169178
```

### age

Get the age of a given time in POSIX seconds.

Syntax:

```sh
age <time as posix seconds>
=> <difference in seconds between input and now>
```

Example:

```sh
age 1620169178
=> 19
```

### newer

Is the age of a given time newer than a given number of seconds?

Syntax:

```sh
TODO
```

Example:

```sh
newer 2000000000 && echo "true" || echo "false
=> true
```

### older

Is the age of a given time older than a given number of seconds?

Syntax:

```sh
TODO
```

Example:

```sh
older 1000000000 && echo "true" || echo "false"
=> true
```

### leap_year

Is the year a leap year?

Syntax:

```sh
leap_year <year>
=> true or false
```

Examples:

```sh
leap_year 2023 => false
leap_year 2024 => true
leap_year 2025 => false
```

### datetime_mday_max

Given a datetime (or year and month), calculate the maximum month-day number.

Syntax:

```sh
datetime_mday_max <yyyy-mm*>
=> true or false
```

Examples:

```sh
datetime_mday_max 2026-01 => 31
datetime_mday_max 2026-02 => 28
```

### datetime_format_for_at_command

Given a datetime as ISO 8601 format "yyyy-mm-ddThh:mm:ss"
return the format for `at` command "yyyymmdddhhmm.ss".

Syntax:

```sh
datetime_format_for_at_command <datetime>
=> <yyyymmdddhhmm.ss>
```

Example:

```sh
datetime_format_for_at_command 2026-12-31T01:02:03
=> 202612310102.03
```

### datetime_format_for_pmset_command

Given a datetime as ISO 8601 format "yyyy-mm-ddThh:mm:ss"
return the format for `pmset` command  "mm/dd/yy hh:mm:ss".

Syntax:

```sh
datetime_format_for_pmset_command <datetime>
=> <mm/dd/yy hh:mm:ss>
```

Example:
```sh
datetime_format_for_pmset_command 2026-12-31T01:02:03
=> 12/31/26 01:02:03
```

### datetime_add

Given a datetime, add years, months, days, hours, minutes, seconds.

Syntax:

```sh
datetime_add <datetime> <years> <months> <days> <hours> <minutes> <seconds>
=> <datetime>
```

Examples:

```sh
datetime_add 2000-01-01T00:00:00 0 0 0 0 0 1 => 2000-01-01T00:00:01 (next second)
datetime_add 2000-01-01T00:00:00 0 0 0 0 1 0 => 2000-01-01T00:01:00 (next minute)
datetime_add 2000-01-01T00:00:00 0 0 0 1 0 0 => 2000-01-01T01:00:00 (next hour)
datetime_add 2000-01-01T00:00:00 0 0 1 0 0 0 => 2000-01-02T00:00:00 (next day)
datetime_add 2000-01-01T00:00:00 0 1 0 0 0 0 => 2000-02-01T00:00:00 (next month)
datetime_add 2000-01-01T00:00:00 1 0 0 0 0 0 => 2001-01-01T00:00:00 (next year)
```

Examples of carry:

```sh
datetime_add 2000-01-01T00:00:00 0 0 0 0 0 1 => 2000-01-01T00:00:01 (next second)
datetime_add 2000-01-01T00:00:59 0 0 0 0 0 1 => 2000-01-01T00:01:00 (next minute)
datetime_add 2000-01-01T00:59:59 0 0 0 0 0 1 => 2000-01-01T01:00:00 (next hour)
datetime_add 2000-01-01T23:59:59 0 0 0 0 0 1 => 2000-01-02T00:00:00 (next day)
datetime_add 2000-01-31T23:59:59 0 0 0 0 0 1 => 2000-02-01T00:00:00 (next month)
datetime_add 2000-12-31T23:59:59 0 0 0 0 0 1 => 2001-01-01T00:00:00 (next year)
```

## Validation helpers

### directory_exists

Does a directory exist?

Syntax:

```sh
TODO
=>
```

Example:

```sh
directory_exists /usr
=> true

directory_exists /loremipsum
=> false
```

### directory_exists_or_die

Does a directory exist? If no then die.

Syntax:

```sh
TODO
=>
```

Example:

```sh
directory_exists_or_die /usr
=> true

directory_exists_or_die /loremipsum
STDERR=> Directory needed: /loremipsum
=> exit $EXIT_IOERR
```

### file_exists

Does a file exist?

Syntax:

```sh
TODO
=>
```

Example:

```sh
file_exists foo.txt
=> true

file_exists loremipsum.txt
=> false
```

### file_exists_or_die

Does a file exist? If no then die.

Syntax:

```sh
TODO
=>
```

Example:

```sh
file_exists_or_die foo.txt
=> true

file_exists_or_die loremipsum.txt
STDERR=> File needed: loremipsum.txt
=> exit $EXIT_IOERR
```

### symlink_exists

Does a symlink exist?

Syntax:

```sh
TODO
=>
```

Example:

```sh
symlink_exists foo.txt
=> true

symlink_exists loremipsum.txt
=> false
```

### symlink_exists_or_die

Does a symlink exist? If no then die.

Syntax:

```sh
TODO
=>
```

Example:

```sh
symlink_exists_or_die foo.txt
=> true

symlink_exists_or_die loremipsum.txt
STDERR=> Symlink needed: loremipsum.txt
=> exit $EXIT_IOERR
```

### command_exists

Does a command exist?

Syntax:

```sh
TODO
=>
```

Example:

```sh
command_exists grep
=> true

command_exists curl
=> false
```

### command_exists_or_die

Does a command exist? If no then die.

Syntax:

```sh
TODO
=>
```

Example:

```sh
command_exists_or_die grep
=> true

command_exists_or_die loremipsum
STDERR=> Command needed: loremipsum
=> exit 1
```

### command_version_exists

Does a command version exist?

Syntax:

```sh
TODO
=>
```

Example:

```sh
command_version_exists grep 2.2 1.1
=> true

command_version_exists grep 2.2 1.1
=> true
```

### command_version_exists_or_die

Does a command version exist? If no then die

Syntax:

```sh
TODO
=>
```

Example:

```sh
command_version_exists_or_die grep 2.2 1.1
=> true

command_version_exists_or_die grep 2.2 3.3
STDERR=> Command version needed: grep >= 3.x
=> exit 1
```

### var_exists

Does a variable exist?

Syntax:

```sh
TODO
=>
```

Example:

```sh
var_exists HOME
=> true

var_exists FOO
=> false
```

### var_exists_or_die

Does a variable exist? If no then die.

Syntax:

```sh
TODO
=>
```

Example:

```sh
var_exists_or_die HOME
=> true

var_exists_or_die FOO
STDERR=> Variable needed: FOO
=> exit 1
```

### version

Is a version number sufficient?

Syntax:

```sh
TODO
=>
```

Example:

```sh
version 1.1 2.2
=> true

version 3.3 2.2
=> false
```

### version_or_die: ensure a version is sufficient

Is a version number sufficient? If no then die.

Syntax:

```sh
TODO
=>
```

Example:

```sh
version_or_die 1.1 2.2
=> true

version_or_die 3.3 2.2
STDERR=> Version needed: >= 3.3 (not 2.2)
```

## Number helpers

### int

Convert a number string to an integer number string.

Syntax:

```sh
TODO
=>
```

Example:

```sh
int 1.23
=> 1
```
int() {

### sum

Print the sum of numbers.

Syntax:

```sh
TODO
=>
```

Example:

```sh
sum 1 2 3
=> 6
```

## Comparison helpers

### cmp_alnums

Compare alnums as groups, such as for word version strings.

Syntax:

```sh
TODO
=>
```

Example:

```
cmp_alnums "a.b.c" "a.b.c"
=> 0 (zero means left == right)

cmp_alnums "a.b.c" "a.b.d"
=> -1 (negative one means left < right)

cmp_alnums "a.b.d" "a.b.c"
=> 1 (positive one means left > right)
```

### cmp_digits

Compare digits as groups, such as for numeric version strings.

Syntax:

```sh
TODO
=>
```

Example:

```
cmp_digits 1.2.3 1.2.3
=> 0 (zero means left == right)

cmp_digits 1.2.3 1.2.4
=> -1 (negative one means left < right)

cmp_digits 1.2.4 1.2.3
=> 1 (positive one means left > right)
```

## Extensibility helpers

### dot_all

Source all the executable files in a given directory and subdirectories.

Syntax:

```sh
TODO
=>
```

Example:

```sh
dot_all ~/temp
=> . ~/temp/a.sh
=> . ~/temp/b.pl
=> . ~/temp/c.js
```

### run_all

Run all the executable commands in a given directory and subdirectories.

Syntax:

```sh
TODO
=>
```

Example:

```sh
run_all ~/temp
=> ~/temp/a.sh
=> ~/temp/b.pl
=> ~/temp/c.js
```

### sh_all

Shell all the executable commands in a given directory and subdirectories.

Syntax:

```sh
TODO
=>
```

Example:

```sh
sh_all ~/temp
=> sh -c ~/temp/a.sh
=> sh -c ~/temp/b.pl
=> sh -c ~/temp/c.js
```

### rm_all

Remove all files in a given directory and subdirectories-- use with caution.

Syntax:

```sh
TODO
=>
```

Example:

```sh
rm_all ~/temp
=> rm ~/temp/a.sh
=> rm ~/temp/b.pl
=> rm ~/temp/c.js
```

## Text helpers

### trim

Remove any space characters at the text's start or finish.

Syntax:

```sh
TODO
=>
```

Example:

```sh
trim "  foo  "
=> foo
#```

### slug

Convert a string from any characters to solely lowercase and single internal
dash characters.

Syntax:

```sh
TODO
=>
```

Example:

```sh
slug "**Foo** **Goo** **Hoo**"
=> foo-goo-hoo
#```

### slugs

Convert a string from any characters to solely lowercase and single internal
dash characters and slash characters.

Syntax:

```sh
TODO
=>
```

Example:

```sh
slugs "**Foo** / **Goo** / **Hoo**"
=> foo/goo/hoo
#```

### upper_case

Convert text from any lowercase letters to uppercase letters.

Syntax:

```sh
TODO
=>
```

Example:

```sh
upper_case AbCdEf
=> ABCDEF
#```

### lower_case

Convert text from any uppercase letters to lowercase letters.

Syntax:

```sh
TODO
=>
```

Example:

```sh
lower_case AbCdEf
=> abcdef
#```

### kebab_case

Convert a string from any characters to solely alphanumeric and single internal dash characters.

Syntax:

```sh
TODO
=>
```

Example:

```sh
kebab_case "**Foo** **Goo** **Hoo**"
=> Foo-Goo-Hoo
#```

### snake_case

Convert a string from any characters to solely alphanumeric and single internal underscore characters.

Syntax:

```sh
TODO
=>
```

Example:

```sh
snake_case "**Foo** **Goo** **Hoo**"
=> Foo_Goo_Hoo
#```

### space_case

Convert a string from any characters to solely alphanumeric and single internal space characters.

Syntax:

```sh
TODO
=>
```

Example:

```sh
space_case "**Foo** **Goo** **Hoo**"
=> Foo Goo Hoo
#```

### touch_case

Convert a string from any characters to solely a command "touch -t" timestamp format.

Syntax:

```sh
TODO
=>
```

Example:

```sh
touch_case "Foo  2021-05-04 22:57:54 Goo"
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

Example with character class:

```sh
reject_character_class foo123goo456 alpha
=> -123--456
```

Example with character class and substring offset:

```sh
reject_character_class foo123goo456 alpha 6
=> 456
```

Example with character class and substring offset and length:

```sh
reject_character_class foo123goo456 alpha 6 1
=> 4
```

## Random character helpers

### random_char

Syntax:

```sh
random_char [characters [length]]
```

Example:

```sh
random_char ABCDEF 8
=> CBACBFDD
#```

Example hexadecimal digit uppercase:

```sh
random_char 0-9A-F 8
=> FC56A95C
#```

Example character class for uppercase letters:

```sh
random_char '[:upper:]' 8
=> ZMGIQBJB
#```

POSiX character classes for ASCII characters:

```txt
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

Random characters using [:alnum:] class.

Syntax:

```sh
random_char_alnum [length]
```

Example:

```sh
random_char_alnum 8
=> 1Yp7M7wc
#```

### random_char_alpha

Random characters using [:alpha:] class.

Syntax:

```sh
random_char_alnum [length]
```

Example:

```sh
random_char_alpha 8
=> dDSmQlYD
#```

### random_char_blank

Random characters using [:blank:] class.

Syntax:

```sh
random_char_alnum [length]
```

Example:

```sh
random_char_blank 8
=> "  \t  \t  \t"
#```

### random_char_cntrl

Random characters using [:cntrl:] class.

Syntax:

```sh
random_char_alnum [length]
```

Example:

```sh
random_char_cntrl 8
=> "^c^m^r^z^a^e^p^u"
#```

### random_char_digit

Random characters using [:digit:] class.

Syntax:

```sh
random_char_alnum [length]
```

Example:

```sh
random_char_digit 8
=> 36415110
#```

### random_char_graph

Random characters using [:graph:] class.

Syntax:

```sh
random_char_alnum [length]
```

Example:

```sh
random_char_graph 8
=> e'2-3d+9
#```

### random_char_lower

Random characters using [:lower:] class.

Syntax:

```sh
random_char_alnum [length]
```

Example:

```sh
random_char_lower 8
=> pgfqrefo
#```

### random_char_lower_digit

Random characters using [:lower:][:digit] classes

Syntax:

```sh
random_char_alnum [length]
```

Example:

```sh
random_char_lower_digit 8
=> 69m7o83i
#```

### random_char_upper

Random characters using [:upper:] class.

Syntax:

```sh
random_char_alnum [length]
```

Example:

```sh
random_char_upper 8
=> EGXUHNIM
#```

### random_char_upper_digit

Random characters using [:upper:][:digit:] classes

Syntax:

```sh
random_char_alnum [length]
```

Example:

```sh
random_char_upper_digit 8
=> L2PT37H6
#```

### random_char_print

Random characters using [:print:] class.

Syntax:

```sb
random_char_alnum [length]
```

Example:

```sh
random_char_print 8
=> ),zN87K;
#```

### random_char_space

Random characters using [:space:] class.

Syntax:

```sh
random_char_alnum [length]
```

Example:

```sh
random_char_space 8
=> "\n \t\r \v \f"
#```

### random_char_xdigit

Random characters using [:xdigit:] class.

Syntax:

```sh
random_char_alnum [length]
```

Example:

```sh
random_char_xdigit 8
=> eC3Ce9eD
#```

## Array helpers

### array_n

Get the array number of fields a.k.a. length a.k.a. size.

Syntax:

```sh
TODO
=>
```

Example:

```sh
set -- a b c d
array_n "$@"
=> 4
```

### array_i

Get the array item at index `i` which is 1-based.

Syntax:

```sh
TODO
=>
```

Example:

```sh
set -- a b c d
array_i "$@" 3
=> c
```

POSIX syntax uses an array index that starts at 1.

Bash syntax uses an array index that starts at 0.

Bash syntax can have more power this way if you prefer it:

```sh
[ $# == 3 ] && awk -F "$2" "{print \$$3}" <<< "$1" || awk "{print \$$2}" <<< "$1"
```

### array_first

Get the array's first item.

Syntax:

```sh
TODO
=>
```

Example:

```sh
set -- a b c d
array_first "$@"
=> a
```

### array_last

Get the array's last item.

Syntax:

```sh
TODO
=>
```

Example:

```sh
set -- a b c d
array_last "$@"
=> d
```

### array_car

Get the array's car item a.k.a. first item.

Syntax:

```sh
TODO
=>
```

Example:

```sh
set -- a b c d
array_car "$@"
=> a
```

### array_cdr

Get the array's cdr items a.k.a. everything after the first item.

Syntax:

```sh
TODO
=>
```

Example:

```sh
set -- a b c
array_cdr "$@"
=> b c d
```

## Assert helpers

### assert_test

Assert a test utility command succeeds.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_test -x program.sh
=> success i.e. no output

assert_test -x notes.txt
STDERR=> assert_test -x notes.txt
```

### assert_empty

Assert an item is empty.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_empty ""
=> success i.e. no output

assert_empty foo
STDERR=> assert_empty foo
```

### assert_not_empty

Assert an item is not empty.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_not_empty foo
=> success i.e. no output

assert_not_empty ""
STDERR=> assert_not_empty
```

### assert_int_eq

Assert an integer is equal to another integer.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_int_eq 1 1
=> success i.e. no output

assert_int_eq 1 2
STDERR=> assert_int_eq 1 2
```

### assert_int_ne

Assert an integer is not equal to another integer.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_int_eq 1 2
=> success i.e. no output

assert_int_eq 1 1
STDERR=> assert_int_ne 1 1
```

### assert_int_ge

Assert an integer is greater than or equal to another integer.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_int_ge 2 1
=> success i.e. no output

assert_int_ge 1 2
STDERR=> assert_int_ge 1 2
```

### assert_int_gt

Assert an integer is greater than another integer.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_int_gt 2 1
=> success i.e. no output

assert_int_gt 1 2
STDERR=> assert_int_gt 1 2
```

### assert_int_le

Assert an integer is less than or equal to another integer.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_int_le 1 2
=> success i.e. no output

assert_int_le 2 1
STDERR=> assert_int_le 2 1
```

### assert_int_lt

Assert an integer is less than to another integer.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_int_lt 1 2
=> success i.e. no output

assert_int_lt 2 1
STDERR=> assert_int_lt 2 1
```

### assert_str_eq

Assert a string is equal to another string.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_str_eq 1 1
=> success i.e. no output

assert_str_eq 1 2
STDERR=> assert_str_eq 1 2
```

### assert_str_ne

Assert a string is not equal to another string.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_str_eq 1 2
=> success i.e. no output

assert_str_eq 1 1
STDERR=> assert_str_ne 1 1
```

### assert_str_ge

Assert a string is greater than or equal to another string.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_str_ge 2 1
=> success i.e. no output

assert_str_ge 1 2
STDERR=> assert_str_ge 1 2
```

### assert_str_gt

Assert a string is greater than another string.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_str_gt 2 1
=> success i.e. no output

assert_str_gt 1 2
STDERR=> assert_str_gt 1 2
```

### assert_str_le

Assert a string is less than or equal to another string.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_str_le 1 2
=> success i.e. no output

assert_str_le 2 1
STDERR=> assert_str_le 2 1
```

### assert_str_lt

Assert a string is less than to another string.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_str_lt 1 2
=> success i.e. no output

assert_str_lt 2 1
STDERR=> assert_str_lt 2 1
```

### assert_str_starts_with

Assert a string starts with a substring.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_str_starts_with foobar foo
=> success i.e. no output

assert_str_starts_with foobar xxx
STDERR=> assert_str_starts_with foobar xxx
```

### assert_str_ends_with

Assert a string ends with with a substring.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_str_ends_with foobar bar
=> success i.e. no output

assert_str_ends_with foobar xxx
STDERR=> assert_str_ends_with foobar xxx
```

### assert_eval_int_eq_x

Assert an eval into an integer is equal to an expression.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_eval_int_eq_x 'echo "1"' 1
=> success i.e. no output

assert_eval_int_eq_x 'echo "1"' 2
STDERR=> assert_eval_int_eq_x echo "1" 2
```

### assert_eval_str_eq_x

Assert an eval into a string is equal to an expression.

Syntax:

```sh
TODO
=>
```

Example:

```sh
assert_eval_str_eq_x 'echo "foo"' foo
=> success i.e. no output

assert_eval_str_eq_x 'echo "foo"' bar
STDERR=> assert_eval_str_eq_x echo "foo" bar
```

## Make temp helpers

### mktemp_dir

Make a temporary directory path.

Syntax:

```sh
TODO
=>
```

Example:

```sh
mktemp_dir
=> /var/folders/4f7b65122b0fb65b0fdad568a65dc97d
```

Immediately after you make it, create a trap to remove it:

```sh
x=mktemp_directory
trap '{ rm -rf "$x"; }' EXIT
```

### mktemp_file

Make a temporary file path.

Syntax:

```sh
TODO
=>
```

Example:

```sh
mktemp_file
=> /var/folders/4f7b65122b0fb65b0fdad568a65dc97d/1d9aafac5373be95d8b4c2dece0b1197
```

Immediately after you make it, create a trap to remove it:

```sh
x=mktemp_file
trap '{ rm -rf "$x"; }' EXIT
```

## Media helpers

### file_media_type

Get a file's media type a.k.a. mime type such as "text/plain".

Syntax:

```sh
TODO
=>
```

Example:

```sh
file_media_type notes.txt
=> text/plain
```

### file_media_type_supertype

Get a file's media type type a.k.a. mime type such as "text".

Syntax:

```sh
TODO
=>
```

Example:

```sh
file_media_type_supertype notes.txt
=> text
```

### file_media_type_subtype

Get a file's media type subtype a.k.a. mime type such as "plain".

Syntax:

```sh
TODO
=>
```

Example:

```sh
file_media_type_subtype notes.txt
=> plain
```

## Font helpers

### font_name_exists

Does a font name exist on this system?

Syntax:

```sh
TODO
=>
```

Example:

```sh
font_name_exists Arial
=> true

font_name_exists Foo
=> false
```

### font_name_exists_or_die

Does a font name exist on this system? If no then die.

Syntax:

```sh
TODO
=>
```

Example:

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

Syntax:

```sh
TODO
=>
```

Example:

```sh
file_ends_with_newline notes.txt
=> true
```

## Directory helpers

### user_dir

Get a user-specific directory via env var, or XDG setting, or HOME.

Syntax:

```sh
TODO
=>
```

Example:

```sh
user_dir foo => $FOO_DIR || $FOO_HOME || $XDG_FOO_DIR || $XDG_FOO_HOME || $HOME/foo
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

See also:

  * https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html

  * https://wiki.archlinux.org/title/XDG_user_directories

