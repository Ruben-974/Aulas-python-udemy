from main import LogPrintMixin, LogFileMixin

lf = LogFileMixin()
lf.log_error('qualquer coisa')
lf.log_success('Que legal')

lp = LogPrintMixin()
lp.log_error('qualquer coisa')
lp.log_success('Que legal')
