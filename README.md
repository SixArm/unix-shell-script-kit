# Unix shell functions

SixArm is a consulting group that creates software and systems.

This is our POSIX shell script file of general-purpose functions.

We aim to emphasize is small functions and clear examples.

Constructive feedback is welcome and appreciated.

To download this file:

```sh
curl -O "https://raw.githubusercontent.com/SixArm/sixarm-unix-shell-functions/main/sixarm-unix-shell-functions"
```

## Tracking

* Package: sixarm-unix-shell-functions
* Version: 10.0.0
* Created: 2017-08-22T00:00:00Z
* Updated: 2023-01-23T19:24:54Z
* License: GPL-2.0-or-later or contact us for custom license
* Contact: Joel Parker Henderson (joel@sixarm.com)

## Input/output helpers

### out: print output message to stdout

Example:

```sh
out "my message"
=> my message
```

Source:

```sh
out() {
        printf %s\\n "$*"
}
```

### err: print error message to stderr

Example:

```sh
err "my message"
STDERR=> my message
```

Source:

```sh
err() {
        >&2 printf %s\\n "$*"
}
```

### die: print error message to stderr, then exit with error code 1

Example:

```sh
die 1 "my message"
STDERR=> my message
=> exit 1
```

Source:

```sh
die() {
        n="$1"; shift; >&2 printf %s\\n "$*" ; exit "$n"
}
```

### big: print a big banner to stdout, good for human readability

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

Source:

```sh
big() {
        printf \\n###\\n#\\n#\ %s\\n#\\n###\\n\\n "$*"
}
```

### log: print a datestamp, unique random id, hostname, process id, and message

Example:

```sh
log "my message"
=> 2021-05-04T22:57:54.000000000+00:00 7e7151dc24bd511098ebb248771d8ffb abc.example.com 1234 my message
```

Source:

```sh
log() {
        printf '%s %s %s %s\n' "$( now )" "$( zid )" "$( hostname )" $$ "$*"
}
```

### zid: generate a 32-bit secure random lowercase hex identifier

Example:

```sh
zid
=> 78577554e967951388b5907854b4c337
```

Source:

```sh
zid() {
        hexdump -n 16 -v -e '16/1 "%02x" "\n"' /dev/random
}
```

### ask: prompt the user for a line of input, then return a trimmed string

Source:

```sh
ask() {
        read x ; echo "$x" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//'
}
```

Example:

```sh
ask
=> prompt
```

## Exit codes

It is good practice to call exit with a value that indicates success (0) 
or a failure condition when ending a program. The pre-defined exit codes
from sysexits can be used, so the caller of the process can get a rough
estimation about the failure class without looking up the source code.

The successful exit is always indicated by a status of 0. 

Error numbers begin at EX__BASE to reduce the possibility of clashing with
other exit statuses that random programs may already return. The meaning of
the codes is approximately as follows.

Success:

```sh
EX_OK=0
```

Usage: The command was used incorrectly, e.g., with the wrong number of
arguments, a bad flag, a bad syntax in a parameter, or whatever.

```sh
EX_USAGE=64
```

Data error: The input data was incorrectin someway. This should only be used for
user's data and not system files.

```sh
EX_DATAERR=65
```

No input: An input file-- not a system file-- did not exist or was not readable.
This could include errors like "No message" to a mailer-- if it cared to catch
it.

```sh
EX_NOINPUT=66
```

No user: The user specified did not exist. This might be used for mail addresses
or remote logins.

```sh
EX_NOUSER=67
```

No host: The host specified did not exist. This is used in mail addresses or
network requests.

```sh
EX_NOHOST=68
```

Unavailable: A service is unavailable. This can occur if a support program or
file does not exist. This can also be used as a catchall message when something
you wanted to do does not work, but you do not know why.

```sh
EX_UNAVAILABLE=69
```

Software: An internal software error has been detected. This should be limited
to non-operating system related errors as possible.

```sh
EX_SOFTWARE=70
```

