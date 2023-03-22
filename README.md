# SixArm POSIX shell functions

SixArm is a consulting group that creates software and systems.

This is our POSIX shell script file of functions for general use.

This script emphasizes small functions, helper variables, and clear examples.

Constructive feedback is welcome and appreciated.

To download this file:

```sh
curl -O "https://raw.githubusercontent.com/SixArm/sixarm-posix-shell-functions/main/sixarm-posix-shell-functions"
```

## Tracking

* Package: sixarm-posix-shell-functions
* Version: 11.0.4
* Created: 2017-08-22T00:00:00Z
* Updated: 2023-03-22T15:32:10Z
* Website: https://github.com/sixarm/sixarm-posix-shell-functions
* License: GPL-2.0 or GPL-3.0 or contact us for more
* Contact: Joel Parker Henderson (joel@sixarm.com)

## Input/output helpers

### out: print output message to stdout

```sh
out "my message"
STDOUT=> my message
```

### err: print error message to stderr

```sh
err "my message"
STDERR=> my message
```

### die: print error message to stderr, then exit with error code 1

```sh
die 1 "my message"
STDERR=> my message
=> exit 1
```

### big: print a big banner to stdout, good for human readability

```sh
big "my message"
=>
###
#
# my message
#
###
```

### log: print a datestamp, unique random id, hostname, process id, and message

```sh
log "my message"
=> 2021-05-04T22:57:54.000000000+00:00 7e7151dc24bd511098ebb248771d8ffb abc.example.com 1234 my message
```

### zid: generate a 32-bit secure random lowercase hex identifier

```sh
zid
=> 78577554e967951388b5907854b4c337
```

### ask: prompt the user for a line of input, then return a trimmed string

```sh
ask
=> prompt
```

## Directory helpers

### user_dir: get user-specific directory via env var or XDG setting or HOME.

```sh
user_dir log
=> $FOO_DIR
=> $FOO_HOME
=> $XDG_FOO_DIR
=> $XDG_FOO_HOME
=> $HOME/foo
```

## Time helpers

### now_date: get a date as our preferred ISO format

```sh
now_date
=> 2021-05-04
```

### now: get a datetime as our preferred ISO format with nanoseconds

```sh
now
=> 2021-05-04T22:59:28.769653000+00:00
```

Example with a custom datetime:

```sh
now -d "2021-01-01" 
=> 2021-01-01T00:00:00.000000000+00:00
```

### sec: get the current time in POSIX seconds

```sh
sec
=> 1620169178
```

### age: get the age of a given time in POSIX secords

```sh
age 1620169178
=> 19
```

### newer: is the age of a given time newer than a given number of seconds?

```sh
newer 2000000000 && echo "true" || echo "false
=> true
```

### older: is the age of a given time older than a given number of seconds?

```sh
older 1000000000 && echo "true" || echo "false"
=> true
```

## Validation helpers

### command_exists: return true iff a command exists

```sh
command_exists grep
=> true

command_exists curl
=> false
```

### command_exists_or_die: ensure a command exists, otherwise die with a help message

```sh
command_exists_or_die grep
=> true

command_exists_or_die curl
STDERR=> Command needed: curl
=> exit 1
```

### command_version_or_die: ensure a command exists and version is sufficient, otherwise die with a help message

```sh
command_version_or_die grep 1.1 2.2
=> true

command_version_or_die grep 3.3 2.2
STDERR=> Command version needed: grep >= 3.3 (not 2.2)
=> exit 1
```

### var_exists: return true iff a variable exists

```sh
var_exists HOME
=> true

var_exists FOO
=> false
```

### var_exists_or_die: ensure a variable exists, otherwise die with a help message

```sh
var_exists_or_die HOME
=> true

var_exists_or_die FOO
STDERR=> Variable needed: FOO
=> exit 1
```

### version: return true iff a version is sufficient.

```sh
version 1.1 2.2
=> true

version 3.3 2.2
=> false
```

### version_or_die: ensure a version is sufficient, otherwise die with a help message

```sh
version_or_die 1.1 2.2
=> true

version_or_die 3.3 2.2
STDERR=> Version needed: >= 3.3 (not 2.2)
```

## Number helpers

### int: convert a number string to an integer number string

```sh
int 1.23
=> 1
```

### sum: print the sum of numbers

```sh
sum 1 2 3
=> 6
```

## Comparison helpers

### cmp_alnums: compare alnums as groups, such as for word version strings.

```sh
cmp_alnums "a.b.c" "a.b.d"
# => -1 (negative one means left < right)
```

### cmp_digits: compare digits as groups, such as for number version strings.

```sh
cmp_digits "1.2.3" "1.2.4"
# => -1 (negative one means left < right)
```

## Extensibility helpers

### dot_all: source all the executable files in a given directory and subdirectories

```sh
dot_all ~/temp
=> . ~/temp/a.sh
=> . ~/temp/b.pl
=> . ~/temp/c.js
```

