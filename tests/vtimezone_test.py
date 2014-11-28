from datetime import datetime as datetime
import pytz
from khal.khalendar.event import create_timezone

berlin = pytz.timezone('Europe/Berlin')
bogota = pytz.timezone('America/Bogota')

atime = datetime(2014, 10, 28, 10, 10)
btime = datetime(2016, 10, 28, 10, 10)


def test_berlin():
    vberlin = [b'BEGIN:VTIMEZONE',
               b'TZID:Europe/Berlin',
               b'BEGIN:STANDARD',
               b'DTSTART;VALUE=DATE-TIME:20141026T020000',
               b'TZNAME:CET',
               b'TZOFFSETFROM:+0200',
               b'TZOFFSETTO:+0100',
               b'END:STANDARD',
               b'BEGIN:DAYLIGHT',
               b'DTSTART;VALUE=DATE-TIME:20150329T030000',
               b'TZNAME:CEST',
               b'TZOFFSETFROM:+0100',
               b'TZOFFSETTO:+0200',
               b'END:DAYLIGHT',
               b'END:VTIMEZONE',
               b'']

    assert create_timezone(berlin, atime, atime).to_ical().split(b'\r\n') == vberlin


def test_berlin_rdate():
    vberlin = [b'BEGIN:VTIMEZONE',
               b'TZID:Europe/Berlin',
               b'BEGIN:STANDARD',
               b'DTSTART;VALUE=DATE-TIME:20141026T020000',
               b'RDATE:20151025T020000,20161030T020000',
               b'TZNAME:CET',
               b'TZOFFSETFROM:+0200',
               b'TZOFFSETTO:+0100',
               b'END:STANDARD',
               b'BEGIN:DAYLIGHT',
               b'DTSTART;VALUE=DATE-TIME:20150329T030000',
               b'RDATE:20160327T030000',
               b'TZNAME:CEST',
               b'TZOFFSETFROM:+0100',
               b'TZOFFSETTO:+0200',
               b'END:DAYLIGHT',
               b'END:VTIMEZONE',
               b'']

    assert create_timezone(berlin, atime, btime).to_ical().split(b'\r\n') == vberlin


def test_bogota():
    vbogota = [b'BEGIN:VTIMEZONE',
               b'TZID:America/Bogota',
               b'BEGIN:STANDARD',
               b'DTSTART;VALUE=DATE-TIME:19930403T230000',
               b'TZNAME:COT',
               b'TZOFFSETFROM:-0400',
               b'TZOFFSETTO:-0500',
               b'END:STANDARD',
               b'END:VTIMEZONE',
               b'']
    assert create_timezone(bogota, atime, atime).to_ical().split(b'\r\n') == vbogota