OS error: An operating system error has been detected. This is intended to be
used for such things as "cannot fork", "cannot create pipe", or the like.  It
includes things like getuid returning a user that does not exist in the passwd
file.

```sh
EX_OSERR=71
```

OS file: Some system file (e.g. /etc/passwd, /var/run/utx.active, etc.) does not
exist, cannot be opened, or has some sort of error (e.g. syntax error).

```sh
EX_OSFILE=72
```

Can't create: A user-specified output file cannot be created.

```sh
EX_CANTCREAT=73
```

IO error: An error occurred while doing I/O on some file.

```sh
EX_IOERR=74
```

Temp fail: Temporary failure, indicating something that is not really an error.
In sendmail, this means that a mailer (e.g. could not create a connection) and
the request should be reattempted later.

```sh
EX_TEMPFAIL=75
```

Protocol: The remote system returned something that was "not possible" during a
protocol exchange.

```sh
EX_PROTOCOL=76
```

No perm: You did not have sufficient permission to perform the operation.  This
is not intended for file system problems, which should use EX_NOINPUT or
EX_CANTCREAT, but rather for higher level permissions.

```sh
EX_NOPERM=77
```

Config: Something was found in an unconfigured or misconfigured state.

```sh
EX_CONFIG=78
```

Git bisect: The special exit code 125 should be used when the current source
code cannot be tested. If the script exits with this code, the current
revision will be skipped (see git bisect skip above). 125 was chosen as the
highest sensible value to use for this purpose, because 126 and 127 are used
by POSIX shells to signal specific error status (127 is for command not found,
126 is for command found but not executable—​these details do not matter, as
they are normal errors in the script, as far as bisect run is concerned).

```sh
EX_GIT_BISECT_SKIP=125
```

GNU bash: If a command is found but is not executable, then return 126. 

```sh
EX_COMMAND_FOUND_BUT_NOT_EXECUTABLE=126
```

GNU bash: If a command is not found, then return 127. 

```sh
EX_COMMAND_NOT_FOUND=127
```

## Directory helpers

### pushdx: pushd with silencer

Example:

```sh
pushdx temp
=> change to directory "temp"
```

Source:

```sh
pushdx() {
        command pushd "$@" > /dev/null
}
```

### popdx: popd with silencer

Example:

```sh
popdx
=> change to previous directory
```

Source:

```sh
popdx() {
        command popd "$@" > /dev/null
}
```

### user_dir: get user-specific directory via env var or XDG setting or HOME.

Example:

```sh
user_dir log
=> $FOO_DIR
=> $FOO_HOME
=> $XDG_FOO_DIR
=> $XDG_FOO_HOME
=> $HOME/foo
```

## Time helpers

### now: get a datetime using our preferred ISO standard format

Example:

```sh
now
=> 2021-05-04T22:59:28.000000000+00:00
```

Example with a custom datetime:

```sh
now -d "2021-01-01" 
=> 2021-01-01T00:00:00.000000000+00:00
```

Source:

```sh
now() {
        date -u "+%Y-%m-%dT%H:%M:%S+00:00" "$@"
}
```

### now_date: get a date using our preferred ISO standard format

Example:

```sh
now_date
=> 2021-05-04
```

Source:

```sh
now() {
        date -u "+%Y-%m-%dT%H:%M:%S+00:00" "$@"
}
```

### sec: get the current time in Unix seconds

Example:

```sh
sec
=> 1620169178
```

Source:

```sh
sec() {
        date "+%s"
}
```

### age: get the age of a given time in Unix secords

Example:

```sh
age 1620169178
=> 19
```

Source:

```sh
age() {
        printf %s\\n "$(( $(date "+%s") - $1 ))"; }
```

### newer: is the age of a given time newer than a given number of seconds?

Example:

```sh
newer 2000000000 && echo "true" || echo "false
=> true
```

Source:

```sh
newer() {
        [ "$(( $(date "+%s") - $1 ))" -lt "$2" ]
}
```

### older: is the age of a given time older than a given number of seconds?