### run_all: run all the executable commands in a given directory and subdirectories

```sh
run_all ~/temp
=> ~/temp/a.sh
=> ~/temp/b.pl
=> ~/temp/c.js
```

### sh_all: shell all the executable commands in a given directory and subdirectories

```sh
sh_all ~/temp
=> sh -c ~/temp/a.sh
=> sh -c ~/temp/b.pl
=> sh -c ~/temp/c.js
```

### rm_all: remove all files in a given directory and subdirectories-- use with caution

```sh
rm_all ~/temp
=> rm ~/temp/a.sh
=> rm ~/temp/b.pl
=> rm ~/temp/c.js
```

## Text helpers

### trim: remove any space characters at the text's start or finish

```sh
trim "  foo  "
=> foo
```

### slug: convert a string from any characters to solely lowercase and single internal dash characters

```sh
slug "**Foo** **Goo** **Hoo**"
=> foo-goo-hoo
```

### slugs: convert a string from any characters to solely lowercase and single internal dash characters and slash characters.

```sh
slugs "**Foo** / **Goo** / **Hoo**"
=> foo/goo/hoo
```

### upper_format: convert text from any lowercase letters to uppercase letters

```sh
upper_format AbCdEf
=> ABCDEF
```

### lower_format: convert text from any uppercase letters to lowercase letters

```sh
lower_format AbCdEf
=> abcdef
```

### chain_format: convert a string from any characters to solely alphanumeric and single internal dash characters

```sh
chain_format "**Foo** **Goo** **Hoo**"
=> Foo-Goo-Hoo
```

### snake_format: convert a string from any characters to solely alphanumeric and single internal underscore characters

```sh
snake_format "**Foo** **Goo** **Hoo**"
=> Foo_Goo_Hoo
```

### space_format: convert a string from any characters to solely alphanumeric and single internal space characters

```sh
space_format "**Foo** **Goo** **Hoo**"
=> Foo Goo Hoo
```

### touch_format: convert a string from any characters to solely a command "touch -t" timestamp format

```sh
touch_format "Foo  2021-05-04 22:57:54 Goo"
=> 202105042257.54
```

### select_character_class: get a string's characters that match a class, with optional offset and length

Syntax: select_character_class <string> <class> [offset [length]]

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


### reject_character_class: get a string's characters that don't match a class, with optional offset and length

Syntax: reject_character_class <string> <class> [offset [length]]

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

## Array helpers

### array_n: get the array number of fields a.k.a. length a.k.a. size

```sh
set -- a b c d
array_n "$@"
=> 4
```

### array_i: get the array item at index `i` which is 1-based.

```sh
set -- a b c d
array_i  "$@" 3
=> c
```

### array_first: return the array's first item.

```
set -- a b c d
array_first "$@"
=> a
```

### array_last: return the array's last item.

```
set -- a b c d
array_last "$@"
=> d
```

### array_car: return the array's car item a.k.a. first item.

```
set -- a b c d
array_car "$@"
=> a
```

### array_cdr: return the array's cdr items a.k.a. everything after the first item.

```
set -- a b c d
array_car "$@"
=> b c d
```

## Assert helpers

### assert_test: assert a test utility command succeeds

```sh
assert_test -x program.sh
=> success i.e. no output

assert_test -x notes.txt
STDERR=> assert_test -x notes.txt 
```

### assert_empty: assert an item is empty i.e. null

```sh
assert_empty ""
=> success i.e. no output

assert_empty foo
STDERR=> assert_empty foo
```

### assert_not_empty: assert an item is not empty i.e. not null

```sh
assert_not_empty foo
=> success i.e. no output

assert_not_empty ""
STDERR=> assert_not_empty
```

### assert_int_(eq|ne|ge|gt|le|lt): assert an integer or string versus another

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

### assert_str_(eq|ne|ge|gt|le|lt): assert a string versus another string

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

### assert_str_starts_with: assert a string starts with a substring

```sh
assert_str_starts_with foobar foo
=> success i.e. no output

assert_str_starts_with foobar xxx
STDERR=> assert_str_starts_with foobar xxx
```

### assert_str_ends_with: assert a string ends with with a substring

```sh
assert_str_ends_with foobar foo
=> success i.e. no output

assert_str_ends_with foobar xxx
STDERR=> assert_str_ends_with foobar xxx
```

## Make temp helpers

### mktemp_dir: make a temporary directory path

```sh
mktemp_dir
=> /var/folders/4f7b65122b0fb65b0fdad568a65dc97d
```

### mktemp_file: make a temporary file path

```sh
mktemp_file
=> /var/folders/4f7b65122b0fb65b0fdad568a65dc97d/1d9aafac5373be95d8b4c2dece0b1197
```

## Media helpers

### file_media_type: get a file's media type a.k.a. mime type such as "text/plain"

```sh
file_media_type notes.txt
=> text/plain
```

### file_media_type_supertype: get a file's media type type a.k.a. mime type such as "text"

