from datetime import datetime;

now = datetime.now()

def horaDeTrabajar():
    if(int(now.hour) <=7):
        print('Hora de descansar')
    else:
        print('Hora de trabajar')
