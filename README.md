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

## Tracking

* Package: posix-shell-script-kit
* Version: 11.0.4
* Created: 2017-08-22T00:00:00Z
* Updated: 2023-03-22T15:32:10Z
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

Print error message to stderr, then exit with error code 1.

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

command_exists_or_die curl
STDERR=> Command needed: curl
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


### reject_character_class

Get a string's characters that don't match a class, with optional offset and length.

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

## Exit codes

Our POSIX shell programs call "exit" with an exit code value.

Conventions:

* 0 = success, and non-zero indicates any other issue.

* 1 = failure

* 2 = failure due to a usage problem

* 3-63 are for a program's progam-specific exit codes.

* 64-78 are based on sysexits documentation from the 1980's.

* 80-119 are SixArm conventions that we find useful in many programs.

Many POSIX shells use exit code 126 and 127 to signal specific error status:
126 is for command found but not executable, and 127 is for command not found.

* 126 is for the shell and indicates command found but not executable.

* 127 is for the shell and indicate command not found.

Many POSIX shells use exit codes above 128 in their $? representation of the
exit status to encode the signal number of a process being killed.

The pre-defined exit codes from sysexits can be used, so the caller of the
process can get a rough estimation about the failure class without looking up
the source code.

See https://man.openbsd.org/sysexits.3

We recommend:

* Authentication issues: EXIT_NOUSER

* Authoriziation issues: EXIT_NOPERM

The exit code list below is subject to change over time, as we learn more.


### Success

The program succeeded.

Exit 0 meaning success is a widespread convention as a catch-all code.

```sh
EXIT_SUCCESS=0
```

### Failure

The program failed.

E.g. an error, an abort, found no results, lack of data, etc.

Exit 1 meaning failure is a widespread convention as a catch-all code.

```sh
EXIT_FAILURE=1
```

### Usage

The program usage is incorrect, or malformed, or in conflict, etc.

E.g. wrong number of args, a bad flag, a syntax error in an option, etc.

Exit 2 meaning usage is a widespread convention as a catch-all CLI code.

```sh
EXIT_USAGE=2
```

### Data Err

The input data was incorrect in some way. This should only be used
for user's data and not system files.

```sh
EXIT_DATAERR=65
```

### No Input

An input file-- not system file-- did not exist or was not readable.
This could include errors like "No message" to a mailer, if it cared about it.

```sh
EXIT_NOINPUT=66
```

### No User

The user specified did not exist. This might be used for mail
addresses or remote logins, or when no user is found during authentication.

```sh
EXIT_NOUSER=67
```

### No Host

The host specified did not exist. This is used in mail addresses or
network requests.

```sh
EXIT_NOHOST=68
```

### Unavailable

A service is unavailable. This can occur if a support program or
file does not exist. This can also be used as a catchall message when
something you wanted to do does not work, but you do not know why.

```sh
EXIT_UNAVAILABLE=69
```

### Software

An internal software error has been detected. This should be limited
to non-operating system related errors as possible.

```sh
EXIT_SOFTWARE=70
```

### OS Err

An operating system error has been detected. This is intended for such
things as "cannot fork", "cannot create pipe", or the like.  It includes
things like getuid returning a user that does not exist in the passwd file.

```sh
EXIT_OSERR=71
```

### OS File

An operating system file (e.g. /etc/passwd) does not exist, or cannot
be opened, or has some sort of error (e.g. syntax error).

```sh
EXIT_OSFILE=72
```

### Can't Create

A user-specified output (e.g. a file) cannot be created.

```sh
EXIT_CANTCREATE=73
```

### IO Err

An error occurred while doing I/O on some file.

```sh
EXIT_IOERR=74
```

### Temp Fail

A temporary failure occurred; this is not a permanent error.
E.g. a mailer could not create a connection. The request can be retried later.

```sh
EXIT_TEMPFAIL=75
```

### Protocol

The remote system returned something that was "not possible" during
a protocol exchange.

```sh
EXIT_PROTOCOL=76
```

### No Perm

You did not have sufficient permission to perform the operation. This
is not for file system problems, which use EXIT_NOINPUT or EXIT_CANTCREATE,
but rather for higher level permissions, access control authorization, etc.

```sh
EXIT_NOPERM=77
```

### Config

Something was found in an unconfigured or misconfigured state.

```sh
EXIT_CONFIG=78
```

### Exit codes 80-119

Exit codes 80-119 are for our own SixArm conventions.

We propose these are generally useful to many kinds of programs.

Caution: these exit codes and their values are work in progress, 
draft only, as a request for comments, in version 11.x of this file.
These exit codes will be set in version 12.x when it's released.

* 80+ for user interation issues

* 90+ for access control issues

* 100+: process runtime issues

* 110+: expected ability issues

### Quit

The user chose to quit, or cancel, or abort, or not continue, etc.

```sh
EXIT_QUIT=80
```

### KYC

Know Your Customer means the program requires more user information.
E.g. email validation, age verification, terms of service agreement, etc.

```sh
EXIT_KYC=81
```

### Update

The program or its dependencies need an update, or upgrade, etc.

```sh
EXIT_UPDATE=82
```

### Conflict

An item has a conflict e.g. edit collision, or merge error, etc.

Akin to HTTP status code 409 Conflict.

```sh
EXIT_CONFLICT=91
```

### Unlawful

E.g. prohibited due to law, or warrant, or court order, etc.

Akin to HTTP status code 451 Unavailable For Legal Reasons (RFC 7725).

```sh
EXIT_UNLAWFUL=92
```

### Payment Issue

E.g. needs a credit card, or invoice, or billing, etc.

Akin to HTTP status code 402 Payment Required.

```sh
EXIT_PAYMENT_ISSUE=93
```

### Busy

A process is too busy, or overloaded, or throttled, or breakered, etc.

Akin to HTTP status code 503 Service Unavailable; always means overloaded.

```sh
EXIT_BUSY=100
```

### Timeout

A process is too slow, or estimated to take too long, etc.

Akin to HTTP status code 408 Request Timeout.

```sh
EXIT_TIMEOUT=101
```

### Lockout

A process is intentionally blocked as a danger, hazard, risk, etc.

This is for lockout-tagout (LOGO) safety, or protecting users or data, etc.

```sh
EXIT_LOCKOUT=102
```

### Loop

A process has detected an infinite loop, so is aborting.

Akin to HTTP status code 508 Loop Detected.

```sh
EXIT_LOOP=103
```

### Gone

An expected ability has been intentionally removed, or deleted, etc.

Akin to HTTP status code 410 Gone; the ability should be purged.

```sh
EXIT_GONE=110
```

### TODO

An expected ability is not yet implemented, or work in progress, etc.

Akin to HTTP status code 501 Not Implemented; implies future availability.

```sh
EXIT_TODO=111
```

### Git bisect skip

Git bisect: The special exit code 125 should be used when the current source
code cannot be tested. If the script exits with this code, the current
revision will be skipped (see git bisect skip above). 125 was chosen as the
highest sensible value to use for this purpose, because 126 and 127 are used
by POSIX shells to signal specific error status; see below for details.

```sh
EXIT_GIT_BISECT_SKIP=125
```

### Command found but not executable

Command found but not executable: A command is found but is not executable.

```sh
EXIT_COMMAND_FOUND_BUT_NOT_EXECUTABLE=126
```

### Command not found

Command not found: A command is not found. 

```sh
EXIT_COMMAND_NOT_FOUND=127
```
