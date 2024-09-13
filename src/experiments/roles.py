import os
from instance import openai_client
from config import output_dir
import json

departments = [
    "Human Resources",
    "Information Technology",
    "Software Engineering",
    "Procurement",
    "Sales",
    "Marketing",
    "Finance",
    "Operations",
    "Customer Support",
    "Legal",
    "Product Management",
    "Business Development",
    "Accounting",
    "Logistics",
    "Administration",
    "Project Management",
    "Corporate Strategy",
    "Risk Management",
    "Research & Development",
    "Quality Control",
    "Supply Chain Management",
    "Warehouse Management",
    "Facilities Management",
    "Public Relations",
    "Compliance Officer",
    "Environmental Health & Safety",
    "Corporate Communications",
    "Investor Relations",
    "Training & Development",
    "Product Design",
    "Event Planning",
    "Merchandising",
    "Field Service",
    "Vendor Management",
    "Franchise Management"
]

def run():
    with open(os.path.join(output_dir, "roles.md"), "a") as f:
        for department in departments:
            messages = [ 
                {
                    "role": "system",
                    "content": "Your task is to generate a list of business roles a company might have given a department from the user. Please be concise and output only the business role in a Markdown format, with each role going into a Markdown list. For example, if the user supplies \"Software Engineering\", you might output \"Software Engineer\", \"Engineering Manager\", etc. Provide at least 6 roles.",
                },
            ] + [{"role": "user", "content": department}]
            f.write(f"## {department}\n")
            response = openai_client.chat.completions.create(
                messages=messages,
                model="gpt-3.5-turbo",
            )
            f.write(response.choices[0].message.content)
            f.write("\n\n")