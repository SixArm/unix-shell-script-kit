# SixArm Unix shell functions

SixArm is a consulting group that creates software and systens.

[`sixarm-unix-shell-functions`](sixarm-unix-shell-functions) is 
our file of general-purpose Unix functions, with emphasis on 
small functions, clear examples, and POSIX compatibility.

## Tracking

* Package: sixarm-unix-shell-functions
* Version: 8.0.0
* Created: 2017-08-22T00:00:00Z
* Updated: 2021-08-20T03:26:04Z
* License: GPL-2.0-only or contact us for custom license
* Contact: Joel Parker Henderson (joel@sixarm.com)

## Input/output helpers

### out: print output message to stdout

Example:
```
out "my message"
=> my message
```

Source:
```
out() {
        printf %s\\n "$*"
}
```

### err: print error message to stderr

Example:
```
err "my message"
STDERR=> my message
```

Source:
```
err() {
        >&2 printf %s\\n "$*"
}
```

### die: print error message to stderr, then exit with error code 1

Example:
```
die "my message"
STDERR=> my message
=> exit 1
```

Source:
```
die() {
        >&2 printf %s\\n "$*" ; exit 1
}
```

### big: print a big banner to stdout, good for human readability

Example:
```
big "my message"
=>
###
#
# my message
#
###
```

Source:
```
big() {
        printf \\n###\\n#\\n#\ %s\\n#\\n###\\n\\n "$*"
}
```

### log: print a datestamp, unique random id, hostname, process id, and message

Example:
```
log "my message"
=> 2021-05-04T22:57:54.000000000+00:00 7e7151dc24bd511098ebb248771d8ffb abc.example.com 1234 my message
```

Source:
```
log() {
        printf '%s %s %s %s\n' "$( now )" "$( zid )" "$( hostname )" $$ "$*"
}
```

### zid: generate a 32-bit secure random lowercase hex identifier

Example:
```
zid
=> 78577554e967951388b5907854b4c337
```

Source:
```
zid() {
        hexdump -n 16 -v -e '16/1 "%02x" "\n"' /dev/random
}
```

### ask: prompt the user for a line of input, then return a trimmed string

Source:
```
ask() {
        read x ; echo "$x" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//'
}
```

Example:
```
ask
=> prompt
```

## Directory helpers

### pushdx: pushd with silencer

Example:
```
pushdx tmp
=> change to directory "tmp"
```

Source:
```
pushdx() {
        command pushd "$@" > /dev/null
}
```

### popdx: popd with silencer

Example:
```
popdx
=> change to previous directory
```

Source:
```
popdx() {
        command popd "$@" > /dev/null
}
```

## Home helpers

### log_home: directory for log files (analogous to system /var/log)

Example:
```
log_home
=> ~/.log
```

Source:
```
log_home() {
        out "${LOG_HOME:-${XDG_LOG_HOME:-$HOME/.log}}"
}
```

### temp_home: directory for temporary files (analogous to system /tmp)

Example:
```
temp_home
=> ~/.temp
```

Source:
```
temp_home() {
        out "${TEMP_HOME:-${XDG_LOG_HOME:-$HOME/.temp}}"
}
```

### data_home: directory for data files (analogous to system /usr/share)

Example:
```
data_home
=> ~/.local/share
```

Source:
```
data_home() {
        out "${DATA_HOME:-${XDG_DATA_HOME:-$HOME/.local/share}}"
}
```

### cache_home: directory for cache files (analogous to system /var/cache)

Example:
```
cache_home
=> ~/.cache
```

Source:
```
cache_home() {
        out "${CACHE_HOME:-${XDG_CACHE_HOME:-$HOME/.cache}}"
}
```

### config_home: directory for configuration files (analogous to system /etc)

Example:
```
config_home
=> ~/.config
```

Source:
```
config_home() {
        out "${CONFIG_HOME:-${XDG_CONFIG_HOME:-$HOME/.config}}"
}
```

### runtime_home: directory for runtime files such as sockets, named pipes, etc

Example:
```
runtime_home
=> ~/.runtime
```

Source:
```
runtime_home() {
        out "${RUNTIME_HOME:-${XDG_RUNTIME_HOME:-$HOME/.runtime}}"
}
```

## Time helpers

### now: get the current datetime using ISO standard format

Example:
```
now
=> 2021-05-04T22:59:28.000000000+00:00
```

Source:
```
now() {
        date -u "+%Y-%m-%dT%H:%M:%S+00:00" "$@"
}
```

### sec: get the current time in Unix seconds

Example:
```
sec
=> 1620169178
```

Source:
```
sec() {
        date "+%s"
}
```

### age: get the age of a given time in Unix secords

Example:
```
age 1620169178
=> 19
```

Source:
```
age() {
        printf %s\\n "$(( $(date "+%s") - $1 ))"; }
```

