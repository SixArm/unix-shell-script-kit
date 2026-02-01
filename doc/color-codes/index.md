## Color helpers

### ANSI escape color codes

Use these directly. Do not use "tput".

Example:

```sh
printf "%sblack\n" $COLOR_BLACK
printf "%sred\n" $COLOR_RED
printf "%sgreen\n" $COLOR_GREEN
printf "%syellow\n" $COLOR_YELLOW
printf "%sblue\n" $COLOR_BLUE
printf "%smagenta\n" $COLOR_MAGENTA
printf "%scyan\n" $COLOR_CYAN
printf "%swhite\n" $COLOR_WHITE
```

For the widest support, use the basic set of 8 colors below,
and respect the user preferences by using the color() function.

Many terminals also support "bright" or "bold" colors;
these colors have their own set of codes, similar to the
basic colors yet with an additional ;1 in their codes.
We do not recommend using these colors in your shell scripts,
because so many users prefer to set their own terminal colors.

### Reset all color information

```sh
COLOR_RESET
```

Basic foreground colors

- `COLOR_BLACK`
- `COLOR_RED`
- `COLOR_GREEN`
- `COLOR_YELLOW`
- `COLOR_BLUE`
- `COLOR_MAGENTA`
- `COLOR_CYAN`
- `COLOR_WHITE`

### Basic background colors

- `COLOR_BG_BLACK`
- `COLOR_BG_RED`
- `COLOR_BG_GREEN`
- `COLOR_BG_YELLOW`
- `COLOR_BG_BLUE`
- `COLOR_BG_MAGENTA`
- `COLOR_BG_CYAN`
- `COLOR_BG_WHITE`

### Set output color and error color

Set our preferred color code for output message and error message.

These variables are used by the out() function and err() function below.

If you wish to set these in your terminal, and your terminal supports
dollar strings with \E meaning escape, then you can use the following:

```sh
export STDOUT_COLOR_START=$'\E[34m'
export STDOUT_COLOR_STOP=$'\E[0m'
export STDERR_COLOR_START=$'\E[31m'
export STDERR_COLOR_STOP=$'\E[0m'
```
