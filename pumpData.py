#!/usr/bin/python

# gets the rainful data in compination with the pumping flow
def getRainfallPumpingOutput(cursor, pump, hourOfTheDayStart, hourOfTheDayEnd, timeWindowStart, timeWindowEnd, monthWindowStart,monthWindowEnd):
  cursor.execute("""
    SELECT pumps.station as 'station', avg(pumps.average_output) as 'average_output',isnull(sum(rainfall),0) as 'rainfall',min(pumps.date_from) as 'date_from',max(pumps.date_to) as 'date_to'
    FROM V_HSY_PUMPS_WEEKDAY pumps
    LEFT JOIN hsy_rainFALL_1H rain 
        ON pumps.station = rain.station
        AND pumps.date_to <= dateadd(hour, %d, rain.DateAndTime)
        AND pumps.date_to >= dateadd(hour, %d, rain.DateAndTime)
    WHERE pumps.station like '%s'
      AND pumps.hour >= %d AND pumps.hour <= %d
      AND datepart(mm,pumps.date_from) >= %d AND datepart(mm,pumps.date_from) <= %d
      AND pumps.average_output > 0
    GROUP BY pumps.station,datepart(yy,pumps.date_from),datepart(mm,pumps.date_from),datepart(dd,pumps.date_from);
    """ % (timeWindowEnd, timeWindowStart, pump,hourOfTheDayStart,hourOfTheDayEnd, monthWindowStart,monthWindowEnd))
  return cursor
