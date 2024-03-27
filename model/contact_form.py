from pydantic import BaseModel
from typing import Optional


class ContactForm(BaseModel):
    company_name: str
    phone: Optional[str] = None
    last_name: str
    first_name: str
    mail_address: str
    content: str

    def to_dict(self):
        return {
            "company_name": self.company_name,
            "phone": self.phone,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "mail_address": self.mail_address,
            "content": self.content
        }

    def form_validation(self):
        errors = []
        if not self.company_name:
            errors.append("company_name is required")
        if not self.last_name:
            errors.append("last_name is required")
        if not self.first_name:
            errors.append("first_name is required")
        if not self.mail_address:
            errors.append("mail_address is required")
        if not self.content:
            errors.append("content is required")
        return len(errors) == 0
