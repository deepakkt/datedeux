# Date Deux
This is basically the Python date module supplanted with some useful functions. This is a superclass so it supports everything the date module does.
It overlaps *some* functions of the calendar module but in general this was designed like a date+ module.

Should work the same on py2 and py3

## Install

`pip install datedeux`

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

### ... start of year

```
>>> x.yearstart()
DateDeux(2017, 1, 1)
```


### ... end of year

```
>>> x.yearend()
DateDeux(2017, 12, 31)
```

### Arithmetic operations

```
>>> x + 45
DateDeux(2017, 8, 12)
>>> x + 45 + 23
DateDeux(2017, 9, 4)
>>> x - 30
DateDeux(2017, 5, 29)
>>> x = DateDeux.today()
>>> x
DateDeux(2017, 7, 15)
>>> y = x.monthend()
>>> y
DateDeux(2017, 7, 31)
>>> y - x
16
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

### Python date to DateDeux

```
>>> from datedeux import DateDeux
>>> from datetime import date
>>> DateDeux.frompydate(date(2017, 4, 1))
DateDeux(2017, 4, 1)
```

### ISO Date to DateDeux

```
>>> DateDeux.fromisodate('2017-04-01')
DateDeux(2017, 4, 1)
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

### Get an iterable value set out (year, month, day)

```
>>> tuple(x)
(2017, 7, 3)
>>> list(x)
[2017, 7, 3]
```

### Quick recipes
The idea behind this module was to make many date operations declarative building on the core module. 

#### Next month start
```
>>> (x.monthend() + 1)
DateDeux(2017, 8, 1)
```

#### Previous month start
```
>>> (x.monthstart() - 1).monthstart()
DateDeux(2017, 6, 1)
```

#### Previous year start
```
>>> x.yearstart() - 1
DateDeux(2016, 12, 31)
```
you get the idea...

#### you have a python date. You want to add 45 days to it and get a python date back
```
>>> y = date.today()
>>> y
datetime.date(2017, 7, 15)
>>> (DateDeux.frompydate(y) + 45).pydate()
datetime.date(2017, 8, 29)
```

#### Get all Sundays in the year
```
>>> x = DateDeux.today()
>>> x
DateDeux(2017, 7, 15)
>>> [z for z in x.yearcalendar() if z.dayname() == "Sunday"]
[DateDeux(2017, 1, 1), DateDeux(2017, 1, 8), DateDeux(2017, 1, 15), DateDeux(2017, 1, 22), DateDeux(2017, 1, 29), DateDeux(2017, 2, 5), DateDeux(2017, 2, 12), DateDeux(2017, 2, 19), DateDeux(2017, 2, 26), DateDeux(2017, 3, 5), DateDeux(2017, 3, 12), DateDeux(2017, 3, 19), DateDeux(2017, 3, 26), DateDeux(2017, 4, 2), DateDeux(2017, 4, 9), DateDeux(2017, 4, 16), DateDeux(2017, 4, 23), DateDeux(2017, 4, 30), DateDeux(2017, 5, 7), DateDeux(2017, 5, 14), DateDeux(2017, 5, 21), DateDeux(2017, 5, 28), DateDeux(2017, 6, 4), DateDeux(2017, 6, 11), DateDeux(2017, 6, 18), DateDeux(2017, 6, 25), DateDeux(2017, 7, 2), DateDeux(2017, 7, 9), DateDeux(2017, 7, 16), DateDeux(2017, 7, 23), DateDeux(2017, 7, 30), DateDeux(2017, 8, 6), DateDeux(2017, 8, 13), DateDeux(2017, 8, 20), DateDeux(2017, 8, 27), DateDeux(2017, 9, 3), DateDeux(2017, 9, 10), DateDeux(2017, 9, 17), DateDeux(2017, 9, 24), DateDeux(2017, 10, 1), DateDeux(2017, 10, 8), DateDeux(2017, 10, 15), DateDeux(2017, 10, 22), DateDeux(2017, 10, 29), DateDeux(2017, 11, 5), DateDeux(2017, 11, 12), DateDeux(2017, 11, 19), DateDeux(2017, 11, 26), DateDeux(2017, 12, 3), DateDeux(2017, 12, 10), DateDeux(2017, 12, 17), DateDeux(2017, 12, 24), DateDeux(2017, 12, 31)]
```

#### Is this a leap year?
```
>>> x
DateDeux(2017, 7, 15)
>>> x.yearstart().monthend() + 1
DateDeux(2017, 2, 1)
>>> (x.yearstart().monthend() + 1).monthend()
DateDeux(2017, 2, 28)
>>> (x.yearstart().monthend() + 1).monthend().day == 29
False
```

### Feedback and additional features
Please raise an issue in the repo

### License
[BSD License](https://opensource.org/licenses/BSD-3-Clause) 
