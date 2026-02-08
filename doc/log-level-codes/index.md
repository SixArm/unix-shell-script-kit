# Log level codes

These log level codes align with syslog priority levels and C include file. For
more about how to use these here, see the function `log`.

We define one extra log level, which is LOG_TRACE=8, because so many
tools have trace capabilties and it's pragmatic for writing scripts.

- LOG_EMERG=0 (Emergency: System is unusable)
- LOG_ALERT=1 (Alert: Action must be taken immediately)
- LOG_CRIT=2 (Critical conditions)
- LOG_ERR=3 (Error conditions)
- LOG_WARN=4 (Warning conditions)
- LOG_NOTICE=5 (Notice: normal but significant conditions)
- LOG_INFO=6 (Informational)
- LOG_DEBUG=7 (Debug-level messages)
- LOG_TRACE=8 (Trace-level messages)

There is a log function for all log levels:

- log <log level> <message> -> <datestamp> <unique random id> <hostname> <process id> <log level> <message>

There are also log functions with convenient log level names:

- log_emerg <message> -> log $LOG_EMERG <message>
- log_alert <message> -> log $LOG_ALERT <message>
- log_crit <message> -> log $LOG_CRIT <message>
- log_err <message> -> log $LOG_ERR <message>
- log_warn <message> -> log $LOG_WARN <message>
- log_notice <message> -> log $LOG_NOTICE <message>
- log_info <message> -> log $LOG_INFO <message>
- log_debug <message> -> log $LOG_DEBUG <message>
- log_trace <message> -> log $LOG_TRACE <message>
