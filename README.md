# Unix shell script kit

Unix shell script kit is a collection of utility functions and constants.

The kit works with POSIX shells, including bash, zsh, dash, ksh, sh, etc.

All suggestions are welcome and appreciated.

[View the source code file with all documentation comments](https://raw.githubusercontent.com/SixArm/unix-shell-script-kit/main/unix-shell-script-kit)

Documentation:

- [Functions](https://github.com/SixArm/unix-shell-script-kit/tree/main/doc/functions/)
- [Color codes](https://github.com/SixArm/unix-shell-script-kit/tree/main/doc/color-codes/)
- [Log level codes](https://github.com/SixArm/unix-shell-script-kit/tree/main/doc/log-level-codes/)
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

- color -&gt; true or false
- out &lt;message&gt; -&gt; message
- err &lt;message&gt; -&gt; message
- die &lt;code&gt; &lt;message&gt;
- big &lt;message&gt;
- zid -&gt; &lt;32-bit secure random lowercase hex identifier&gt;
- ask -&gt; &lt;prompt&gt;
- utf8 -&gt; true or false
- print_success &lt;message&gt;
- print_warning &lt;message&gt;
- print_failure &lt;message&gt;
- now -&gt; &lt;datetime as our preferred ISO format&gt;
- now_date -&gt; &lt;date as our preferred ISO format&gt;
- sec -&gt; &lt;current time as posix sections&gt;
- age &lt;epoch&gt; -&gt; &lt;difference in seconds between epoch and now&gt;
- age_lt &lt;epoch&gt; &lt;seconds&gt; -&gt; true or false
- age_gt &lt;epoch&gt; &lt;seconds&gt; -&gt; true or false
- leap_year &lt;year&gt; -&gt; true or false
- datetime_mday_max &lt;datetime | yyyy-mm\*&gt; -&gt; true or false
- datetime_format_for_at_command &lt;datetime&gt; -&gt; &lt;yyyymmdddhhmm.ss&gt;
- datetime_format_for_pmset_command &lt;datetime&gt; -&gt; &lt;mm/dd/yy hh:mm:ss&gt;
- datetime_add &lt;datetime&gt; &lt;years&gt; &lt;months&gt; &lt;days&gt; &lt;hours&gt; &lt;minutes&gt; &lt;seconds&gt; -&gt; &lt;datetime&gt;
- directory_exists &lt;directory_path&gt; -&gt; true or false
- directory_exists_or_err &lt;directory_path&gt; -&gt; true or err
- directory_exists_or_die &lt;directory_path&gt; -&gt; true or die
- file_exists &lt;file_path&gt; -&gt; true or false
- file_exists_or_err &lt;file_path&gt; -&gt; true or err
- file_exists_or_die &lt;file_path&gt; -&gt; true or die
- symlink_exists &lt;symlink_path&gt; -&gt; true or false
- symlink_exists_or_err &lt;symlink_path&gt; -&gt; true or err
- symlink_exists_or_die &lt;symlink_path&gt; -&gt; true or die
- command_exists &lt;command_name&gt; -&gt; true or false
- command_exists_or_err &lt;command_name&gt; -&gt; true or err
- command_exists_or_die &lt;command_name&gt; -&gt; true or die
- command_version_exists &lt;command_name&gt; &lt;version_actual&gt; &lt;version_minimum&gt; -&gt; true or false
- command_version_exists_or_err &lt;command_name&gt; &lt;version_actual&gt; &lt;version_minimum&gt; -&gt; true or err
- command_version_exists_or_die &lt;command_name&gt; &lt;version_actual&gt; &lt;version_minimum&gt; -&gt; true or die
- var_exists &lt;var_name&gt; -&gt; true or false
- var_exists_or_err &lt;var_name&gt; -&gt; true or err
- var_exists_or_die &lt;var_name&gt; -&gt; true or die
- version &lt;version_actual&gt; &lt;version_minimum&gt; -&gt; true or false
- version_or_err &lt;version_actual&gt; &lt;version_minimum&gt; -&gt; true or err
- version_or_die &lt;version_actual&gt; &lt;version_minimum&gt; -&gt; true or die
- int &lt;number_string&gt; -&gt; integer
- sum &lt;number&gt; ... -&gt; sum of numbers
- cmp_alnums &lt;alnum_string&gt; &lt;alnum_string&gt; -&gt; 0 or -1 or 1
- cmp_digits &lt;digits_string&gt; &lt;digits_string&gt; -&gt; 0 or -1 or 1
- dot_all &lt;directory_path&gt; -&gt; source all executable files
- run_all &lt;directory_path&gt; -&gt; run all executable files
- sh_all &lt;directory_path&gt; -&gt; shell all executable files
- rm_all &lt;directory_path&gt; -&gt; remove all files
- trim &lt;string&gt; -&gt; string without leading/trailing spaces
- slug &lt;string&gt; -&gt; string with solely lowercase and single internal dash characters
- slugs &lt;string&gt; -&gt; string with solely lowercase and single internal dash characters and slash characters
- upper_case &lt;string&gt; -&gt; string with uppercase not lowercase
- lower_case &lt;string&gt; -&gt; string with lowercase nor uppercase
- kebab_case &lt;string&gt; -&gt; string with solely alphanumeric and single internal dash characters
- snake_case &lt;string&gt; -&gt; string with solely alphanumeric and single internal underscore characters
- space_case &lt;string&gt; -&gt; string with solely solely alphanumeric and single internal space characters
- touch_case &lt;string&gt; -&gt; string with solely a command "touch -t" timestamp format
- select_character_class &lt;string&gt; &lt;class&gt; [offset [length]] -&gt; selected characters
- reject_character_class &lt;string&gt; &lt;class&gt; [offset [length]] -&gt; rejected characters
- random_char [characters [length]] -&gt; random characters
- random_char_alnum [length] -&gt; random characters in class [:alnum:]
- random_char_alpha [length] -&gt; random characters in class [:alpha:]
- random_char_blank [length] -&gt; random characters in class [:blank:]
- random_char_cntrl [length] -&gt; random characters in class [:cntrl:]
- random_char_digit [length] -&gt; random characters in class [:digit:]
- random_char_graph [length] -&gt; random characters in class [:graph:]
- random_char_lower [length] -&gt; random characters in class [:lower:]
- random_char_lower_digit [length] -&gt; random characters in classes [:lower:][:digit]
- random_char_upper [length] -&gt; random characters in class [:upper:]
- random_char_upper_digit [length] -&gt; random characters in classes [:upper:][:digit]
- random_char_space [length] -&gt; random characters in class [:space:]
- random_char_xdigit [length] -&gt; random characters in class [:xdigit:]
- array_n &lt;array&gt; -&gt; number of fields
- array_i &lt;array&gt; &lt;index&gt; -&gt; array element at index
- array_first &lt;array&gt; -&gt; array first element
- array_last &lt;array&gt; -&gt; array last element
- array_car &lt;array&gt; -&gt; array car element
- array_cdr &lt;array&gt; -&gt; array cdr elements
- mktemp_directory -&gt; temporary directory path
- mktemp_file -&gt; temporary file path
- file_media_type &lt;file_path&gt; -&gt; media type
- file_media_type_supertype &lt;file_path&gt; -&gt; media type supertype
- file_media_type_subtype &lt;file_path&gt; -&gt; media type subtype
- font_name_exists &lt;font_name&gt; -&gt; true or false
- font_name_exists_or_die &lt;font_name&gt; -&gt; true or die
- file_ends_with_newline &lt;file_path&gt; -&gt; true or false
- user_dir &lt;directory_locator&gt; -&gt; directory path

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

Log level codes:

- LOG_EMERG=0
- LOG_ALERT=1
- LOG_CRIT=2
- LOG_ERR=3
- LOG_WARN=4
- LOG_NOTICE=5
- LOG_INFO=6
- LOG_DEBUG=7
- LOG_TRACE=8

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
- Version: 13.2.1
- Created: 2017-08-22T00:00:00Z
- Updated: 2026-03-29T22:23:51Z
- Website: https://github.com/sixarm/unix-shell-script-kit
- License: GPL-2.0 or GPL-3.0 or contact us for more
- Contact: Joel Parker Henderson (joel@sixarm.com)
