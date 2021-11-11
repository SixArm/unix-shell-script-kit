# SixArm Unix shell functions

SixArm is a consulting group that creates software and systens.

[`sixarm-unix-shell-functions`](sixarm-unix-shell-functions) is 
our file of general-purpose Unix functions, with emphasis on 
small functions, clear examples, and POSIX compatibility.

## Tracking

* Package: sixarm-unix-shell-functions
* Version: 9.0.0
* Created: 2017-08-22T00:00:00Z
* Updated: 2021-11-11T21:02:26Z
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

## Directory helpers

### pushdx: pushd with silencer

Example:

```sh
pushdx tmp
=> change to directory "tmp"
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

## Home helpers

### log_home: directory for log files (analogous to system /var/log)

Example:

```sh
log_home
=> ~/.log
```

Source:

```sh
log_home() {
        out "${LOG_HOME:-${XDG_LOG_HOME:-$HOME/.log}}"
}
```

### temp_home: directory for temporary files (analogous to system /tmp)

Example:

```sh
temp_home
=> ~/.temp
```

Source:

```sh
temp_home() {
        out "${TEMP_HOME:-${XDG_LOG_HOME:-$HOME/.temp}}"
}
```

### data_home: directory for data files (analogous to system /usr/share)

Example:

```sh
data_home
=> ~/.local/share
```

Source:

```sh
data_home() {
        out "${DATA_HOME:-${XDG_DATA_HOME:-$HOME/.local/share}}"
}
```

### cache_home: directory for cache files (analogous to system /var/cache)

Example:

```sh
cache_home
=> ~/.cache
```

Source:

```sh
cache_home() {
        out "${CACHE_HOME:-${XDG_CACHE_HOME:-$HOME/.cache}}"
}
```

### config_home: directory for configuration files (analogous to system /etc)

Example:

```sh
config_home
=> ~/.config
```

Source:

```sh
config_home() {
        out "${CONFIG_HOME:-${XDG_CONFIG_HOME:-$HOME/.config}}"
}
```

### runtime_home: directory for runtime files such as sockets, named pipes, etc

Example:

```sh
runtime_home
=> ~/.runtime
```

Source:

```sh
runtime_home() {
        out "${RUNTIME_HOME:-${XDG_RUNTIME_HOME:-$HOME/.runtime}}"
}
```

## Time helpers

### now: get the current datetime using ISO standard format

Example:

```sh
now
=> 2021-05-04T22:59:28.000000000+00:00
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
        awk '{ print int($1) }'
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
dot_all ~/tmp
=> . ~/tmp/a.sh
=> . ~/tmp/b.pl
=> . ~/tmp/c.js
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
run_all ~/tmp
=> ~/tmp/a.sh
=> ~/tmp/b.pl
=> ~/tmp/c.js
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
sh_all ~/tmp
=> sh -c ~/tmp/a.sh
=> sh -c ~/tmp/b.pl
=> sh -c ~/tmp/c.js
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
rm_all ~/tmp
=> rm ~/tmp/a.sh
=> rm ~/tmp/b.pl
=> rm ~/tmp/c.js
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

## Array helpers

### array_i: get the array item at index `i`

Example:

```sh
array_i
=> TODO
```

Source:

```sh
array_i() {
        [ $# == 3 ] && awk -F "$2" "{print \$$3}" <<< "$1" || awk "{print \$$2}" <<< "$1"
}
```

### array_n: get the array number of fields a.k.a. length a.k.a. size

Example:

```sh
array_n
=> TODO
```

Source:

```sh
array_n() {
        [ $# == 2 ] && awk -F "$2" "{print NF}" <<< "$1" || awk "{print NF}" <<< "$1"
}
```

## Assert helpers

### assert_test: assert a test utility command succeeds

Example:

```sh
assert_test -x program.sh
=> success i.e. no output

assert_test -x notes.txt
STDERR=> assert_test -x notes.txt  (because failure prints diagnostic info)
```

Source:

```sh
assert_test() {
        test "$1" "$2" || err assert_test "$@"
}
```

### assert_empty: assert an item is empty

Example:

```sh
assert_empty ""
=> success i.e. no output

assert_empty foo
STDERR=> assert_empty foo (because failure prints diagnostic info)
```

Source:

```sh
assert_empty() {
        [ -z "$1" ] || err assert_empty "$@"
}
```

### assert_equal: assert an item is equal to another item

Example:

```sh
assert_equal foo foo
=> success i.e. no output

assert_equal foo bar
STDERR=> assert_equal foo bar (because failure prints diagnostic info)
```

Source:

```sh
assert_equal() {
        [ "$1" = "$2" ] || err assert_equal "$@"
}
```

### assert_match: assert a regular expression matches an item

Example:

```sh
assert_match o foo
=> success i.e. no output

assert_match x foo
STDERR=> assert_match x foo
```

Source:

```sh
assert_match() {
        [[ "$2" =~ $1 ]] || err assert_match "$@"
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
