# Support Ticket Classifier

An AI-powered command-line tool designed to automatically classify customer support tickets into distinct categories using the Gemini API and Pydantic-based structured outputs.

## Features

- **Multi-Category Classification**: Automatically classifies tickets into four key areas:
  1. **Billing**
  2. **Technical support**
  3. **Account access**
  4. **General inquiry**
- **Dual Output Modes**:
  - **Structured JSON Mode**: Leveraging Gemini's native structured JSON output using Pydantic schemas for downstream integrations. It returns the issue description, recommended categories, and detailed reasoning.
  - **Fast Text Mode**: Returns a simple, low-latency category name directly.
- **Deterministic Results**: Configured with `temperature=0.0` to ensure highly consistent and predictable classifications.
- **Cost & Latency Optimized**: 
  - Token budget controls using `max_output_tokens=10` for fast text output and `max_output_tokens=512` for structured JSON output.
  - Tracking and displaying the exact token usage count (`total_token_count`) for every API call.
- **Few-Shot Prompting**: Optimized using targeted training examples in the prompt to drastically improve classification accuracy for complex support scenarios.

---

## Project Structure

- `app/main.py`: Interactive CLI entry point managing user input, running the classifier, and printing results with token counts.
- `app/services/classifier_service.py`: Service class hosting LLM configuration, system instructions, few-shot examples, and Gemini API integration.
- `app/models/classifier.py`: Pydantic models mapping out the rigid structured output schema (`OutputData`) with validators (e.g., controlling reasoning list length).

---

## Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.10+ installed on your system.

### 2. Configure Virtual Environment
Set up a Python virtual environment and activate it:
```bash
# Create a virtual environment from the workspace root
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate
```

### 3. Install Dependencies
Install the required packages (ensure `google-genai` and `pydantic` are installed):
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Create a `.env` file in the `support-ticket-classifier` directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## Usage

Start the interactive CLI:
```bash
python -m app.main
```

### Example Interaction

```text
**** Welcome to support ticket classifier ****

Please type/paste your issue here. We will classify it in 4 categories:
1. Billing
2. Technical support
3. Account access
4. General inquiry

If you want to exit please type exit.

 Do you want the output in JSON format? (y/n): y

Type/paste your issue description here: I paid for the Premium tier an hour ago, but my dashboard features are still locked.

Output: {
    "given_issue_description": "I paid for the Premium tier an hour ago, but my dashboard features are still locked.",
    "suggested_categories": [
        "Technical support"
    ],
    "reasoning": [
        "The user is experiencing a technical issue where their dashboard features remain locked despite payment.",
        "The problem requires technical investigation to unlock the purchased features."
    ]
}

Tokens used: 715
```

---

## Test Dataset

The few-shot prompts have been optimized to handle complex ticket descriptions. You can use the following test cases to validate classification accuracy:

```json
[
    {
        "text": "My subscription automatically renewed today even though I clicked cancel yesterday. Please undo this.",
        "expected": "BILLING"
    },
    {
        "text": "Our company audit is tomorrow and our finance team can't find the downloadable PDF for our March transaction.",
        "expected": "BILLING"
    },
    {
        "text": "I need to split our monthly payment across two different corporate credit cards.",
        "expected": "BILLING"
    },
    {
        "text": "The system says my credit card on file expired, but I just updated it and it still says expired.",
        "expected": "BILLING"
    },
    {
        "text": "Is your checkout system compliant with PCI-DSS level 1 security standards?",
        "expected": "GENERAL_INQUIRY"
    },
    {
        "text": "If we evaluate your platform for a month, do we have to enter a credit card up front?",
        "expected": "GENERAL_INQUIRY"
    },
    {
        "text": "Do you offer regional pricing or localized currency adjustments for teams based in India?",
        "expected": "GENERAL_INQUIRY"
    },
    {
        "text": "Can your software handle 10,000 concurrent API calls, or will we need a custom enterprise contract?",
        "expected": "GENERAL_INQUIRY"
    },
    {
        "text": "I am on the Enterprise plan but the 'Export to CSV' button is completely grayed out for my user profile.",
        "expected": "TECHNICAL_SUPPORT"
    },
    {
        "text": "Every time I try to add a new seat to my team page, the screen goes completely white.",
        "expected": "TECHNICAL_SUPPORT"
    },
    {
        "text": "We keep getting a 403 Forbidden error when trying to sync our database with your webhook.",
        "expected": "TECHNICAL_SUPPORT"
    },
    {
        "text": "Your pricing page says SSO is included, but I can't find the SAML configuration settings anywhere.",
        "expected": "TECHNICAL_SUPPORT"
    },
    {
        "text": "Why youtube on screen mini player is not working in mac latest OS?",
        "expected": "TECHNICAL_SUPPORT"
    },
    {
        "text": "Why my expense invoices are not properly generated and updated in GST portal?",
        "expected": "TECHNICAL_SUPPORT"
    },
    {
        "text": "Why I'm not able to transfer my profile and its data in mobile.",
        "expected": "TECHNICAL_SUPPORT"
    }
]
```
