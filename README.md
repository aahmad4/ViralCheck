# ViralCheck

This project was done for the NotUniversity Hacks Hackathon, a competition geared towards High School students and under. Due to the recent situation with the Pandemic and the large amount of free time available to most students and young adults, we thought we should try and do our part on delivering a positive difference. That’s why we created ViralCheck, to provide a social media experience for aspiring business people looking for a platform to share ideas, find inspiration, and even get creative with some of the machine learning features. 
A link to our devpost submission can be found here: https://devpost.com/software/viralcheck-social-media-app
A link to a small YouTube demo of the apps purpose and functionality can be seen here: https://www.youtube.com/watch?v=3txJLnwXW24&t=2s

## An Overview Of The Completed Product

Our project consists of a web-app, whose main feature is predicting the number of likes a YouTube video will get, based on past and current data such as the subscriber count, title of the video, and average views. The user has to simply enter the URL of the video, and our app will automatically extract the required data, using the Youtube API v3. The other features of our web-app include a forums page to allow users with accounts to post questions, ideas, and answers, as well as a thumbnail gallery. We also built a login system, so that users can create accounts and post in the forums. On top of this, we have a special section to allow logged in users to adjust their credentials if they wish and even customize their own profile pictures.

## Features

* User authentication
   * Login system
   * Registration system
   * Cryptography
   * Automated forgot password email responses
* Machine Learning
   * Uses models built with TensorFlow, Keras, and Scikit Learn to detect how many likes a YouTube video will get
   * Currently working on a thumbnail detector
* Databases
   * Uses a Postgres database to store user accounts, allow users to create new posts to forumns, and share new thumbnail and video          content ideas
   
## How we built it

##### The Machine Learning Model
The model takes data from the video and the youtube channel as input (such as subscriber count, average view count of the channel, number of comments, current view count, time of uploading etc.), and outputs the expected number of likes the video will get. For this prediction, we used a python-based Random Forester Regressor classifier, implemented using the sklearn library and trained using a dataset extracted from Youtube’s 8M dataset. To save the model after training, we used a .pickle file. 

##### The Youtube API
We wanted to make our app such that the user can predict the number of likes using only the URL of the video. For doing this, we first extracted the unique video-id from the URL. Then, we used this id to get the rest of the data using the Youtube API v3. We then fed this data into our ML model.

##### Front-end
The front-end of the web app itself is built with Flask, using templates with html and css. We used the library bootstrap and semantic UI for responsiveness and design. We are proud of the counting up animation of the likes prediction. 

##### Back-end and hosting
We used flask and postgres for the back-end as well as encrypting libraries like bcrypt to secure users passwords. We're hosting on microsoft azure. 

##### Account manager and forums
Users are able to adjust their account details and profile picture for more customization.


## Model
Since our model was too large to upload directly on GitHub (1 Gig), we decided to upload it on dropbox and leave a link if someone wants to download and test out our app. Simply download this model and put it in the same directory as the predict.py file. Download the model pickle file here: https://www.dropbox.com/s/g2sqw4l2yoqufr8/model-final?dl=0
its too big for github.

## Clone
```
git clone https://github.com/aahmad4/ViralCheck-Social-Media-App
```

## Usage
```
python main.py
```
Then go to 
```
localhost:8080
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
