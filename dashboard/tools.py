from datetime import datetime
from django.utils.dateparse import parse_date

def checkDate(dateData):
    try:
        clean_date = datetime.strptime(dateData, '%Y-%m-%d')
        return clean_date
    except ValueError:
        return False
    
def checkYearMonth(date_str):
    try:
        clean_date = datetime.strptime(date_str, '%Y-%m')
        return(2,clean_date)
    except ValueError:
        try:
            clean_date = datetime.strptime(date_str, '%Y')
            return(1,clean_date)
        except ValueError:
            return False
