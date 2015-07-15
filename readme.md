<h1>A FoobotWeb Library | Python</h1>

A Python library for the Foobot to fetch its Air Quality reading data using its REST API for the desired time interval to be used for further analysis by other products/services.

Look at the official API Documentation <a href = "http://foobot.io/support/">here</a>.

<h3>Features:</h3>
<hr>
Contains the FoobotWeb class with the following functions -
- Login - Called in the constructor. It establishes a connection with the server using basic authentication.
- DeviceInfo - Gets the Device UUID.
- GetDatapointLast - Takes period, sampling and save as parameters. Asserting save stores the fetched data in JSON. Refer to the <a href = "http://foobot.io/support/">main docs</a> for more information.
- GetLastHour - Fetches the data for the last hour.
- GetLastDay - Fetches the data for the last day.
- GetDataInterval - Fetches all the data in the specified time interval. Parameters include starttime, endtime, sampling and save.

<h3>Requirements</h3>
<hr>
- Requests or Requests[security]



Analyze.py converts the saved JSON data to CSV format to be used for plotting and further analysis in Excel.

Please refer to main.py for example use. Sample output is visible in the data folder.

Please send me an email in case of any questions.

Author - bagarwa2
