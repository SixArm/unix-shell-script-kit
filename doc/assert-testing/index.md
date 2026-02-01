# Assert testing

Assert testing uses these shell functions to compare actual results to expected results.

## Assert testing

### assert_test

Assert a test utility command succeeds.

Syntax:

```sh
assert_test <condition>
=> success or error
```

Example:

```sh
assert_test -x program.sh
=> success i.e. no output

assert_test -x notes.txt
STDERR=> assert_test -x notes.txt
```

### assert_empty

Assert a value is empty.

Syntax:

```sh
assert_empty <value>
=> success or error
```

Example:

```sh
assert_empty ""
=> success i.e. no output

assert_empty foo
STDERR=> assert_empty foo
```

### assert_not_empty

Assert a value is not empty.

Syntax:

```sh
assert_not_empty <value>
=> success or error
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
assert_int_eq <int> <int>
=> success or error
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
assert_int_ne_ <int> <int>
=> success or error
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
assert_int_ge <int> <int>
=> success or error
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
assert_int_gt <int> <int>
=> success or error
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
assert_int_le <int> <int>
=> success or error
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
assert_int_lt <int> <int>
=> success or error
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
assert_str_eq <string> <string>
=> success or error
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
assert_str_ne <string> <string>
=> success or error
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
assert_str_ge <string> <string>
=> success or error
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
assert_str_gt <string> <string>
=> success or error
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
assert_str_le <string> <string>
=> success or error
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
assert_str_lt <string> <string>
=> success or error
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
assert_str_starts_with <string> <substring>
=> success or error
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
assert_str_ends_with <string> <substring>
=> success or error
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
assert_eval_int_eq_x <eval_expression> <integer>
=> success or error
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
assert_eval_str_eq_x <eval_expression> <string>
=> success or error
```

Example:

```sh
assert_eval_str_eq_x 'echo "foo"' foo
=> success i.e. no output

assert_eval_str_eq_x 'echo "foo"' bar
STDERR=> assert_eval_str_eq_x echo "foo" bar
```