Example:

```sh
older 1000000000 && echo "true" || echo "false"
=> true
```

Source:

```sh
older() {
        [ "$(( $(date "+%s") - $1 ))" -gt "$2" ]
}
```

## Validation helpers

### cmd: return true iff a command exists

Example:

```sh
cmd grep
=> true

cmd curl
=> false
```

Source:

```sh
cmd() {
        command -v "$1" >/dev/null 2>&1
}
```

### cmd_or_die: ensure a command exists, otherwise die with a help message

Example:

```sh
cmd_or_die grep
=> true

cmd_or_die curl
STDERR=> Command needed: curl
=> exit 1
```


Source:

```sh
cmd_or_die() {
        cmd "$1" || die "$EX_UNAVAILABLE" "Command needed: $1"
}
```

### cmd_ver_or_die: ensure a command exists and version is sufficient, otherwise die with a help message

Example:

```sh
cmd_ver_or_die grep 1.1 2.2
=> true

cmd_ver_or_die grep 3.3 2.2
STDERR=> Command version needed: grep >= 3.3 (not 2.2)
=> exit 1
```

Source:

```sh
cmd_ver_or_die() {
        cmd "$1" && ver "$2" "$3" || die "$EX_UNAVAILABLE" "Command version needed: $1 >= $2 (not ${3:-?})"
}
```

### var: return true iff a variable exists

Example:

```sh
var HOME
=> true

var FOO
=> false
```

Source:

```sh
var() {
        ! eval 'test -z ${'$1'+x}'
}
```

### var_or_die: ensure a variable exists, otherwise die with a help message

Example:

```sh
var_or_die HOME
=> true

var_or_die FOO
STDERR=> Variable needed: FOO
=> exit 1
```

Source:

```sh
var_or_die() {
        var "$1" || die "$EX_CONFIG" "Variable needed: $1"
}
```

### ver: return true iff a version is sufficient.

Example:
 ```
ver 1.1 2.2
=> true

ver 3.3 2.2
=> false
```

Source:

```sh
ver() {
        [ "$(cmp_digits "$1" "$2")" -le 0 ]
}
```

### ver_or_die: ensure a version is sufficient, otherwise die with a help message

Example:
 ```
ver_or_die 1.1 2.2
=> true

ver_or_die 3.3 2.2
STDERR=> Version needed: >= 3.3 (not 2.2)
```

Source:

```sh
ver_or_die() {
        ver "$1" "$2" || die "$EX_CONFIG" "Version needed: >= $1 (not ${2:-?})"
}
```

## Number helpers

### int: convert a number string to an integer number string

Example:

```sh
int 1.23
=> 1
```

Source:

```sh
int() {
        printf %s\\n "$1" | awk '{ print int($0); exit }'
}
```

### sum: print the sum of numbers

Example:

```sh
sum 1 2 3
=> 6
```

Source:

```sh
sum() {
        awk '{for(i=1; i<=NF; i++) sum+=$i; } END {print sum}'
}
```

## Comparison helpers

### cmp_alnums: compare alnums as groups, such as for word version strings.

Example:

```sh
cmp_alnums "a.b.c" "a.b.d"
# => -1 (negative one means left < right)
```

Source: see file


### cmp_digits: compare digits as groups, such as for number version strings.

Example:

```sh
cmp_digits "1.2.3" "1.2.4"
# => -1 (negative one means left < right)
```

Source: see file

## Extensibility helpers

### dot_all: source all the executable files in a given directory and subdirectories

Example:

```sh
dot_all ~/temp
=> . ~/temp/a.sh
=> . ~/temp/b.pl
=> . ~/temp/c.js
```

Source:

```sh
dot_all() {
        find "${1:-.}" -type f \( -perm -u=x -o -perm -g=x -o -perm -o=x \) -exec test -x {} \; -exec . {} \;
}
```

### run_all: run all the executable commands in a given directory and subdirectories

Example:

```sh
run_all ~/temp
=> ~/temp/a.sh
=> ~/temp/b.pl
=> ~/temp/c.js
```

