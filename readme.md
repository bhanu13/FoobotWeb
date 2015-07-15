FoobotWeb Library | Python

A Python library for the Foobot to fetch data from its REST API for the desired interval to be used for further analysis by other products/services.

Look at the API Documentation <a href = "#">here</a>.

<h3>Features:</h3>
<hr>
Contains the FoobotWeb class with the following functions -
- Login - Called in the constructor. It establishes a connection with the server using basic authentication.
- DeviceInfo - Gets the Device UUID.
- GetDatapointLast - Takes period, sampling and save as parameters. Asserting save stores the fetched data in JSON. Refer to the main docs for more information.
- GetLastHour - Fetches the data for the last hour.
- GetLastDay - Fetches the data for the last day.
- GetDataInterval - Fetches all the data in the specified time interval. Parameters include starttime, endtime, sampling and save.

Analyze.py converts the saved JSON data to CSV format to be used for plotting and further analyzing in Excel.

Please refer to main.py for example use. Sample outputs are visible in the data folder.

Author - bhanu13



