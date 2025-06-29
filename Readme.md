
# Translation Microservice

![Imaage1](assets/Screenshot%202025-06-29%20193809.png)

The Translation MicroService is a lightweight, modular application designed to translate text using the Google Cloud Translate API. The service is built using FastAPI, a modern and fast web framework for building APIs with Python, and is served using Uvicorn, an ASGI server. The application is designed to handle both single and bulk translations, splitting longer texts into manageable chunks to ensure efficient processing.   

The service supports a variety of languages, including but not limited to English (en), Hindi (hi), Tamil (ta), Kannada (kn), Bengali (bn), French (fr), and Spanish (es). Users can select their desired target language from a dropdown menu in the web interface, making the service versatile and accessible for a wide range of users.

[Documentation](https://docs.google.com/document/d/1yMmJ7tDfi7moVpnZZJfdJQRN9hTeTr4o4oDRlrt6oV0/edit?usp=sharing)

### Usage

1. Setup the Environment:
- Ensure you have `python 3.9` or later version installed on your system.
- Install the required dependencies using pip: 
    
        
    ```
    pip install -r requirements.txt 
    ```

2. Setup the Variable:
- Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your Google Cloud credentials JSON file. This is necessary for accessing the Google Cloud Translate API.
    

    ```
    export GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json
    ```

3. Run the Application:
- Navigate to the project directory and run the FastAPI application using Uvicorn:
    
    ```
    uvicorn main:app --reload 
    ```

4. Access the Application:
Open your web browser and navigate to `http://127.0.0.1:8000` to access the application.


### Development Status
- Integration to deploy on Docker,
- Make it more user friendly and etc..