Source:

```sh
run_all() {
        find "${1:-.}" -type f \( -perm -u=x -o -perm -g=x -o -perm -o=x \) -exec test -x {} \; -exec {} \;
}
```

### sh_all: shell all the executable commands in a given directory and subdirectories

Example:

```sh
sh_all ~/temp
=> sh -c ~/temp/a.sh
=> sh -c ~/temp/b.pl
=> sh -c ~/temp/c.js
```

Source:

```sh
sh_all() {
        find "${1:-.}" -type f \( -perm -u=x -o -perm -g=x -o -perm -o=x \) -exec test -x {} \; -print0 | xargs -0I{} -n1 sh -c "{}"
}
```

### rm_all: remove all files in a given directory and subdirectories-- use with caution

Example:

```sh
rm_all ~/temp
=> rm ~/temp/a.sh
=> rm ~/temp/b.pl
=> rm ~/temp/c.js
```

Source:

```sh
rm_all() {
        find "${1:-.}" -type f -exec rm {} \;
}
```

## Text helpers

### trim: remove any space characters at the text's start or finish

Example:

```sh
trim "  foo  "
=> foo
```

Source:

```sh
trim() {
        printf %s\\n "$*" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//'
}
```


### slug: convert a string from any characters to solely lowercase and single internal dash characters

Example:

```sh
slug "**Foo** **Goo** **Hoo**"
=> foo-goo-hoo
```

Source:

```sh
slug() {
        printf %s\\n "$*" | sed 's/[^[:alnum:]]/_/g; s/--*/-/; s/^-*//; s/-*$//;' | tr '[[:upper:]]' '[[:lower:]]'
}
```

### slugs: convert a string from any characters to solely lowercase and single internal dash characters and slash characters.

Example:

```sh
slugs "**Foo** / **Goo** / **Hoo**"
=> foo/goo/hoo
```

Source:

```sh
slugs() {
        printf %s\\n "$*" | sed 's/[^[:alnum:]\/]/-/g; s/--*/-/g; s/^-*//; s/-*$//; s/-*\/-*/\//g' | tr '[[:upper:]]' '[[:lower:]]'
}
```


### upper_format: convert text from any lowercase letters to uppercase letters

Example:

```sh
upper_format AbCdEf
=> ABCDEF
```

Source:

```sh
upper_format() {
        printf %s\\n "$*" | tr '[[:lower:]]' '[[:upper:]]'
}
```

### lower_format: convert text from any uppercase letters to lowercase letters

Example:

```sh
lower_format AbCdEf
=> abcdef
```

Source:

```sh
lower_format() {
        printf %s\\n "$*" | tr '[[:upper:]]' '[[:lower:]]'
}
```

### chain_format: convert a string from any characters to solely alphanumeric and single internal dash characters

Example:

```sh
chain_format "**Foo** **Goo** **Hoo**"
=> Foo-Goo-Hoo
```

Source:

```sh
chain_format() {
        printf %s\\n "$*" | sed 's/[^[:alnum:]]\{1,\}/-/g; s/-\{2,\}/-/g; s/^-\{1,\}//; s/-\{1,\}$//;'
}
```

### snake_format: convert a string from any characters to solely alphanumeric and single internal underscore characters

Example:

```sh
snake_format "**Foo** **Goo** **Hoo**"
=> Foo_Goo_Hoo
```

Source:

```sh
snake_format() {
        printf %s\\n "$*" | sed 's/[^[:alnum:]]\{1,\}/_/g; s/_\{2,\}/_/g; s/^_\{1,\}//; s/_\{1,\}$//;'
}
```

### space_format: convert a string from any characters to solely alphanumeric and single internal space characters

Example:

```sh
space_format "**Foo** **Goo** **Hoo**"
=> Foo Goo Hoo
```

Source:

```sh
space_format() {
        printf %s\\n "$*" | sed 's/[^[:alnum:]]\{1,\}/ /g; s/ \{2,\}/ /g; s/^ \{1,\}//; s/ \{1,\}$//;'
}
```

