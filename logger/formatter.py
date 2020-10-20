import logging


class LogFormatter(logging.Formatter):
    def formatMessage(self, record):
        if not record.__dict__.get('unique_id'):
            record.unique_id = '-'
        return super(LogFormatter, self).formatMessage(record)
