# Exit codes

Our POSIX shell programs call "exit" with an exit code value.

Conventions:

* 0 = success, and non-zero indicates any other issue.

* 1 = failure

* 2 = failure due to a usage problem

* 3-63 are for a program-specific exit codes.

* 64-78 are based on BSD sysexits <https://man.openbsd.org/sysexits.3>

* 80-119 are SixArm conventions that we find useful in many programs.

Many shells use exit codes 126-128 to signal specific error status:

* 126 is for the shell and indicates command found but is not executable.

* 127 is for the shell and indicate command not found.

* 128 is for invalid argument to exit.

Many shells use exit codes above 128 in their $? representation of the
exit status to encode the signal number of a process being killed.

* 128+n means fatal error signal "n"

* Example: 130 means terminated by ctrl-c (because ctrl-c is signal 2)

* Example: 137 means terminated by kill -9 (because 128 + 9 = 137)

Finally, the highest exit code:

* 255 Exit status out of range (exit takes integer args 0-255)

Be aware that on some shells, ut of range exit values can result in unexpected
exit codes. An exit value greater than 255 returns an exit code modulo 256.

* Example: exit 257 becomes exit 1 (because 257 % 256 = 1)

* Caution: exit 256 becomes exit 0, which probably isn't what you want.

For some typical needs that we encounter, we can suggest these:

* Authentication issues: `exit $EXIT_NOUSER`

* Authorization issues: `exit $EXIT_NOPERM`

* A user chooses cancel: `exit $EXIT_QUIT`

The exit code list below is subject to change over time, as we learn more.


### Success

```sh
EXIT_SUCCESS=0
```

The program succeeded.

Exit 0 meaning success is a widespread convention as a catch-all code.


### Failure

```sh
EXIT_FAILURE=1
```

The program failed.

E.g. an error, an abort, found no results, lack of data, etc.

Exit 1 meaning failure is a widespread convention as a catch-all code.


### Usage

```sh
EXIT_USAGE=2
```

The program usage is incorrect, or malformed, or in conflict, etc.

E.g. wrong number of args, a bad flag, a syntax error in an option, etc.

Exit 2 meaning usage is a widespread convention as a catch-all CLI code.


### Data Err

```sh
EXIT_DATAERR=65
```

The input data was incorrect in some way.

This should only be used for user's data and not system files.


### No Input

```sh
EXIT_NOINPUT=66
```

An input file-- not a system file-- did not exist or was not readable.

This could include errors like "No message" to a mailer, if it cared about it.


### No User

```sh
EXIT_NOUSER=67
```

The user specified did not exist.

E.g. for email addresses, or remote logins, or authentication issues, etc.


### No Host

```sh
EXIT_NOHOST=68
```

The host specified did not exist.

E.g. for email addresses, or network requests, or web links, etc.



### Unavailable

```sh
EXIT_UNAVAILABLE=69
```

A service is unavailable.

E.g. a support program or file does not exist. This can also be a catchall
message when something does not work, but you do not know why.


### Software

```sh
EXIT_SOFTWARE=70
```

An internal software error has been detected.

This should be limited to non-operating system related errors as possible.


### OS Err

```sh
EXIT_OSERR=71
```

An operating system error has been detected.

E.g. errors such as "cannot fork", "cannot create pipe", or getuid returns a
user that does not exist in the passwd file, etc.


### OS File

An operating system file (e.g. /etc/passwd) does not exist, or cannot
be opened, or has some sort of error (e.g. syntax error).

```sh
EXIT_OSFILE=72
```

### Can't Create

```sh
EXIT_CANTCREATE=73
```

A user-specified output (e.g. a file) cannot be created.


### IO Err

An error occurred while doing I/O on some file, or stream, etc.

```sh
EXIT_IOERR=74
```

### Temp Fail

```sh
EXIT_TEMPFAIL=75
```

A temporary failure occurred; this is not a permanent error.

E.g. a mailer could not create a connection. The request can be retried later.


### Protocol

```sh
EXIT_PROTOCOL=76
```

The remote system returned something that was "not possible" during
a protocol exchange.


### No Perm

```sh
EXIT_NOPERM=77
```

You did not have sufficient permission to perform the operation.

This is not for file system problems, which use EXIT_NOINPUT or EXIT_CANTCREATE,
but for higher level permissions, authorizations, etc.


### Config

```sh
EXIT_CONFIG=78
```

