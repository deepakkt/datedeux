'''Copyright 2017, Deepak

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import unittest
from datedeux import DateDeux


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
    """check if year starts are ok"""

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


if __name__ == "__main__":
    unittest.main()