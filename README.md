# Junnto

## Inspiration
Our inspiration for JUNTO was solving the following problem. According to the most recent data, of the total 41.3 million immigrants in the United States in 2017 about half, 20.4 million, spoke English less than “very well." Knowing this, we wanted to provide immigrants with a leading practice resource that is both engaging and interactive for the targeted demographic. While many practice resource applications are available withstanding a saturated market there is currently no SMS platform that helps immigrants study for the Naturalization Civics Immigration Test that is composed of 150 U.S. History questions. While many immigrants often come to America in a weak socioeconomic background, we believe that a comprehensive study platform that not only considers their working hours but the common lack of technical efficiency among immigrants is important. JUNTO will help immigrants swim through the citizenship process.

## What it does
JUNTO is a learning practice resource tool that was created to create a periodical study system for working-class immigrants that wish to take and pass the Civics Immigration Test. While there have been practice resource tools in the past, JUNTO is the only interactive SMS platform that sends periodical texts free at charge, keeping in mind that almost 90% of immigrants are working class individuals and the average study period for immigrants constitutes 5 months. Not only does our product have the best UI/UX interface presented in a Civics Resource Study Resource Tool but acknowledges that almost 3 quarters of incoming immigrants are not proficient with technology.

## How we built it
We built our application mainly using Python. Our back-end is running a Python Flask server that uses Ngrok to handle Webhooks for Twilio's API. We use a simple algorithm that selects and sends random questions to our users using Twilio's API. We have a file of questions and answers we read from.

## Challenges we ran into
We ran into a lot of challenges using Twilio's API. Sending texts was very easy to accomplish, however, we encountered debilitating bugs when we tried to implement receiving a text from our users. After a lot of trial and error, we finally came up with a working prototype and realized that the phones we were initially using didn't support some of these functionalities we were trying to implement.

## Accomplishments that we're proud of
We're very proud of our prototype since we put a lot of work into it. While we began to build a prototype for an IOS app that would provide a network and like-minded services we are proud of the research that we put into the product to ensure successful customer validation. We believe that while an iOS app may seem appealing, many incoming older immigrants are not tech-savvy and are much more comfortable with an application that is provided through an SMS server.

## What we learned
We learned that although sometimes it simpler to default to the most redundant idea, the most profitable and effective products are those that meet the needs of the targeted demographic and consider their issues and struggles in order to maximize effective customer loyalty and usage, alongside customer validation.

## What's next for JUNTO
We believe that JUNTO can ultimately grow into an intergovernmental organization supported by the U.S. Immigration Services and Border Control. By providing a proficient service that simplifies the educational process of immigrants preparing for the naturalization test, the U.S. government can state that is legally provided all the services to citizens to succeed in passing the test, alongside helping many immigrants achieve citizenship free of charge.

<a href="http://tinypic.com?ref=2dtrezb" target="_blank"><img src="http://i64.tinypic.com/2dtrezb.jpg" border="0" alt="Image and video hosting by TinyPic"></a>