### touch_format: convert a string from any characters to solely a command "touch -t" timestamp format

Example:

```sh
touch_format "Foo  2021-05-04 22:57:54 Goo"
=> 202105042257.54
```

Source:

```sh
touch_format() {
        printf %s\\n "$*" | sed 's/[^[:digit:]]//g; s/^\([[:digit:]]\{12\}\)\([[:digit:]]\{2\}\)/\1.\2/;'
}
```

### select_character_class: get a string's characters that match a class, with optional offset and length

Syntax: select_character_class <string> <class> [offset [length]]

Example:

```sh
select_character_class foo123goo456 alpha
=> foogoo
```

Example with substring offset:

```sh
select_character_class foo123goo456 alpha 3
=> goo
```

Example with substring offset and length:

```sh
select_character_class foo123goo456 alpha 3 1
=> g
```

Source:

```sh
select_character_class() {
	string=${1//[^[:$2:]]/}
	offset=${3:-0}
	length=${4:-${#string}}
	printf %s\\n ${string:$offset:$length}
}
```

### reject_character_class: get a string's characters that don't match a class, with optional offset and length

Example:

```sh
reject_character_class foo123goo456 alpha
=> 123456
```

Example with substring offset:

```sh
reject_character_class foo123goo456 alpha 3
=> 456
```

Example with substring offset and length:

```sh
reject_character_class foo123goo456 alpha 3 1
=> 4
```

Source:

```sh
reject_character_class() {
	string=${1//[[:$2:]]/}
	offset=${3:-0}
	length=${4:-${#string}}
	printf %s\\n ${string:$offset:$length}
}
```

## Array helpers

### array_n: get the array number of fields a.k.a. length a.k.a. size

Example:

```sh
set -- a b c d
array_n "$@"
=> 4
```

### array_i: get the array item at index `i` which is 1-based.

Example:

```sh
set -- a b c d
array_i  "$@" 3
=> c
```

### array_first: return the array's first item.

Example:

```
set -- a b c d
array_first "$@"
=> a
```

### array_last: return the array's last item.

Example:

```
set -- a b c d
array_last "$@"
=> d
```

### array_car: return the array's car item a.k.a. first item.

Example:

```
set -- a b c d
array_car "$@"
=> a
```

### array_cdr: return the array's cdr items a.k.a. everything after the first item.

Example:

```
set -- a b c d
array_car "$@"
=> b c d
```

## Assert helpers

### assert_test: assert a test utility command succeeds

Example:

```sh
assert_test -x program.sh
=> success i.e. no output

assert_test -x notes.txt
STDERR=> assert_test -x notes.txt 
```

Source:

```sh
assert_test() {
        test "$1" "$2" || err assert_test "$@"
}
```

### assert_empty: assert an item is empty i.e. null

Example:

```sh
assert_empty ""
=> success i.e. no output

assert_empty foo
STDERR=> assert_empty foo
```

Source:

```sh
assert_empty() {
        [ -z "$1" ] || err assert_empty "$@"
}
```

### assert_not_empty: assert an item is not empty i.e. not null

Example:

```sh
assert_not_empty foo
=> success i.e. no output

assert_not_empty ""
STDERR=> assert_not_empty
```

Source:

```sh
assert_not_empty() {
        [ -n "$1" ] || err assert_not_empty "$@"
}
```

### assert_int_(eq|ne|ge|gt|le|lt): assert an integer or string versus another

Example:

```sh
assert_int_eq 1 1
=> success i.e. no output

assert_int_eq 1 2
STDERR=> assert_int_eq 1 2
```

Source:

```sh
assert_int_eq() {
        [ "$1" -eq "$2" ] || err assert_int_eq "$@"
}
```

There are comparison assertions for integers:

* `assert_int_eq` is equal to
* `assert_int_ne` is not equal to 
* `assert_int_ge` is greater than or equal to
* `assert_int_gt` is greater than
* `assert_int_le` is less than or equal to
* `assert_int_lt` is less than

