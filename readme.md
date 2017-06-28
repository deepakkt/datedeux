# Date Deux
This is basically the Python date module supplanted with some useful functions. This is a superclass so it supports everything the date module does

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

### Get a Python date back out

```
>>> x
DateDeux(2017, 6, 28)
>>> x.pydate()
datetime.date(2017, 6, 28)
```

### License
[BSD License](https://opensource.org/licenses/BSD-3-Clause) 