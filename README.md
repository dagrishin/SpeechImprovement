# SpeechImprovement

## Description
SpeechImprovement is a Python web application for improving pronunciation in foreign languages. The application offers a set of exercises that users can perform while recording their voice and getting feedback on the results of the analysis.
## Installation
1. Clone the repository to your local machine:
`git clone https://github.com/dagrishin/SpeechImprovement.git`
2. Change to the project directory:
`cd SpeechImprovement`
3. Install the required dependencies by running:
`pip install -r requirements.txt`
4. Create a config.py file in the instance folder and add settings for the application:
`SECRET_KEY = 'mysecretkey'
DATABASE_URI = 'sqlite:///SpeechImprovement.db'`
5. Create a database:
`python app/create_db.py`
6. Run `python app.py` to start the application.
7. Navigate your browser to http://localhost:5000/ and start using the application.

## Usage
Once the application is running, users can sign up for an account and start practicing their pronunciation. The application provides a variety of exercises in the target foreign language, and uses speech recognition technology to analyze the user's voice and provide feedback on areas for improvement. The user's progress is saved in the database, allowing them to track their improvement over time.

## Technologies Used
The Speech Improvement Project is built using the following technologies:
- Python
- Flask
- PostgreSQL
- Web Audio API
- SpeechRecognition
- Pydub
- Librosa

## Future Improvements
Some potential improvements for the Speech Improvement Project include:
- Adding support for multiple foreign languages
- Implementing more advanced speech analysis algorithms
- Adding a social component to allow users to practice with each other
- Integrating with popular language learning platforms

## Contributing
Contributions to the Speech Improvement Project are welcome. To contribute, please fork the repository, make your changes, and submit a pull request.

## License
The Speech Improvement Project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
