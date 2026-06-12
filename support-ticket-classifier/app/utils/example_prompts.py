example_prompts_for_json_response = """
    <example>
        Input: I was charged twice for my subscription this month. Please refund me.
        Output: {
            "given_issue_description": "I was charged twice for my subscription this month. Please refund me.",
            "suggested_categories": ["Billing"],
            "reasoning": ["The user is complaining about being charged twice and requests a refund, which clearly falls under the Billing category."]
        }
    </example>

    <example>
        Input: The mobile app keeps crashing on the login screen. I am using an iPhone 15.
        Output: {
            "given_issue_description": "The mobile app keeps crashing on the login screen. I am using an iPhone 15.",
            "suggested_categories": [
                "Technical support"
            ],
            "reasoning": [
                "The user is experiencing a technical issue with the mobile app crashing.",
                "The issue occurs on the login screen, indicating a problem with the application's functionality.",
                "The user has provided device information (iPhone 15), which is relevant for technical troubleshooting."
            ]
        }
    </example>

    <example>
        Input: I forgot my password and the reset email link is expiring before I can click it.
        Output: {
            "given_issue_description": "I forgot my password and the reset email link is expiring before I can click it.",
            "suggested_categories": [
                "Account access"
            ],
            "reasoning": [
                "The user is explicitly stating they forgot their password and cannot access their account due to an expiring reset link. This directly falls under the 'Account access' category."
            ]
        }
    </example>

    <example>
        Input: Do you offer bulk discounts for teams larger than 50 people?
        Output: {
            "given_issue_description": "Do you offer bulk discounts for teams larger than 50 people?",
            "suggested_categories": [
                "General inquiry"
            ],
            "reasoning": [
                "The user is asking about potential discounts and pricing for a larger group, which falls under a general inquiry about services and offerings rather than a specific billing issue, technical problem, or account access problem."
            ]
        }
    </example>
"""

example_prompts_for_one_word_response = f"""
    <example>
        Input: I was charged twice for my subscription this month. Please refund me.
        Output: Billing
    </example>

    <example>
        Input: The mobile app keeps crashing on the login screen. I am using an iPhone 15.
        Output: Technical support
    </example>

    <example>
        Input: I forgot my password and the reset email link is expiring before I can click it.
        Output: Account access
    </example>

    <example>
        Input: Do you offer bulk discounts for teams larger than 50 people?
        Output: General inquiry
    </example>

    <example>
        Input: What forms of payment do you accept for international corporate accounts?
        Output: GENERAL_INQUIRY
    </example>

    <example>
        Input: Where can I find your pricing matrix for the Enterprise tier?
        Output: GENERAL_INQUIRY
    </example>

    <example>
        Input: If I add 15 more users next month, how does that impact my overall subscription rate?
        Output: GENERAL_INQUIRY
    </example>

    <example>
        Input: I tried to upgrade my plan but the checkout page keeps giving me a Processor Error 402.
        Output: BILLING
    </example>

    <example>
        Input: Can you update the VAT number and company address shown on invoice #1042?
        Output: BILLING
    </example>

    <example>
        Input: I deactivated my account last week but I still see a pending charge on my bank statement.
        Output: BILLING
    </example>

    <example>
        Input: I paid for the Premium tier an hour ago, but my dashboard features are still locked.
        Output: TECHNICAL_SUPPORT
    </example>

    <example>
        Input: The system says my account is suspended due to an API limit, but we barely used it today.
        Output: TECHNICAL_SUPPORT
    </example>
"""

