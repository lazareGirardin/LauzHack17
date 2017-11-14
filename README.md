# LauzHack17: Destination Advisor
A new interactive experience to plan and discover new destinations!  

Started during LauzHack17 hackathon for the SkyScanner challenge. Unfortunately, our teammates were sick and we were just 2. The project is still under construction. 

## Goal
Travelling might be the world's favorite hobby. Going on vacation is extremely rewarding. Some want to visit museums, some like to party and some like to chill at the beach. However, sometimes we know what we want to do, but not where we want to go! This is why we created Destination Advisor.

We enable the user to choose his dream vacations by selecting various features. According to his filters, we propose several destintions through our interactive map, using SkyScanner's API. Once the destination chosen, the user can directly click on a flight he would like to book which will redirect him to the SkyScanner website. Or if the you feel adventurous you can choose the "Surprise Me" option!

## User Interface

![Website Screenshot](https://i.imgur.com/FCUrQwk.png)

## The data
We have scrapped data to add multiple layers of cultural options eg, show towns with active nightlife, UNESCO sights, museums, parks, etc. from http://www.worldcitiescultureforum.com/ 

## The implementation
The back-end was done using python Flask and the front-end with Javascript D3. The data processing was done using python's pandas. 


## Future work
We would like to add a wishlist.
And the "Surprise Me" selects a random location. We wanted it to be filtered by user choices of cultural interests.
Also we obviously wanted to make the relation to the API more flexible (simple fix) : add start destination as well as dates. 

Hope you enjoy our very first use of javascript and D3 visualizations 🙂


## Credits
This project was done by [Lazare Girardin](https://github.com/lazareGirardin/) and [Brandon Le Sann](https://github.com/BrandonLS) during the [LauzHack 2017](http://lauzhack.com/), November 2017