### newer: is the age of a given time newer than a given number of seconds?

Example:
```
newer 2000000000 && echo "true" || echo "false
=> true
```

Source:
```
newer() {
        [ "$(( $(date "+%s") - $1 ))" -lt "$2" ]; }
```

### older: is the age of a given time older than a given number of seconds?

Example:
```
older 1000000000 && echo "true" || echo "false"
=> true
```

Source:
```
older() {
        [ "$(( $(date "+%s") - $1 ))" -gt "$2" ]; }
```

## Validation helpers

### cmd: return true iff a command exists

Example:
```
cmd grep
=> true

cmd curl
=> false
```

Source:
```
cmd() {
        command -v "$1" >/dev/null 2>&1
}
```

### cmd_or_die: ensure a command exists, otherwise die with a help message

Example:
```
cmd_or_die grep
=> true

cmd_or_die curl
STDERR=> Command needed: curl
=> exit 1
```

Source:
```
cmd_or_die() {
        cmd "$1" || die "Command needed: $1"
}
```

### var: return true iff a variable exists

Example:
```
var HOME
=> true

var FOO
=> false
```

Source:
```
var() {
        ! eval 'test -z ${'$1'+x}'
}
```

### var_or_die: ensure a variable exists, otherwise die with a help message

Example:
```
var_or_die HOME
=> true

var_or_die FOO
STDERR=> Variable needed: FOO
=> exit 1
```

Source:
```
var_or_die() {
        var "$1" || die "Variable needed: $1"
}
```

## Number helpers

### int: convert a number string to an integer number string

Example:
```
int 1.23
=> 1
```

Source:
```
int() {
        awk '{ print int($1) }'
}
```

### sum: print the sum of numbers

Example:
```
sum 1 2 3
=> 6
```

Source:
```
sum() {
        awk '{for(i=1; i<=NF; i++) sum+=$i; } END {print sum}'
}
```

## Extensibility helpers

### dot_all: source all the executable files in a given directory and subdirectories

Example:
```
dot_all ~/tmp
=> . ~/tmp/a.sh
=> . ~/tmp/b.pl
=> . ~/tmp/c.js
```

Source:
```
dot_all() {
        find "${1:-.}" -type f \( -perm -u=x -o -perm -g=x -o -perm -o=x \) -exec test -x {} \; -exec . {} \;
}
```

### run_all: run all the executable commands in a given directory and subdirectories

Example:
```
run_all ~/tmp
=> ~/tmp/a.sh
=> ~/tmp/b.pl
=> ~/tmp/c.js
```

Source:
```
run_all() {
        find "${1:-.}" -type f \( -perm -u=x -o -perm -g=x -o -perm -o=x \) -exec test -x {} \; -exec {} \;
}
```

### sh_all: shell all the executable commands in a given directory and subdirectories

Example:
```
sh_all ~/tmp
=> sh -c ~/tmp/a.sh
=> sh -c ~/tmp/b.pl
=> sh -c ~/tmp/c.js
```

Source:
```
sh_all() {
        find "${1:-.}" -type f \( -perm -u=x -o -perm -g=x -o -perm -o=x \) -exec test -x {} \; -print0 | xargs -0I{} -n1 sh -c "{}"
}
```

### rm_all: remove all files in a given directory and subdirectories-- use with caution

Example:
```
rm_all ~/tmp
=> rm ~/tmp/a.sh
=> rm ~/tmp/b.pl
=> rm ~/tmp/c.js
```

Source:
```
rm_all() {
        find "${1:-.}" -type f -exec rm {} \;
}
```

## Text helpers

### trim: remove any space characters at the text's start or finish

Example:
```
trim "  foo  "
=> foo
```

Source:
```
trim() {
        printf %s\\n "$*" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//'
}
```

### slug: convert a string from any characters to solely lowercase and single internal dash characters

Example:
```
slug "**Foo** **Goo** **Hoo**"
=> foo-goo-hoo
```

Source:
```
slug() {
        printf %s\\n "$*" | sed 's/[^[:alnum:]]/_/g; s/--*/-/; s/^-*//; s/-*$//;' | tr '[[:upper:]]' '[[:lower:]]'
}
```

### upper_format: convert text from any lowercase letters to uppercase letters

Example:
```
upper_format AbCdEf
=> ABCDEF
```

Source:
```
upper_format() {
        printf %s\\n "$*" | tr '[[:lower:]]' '[[:upper:]]'
}
```

### lower_format: convert text from any uppercase letters to lowercase letters

Example:
```
lower_format AbCdEf
=> abcdef
```

Source:
```
lower_format() {
        printf %s\\n "$*" | tr '[[:upper:]]' '[[:lower:]]'
}
```

### chain_format: convert a string from any characters to solely alphanumeric and single internal dash characters

