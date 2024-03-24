# Fit File Decoder
## Decodes Readable Values from Fit Activity

Load up a *.fit file with an activity, such as running, and decode values like speed, longitude, latitude and more.

Is currently only tested on ```Garmin Forerunner 35``` files, as I have written the decoder (with the help of [Garmin SDK](https://developer.garmin.com/connect-iq/sdk/)) to process my own running activites without using Strava or similar platforms.

Will currently only decode a few values, like longitude, latitude and speed, and return them as readable numbers. The speed is translated into pace. All units are in km (i.e. pace is km per minute). Speed is converted from ```meters per seconds``` as given in the original file.

  
