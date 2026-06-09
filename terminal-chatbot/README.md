# Terminal Chatbot

A terminal-based chatbot powered by Gemini that demonstrates stateful multi-turn conversation and structured JSON output.

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