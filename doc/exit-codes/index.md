# Exit codes

Our POSIX shell programs call "exit" with an exit code value.

Conventions:

- 0 = success, and non-zero indicates any other issue.

- 1 = failure

- 2 = failure due to a usage problem

- 3-63 are for a program-specific exit codes.

- 64-78 are based on BSD sysexits <https://man.openbsd.org/sysexits.3>

Conventions we propose for use worldwide:

- 80+ for user interation issues

- 90+ for access control issues

- 100+: process runtime issues

- 110+: expected ability issues

Many shells use exit codes 126-128 to signal specific error status:

- 126 is for the shell and indicates command found but is not executable.

- 127 is for the shell and indicate command not found.

- 128 is for invalid argument to exit.

Many shells use exit codes above 128 in their $? representation of the exit
status to encode the signal number of a process being killed.

- 128+n means fatal error signal "n"

- Example: 130 means terminated by ctrl-C (because ctrl-c is signal 2)

- Example: 137 means terminated by kill -9 (because 128 + 9 = 137)

Finally, the highest exit code:

- 255 Exit status out of range (exit takes integer args 0-255)

Be aware that on some shells, ut of range exit values can result in unexpected
exit codes. An exit value greater than 255 returns an exit code modulo 256.

- Example: exit 257 becomes exit 1 (because 257 % 256 = 1)

- Caution: exit 256 becomes exit 0, which probably isn't what you want.

For some typical needs that we encounter, we can suggest these:

- Authentication issues: exit $EXIT_NOUSER

- Authorization issues: exit $EXIT_NOPERM

- A user chooses cancel: exit $EXIT_QUIT

The exit code list below is subject to change over time, as we learn more.

### EXIT_SUCCESS=0 (Success)

The program succeeded.

E.g. everything worked as expected; any pipe processing will continue.

Exit 0 meaning success is a widespread convention as a catch-all code.

### EXIT_FAILURE=1 (Failure)

The program failed.

E.g. an error, an abort, found no results, lack of data, etc.

Exit 1 meaning failure is a widespread convention as a catch-all code.

### EXIT_USAGE=2 (Usage)

The program usage is incorrect, or malformed, or in conflict, etc.

E.g. wrong number of args, a bad flag, a syntax error in an option, etc.

Exit 2 meaning usage is a widespread convention as a catch-all CLI code.

### EXIT_DATAERR=65 (Data Error)

The input data was incorrect in some way.

This should only be used for user's data and not system files.

### EXIT_NOINPUT=66 (No Input)

An input file-- not a system file-- did not exist or was not readable.

This could include errors like "No message" to a mailer, if it cared about it.

### EXIT_NOUSER=67 (No User)

The user specified did not exist.

E.g. for email addresses, or remote logins, or authentication issues, etc.

### EXIT_NOHOST=68 (No Host)

The host specified did not exist.

E.g. for email addresses, or network requests, or webs links, etc.

### EXIT_UNAVAILABLE=69 (Unavailable)

A service is unavailable.

E.g. a support program or file does not exist. This can also be a catchall
message when something does not work, but you do not know why.

### EXIT_SOFTWARE=70 (Software)

An internal software error has been detected.

This should be limited to non-operating system related errors as possible.

### EXIT_OSERR=71 (Operating System Error)

An operating system error has been detected.

E.g. errors such as "cannot fork", "cannot create pipe", or getuid returns a
user that does not exist in the passwd file, etc.

### EXIT_OSFILE=72 (Operating System File)

An operating system file (e.g. /etc/passwd) does not exist, or cannot
be opened, or has some sort of error (e.g. syntax error).

### EXIT_CANTCREATE=73 (Can't Create)

A user-specified output (e.g. a file) cannot be created.

### EXIT_IOERR=74 (Input/Output Error)

An error occurred while doing input/output on some file, or stream, etc.

### EXIT_TEMPFAIL=75 (Temporary Failure)

A temporary failure occurred; this is not a permanent error.

E.g. a mailer could not create a connection. The request can be retried later.

