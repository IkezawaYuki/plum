from fastapi import FastAPI, UploadFile, File, Form
from model.contact_form import ContactForm
from typing import List


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello"}


@app.post("/support/contact")
def support_contact(contact_form: ContactForm):
    return contact_form


@app.post("/support/update")
def support_update(
    company_name: str = Form(...),
    last_name: str = Form(...),
    first_name: str = Form(...),
    mail_address: str = Form(...),
    wordpress_url: str = Form(...),
    request_content: str = Form(...),
    request_detail: str = Form(...),
    upload_files: List[UploadFile] = File(...)
):
    update_form = {
        "company_name" : company_name,
        "last_name": last_name,
        "first_name": first_name,
        "mail_address": mail_address,
        "wordpress_url": wordpress_url,
        "request_content": request_content,
        "request_detail": request_detail,
        "upload_files": upload_files,
    }
    return update_form