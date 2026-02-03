# Unix shell script kit

Unix shell script kit is a collection of utility functions and constants.

The kit works with POSIX shells, including bash, zsh, dash, ksh, sh, etc.

All suggestions are welcome and appreciated.

[View the source code file with all documentation comments](https://raw.githubusercontent.com/SixArm/unix-shell-script-kit/main/unix-shell-script-kit)

Documentation:

- [Functions](https://github.com/SixArm/unix-shell-script-kit/tree/main/doc/functions/)
- [Color codes](https://github.com/SixArm/unix-shell-script-kit/tree/main/doc/color-codes/)
- [Exit codes](https://github.com/SixArm/unix-shell-script-kit/tree/main/doc/exit-codes/)
- [Assert testing](https://github.com/SixArm/unix-shell-script-kit/tree/main/doc/assert-testing/)

## Download

Download the kit as one file that has everything:

```sh
curl -O "https://raw.githubusercontent.com/SixArm/unix-shell-script-kit/main/unix-shell-script-kit"
```

## Source

To use the kit in your own script, you source the kit like this:

```sh
. /your/path/here/unix-shell-script-kit
```

To use the kit in your own script in the same directory, you source the kit like this:

```sh
. "$(dirname "$(readlink -f "$0")")/unix-shell-script-kit"
```

## AI

This work is 100% by humans. If you want to use this kit with your AI, then you can download AI-friendly files.

- If your AI is small, then download [llms-small.txt](https://raw.githubusercontent.com/SixArm/unix-shell-script-kit/main/llms-small.txt)

- If your AI is large, then download [llms-large.txt](https://raw.githubusercontent.com/SixArm/unix-shell-script-kit/main/llms-large.txt)

## Overview

Overview of the functions, color codes, exit codes, and assert testing. For more information please see the [source](https://raw.githubusercontent.com/SixArm/unix-shell-script-kit/main/unix-shell-script-kit)

Functions:

- color -> true or false
- out <message> -> message
- err <message> -> message
- die <code> <message>
- big <message>
- zid -> <32-bit secure random lowercase hex identifier>
- ask -> <prompt>
- utf8 -> true or false
- print_success <message>
- print_warning <message>
- print_failure <message>
- now -> <datetime as our preferred ISO format>
- now_date -> <date as our preferred ISO format>
- sec -> <current time as posix sections>
- age <epoch> -> <difference in seconds between epoch and now>
- age_lt <epoch> <seconds> -> true or false
- age_gt <epoch> <seconds> -> true or false
- leap_year <year> -> true or false
- datetime_mday_max <datetime | yyyy-mm\*> -> true or false
- datetime_format_for_at_command <datetime> -> <yyyymmdddhhmm.ss>
- datetime_format_for_pmset_command <datetime> -> <mm/dd/yy hh:mm:ss>
- datetime_add <datetime> <years> <months> <days> <hours> <minutes> <seconds> -> <datetime>
- directory_exists <directory_path> -> true or false
- directory_exists_or_die <directory_path> -> true or die
- file_exists <file_path> -> true or false
- file_exists_or_die <file_path> -> true or die
- symlink_exists <symlink_path> -> true or false
- symlink_exists_or_die <symlink_path> -> true or die
- command_exists <command_name> -> true or false
- command_exists_or_die <command_name> -> true or die
- command_version_exists <command_name> <version_actual> <version_minimum> -> true or false
- command_version_exists_or_die <command_name> <version_actual> <version_minimum> -> true or die
- var_exists <var_name> -> true or false
- var_exists_or_die <var_name> -> true or die
- version <version_actual> <version_minimum> -> true or false
- version_or_die <version_actual> <version_minimum> -> true or die
- int <number_string> -> integer
- sum <number> ... -> sum of numbers
- cmp_alnums <alnum_string> <alnum_string> -> 0 or -1 or 1
- cmp_digits <digits_string> <digits_string> -> 0 or -1 or 1
- dot_all <directory_path> -> source all executable files
- run_all <directory_path> -> run all executable files
- sh_all <directory_path> -> shell all executable files
- rm_all <directory_path> -> remove all files
- trim <string> -> string without leading/trailing spaces
- slug <string> -> string with solely lowercase and single internal dash characters
- slugs <string> -> string with solely lowercase and single internal dash characters and slash characters
- upper_case <string> -> string with uppercase not lowercase
- lower_case <string> -> string with lowercase nor uppercase
- kebab_case <string> -> string with solely alphanumeric and single internal dash characters
- snake_case <string> -> string with solely alphanumeric and single internal underscore characters
- space_case <string> -> string with solely solely alphanumeric and single internal space characters
- touch_case <string> -> string with solely a command "touch -t" timestamp format
- select_character_class <string> <class> [offset [length]] -> selected characters
- reject_character_class <string> <class> [offset [length]] -> rejected characters
- random_char [characters [length]] -> random characters
- random_char_alnum [length] -> random characters in class [:alnum:]
- random_char_alpha [length] -> random characters in class [:alpha:]
- random_char_blank [length] -> random characters in class [:blank:]
- random_char_cntrl [length] -> random characters in class [:cntrl:]
- random_char_digit [length] -> random characters in class [:digit:]
- random_char_graph [length] -> random characters in class [:graph:]
- random_char_lower [length] -> random characters in class [:lower:]
- random_char_lower_digit [length] -> random characters in classes [:lower:][:digit]
- random_char_upper [length] -> random characters in class [:upper:]
- random_char_upper_digit [length] -> random characters in classes [:upper:][:digit]
- random_char_space [length] -> random characters in class [:space:]
- random_char_xdigit [length] -> random characters in class [:xdigit:]
- array_n <array> -> number of fields
- array_i <array> <index> -> array element at index
- array_first <array> -> array first element
- array_last <array> -> array last element
- array_car <array> -> array car element
- array_cdr <array> -> array cdr elements
- mktemp_dir -> temporary directory path
- mktemp_file -> temporary file path
- file_media_type <file_path> -> media type
- file_media_type_supertype <file_path> -> media type supertype
- file_media_type_subtype <file_path> -> media type subtype
- font_name_exists <font_name> -> true or false
- font_name_exists_or_die <font_name> -> true or die
- file_ends_with_newline <file_path> -> true or false
- user_dir <directory_locator> -> directory path

Color codes:

- COLOR_RESET
- COLOR_BLACK
- COLOR_RED
- COLOR_GREEN
- COLOR_YELLOW
- COLOR_BLUE
- COLOR_MAGENTA
- COLOR_CYAN
- COLOR_WHITE
- COLOR_BG_BLACK
- COLOR_BG_RED
- COLOR_BG_GREEN
- COLOR_BG_YELLOW
- COLOR_BG_BLUE
- COLOR_BG_MAGENTA
- COLOR_BG_CYAN
- COLOR_BG_WHITE

Exit codes:

- EXIT_SUCCESS=0
- EXIT_FAILURE=1
- EXIT_USAGE=2
- EXIT_DATAERR=65
- EXIT_NOINPUT=66
- EXIT_NOUSER=67
- EXIT_NOHOST=68
- EXIT_UNAVAILABLE=69
- EXIT_SOFTWARE=70
- EXIT_OSERR=71
- EXIT_OSFILE=72
- EXIT_CANTCREATE=73
- EXIT_IOERR=74
- EXIT_TEMPFAIL=75
- EXIT_PROTOCOL=76
- EXIT_NOPERM=77
- EXIT_CANTCREATE=73
- EXIT_CONFIG=78
- EXIT_QUIT=80
- EXIT_KYC=81
- EXIT_UPDATE=89
- EXIT_CONFLICT=90
- EXIT_UNLAWFUL=91
- EXIT_PAYMENT_ISSUE=92
- EXIT_QUOTA_ISSUE=93
- EXIT_BUSY=100
- EXIT_TIMEOUT=101
- EXIT_LOCKOUT=102
- EXIT_LOOP=103
- EXIT_MOVED_PERMANENTLY=110
- EXIT_MOVED_TEMPORARILY=111
- EXIT_GONE=112
- EXIT_FUTURE=119
- EXIT_GIT_BISECT_SKIP=125
- EXIT_COMMAND_FOUND_BUT_NOT_EXECUTABLE=126
- EXIT_COMMAND_NOT_FOUND=127
- EXIT_CODE_INVALID=128
- EXIT_CODE_OUT_OF_RANGE=255

Assert testing:

- assert_test <condition>
- assert_empty <value>
- assert_not_empty <value>
- assert_int_eq <int> <int>
- assert_int_ne <int> <int>
- assert_int_ge <int> <int>
- assert_int_gt <int> <int>
- assert_int_le <int> <int>
- assert_int_lt <int> <int>
- assert_str_eq <string> <string>
- assert_str_ne <string> <string>
- assert_str_ge <string> <string>
- assert_str_gt <string> <string>
- assert_str_le <string> <string>
- assert_str_lt <string> <string>
- assert_str_starts_with <string> <substring>
- assert_str_ends_with <string> <substring>
- assert_eval_int_eq_x <eval_expression> <integer>
- assert_eval_str_eq_x <eval_expression> <string>

## Tracking

- Package: unix-shell-script-kit
- Version: 13.0.1
- Created: 2017-08-22T00:00:00Z
- Updated: 2026-02-03T22:43:34Z
- Website: https://github.com/sixarm/unix-shell-script-kit
- License: GPL-2.0 or GPL-3.0 or contact us for more
- Contact: Joel Parker Henderson (joel@sixarm.com)
