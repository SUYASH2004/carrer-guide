# Career Guide AI

A web application that generates personalized career roadmaps using Google's Gemini AI. The application provides detailed guidance for various computer-related career paths including Data Science, Web Development, App Development, and more.

## Features

- Modern, responsive UI
- Multiple career role options
- Experience level selection
- Detailed career roadmaps
- AI-powered recommendations
- Real-time response generation

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

6. Open your browser and navigate to `http://localhost:8000`

## Usage

1. Select your desired career role from the dropdown menu
2. Choose your current experience level
3. Click "Generate Roadmap"
4. View your personalized career roadmap

## Project Structure

- `main.py` - FastAPI application and routes
- `templates/` - HTML templates
- `requirements.txt` - Python dependencies
- `.env` - Environment variables

## Technologies Used

- FastAPI
- Google Gemini AI
- Tailwind CSS
- HTML5 
