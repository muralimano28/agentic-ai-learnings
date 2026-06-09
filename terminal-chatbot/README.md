# Terminal Chatbot

A terminal-based chatbot powered by Gemini that demonstrates stateful multi-turn conversation and structured JSON output.

---

## Getting Started

### Prerequisites
- Python 3.9 or higher

### Installation

1. **Navigate to the project directory:**
   ```bash
   cd terminal-chatbot
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required Python libraries:**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Create a `.env` file in the root of the `terminal-chatbot` directory and add your Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## Running the Application

To start the interactive terminal chatbot, run the following command from the `terminal-chatbot` directory:
```bash
python -m app.main
```

During startup, the application will prompt you for:
1. **Name:** Enter your name to start the session.
2. **Stateful Chatbot (y/n):** Enable to preserve conversation history across turns.
3. **JSON Structured Output (y/n):** Enable to enforce responses to follow a structured JSON schema.

---

## Example Usage

Below is an example of an interactive session demonstrating stateful conversation history and structured JSON responses:

### Turn 1

**User (Murali):**
> Hi, I'm trying to find a job. I'm Murali manohar. My last name is perumal. I have 10+ years of experience in building web apps and optimizing them in the mobile.

**Bot Response (Structured JSON):**
```json
{
  "user_name": "Murali manohar perumal",
  "topic": "Job search assistance",
  "sentiment": "positive",
  "summary": "Murali is seeking job opportunities leveraging his 10+ years of experience in web application development and mobile optimization.",
  "company_name": "N/A",
  "domain": "Web Development",
  "years_of_experience": 10,
  "action_items": [
    "Update resume with mobile optimization focus",
    "Identify target companies in the web sector",
    "Network with industry professionals"
  ],
  "actual_response": "Welcome, Murali! With a decade of experience, you are essentially a web wizard. Let's get that resume polished and find you a role that actually appreciates your mobile optimization magic."
}
```

### Turn 2

**User (Murali):**
> I have tried applying to 100+ companies. None responded till now. Am not very happy about this.

**Bot Response (Structured JSON):**
```json
{
  "user_name": "Murali manohar perumal",
  "topic": "Job search frustration",
  "sentiment": "negative",
  "summary": "Murali has applied to over 100 companies with no response, leading to frustration in his job search process.",
  "company_name": "N/A",
  "domain": "Web Development",
  "years_of_experience": 10,
  "action_items": [
    "Review resume for ATS compatibility",
    "Tailor cover letters for specific roles",
    "Focus on networking instead of mass-applying"
  ],
  "actual_response": "100 applications without a bite? That sounds like a broken algorithm, not a reflection of your skills. Let's pivot from the 'spray and pray' method to a sniper approach—quality over quantity, Murali!"
}
```
