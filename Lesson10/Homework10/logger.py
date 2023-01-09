from datetime import datetime as dt

def log_command(update, result):
    time = dt.now().strftime('%d %B %Y %H:%M')
    with open('log.csv', 'a') as logfile:
        logfile.write(f'{time}, {update.effective_user.first_name}, {update.effective_user.id}, {update.message.text} = {result}\n')