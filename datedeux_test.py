'''Copyright 2017, Deepak

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import unittest
from datedeux import DateDeux
from datetime import date


class MonthEndTestCase(unittest.TestCase):
    """test if it produces month end properly"""

    def test_month_end(self):
        first_date = DateDeux(2017, 1, 1)

        month_ends = {1: DateDeux(2017, 1, 31), 2: DateDeux(2017, 2, 28),
        3: DateDeux(2017, 3, 31), 4: DateDeux(2017, 4, 30),
        5: DateDeux(2017, 5, 31), 6: DateDeux(2017, 6, 30),
        7: DateDeux(2017, 7, 31), 8: DateDeux(2017, 8, 31), 
        9: DateDeux(2017, 9, 30), 10: DateDeux(2017, 10, 31),
        11: DateDeux(2017, 11, 30), 12: DateDeux(2017, 12, 31)}


        current_date = first_date

        while current_date.year == 2017:
            _monthend = current_date.monthend()
            self.assertTrue(_monthend == month_ends[_monthend.month])
            current_date = current_date + 1


    def test_leap_month_end(self):
        self.assertTrue(DateDeux(2016, 2, 5).monthend() == DateDeux(2016, 2, 29))
        self.assertTrue(DateDeux(2012, 2, 5).monthend() == DateDeux(2012, 2, 29))
        self.assertTrue(DateDeux(1996, 2, 5).monthend() == DateDeux(1996, 2, 29))


class MonthStartTestCase(unittest.TestCase):
    """test if it produces month start properly"""

    def test_month_end(self):
        first_date = DateDeux(2017, 1, 1)

        month_starts = {1: DateDeux(2017, 1, 1), 2: DateDeux(2017, 2, 1),
        3: DateDeux(2017, 3, 1), 4: DateDeux(2017, 4, 1),
        5: DateDeux(2017, 5, 1), 6: DateDeux(2017, 6, 1),
        7: DateDeux(2017, 7, 1), 8: DateDeux(2017, 8, 1), 
        9: DateDeux(2017, 9, 1), 10: DateDeux(2017, 10, 1),
        11: DateDeux(2017, 11, 1), 12: DateDeux(2017, 12, 1)}


        current_date = first_date

        while current_date.year == 2017:
            _monthstart = current_date.monthstart()
            self.assertTrue(_monthstart == month_starts[_monthstart.month])
            current_date = current_date + 1


class YearStartTestCase(unittest.TestCase):
    """check if year starts are ok"""

    def test_year_start(self):
        year_list = list(range(2010, 2026))
        year_starts = {2010:DateDeux(2010, 1, 1), 
                        2011:DateDeux(2011, 1, 1), 
                        2012:DateDeux(2012, 1, 1), 
                        2013:DateDeux(2013, 1, 1), 
                        2014:DateDeux(2014, 1, 1), 
                        2015:DateDeux(2015, 1, 1), 
                        2016:DateDeux(2016, 1, 1), 
                        2017:DateDeux(2017, 1, 1), 
                        2018:DateDeux(2018, 1, 1), 
                        2019:DateDeux(2019, 1, 1), 
                        2020:DateDeux(2020, 1, 1), 
                        2021:DateDeux(2021, 1, 1), 
                        2022:DateDeux(2022, 1, 1), 
                        2023:DateDeux(2023, 1, 1), 
                        2024:DateDeux(2024, 1, 1), 
                        2025:DateDeux(2025, 1, 1)}

        for year in year_list:
            sample_date = DateDeux(year, 6, 30)

            for each_date in sample_date.yearcalendar():
                self.assertTrue(each_date.yearstart() == year_starts[each_date.year])



class YearEndTestCase(unittest.TestCase):
    """check if year ends are ok"""

    def test_year_start(self):
        year_list = list(range(2010, 2026))
        year_ends = {2010:DateDeux(2010, 12, 31), 
                    2011:DateDeux(2011, 12, 31), 
                    2012:DateDeux(2012, 12, 31), 
                    2013:DateDeux(2013, 12, 31), 
                    2014:DateDeux(2014, 12, 31), 
                    2015:DateDeux(2015, 12, 31), 
                    2016:DateDeux(2016, 12, 31), 
                    2017:DateDeux(2017, 12, 31), 
                    2018:DateDeux(2018, 12, 31), 
                    2019:DateDeux(2019, 12, 31), 
                    2020:DateDeux(2020, 12, 31), 
                    2021:DateDeux(2021, 12, 31), 
                    2022:DateDeux(2022, 12, 31), 
                    2023:DateDeux(2023, 12, 31), 
                    2024:DateDeux(2024, 12, 31), 
                    2025:DateDeux(2025, 12, 31)}

        for year in year_list:
            sample_date = DateDeux(year, 6, 30)

            for each_date in sample_date.yearcalendar():
                self.assertTrue(each_date.yearend() == year_ends[each_date.year])


class DayOfWeekTestCase(unittest.TestCase):
    """check if day of week is properly done"""

    def test_weekday(self):
        weekdays = {"2017-01-01":"Sunday",
        "2017-01-02":"Monday",
        "2017-01-03":"Tuesday",
        "2017-01-04":"Wednesday",
        "2017-01-05":"Thursday",
        "2017-01-06":"Friday",
        "2017-01-07":"Saturday",
        "2017-01-08":"Sunday",
        "2017-01-09":"Monday",
        "2017-01-10":"Tuesday",
        "2017-01-11":"Wednesday",
        "2017-01-12":"Thursday",
        "2017-01-13":"Friday",
        "2017-01-14":"Saturday",
        "2017-01-15":"Sunday",
        "2017-01-16":"Monday",
        "2017-01-17":"Tuesday",
        "2017-01-18":"Wednesday",
        "2017-01-19":"Thursday",
        "2017-01-20":"Friday",
        "2017-01-21":"Saturday",
        "2017-01-22":"Sunday",
        "2017-01-23":"Monday",
        "2017-01-24":"Tuesday",
        "2017-01-25":"Wednesday",
        "2017-01-26":"Thursday",
        "2017-01-27":"Friday",
        "2017-01-28":"Saturday",
        "2017-01-29":"Sunday",
        "2017-01-30":"Monday",
        "2017-01-31":"Tuesday",
        "2017-02-01":"Wednesday",
        "2017-02-02":"Thursday",
        "2017-02-03":"Friday",
        "2017-02-04":"Saturday",
        "2017-02-05":"Sunday",
        "2017-02-06":"Monday",
        "2017-02-07":"Tuesday",
        "2017-02-08":"Wednesday",
        "2017-02-09":"Thursday",
        "2017-02-10":"Friday",
        "2017-02-11":"Saturday",
        "2017-02-12":"Sunday",
        "2017-02-13":"Monday",
        "2017-02-14":"Tuesday",
        "2017-02-15":"Wednesday",
        "2017-02-16":"Thursday",
        "2017-02-17":"Friday",
        "2017-02-18":"Saturday",
        "2017-02-19":"Sunday",
        "2017-02-20":"Monday",
        "2017-02-21":"Tuesday",
        "2017-02-22":"Wednesday",
        "2017-02-23":"Thursday",
        "2017-02-24":"Friday",
        "2017-02-25":"Saturday",
        "2017-02-26":"Sunday",
        "2017-02-27":"Monday",
        "2017-02-28":"Tuesday",
        "2017-03-01":"Wednesday",
        "2017-03-02":"Thursday",
        "2017-03-03":"Friday",
        "2017-03-04":"Saturday",
        "2017-03-05":"Sunday",
        "2017-03-06":"Monday",
        "2017-03-07":"Tuesday",
        "2017-03-08":"Wednesday",
        "2017-03-09":"Thursday",
        "2017-03-10":"Friday",
        "2017-03-11":"Saturday",
        "2017-03-12":"Sunday",
        "2017-03-13":"Monday",
        "2017-03-14":"Tuesday",
        "2017-03-15":"Wednesday",
        "2017-03-16":"Thursday",
        "2017-03-17":"Friday",
        "2017-03-18":"Saturday",
        "2017-03-19":"Sunday",
        "2017-03-20":"Monday",
        "2017-03-21":"Tuesday",
        "2017-03-22":"Wednesday",
        "2017-03-23":"Thursday",
        "2017-03-24":"Friday",
        "2017-03-25":"Saturday",
        "2017-03-26":"Sunday",
        "2017-03-27":"Monday",
        "2017-03-28":"Tuesday",
        "2017-03-29":"Wednesday",
        "2017-03-30":"Thursday",
        "2017-03-31":"Friday",
        "2017-04-01":"Saturday",
        "2017-04-02":"Sunday",
        "2017-04-03":"Monday",
        "2017-04-04":"Tuesday",
        "2017-04-05":"Wednesday",
        "2017-04-06":"Thursday",
        "2017-04-07":"Friday",
        "2017-04-08":"Saturday",
        "2017-04-09":"Sunday",
        "2017-04-10":"Monday",
        "2017-04-11":"Tuesday",
        "2017-04-12":"Wednesday",
        "2017-04-13":"Thursday",
        "2017-04-14":"Friday",
        "2017-04-15":"Saturday",
        "2017-04-16":"Sunday",
        "2017-04-17":"Monday",
        "2017-04-18":"Tuesday",
        "2017-04-19":"Wednesday",
        "2017-04-20":"Thursday",
        "2017-04-21":"Friday",
        "2017-04-22":"Saturday",
        "2017-04-23":"Sunday",
        "2017-04-24":"Monday",
        "2017-04-25":"Tuesday",
        "2017-04-26":"Wednesday",
        "2017-04-27":"Thursday",
        "2017-04-28":"Friday",
        "2017-04-29":"Saturday",
        "2017-04-30":"Sunday",
        "2017-05-01":"Monday",
        "2017-05-02":"Tuesday",
        "2017-05-03":"Wednesday",
        "2017-05-04":"Thursday",
        "2017-05-05":"Friday",
        "2017-05-06":"Saturday",
        "2017-05-07":"Sunday",
        "2017-05-08":"Monday",
        "2017-05-09":"Tuesday",
        "2017-05-10":"Wednesday",
        "2017-05-11":"Thursday",
        "2017-05-12":"Friday",
        "2017-05-13":"Saturday",
        "2017-05-14":"Sunday",
        "2017-05-15":"Monday",
        "2017-05-16":"Tuesday",
        "2017-05-17":"Wednesday",
        "2017-05-18":"Thursday",
        "2017-05-19":"Friday",
        "2017-05-20":"Saturday",
        "2017-05-21":"Sunday",
        "2017-05-22":"Monday",
        "2017-05-23":"Tuesday",
        "2017-05-24":"Wednesday",
        "2017-05-25":"Thursday",
        "2017-05-26":"Friday",
        "2017-05-27":"Saturday",
        "2017-05-28":"Sunday",
        "2017-05-29":"Monday",
        "2017-05-30":"Tuesday",
        "2017-05-31":"Wednesday",
        "2017-06-01":"Thursday",
        "2017-06-02":"Friday",
        "2017-06-03":"Saturday",
        "2017-06-04":"Sunday",
        "2017-06-05":"Monday",
        "2017-06-06":"Tuesday",
        "2017-06-07":"Wednesday",
        "2017-06-08":"Thursday",
        "2017-06-09":"Friday",
        "2017-06-10":"Saturday",
        "2017-06-11":"Sunday",
        "2017-06-12":"Monday",
        "2017-06-13":"Tuesday",
        "2017-06-14":"Wednesday",
        "2017-06-15":"Thursday",
        "2017-06-16":"Friday",
        "2017-06-17":"Saturday",
        "2017-06-18":"Sunday",
        "2017-06-19":"Monday",
        "2017-06-20":"Tuesday",
        "2017-06-21":"Wednesday",
        "2017-06-22":"Thursday",
        "2017-06-23":"Friday",
        "2017-06-24":"Saturday",
        "2017-06-25":"Sunday",
        "2017-06-26":"Monday",
        "2017-06-27":"Tuesday",
        "2017-06-28":"Wednesday",
        "2017-06-29":"Thursday",
        "2017-06-30":"Friday",
        "2017-07-01":"Saturday",
        "2017-07-02":"Sunday",
        "2017-07-03":"Monday",
        "2017-07-04":"Tuesday",
        "2017-07-05":"Wednesday",
        "2017-07-06":"Thursday",
        "2017-07-07":"Friday",
        "2017-07-08":"Saturday",
        "2017-07-09":"Sunday",
        "2017-07-10":"Monday",
        "2017-07-11":"Tuesday",
        "2017-07-12":"Wednesday",
        "2017-07-13":"Thursday",
        "2017-07-14":"Friday",
        "2017-07-15":"Saturday",
        "2017-07-16":"Sunday",
        "2017-07-17":"Monday",
        "2017-07-18":"Tuesday",
        "2017-07-19":"Wednesday",
        "2017-07-20":"Thursday",
        "2017-07-21":"Friday",
        "2017-07-22":"Saturday",
        "2017-07-23":"Sunday",
        "2017-07-24":"Monday",
        "2017-07-25":"Tuesday",
        "2017-07-26":"Wednesday",
        "2017-07-27":"Thursday",
        "2017-07-28":"Friday",
        "2017-07-29":"Saturday",
        "2017-07-30":"Sunday",
        "2017-07-31":"Monday",
        "2017-08-01":"Tuesday",
        "2017-08-02":"Wednesday",
        "2017-08-03":"Thursday",
        "2017-08-04":"Friday",
        "2017-08-05":"Saturday",
        "2017-08-06":"Sunday",
        "2017-08-07":"Monday",
        "2017-08-08":"Tuesday",
        "2017-08-09":"Wednesday",
        "2017-08-10":"Thursday",
        "2017-08-11":"Friday",
        "2017-08-12":"Saturday",
        "2017-08-13":"Sunday",
        "2017-08-14":"Monday",
        "2017-08-15":"Tuesday",
        "2017-08-16":"Wednesday",
        "2017-08-17":"Thursday",
        "2017-08-18":"Friday",
        "2017-08-19":"Saturday",
        "2017-08-20":"Sunday",
        "2017-08-21":"Monday",
        "2017-08-22":"Tuesday",
        "2017-08-23":"Wednesday",
        "2017-08-24":"Thursday",
        "2017-08-25":"Friday",
        "2017-08-26":"Saturday",
        "2017-08-27":"Sunday",
        "2017-08-28":"Monday",
        "2017-08-29":"Tuesday",
        "2017-08-30":"Wednesday",
        "2017-08-31":"Thursday",
        "2017-09-01":"Friday",
        "2017-09-02":"Saturday",
        "2017-09-03":"Sunday",
        "2017-09-04":"Monday",
        "2017-09-05":"Tuesday",
        "2017-09-06":"Wednesday",
        "2017-09-07":"Thursday",
        "2017-09-08":"Friday",
        "2017-09-09":"Saturday",
        "2017-09-10":"Sunday",
        "2017-09-11":"Monday",
        "2017-09-12":"Tuesday",
        "2017-09-13":"Wednesday",
        "2017-09-14":"Thursday",
        "2017-09-15":"Friday",
        "2017-09-16":"Saturday",
        "2017-09-17":"Sunday",
        "2017-09-18":"Monday",
        "2017-09-19":"Tuesday",
        "2017-09-20":"Wednesday",
        "2017-09-21":"Thursday",
        "2017-09-22":"Friday",
        "2017-09-23":"Saturday",
        "2017-09-24":"Sunday",
        "2017-09-25":"Monday",
        "2017-09-26":"Tuesday",
        "2017-09-27":"Wednesday",
        "2017-09-28":"Thursday",
        "2017-09-29":"Friday",
        "2017-09-30":"Saturday",
        "2017-10-01":"Sunday",
        "2017-10-02":"Monday",
        "2017-10-03":"Tuesday",
        "2017-10-04":"Wednesday",
        "2017-10-05":"Thursday",
        "2017-10-06":"Friday",
        "2017-10-07":"Saturday",
        "2017-10-08":"Sunday",
        "2017-10-09":"Monday",
        "2017-10-10":"Tuesday",
        "2017-10-11":"Wednesday",
        "2017-10-12":"Thursday",
        "2017-10-13":"Friday",
        "2017-10-14":"Saturday",
        "2017-10-15":"Sunday",
        "2017-10-16":"Monday",
        "2017-10-17":"Tuesday",
        "2017-10-18":"Wednesday",
        "2017-10-19":"Thursday",
        "2017-10-20":"Friday",
        "2017-10-21":"Saturday",
        "2017-10-22":"Sunday",
        "2017-10-23":"Monday",
        "2017-10-24":"Tuesday",
        "2017-10-25":"Wednesday",
        "2017-10-26":"Thursday",
        "2017-10-27":"Friday",
        "2017-10-28":"Saturday",
        "2017-10-29":"Sunday",
        "2017-10-30":"Monday",
        "2017-10-31":"Tuesday",
        "2017-11-01":"Wednesday",
        "2017-11-02":"Thursday",
        "2017-11-03":"Friday",
        "2017-11-04":"Saturday",
        "2017-11-05":"Sunday",
        "2017-11-06":"Monday",
        "2017-11-07":"Tuesday",
        "2017-11-08":"Wednesday",
        "2017-11-09":"Thursday",
        "2017-11-10":"Friday",
        "2017-11-11":"Saturday",
        "2017-11-12":"Sunday",
        "2017-11-13":"Monday",
        "2017-11-14":"Tuesday",
        "2017-11-15":"Wednesday",
        "2017-11-16":"Thursday",
        "2017-11-17":"Friday",
        "2017-11-18":"Saturday",
        "2017-11-19":"Sunday",
        "2017-11-20":"Monday",
        "2017-11-21":"Tuesday",
        "2017-11-22":"Wednesday",
        "2017-11-23":"Thursday",
        "2017-11-24":"Friday",
        "2017-11-25":"Saturday",
        "2017-11-26":"Sunday",
        "2017-11-27":"Monday",
        "2017-11-28":"Tuesday",
        "2017-11-29":"Wednesday",
        "2017-11-30":"Thursday",
        "2017-12-01":"Friday",
        "2017-12-02":"Saturday",
        "2017-12-03":"Sunday",
        "2017-12-04":"Monday",
        "2017-12-05":"Tuesday",
        "2017-12-06":"Wednesday",
        "2017-12-07":"Thursday",
        "2017-12-08":"Friday",
        "2017-12-09":"Saturday",
        "2017-12-10":"Sunday",
        "2017-12-11":"Monday",
        "2017-12-12":"Tuesday",
        "2017-12-13":"Wednesday",
        "2017-12-14":"Thursday",
        "2017-12-15":"Friday",
        "2017-12-16":"Saturday",
        "2017-12-17":"Sunday",
        "2017-12-18":"Monday",
        "2017-12-19":"Tuesday",
        "2017-12-20":"Wednesday",
        "2017-12-21":"Thursday",
        "2017-12-22":"Friday",
        "2017-12-23":"Saturday",
        "2017-12-24":"Sunday",
        "2017-12-25":"Monday",
        "2017-12-26":"Tuesday",
        "2017-12-27":"Wednesday",
        "2017-12-28":"Thursday",
        "2017-12-29":"Friday",
        "2017-12-30":"Saturday",
        "2017-12-31":"Sunday",
        "2018-01-01":"Monday",
        "2018-01-02":"Tuesday",
        "2018-01-03":"Wednesday",
        "2018-01-04":"Thursday",
        "2018-01-05":"Friday",
        "2018-01-06":"Saturday",
        "2018-01-07":"Sunday",
        "2018-01-08":"Monday",
        "2018-01-09":"Tuesday",
        "2018-01-10":"Wednesday",
        "2018-01-11":"Thursday",
        "2018-01-12":"Friday",
        "2018-01-13":"Saturday",
        "2018-01-14":"Sunday",
        "2018-01-15":"Monday",
        "2018-01-16":"Tuesday",
        "2018-01-17":"Wednesday",
        "2018-01-18":"Thursday",
        "2018-01-19":"Friday",
        "2018-01-20":"Saturday",
        "2018-01-21":"Sunday",
        "2018-01-22":"Monday",
        "2018-01-23":"Tuesday",
        "2018-01-24":"Wednesday",
        "2018-01-25":"Thursday",
        "2018-01-26":"Friday",
        "2018-01-27":"Saturday",
        "2018-01-28":"Sunday",
        "2018-01-29":"Monday",
        "2018-01-30":"Tuesday",
        "2018-01-31":"Wednesday",
        "2018-02-01":"Thursday",
        "2018-02-02":"Friday",
        "2018-02-03":"Saturday",
        "2018-02-04":"Sunday",
        "2018-02-05":"Monday",
        "2018-02-06":"Tuesday",
        "2018-02-07":"Wednesday",
        "2018-02-08":"Thursday",
        "2018-02-09":"Friday",
        "2018-02-10":"Saturday",
        "2018-02-11":"Sunday",
        "2018-02-12":"Monday",
        "2018-02-13":"Tuesday",
        "2018-02-14":"Wednesday",
        "2018-02-15":"Thursday",
        "2018-02-16":"Friday",
        "2018-02-17":"Saturday",
        "2018-02-18":"Sunday",
        "2018-02-19":"Monday",
        "2018-02-20":"Tuesday",
        "2018-02-21":"Wednesday",
        "2018-02-22":"Thursday",
        "2018-02-23":"Friday",
        "2018-02-24":"Saturday",
        "2018-02-25":"Sunday",
        "2018-02-26":"Monday",
        "2018-02-27":"Tuesday",
        "2018-02-28":"Wednesday",
        "2018-03-01":"Thursday",
        "2018-03-02":"Friday",
        "2018-03-03":"Saturday",
        "2018-03-04":"Sunday",
        "2018-03-05":"Monday",
        "2018-03-06":"Tuesday",
        "2018-03-07":"Wednesday",
        "2018-03-08":"Thursday",
        "2018-03-09":"Friday",
        "2018-03-10":"Saturday",
        "2018-03-11":"Sunday",
        "2018-03-12":"Monday",
        "2018-03-13":"Tuesday",
        "2018-03-14":"Wednesday",
        "2018-03-15":"Thursday",
        "2018-03-16":"Friday",
        "2018-03-17":"Saturday",
        "2018-03-18":"Sunday",
        "2018-03-19":"Monday",
        "2018-03-20":"Tuesday",
        "2018-03-21":"Wednesday",
        "2018-03-22":"Thursday",
        "2018-03-23":"Friday",
        "2018-03-24":"Saturday",
        "2018-03-25":"Sunday",
        "2018-03-26":"Monday"}

        for eachday in weekdays:
            self.assertEquals(DateDeux.fromisodate(eachday).dayname(), weekdays[eachday])

    def test_weekday_short(self):
        weekdays = {"2017-01-01":"Sun",
                "2017-01-02":"Mon",
                "2017-01-03":"Tue",
                "2017-01-04":"Wed",
                "2017-01-05":"Thu",
                "2017-01-06":"Fri",
                "2017-01-07":"Sat",
                "2017-01-08":"Sun",
                "2017-01-09":"Mon",
                "2017-01-10":"Tue",
                "2017-01-11":"Wed",
                "2017-01-12":"Thu",
                "2017-01-13":"Fri",
                "2017-01-14":"Sat",
                "2017-01-15":"Sun",
                "2017-01-16":"Mon",
                "2017-01-17":"Tue",
                "2017-01-18":"Wed",
                "2017-01-19":"Thu",
                "2017-01-20":"Fri",
                "2017-01-21":"Sat",
                "2017-01-22":"Sun",
                "2017-01-23":"Mon",
                "2017-01-24":"Tue",
                "2017-01-25":"Wed",
                "2017-01-26":"Thu",
                "2017-01-27":"Fri",
                "2017-01-28":"Sat",
                "2017-01-29":"Sun",
                "2017-01-30":"Mon",
                "2017-01-31":"Tue",
                "2017-02-01":"Wed",
                "2017-02-02":"Thu",
                "2017-02-03":"Fri",
                "2017-02-04":"Sat",
                "2017-02-05":"Sun",
                "2017-02-06":"Mon",
                "2017-02-07":"Tue",
                "2017-02-08":"Wed",
                "2017-02-09":"Thu",
                "2017-02-10":"Fri",
                "2017-02-11":"Sat",
                "2017-02-12":"Sun",
                "2017-02-13":"Mon",
                "2017-02-14":"Tue",
                "2017-02-15":"Wed",
                "2017-02-16":"Thu",
                "2017-02-17":"Fri",
                "2017-02-18":"Sat",
                "2017-02-19":"Sun",
                "2017-02-20":"Mon",
                "2017-02-21":"Tue",
                "2017-02-22":"Wed",
                "2017-02-23":"Thu",
                "2017-02-24":"Fri",
                "2017-02-25":"Sat",
                "2017-02-26":"Sun",
                "2017-02-27":"Mon",
                "2017-02-28":"Tue",
                "2017-03-01":"Wed",
                "2017-03-02":"Thu",
                "2017-03-03":"Fri",
                "2017-03-04":"Sat",
                "2017-03-05":"Sun",
                "2017-03-06":"Mon",
                "2017-03-07":"Tue",
                "2017-03-08":"Wed",
                "2017-03-09":"Thu",
                "2017-03-10":"Fri",
                "2017-03-11":"Sat",
                "2017-03-12":"Sun",
                "2017-03-13":"Mon",
                "2017-03-14":"Tue",
                "2017-03-15":"Wed",
                "2017-03-16":"Thu",
                "2017-03-17":"Fri",
                "2017-03-18":"Sat",
                "2017-03-19":"Sun",
                "2017-03-20":"Mon",
                "2017-03-21":"Tue",
                "2017-03-22":"Wed",
                "2017-03-23":"Thu",
                "2017-03-24":"Fri",
                "2017-03-25":"Sat",
                "2017-03-26":"Sun",
                "2017-03-27":"Mon",
                "2017-03-28":"Tue",
                "2017-03-29":"Wed",
                "2017-03-30":"Thu",
                "2017-03-31":"Fri",
                "2017-04-01":"Sat",
                "2017-04-02":"Sun",
                "2017-04-03":"Mon",
                "2017-04-04":"Tue",
                "2017-04-05":"Wed",
                "2017-04-06":"Thu",
                "2017-04-07":"Fri",
                "2017-04-08":"Sat",
                "2017-04-09":"Sun",
                "2017-04-10":"Mon",
                "2017-04-11":"Tue",
                "2017-04-12":"Wed",
                "2017-04-13":"Thu",
                "2017-04-14":"Fri",
                "2017-04-15":"Sat",
                "2017-04-16":"Sun",
                "2017-04-17":"Mon",
                "2017-04-18":"Tue",
                "2017-04-19":"Wed",
                "2017-04-20":"Thu",
                "2017-04-21":"Fri",
                "2017-04-22":"Sat",
                "2017-04-23":"Sun",
                "2017-04-24":"Mon",
                "2017-04-25":"Tue",
                "2017-04-26":"Wed",
                "2017-04-27":"Thu",
                "2017-04-28":"Fri",
                "2017-04-29":"Sat",
                "2017-04-30":"Sun",
                "2017-05-01":"Mon",
                "2017-05-02":"Tue",
                "2017-05-03":"Wed",
                "2017-05-04":"Thu",
                "2017-05-05":"Fri",
                "2017-05-06":"Sat",
                "2017-05-07":"Sun",
                "2017-05-08":"Mon",
                "2017-05-09":"Tue",
                "2017-05-10":"Wed",
                "2017-05-11":"Thu",
                "2017-05-12":"Fri",
                "2017-05-13":"Sat",
                "2017-05-14":"Sun",
                "2017-05-15":"Mon",
                "2017-05-16":"Tue",
                "2017-05-17":"Wed",
                "2017-05-18":"Thu",
                "2017-05-19":"Fri",
                "2017-05-20":"Sat",
                "2017-05-21":"Sun",
                "2017-05-22":"Mon",
                "2017-05-23":"Tue",
                "2017-05-24":"Wed",
                "2017-05-25":"Thu",
                "2017-05-26":"Fri",
                "2017-05-27":"Sat",
                "2017-05-28":"Sun",
                "2017-05-29":"Mon",
                "2017-05-30":"Tue",
                "2017-05-31":"Wed",
                "2017-06-01":"Thu",
                "2017-06-02":"Fri",
                "2017-06-03":"Sat",
                "2017-06-04":"Sun",
                "2017-06-05":"Mon",
                "2017-06-06":"Tue",
                "2017-06-07":"Wed",
                "2017-06-08":"Thu",
                "2017-06-09":"Fri",
                "2017-06-10":"Sat",
                "2017-06-11":"Sun",
                "2017-06-12":"Mon",
                "2017-06-13":"Tue",
                "2017-06-14":"Wed",
                "2017-06-15":"Thu",
                "2017-06-16":"Fri",
                "2017-06-17":"Sat",
                "2017-06-18":"Sun",
                "2017-06-19":"Mon",
                "2017-06-20":"Tue",
                "2017-06-21":"Wed",
                "2017-06-22":"Thu",
                "2017-06-23":"Fri",
                "2017-06-24":"Sat",
                "2017-06-25":"Sun",
                "2017-06-26":"Mon",
                "2017-06-27":"Tue",
                "2017-06-28":"Wed",
                "2017-06-29":"Thu",
                "2017-06-30":"Fri",
                "2017-07-01":"Sat",
                "2017-07-02":"Sun",
                "2017-07-03":"Mon",
                "2017-07-04":"Tue",
                "2017-07-05":"Wed",
                "2017-07-06":"Thu",
                "2017-07-07":"Fri",
                "2017-07-08":"Sat",
                "2017-07-09":"Sun",
                "2017-07-10":"Mon",
                "2017-07-11":"Tue",
                "2017-07-12":"Wed",
                "2017-07-13":"Thu",
                "2017-07-14":"Fri",
                "2017-07-15":"Sat",
                "2017-07-16":"Sun",
                "2017-07-17":"Mon",
                "2017-07-18":"Tue",
                "2017-07-19":"Wed",
                "2017-07-20":"Thu",
                "2017-07-21":"Fri",
                "2017-07-22":"Sat",
                "2017-07-23":"Sun",
                "2017-07-24":"Mon",
                "2017-07-25":"Tue",
                "2017-07-26":"Wed",
                "2017-07-27":"Thu",
                "2017-07-28":"Fri",
                "2017-07-29":"Sat",
                "2017-07-30":"Sun",
                "2017-07-31":"Mon",
                "2017-08-01":"Tue",
                "2017-08-02":"Wed",
                "2017-08-03":"Thu",
                "2017-08-04":"Fri",
                "2017-08-05":"Sat",
                "2017-08-06":"Sun",
                "2017-08-07":"Mon",
                "2017-08-08":"Tue",
                "2017-08-09":"Wed",
                "2017-08-10":"Thu",
                "2017-08-11":"Fri",
                "2017-08-12":"Sat",
                "2017-08-13":"Sun",
                "2017-08-14":"Mon",
                "2017-08-15":"Tue",
                "2017-08-16":"Wed",
                "2017-08-17":"Thu",
                "2017-08-18":"Fri",
                "2017-08-19":"Sat",
                "2017-08-20":"Sun",
                "2017-08-21":"Mon",
                "2017-08-22":"Tue",
                "2017-08-23":"Wed",
                "2017-08-24":"Thu",
                "2017-08-25":"Fri",
                "2017-08-26":"Sat",
                "2017-08-27":"Sun",
                "2017-08-28":"Mon",
                "2017-08-29":"Tue",
                "2017-08-30":"Wed",
                "2017-08-31":"Thu",
                "2017-09-01":"Fri",
                "2017-09-02":"Sat",
                "2017-09-03":"Sun",
                "2017-09-04":"Mon",
                "2017-09-05":"Tue",
                "2017-09-06":"Wed",
                "2017-09-07":"Thu",
                "2017-09-08":"Fri",
                "2017-09-09":"Sat",
                "2017-09-10":"Sun",
                "2017-09-11":"Mon",
                "2017-09-12":"Tue",
                "2017-09-13":"Wed",
                "2017-09-14":"Thu",
                "2017-09-15":"Fri",
                "2017-09-16":"Sat",
                "2017-09-17":"Sun",
                "2017-09-18":"Mon",
                "2017-09-19":"Tue",
                "2017-09-20":"Wed",
                "2017-09-21":"Thu",
                "2017-09-22":"Fri",
                "2017-09-23":"Sat",
                "2017-09-24":"Sun",
                "2017-09-25":"Mon",
                "2017-09-26":"Tue",
                "2017-09-27":"Wed",
                "2017-09-28":"Thu",
                "2017-09-29":"Fri",
                "2017-09-30":"Sat",
                "2017-10-01":"Sun",
                "2017-10-02":"Mon",
                "2017-10-03":"Tue",
                "2017-10-04":"Wed",
                "2017-10-05":"Thu",
                "2017-10-06":"Fri",
                "2017-10-07":"Sat",
                "2017-10-08":"Sun",
                "2017-10-09":"Mon",
                "2017-10-10":"Tue",
                "2017-10-11":"Wed",
                "2017-10-12":"Thu",
                "2017-10-13":"Fri",
                "2017-10-14":"Sat",
                "2017-10-15":"Sun",
                "2017-10-16":"Mon",
                "2017-10-17":"Tue",
                "2017-10-18":"Wed",
                "2017-10-19":"Thu",
                "2017-10-20":"Fri",
                "2017-10-21":"Sat",
                "2017-10-22":"Sun",
                "2017-10-23":"Mon",
                "2017-10-24":"Tue",
                "2017-10-25":"Wed",
                "2017-10-26":"Thu",
                "2017-10-27":"Fri",
                "2017-10-28":"Sat",
                "2017-10-29":"Sun",
                "2017-10-30":"Mon",
                "2017-10-31":"Tue",
                "2017-11-01":"Wed",
                "2017-11-02":"Thu",
                "2017-11-03":"Fri",
                "2017-11-04":"Sat",
                "2017-11-05":"Sun",
                "2017-11-06":"Mon",
                "2017-11-07":"Tue",
                "2017-11-08":"Wed",
                "2017-11-09":"Thu",
                "2017-11-10":"Fri",
                "2017-11-11":"Sat",
                "2017-11-12":"Sun",
                "2017-11-13":"Mon",
                "2017-11-14":"Tue",
                "2017-11-15":"Wed",
                "2017-11-16":"Thu",
                "2017-11-17":"Fri",
                "2017-11-18":"Sat",
                "2017-11-19":"Sun",
                "2017-11-20":"Mon",
                "2017-11-21":"Tue",
                "2017-11-22":"Wed",
                "2017-11-23":"Thu",
                "2017-11-24":"Fri",
                "2017-11-25":"Sat",
                "2017-11-26":"Sun",
                "2017-11-27":"Mon",
                "2017-11-28":"Tue",
                "2017-11-29":"Wed",
                "2017-11-30":"Thu",
                "2017-12-01":"Fri",
                "2017-12-02":"Sat",
                "2017-12-03":"Sun",
                "2017-12-04":"Mon",
                "2017-12-05":"Tue",
                "2017-12-06":"Wed",
                "2017-12-07":"Thu",
                "2017-12-08":"Fri",
                "2017-12-09":"Sat",
                "2017-12-10":"Sun",
                "2017-12-11":"Mon",
                "2017-12-12":"Tue",
                "2017-12-13":"Wed",
                "2017-12-14":"Thu",
                "2017-12-15":"Fri",
                "2017-12-16":"Sat",
                "2017-12-17":"Sun",
                "2017-12-18":"Mon",
                "2017-12-19":"Tue",
                "2017-12-20":"Wed",
                "2017-12-21":"Thu",
                "2017-12-22":"Fri",
                "2017-12-23":"Sat",
                "2017-12-24":"Sun",
                "2017-12-25":"Mon",
                "2017-12-26":"Tue",
                "2017-12-27":"Wed",
                "2017-12-28":"Thu",
                "2017-12-29":"Fri",
                "2017-12-30":"Sat",
                "2017-12-31":"Sun",
                "2018-01-01":"Mon",
                "2018-01-02":"Tue",
                "2018-01-03":"Wed",
                "2018-01-04":"Thu",
                "2018-01-05":"Fri",
                "2018-01-06":"Sat",
                "2018-01-07":"Sun",
                "2018-01-08":"Mon",
                "2018-01-09":"Tue",
                "2018-01-10":"Wed",
                "2018-01-11":"Thu",
                "2018-01-12":"Fri",
                "2018-01-13":"Sat",
                "2018-01-14":"Sun",
                "2018-01-15":"Mon",
                "2018-01-16":"Tue",
                "2018-01-17":"Wed",
                "2018-01-18":"Thu",
                "2018-01-19":"Fri",
                "2018-01-20":"Sat",
                "2018-01-21":"Sun",
                "2018-01-22":"Mon",
                "2018-01-23":"Tue",
                "2018-01-24":"Wed",
                "2018-01-25":"Thu",
                "2018-01-26":"Fri",
                "2018-01-27":"Sat",
                "2018-01-28":"Sun",
                "2018-01-29":"Mon",
                "2018-01-30":"Tue",
                "2018-01-31":"Wed",
                "2018-02-01":"Thu",
                "2018-02-02":"Fri",
                "2018-02-03":"Sat",
                "2018-02-04":"Sun",
                "2018-02-05":"Mon",
                "2018-02-06":"Tue",
                "2018-02-07":"Wed",
                "2018-02-08":"Thu",
                "2018-02-09":"Fri",
                "2018-02-10":"Sat",
                "2018-02-11":"Sun",
                "2018-02-12":"Mon",
                "2018-02-13":"Tue",
                "2018-02-14":"Wed",
                "2018-02-15":"Thu",
                "2018-02-16":"Fri",
                "2018-02-17":"Sat",
                "2018-02-18":"Sun",
                "2018-02-19":"Mon",
                "2018-02-20":"Tue",
                "2018-02-21":"Wed",
                "2018-02-22":"Thu",
                "2018-02-23":"Fri",
                "2018-02-24":"Sat",
                "2018-02-25":"Sun",
                "2018-02-26":"Mon",
                "2018-02-27":"Tue",
                "2018-02-28":"Wed",
                "2018-03-01":"Thu",
                "2018-03-02":"Fri",
                "2018-03-03":"Sat",
                "2018-03-04":"Sun",
                "2018-03-05":"Mon",
                "2018-03-06":"Tue",
                "2018-03-07":"Wed",
                "2018-03-08":"Thu",
                "2018-03-09":"Fri",
                "2018-03-10":"Sat",
                "2018-03-11":"Sun",
                "2018-03-12":"Mon",
                "2018-03-13":"Tue",
                "2018-03-14":"Wed",
                "2018-03-15":"Thu",
                "2018-03-16":"Fri",
                "2018-03-17":"Sat",
                "2018-03-18":"Sun",
                "2018-03-19":"Mon",
                "2018-03-20":"Tue",
                "2018-03-21":"Wed",
                "2018-03-22":"Thu",
                "2018-03-23":"Fri",
                "2018-03-24":"Sat",
                "2018-03-25":"Sun",
                "2018-03-26":"Mon"}

        for eachday in weekdays:
            self.assertEquals(DateDeux.fromisodate(eachday).dayname_short(), weekdays[eachday])


class MonthCalendarTestCase(unittest.TestCase):
    def build_month_cal(self, year, month):
        _continue = True
        month_list = []
        _current = DateDeux(year, month, 1)

        while _continue:
            month_list.append(_current)
            _current_pydate = _current.pydate()
            _current_pydate = date.fromordinal(_current_pydate.toordinal() + 1)
            _current = DateDeux.frompydate(_current_pydate)

            if _current.month != month:
                _continue = False

        return tuple(month_list)


    def test_month_cal(self):
        self.assertTrue(tuple(DateDeux(1996, 1, 1).monthcalendar()) == self.build_month_cal(1996, 1))
        self.assertTrue(tuple(DateDeux(1996, 2, 1).monthcalendar()) == self.build_month_cal(1996, 2))
        self.assertTrue(tuple(DateDeux(1996, 12, 1).monthcalendar()) == self.build_month_cal(1996, 12))
        self.assertTrue(tuple(DateDeux(1997, 2, 1).monthcalendar()) == self.build_month_cal(1997, 2))



class YearCalendarTestCase(unittest.TestCase):
    def build_year_cal(self, year):
        _continue = True
        year_list = []
        _current = DateDeux(year, 1, 1)

        while _continue:
            year_list.append(_current)
            _current_pydate = _current.pydate()
            _current_pydate = date.fromordinal(_current_pydate.toordinal() + 1)
            _current = DateDeux.frompydate(_current_pydate)

            if _current.year != year:
                _continue = False

        return tuple(year_list)


    def test_month_cal(self):
        self.assertTrue(tuple(DateDeux(1996, 1, 1).yearcalendar()) == self.build_year_cal(1996))
        self.assertTrue(tuple(DateDeux(1997, 1, 1).yearcalendar()) == self.build_year_cal(1997))
        self.assertTrue(tuple(DateDeux(1998, 1, 1).yearcalendar()) == self.build_year_cal(1998))
        self.assertTrue(tuple(DateDeux(1999, 1, 1).yearcalendar()) == self.build_year_cal(1999))
        self.assertTrue(tuple(DateDeux(2000, 1, 1).yearcalendar()) == self.build_year_cal(2000))


if __name__ == "__main__":
    unittest.main()