Something was found in an unconfigured or misconfigured state.


## Exit codes 80-119

Exit codes 80-119 are for our own SixArm conventions.

We propose these are generally useful to many kinds of programs.

Caution: these exit codes and their values are work in progress,
draft only, as a request for comments, in version 11.x of this file.
These exit codes will be set in version 12.x when it's released.

* 80+ for user interation issues

* 90+ for access control issues

* 100+: process runtime issues

* 110+: expected ability issues


## Exit codes for 80+ for user interaction issues


### Quit

```sh
EXIT_QUIT=80
```

The user chose to quit, or cancel, or abort, or discontinue, etc.


### KYC (Know Your Customer)

```sh
EXIT_KYC=81
```

The program requires more user interaction, or user information, etc.

E.g. email validation, age verification, terms of service agreement, etc.


### Update

```sh
EXIT_UPDATE=89
```

The program or its dependencies need an update, or upgrade, etc.


## Exit codes 90+ for access control issues


### Conflict

```sh
EXIT_CONFLICT=90
```

An item has a conflict e.g. edit collision, or merge error, etc.

Akin to HTTP status code 409 Conflict.


### Unlawful

```sh
EXIT_UNLAWFUL=91
```

Something is prohibited due to law, or warrant, or court order, etc.

Akin to HTTP status code 451 Unavailable For Legal Reasons (RFC 7725).


### Payment Issue

```sh
EXIT_PAYMENT_ISSUE=92
```

Something needs a credit card, or invoice, or billing, etc.

Akin to a superset of HTTP status code 402 Payment Required.


### Quota Issue

```sh
EXIT_QUOTA_ISSUE=93
```

A quota is reached, such as exhausting a free trial, out of fuel, etc.

Akin to a superset of HTTP status code 429 Too Many Requests.


## Exit codes 100+ for process runtime issues


### Busy

```sh
EXIT_BUSY=100
```

A process is too busy, or overloaded, or throttled, or breakered, etc.

Akin to HTTP status code 503 Service Unavailable; always means overloaded.


### Timeout

```sh
EXIT_TIMEOUT=101
```

A process is too slow, or estimated to take too long, etc.

Akin to HTTP status code 408 Request Timeout.


### Lockout

```sh
EXIT_LOCKOUT=102
```

A process is intentionally blocked as a danger, hazard, risk, etc.

This is for lockout-tagout (LOTO) safety, or protecting users or data, etc.


### Loop

```sh
EXIT_LOOP=103
```

A process has detected an infinite loop, so is aborting.

Akin to HTTP status code 508 Loop Detected.


## Exit codes 110+ for expected ability issues


### Moved Permanently

```sh
EXIT_MOVED_PERMANENTLY=110
```

An expected ability has been moved permanently.

Akin to HTTP status code 301 Moved Permanently.


### Moved Temporarily

```sh
EXIT_MOVED_TEMPORARILY=111
```

An expected ability has been moved temporarily.

Akin to HTTP status code 302 Moved Temporarily.


### Gone

```sh
EXIT_GONE=112
```

An expected ability has been intentionally removed, or deleted, etc.

Akin to HTTP status code 410 Gone; the ability should be purged.


### Future

```sh
EXIT_FUTURE=119
```

An expected ability is coming in the future, but is not yet implemented.

Akin to HTTP status code 501 Not Implemented; implies future availability.


## Exit code 125 for git


### Git bisect skip

```sh
EXIT_GIT_BISECT_SKIP=125
```

Git bisect: The special exit code 125 should be used when the current source
code cannot be tested. If the script exits with this code, the current
revision will be skipped (see git bisect skip above).

Value 125 was chosen as the highest sensible value to use for this purpose,
because 126 and 127 are used by shells to signal specific error status.


## Exit codes 126-127 for shell conventions


### Command found but not executable

```sh
EXIT_COMMAND_FOUND_BUT_NOT_EXECUTABLE=126
```

A command is found but is not executable.


### Command not found

```sh
EXIT_COMMAND_NOT_FOUND=127
```

A command is not found.


### Exit code invalid

```sh
EXIT_CODE_INVALID=128
```

The exit code is invalid.

Compare EXIT_CODE_OUT_OF_RANGE=255


### Exit code out of range

```sh
EXIT_CODE_INVALID=128
```

The exit code is out of range i.e. not in 0-255.

Compare EXIT_CODE_INVALID=128
