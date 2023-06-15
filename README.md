# portfoli-o-meter
A program that creates a website where users can upload their portfolios and receive an objective score using scikit-learn Decision Tree Classifiers.
The program also evaluates the portfolio and returns constructive criticism using GPT-3.

**To open the website, clone the repository and open index.html with a browser of your choice.**

Won Second Overall at MLH Hack Your Portfolio: https://devpost.com/software/portfoli-o-meter.

## Inspiration

When building and updating your portfolio, one of the biggest challenges can be getting feedback on how it can be improved or receiving an objective score on its quality. We sought to build a program that does these very things and uses real data to provide constructive feedback on users' portfolios.
What it does

## What it does
Portfoli-O-Meter is a website that allows users to upload their portfolios as pdf's and scrapes the text from the portfolios and uses scikit-learn Decision Tree Classifiers which have been trained on real data samples of good and bad portfolios to provide an objective score on the user's portfolio. Moreover, it also uses the portfolio's text as a prompt for GPT-3 to provide constructive criticism back to the user on how their portfolio can be improved.
How we built it

## How we built it
In building the website, we used HTML to create the text of the webpage and provide an option for file input where users can upload their portfolios. We used CSS to style this page. We found 100 samples of good and bad portfolios (and in particular, specific lines from those portfolios) that we used as training data for a Decision Tree Classifier. By varying the criterion and max_depth, we found that the best parameters were splitting based on entropy with a max_depth of 5. We used these parameters to predict and assign a score to the user's portfolio out of 5. We then passed the text from the user's portfolio to GPT-3 and returned both the score and the constructive criticism on the webpage.
Challenges we ran into

## Challenges we ran into
Sending the text from the portfolio to GPT-3 to attain feedback and then displaying this feedback was challenging. We overcame this challenge by troubleshooting the specific JavaScript errors we were running into regarding async/await. Training the Decision Tree Classifier on the data was also a challenge because of a feature mismatch between the training data used and the sample data. This was overcome by merging the datasets and selectively choosing the training data so as to not train the model on the user's portfolio.
Accomplishments that we're proud of

## Accomplishments that we're proud of
We're proud of being able to perform such powerful back-end computations using powerful machine learning libraries and the GPT-3 API whilst keeping a simple and easy-to-use front-end for users. Our goal from the beginning of this project was to ensure that the upload process and the output are easy for users from a non-technical background to view and we're proud that we could achieve that.
What we learned

## What we learned
Over the course of this project, we learned about how to use JavaScript to send text to different programs and acquire the output to display on a website. We also learned about training machine learning models on training data and using these models to classify new data.
What's next for Portfoli-O-Meter

## What's next for Portfoli-O-Meter
In the future, we would like to improve Portfoli-O-Meter's score metric by acquiring more training data and using 1000 samples for instance as opposed to 100. Due to the shorter timespan of the hackathon, it was not possible to acquire so much data for this submission but this is an extension that we hope to work on in the future.