```sh
file_media_type_supertype notes.txt
=> text
```

### file_media_type_subtype: get a file's media type subtype a.k.a. mime type such as "plain"

```sh
file_media_type_subtype notes.txt
=> plain
```

## Font helpers

### font_exists: does a font name exist on this system?

```sh
font_exists Arial
=> true

font_exists Foo
=> false
```

### font_exists_or_die: ensure a font name exists.

```sh
font_exists_or_die Arial
=> true

font_exists_or_die Foo
STDERR=> Font needed: Foo
=> exit 1
```

## Content helpers

### file_ends_with_newline: file ends with newline?

```sh
file_ends_with_newline notes.txt
=> true
```

## Exit codes

It is good practice to call exit with a value that indicates success (0) 
or a failure condition when ending a program. The pre-defined exit codes
from sysexits can be used, so the caller of the process can get a rough
estimation about the failure class without looking up the source code.

The successful exit is always indicated by a status of 0. 

Error numbers begin at EXIT__BASE to reduce the possibility of clashing with
other exit statuses that random programs may already return. The meaning of
the codes is approximately as follows.

SUCCESS: the program succeeded, as defined by the program. 
Exit 0 meaning SUCCESS is a widespread convention as a catch-all code.

```sh
EXIT_SUCCESS=0
```

FAILURE: the program failed, as defined by the program.
Exit 1 meaning FAILURE is a widespread convention as a catch-all code.
E.g. an error, an abort, found no results, lack of data, etc.

```sh
EXIT_FAILURE=1
```

USAGE: a command is used incorrectly.
Exit 2 meaning USAGE is a widespread convention as a catch-all CLI code.
E.g. wrong number of args, a bad flag, a syntax error in an option, etc.
This code supersedes sysexists EXIT_USAGE=64, which is old and seldom used.

```sh
EXIT_USAGE=2
```

CANCEL: when a user chooses to cancel, such as declines to continue, etc.
Exit 3 meaning CANCEL is a SixArm convention, because it's common for us.
E.g. a prompt says "Continue? yes/no", then the user types "n" for no.

```sh
EXIT_CANCEL=3
```

The input data was incorrect in some way. This should only be used for user's
data and not system files.

```sh
EXIT_DATAERR=65
```

An input file-- not a system file-- did not exist or was not readable.  This
could include errors like "No message" to a mailer-- if it cared to catch it.

```sh
EXIT_NOINPUT=66
```

The user specified did not exist. This might be used for mail addresses or
remote logins.

```sh
EXIT_NOUSER=67
```

The host specified did not exist. This is used in mail addresses or network
requests.

```sh
EXIT_NOHOST=68
```

A service is unavailable. This can occur if a support program or file does not
exist. This can also be used as a catchall message when something you wanted
to do does not work, but you do not know why.

```sh
EXIT_UNAVAILABLE=69
```

An internal software error has been detected. This should be limited to
non-operating system related errors as possible.

```sh
EXIT_SOFTWARE=70
```

An operating system error has been detected. This is intended to be used for
such things as "cannot fork", "cannot create pipe", or the like.  It includes
things like getuid returning a user that does not exist in the passwd file.

```sh
EXIT_OSERR=71
```

Some system file (e.g. /etc/passwd, /var/run/utx.active, etc.) does not exist,
cannot be opened, or has some sort of error (e.g. syntax error).

```sh
EXIT_OSFILE=72
```

A user-specified output file cannot be created.

```sh
EXIT_CANTCREAT=73
```

An error occurred while doing I/O on some file.

```sh
EXIT_IOERR=74
```

Temporary failure, indicating something that is not really an error.  In
sendmail, this means that a mailer (e.g. could not create a connection) and
the request should be reattempted later.

```sh
EXIT_TEMPFAIL=75
```

The remote system returned something that was "not possible" during a protocol
exchange.

```sh
EXIT_PROTOCOL=76
```

You did not have sufficient permission to perform the operation.  This is not
intended for file system problems, which should use EXIT_NOINPUT or
EXIT_CANTCREAT, but rather for higher level permissions.

```sh
EXIT_NOPERM=77
```

Something was found in an unconfigured or misconfigured state.

```sh
EXIT_CONFIG=78
```

Git bisect: The special exit code 125 should be used when the current source
code cannot be tested. If the script exits with this code, the current
revision will be skipped (see git bisect skip above). 125 was chosen as the
highest sensible value to use for this purpose, because 126 and 127 are used
by POSIX shells to signal specific error status (127 is for command not found,
126 is for command found but not executable—​these details do not matter, as
they are normal errors in the script, as far as bisect run is concerned).

```sh
EXIT_GIT_BISECT_SKIP=125
```

GNU bash: If a command is found but is not executable, then return 126. 

```sh
EXIT_COMMAND_FOUND_BUT_NOT_EXECUTABLE=126
```

GNU bash: If a command is not found, then return 127. 

```sh
EXIT_COMMAND_NOT_FOUND=127
```