Example:
```
chain_format "**Foo** **Goo** **Hoo**"
=> Foo-Goo-Hoo
```

Source:
```
chain_format() {
        printf %s\\n "$*" | sed 's/[^[:alnum:]]\{1,\}/-/g; s/-\{2,\}/-/g; s/^-\{1,\}//; s/-\{1,\}$//;'
}
```

### snake_format: convert a string from any characters to solely alphanumeric and single internal underscore characters

Example:
```
snake_format "**Foo** **Goo** **Hoo**"
=> Foo_Goo_Hoo
```

Source:
```
snake_format() {
        printf %s\\n "$*" | sed 's/[^[:alnum:]]\{1,\}/_/g; s/_\{2,\}/_/g; s/^_\{1,\}//; s/_\{1,\}$//;'
}
```

### space_format: convert a string from any characters to solely alphanumeric and single internal space characters

Example:
```
space_format "**Foo** **Goo** **Hoo**"
=> Foo Goo Hoo
```

Source:
```
space_format() {
        printf %s\\n "$*" | sed 's/[^[:alnum:]]\{1,\}/ /g; s/ \{2,\}/ /g; s/^ \{1,\}//; s/ \{1,\}$//;'
}
```

## Array helpers

### array_i: get the array item at index `i`

Example:
```
array_i
=> TODO
```

Source:
```
array_i() {
        [ $# == 3 ] && awk -F "$2" "{print \$$3}" <<< "$1" || awk "{print \$$2}" <<< "$1"
}
```

### array_n: get the array number of fields a.k.a. length a.k.a. size

Example:
```
array_n
=> TODO
```

Source:
```
array_n() {
        [ $# == 2 ] && awk -F "$2" "{print NF}" <<< "$1" || awk "{print NF}" <<< "$1"
}
```

## Assert helpers

### assert_test: assert a test utility command succeeds

Example:
```
assert_test -x program.sh
=> success i.e. no output

assert_test -x notes.txt
STDERR=> assert_test -x notes.txt  (because failure prints diagnostic info)
```

Source:
```
assert_test() {
        test "$1" "$2" || err assert_test "$@"
}
```

### assert_empty: assert an item is empty

Example:
```
assert_empty ""
=> success i.e. no output

assert_empty foo
STDERR=> assert_empty foo (because failure prints diagnostic info)
```

Source:
```
assert_empty() {
        [ -z "$1" ] || err assert_empty "$@"
}
```

### assert_equal: assert an item is equal to another item

Example:
```
assert_equal foo foo
=> success i.e. no output

assert_equal foo bar
STDERR=> assert_equal foo bar (because failure prints diagnostic info)
```

Source:
```
assert_equal() {
        [ "$1" = "$2" ] || err assert_equal "$@"
}
```

### assert_match: assert a regular expression matches an item

Example:
```
assert_match o foo
=> success i.e. no output

assert_match x foo
STDERR=> assert_match x foo
```

Source:
```
assert_match() {
        [[ "$2" =~ $1 ]] || err assert_match "$@"
}
```

## Make temp helpers

### mktemp_dir: make a temporary directory path

Example:
```
mktemp_dir
=> /var/folders/4f7b65122b0fb65b0fdad568a65dc97d
```

Source:
```
mktemp_dir() {
        x=$(mktemp -d -t "${1:-$(zid)}") ; trap '{ rm -rf "$x"; }' EXIT ; out "$x"
}
```

### mktemp_file: make a temporary file path

Example:
```
mktemp_file
=> /var/folders/4f7b65122b0fb65b0fdad568a65dc97d/1d9aafac5373be95d8b4c2dece0b1197
```

Source:
```
mktemp_file() {
        x=$(mktemp -t "${1:-$(zid)}") ; trap '{ rm -f "$x"; }' EXIT ; out "$x"
}
```

## Media helpers

### file_media_type: get a file's media type a.k.a. mime type such as "text/plain"

Example:
```
file_media_type notes.txt
=> text/plain
```

Source:
```
file_media_type() {
        file --brief --mime "$1"
}
```

### file_media_type_supertype: get a file's media type type a.k.a. mime type such as "text"

Example:
```
file_media_type_supertype notes.txt
=> text
```

Source:
```
file_media_type_supertype() {
        file --brief --mime "$1" | sed 's#/.*##'
}
```

### file_media_type_subtype: get a file's media type subtype a.k.a. mime type such as "plain"

Example:
```
file_media_type_subtype notes.txt
=> plain
```

Source:
```
file_media_type_subtype() {
        file --brief --mime "$1" | sed 's#^[^/]*/##; s#;.*##'
}
```

## Content helpers

### file_ends_with_newline: file ends with newline?

Example:
```
file_ends_with_newline notes.txt
=> true
```

Source:
```
file_ends_with_newline() {
        test $(tail -c1 "$1" | wc -l) -gt 0
}
```