from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Career roles and their descriptions
CAREER_ROLES = {
    "data_science": "Data Science",
    "web_development": "Web Development",
    "app_development": "App Development",
    "ai_ml": "AI/ML Engineering",
    "devops": "DevOps Engineering",
    "cybersecurity": "Cybersecurity",
    "cloud_engineering": "Cloud Engineering"
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "career_roles": CAREER_ROLES})

@app.post("/generate-roadmap")
async def generate_roadmap(role: str = Form(...), experience: str = Form(...)):
    try:
        # Initialize Gemini model
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Create structured prompt
        prompt = f"""Create a detailed career roadmap for {CAREER_ROLES[role]} with {experience} level of experience.
        Format the response in a clear, structured way using the following sections and HTML-like format:

        <section class="overview">
        Brief overview of the {CAREER_ROLES[role]} career path and what to expect
        </section>

        <section class="skills">
        <h3>🛠 Required Skills and Technologies</h3>
        • List key technical skills
        • List important tools and technologies
        • List soft skills needed
        </section>

        <section class="learning">
        <h3>📚 Learning Resources</h3>
        • Online courses (with specific recommendations)
        • Books
        • Tutorials and documentation
        • Learning platforms
        </section>

        <section class="projects">
        <h3>🚀 Project Ideas</h3>
        • List 3-4 practical projects with increasing complexity
        • Include project descriptions and learning outcomes
        </section>

        <section class="certifications">
        <h3>📜 Recommended Certifications</h3>
        • List relevant certifications
        • Include difficulty level and prerequisites
        </section>

        <section class="market">
        <h3>💼 Job Market Insights</h3>
        • Current demand
        • Industry trends
        • Popular job titles
        • Required experience levels
        </section>

        <section class="salary">
        <h3>💰 Salary Expectations</h3>
        • Entry-level range
        • Mid-level range
        • Senior-level range
        • Factors affecting salary
        </section>

        <section class="growth">
        <h3>📈 Growth Opportunities</h3>
        • Career progression path
        • Advanced specializations
        • Future prospects
        • Skills to develop for advancement
        </section>

        Make sure to include practical, actionable information and keep the content concise but informative.
        Use bullet points for better readability."""
        
        # Generate response with safety settings
        generation_config = {
            "temperature": 0.7,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        }
        
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE",
            },
        ]
        
        response = model.generate_content(
            prompt,
            generation_config=generation_config,
            safety_settings=safety_settings
        )
        
        return {"roadmap": response.text}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 