### EXIT_PROTOCOL=76 (Protocol)

The remote system returned something that was "not possible" during
a protocol exchange.

### EXIT_NOPERM=77 (No Permission)

You did not have sufficient permission to perform the operation.

This is not for file system problems, which use EXIT_NOINPUT or
EXIT_CANTCREATE, but for higher level permissions, authorizations, etc.

### EXIT_CONFIG=78 (Config)

Something was found in an unconfigured or misconfigured state.

### EXIT_QUIT=80 (Quit)

The user chose to quit, or cancel, or abort, or discontinue, etc.

### EXIT_KYC=81 (Know Your Customer)

The program requires more user interaction, or user information, etc.

E.g. email validation, age verification, terms of service agreement, etc.

### EXIT_UPDATE=89 (Update)

The program or its dependencies need an update, or upgrade, etc.

### EXIT_CONFLICT=90 (Conflict)

An item has a conflict e.g. edit collision, or merge error, etc.

Akin to HTTP status code 409 Conflict.

### EXIT_UNLAWFUL=91 (Unlawful)

Something is prohibited due to law, or warrant, or court order, etc.

Akin to HTTP status code 451 Unavailable For Legal Reasons (RFC 7725).

### EXIT_PAYMENT_ISSUE=92 (Payment Issue)

Something needs a credit card, or invoice, or billing, etc.

Akin to a superset of HTTP status code 402 Payment Required.

### EXIT_QUOTA_ISSUE=93 (Quota Issue)

A quota is reached, such as exhausting a free trial, out of fuel, etc.

Akin to a superset of HTTP status code 429 Too Many Requests.

### EXIT_BUSY=100 (Busy)

A process is too busy, or overloaded, or throttled, or breakered, etc.

Akin to HTTP status code 503 Service Unavailable; always means overloaded.

### EXIT_TIMEOUT=101 (Timeout)

A process is too slow, or estimated to take too long, etc.

Akin to HTTP status code 408 Request Timeout.

### EXIT_LOCKOUT=102 (Lockout)

A process is intentionally blocked as a danger, hazard, risk, etc.

This is for lockout-tagout (LOTO) safety, or protecting users or data, etc.

### EXIT_LOOP=103 (Loop)

A process has detected an infinite loop, so is aborting.

Akin to HTTP status code 508 Loop Detected.

### EXIT_MOVED_PERMANENTLY=110 (Moved Permanently)

An expected ability has been moved permanently.

Akin to HTTP status code 301 Moved Permanently.

### EXIT_MOVED_TEMPORARILY=111 (Moved Temporarily)

An expected ability has been moved temporarily.

Akin to HTTP status code 302 Moved Temporarily.

### EXIT_GONE=112 (Gone)

An expected ability has been intentionally removed, or deleted, etc.

Akin to HTTP status code 410 Gone; the ability should be purged.

### EXIT_FUTURE=119 (Future)

An expected ability is not yet implemented, or work in progress, etc.

Akin to HTTP status code 501 Not Implemented; implies future availability.

### EXIT_GIT_BISECT_SKIP=125 (Git bisect skip)

The special exit code 125 should be used when the current source code cannot
be tested. If the script exits with this code, the current revision will be
skipped (see git bisect skip above).

Value 125 was chosen as the highest sensible value to use for this
purpose, because 126 and 127 are used by shells to signal specific errors.

### EXIT_COMMAND_FOUND_BUT_NOT_EXECUTABLE=126 (Command found but not executable)

A command is found but is not executable.

This is a shell convention.

### EXIT_COMMAND_NOT_FOUND=127 (Command not found)

A command is not found.

This is a shell convention.

### EXIT_CODE_INVALID=128 (Exit code invalid)

The exit code is invalid.

This is a shell convention.

Compare EXIT_CODE_OUT_OF_RANGE=255.

### EXIT_CODE_OUT_OF_RANGE=255 (Exit code out of range)

The exit code is out of range i.e. not in 0-255.

This is a shell convention.

Compare EXIT_CODE_INVALID=128