### assert_str_(eq|ne|ge|gt|le|lt): assert a string versus another string

Example:

```sh
assert_str_eq foo foo
=> success i.e. no output

assert_str_eq foo bar
STDERR=> assert_str_eq foo bar
```

Source:

```sh
assert_str_eq() {
        [ "$1" = "$2" ] || err assert_str_eq "$@"
}
```

There are comparison assertions for strings:

* `assert_str_eq` is equal to
* `assert_str_ne` is not equal to 
* `assert_str_ge` is greater than or equal to
* `assert_str_gt` is greater than
* `assert_str_le` is less than or equal to
* `assert_str_lt` is less than

### assert_str_starts_with: assert a string starts with a substring

Example:

```sh
assert_str_starts_with foobar foo
=> success i.e. no output

assert_str_starts_with foobar xxx
STDERR=> assert_str_starts_with foobar xxx
```

Source:

```sh
assert_str_starts_with() {
        [ "$1" != "${1#"$2"}" ] || err assert_str_starts_with "$@"
}
```

### assert_str_ends_with: assert a string ends with with a substring

Example:

```sh
assert_str_ends_with foobar foo
=> success i.e. no output

assert_str_ends_with foobar xxx
STDERR=> assert_str_ends_with foobar xxx
```

Source:

```sh
assert_str_ends_with() {
        [ "$1" != "${1%"$2"}" ] || err assert_str_ends_with "$@"
}
```

## Make temp helpers

### mktemp_dir: make a temporary directory path

Example:

```sh
mktemp_dir
=> /var/folders/4f7b65122b0fb65b0fdad568a65dc97d
```

Source:

```sh
mktemp_dir() {
        x=$(mktemp -d -t "${1:-$(zid)}") ; trap '{ rm -rf "$x"; }' EXIT ; out "$x"
}
```

### mktemp_file: make a temporary file path

Example:

```sh
mktemp_file
=> /var/folders/4f7b65122b0fb65b0fdad568a65dc97d/1d9aafac5373be95d8b4c2dece0b1197
```

Source:

```sh
mktemp_file() {
        x=$(mktemp -t "${1:-$(zid)}") ; trap '{ rm -f "$x"; }' EXIT ; out "$x"
}
```

## Media helpers

### file_media_type: get a file's media type a.k.a. mime type such as "text/plain"

Example:

```sh
file_media_type notes.txt
=> text/plain
```

Source:

```sh
file_media_type() {
        file --brief --mime "$1"
}
```

### file_media_type_supertype: get a file's media type type a.k.a. mime type such as "text"

Example:

```sh
file_media_type_supertype notes.txt
=> text
```

Source:

```sh
file_media_type_supertype() {
        file --brief --mime "$1" | sed 's#/.*##'
}
```

### file_media_type_subtype: get a file's media type subtype a.k.a. mime type such as "plain"

Example:

```sh
file_media_type_subtype notes.txt
=> plain
```

Source:

```sh
file_media_type_subtype() {
        file --brief --mime "$1" | sed 's#^[^/]*/##; s#;.*##'
}
```

## Font helpers

### font_exists: does a font name exist on this system?

Example:

```sh
font_exists Arial
=> true

font_exists Foo
=> false
```

Source:

```sh
font_exists() {
        fc-list | grep -q ": $1:"
}
```

### font_exists_or_die: ensure a font name exists.

Example:

```sh
font_exists_or_die Arial
=> true

font_exists_or_die Foo
STDERR=> Font needed: Foo
=> exit 1
```

Source:

```sh
font_exists_or_die() {
        font_exists "$1" || die "$EX_UNAVAILABLE" "Font needed: $1" 
}
```

## Content helpers

### file_ends_with_newline: file ends with newline?

Example:

```sh
file_ends_with_newline notes.txt
=> true
```

Source:

```sh
file_ends_with_newline() {
        test $(tail -c1 "$1" | wc -l) -gt 0
}
```
