# Date Deux
This is basically the Python date module supplanted with some useful functions. This is a superclass so it supports everything the date module does.
It overlaps *some* functions of the calendar module but in general this was designed like a date+ module.

Works well on py2 and py3

## Basic Usage

```
>>> from datedeux import DateDeux
>>> x = DateDeux.today()
>>> x
DateDeux(2017, 6, 28)
```

### ... start of month
```
>>> x.monthstart()
DateDeux(2017, 6, 1)
```

### ... end of month
```
>>> x.monthend()
DateDeux(2017, 6, 30)
```

### Arithmetic operations

```
>>> x + 45
DateDeux(2017, 8, 12)
>>> x + 45 + 23
DateDeux(2017, 9, 4)
>>> x - 30
DateDeux(2017, 5, 29)
```

### ... readable day of week


```
>>> x.dayname()
'Wednesday'
>>> x.dayname_short()
'Wed'
```

### ... readable month name

```
>>> x.monthname()
'June'
>>> x.monthname_short()
'Jun'
>>> 
```

### Format date to make it readable

```
>>> x.dateformat('dd-mmm-yyyy')
'29-Jun-2017'
>>> x.dateformat('dd-mmm-yy')
'29-Jun-17'
>>> x.dateformat('mm/dd/yy')
'06/29/17'
```


### Make a calendar

```
>>> [(z.dateformat('dd-mmm-yyyy'), z.dayname_short()) for z in x.monthcalendar()]
>>> pprint([(z.dateformat('dd-mmm-yyyy'), z.dayname_short()) for z in x.monthcalendar()])
[('01-Jun-2017', 'Thu'),
 ('02-Jun-2017', 'Fri'),
 ('03-Jun-2017', 'Sat'),
 ('04-Jun-2017', 'Sun'),
 ('05-Jun-2017', 'Mon'),
 ('06-Jun-2017', 'Tue'),
 ('07-Jun-2017', 'Wed'),
 ('08-Jun-2017', 'Thu'),
 ('09-Jun-2017', 'Fri'),
 ('10-Jun-2017', 'Sat'),
 ('11-Jun-2017', 'Sun'),
 ('12-Jun-2017', 'Mon'),
 ('13-Jun-2017', 'Tue'),
 ('14-Jun-2017', 'Wed'),
 ('15-Jun-2017', 'Thu'),
 ('16-Jun-2017', 'Fri'),
 ('17-Jun-2017', 'Sat'),
 ('18-Jun-2017', 'Sun'),
 ('19-Jun-2017', 'Mon'),
 ('20-Jun-2017', 'Tue'),

>>> [(z.dateformat('dd-mmm-yyyy'), z.dayname_short()) for z in x.yearcalendar()]
>>> pprint([(z.dateformat('dd-mmm-yyyy'), z.dayname_short()) for z in x.yearcalendar()])
[('01-Jan-2017', 'Sun'),
 ('02-Jan-2017', 'Mon'),
 ('03-Jan-2017', 'Tue'),
 ('04-Jan-2017', 'Wed'),
 ('05-Jan-2017', 'Thu'),
 ('06-Jan-2017', 'Fri'),
 ('07-Jan-2017', 'Sat'),
 ('08-Jan-2017', 'Sun'),
 ('09-Jan-2017', 'Mon'),
 ('10-Jan-2017', 'Tue'),
 ('11-Jan-2017', 'Wed'),
 ('12-Jan-2017', 'Thu'),
 ('13-Jan-2017', 'Fri'),
```


### Get a Python date back out

```
>>> x
DateDeux(2017, 6, 28)
>>> x.pydate()
datetime.date(2017, 6, 28)
```

### License
[BSD License](https://opensource.org/licenses/BSD-3-Clause) 