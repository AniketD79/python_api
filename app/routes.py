from fastapi import APIRouter

router =APIRouter()
#router can be namer anythning like routers @routers.get
# @router.get("/")
# def home():
#     return {"message" : "Welcome to Anikets Fast API"}

@router.get("/")
def home():
    return {"message" : "Welcome to Aniket's Fastest API"}

@router.get("/new")
def newmessage():
    return {"message" : "Welcome to Aniket's Fastest API V2"}

@router.get("/third")
def newmessage3():
    return {"message" : "Welcome to Aniket's Fastest API V3"}

@router.get("/form-data")
def get_form_data():
    form_data = {
        "form_title": "User Survey",
        "description": "This is a sample survey form.",
        "fields": [
            {
                "label": "Full Name",
                "type": "text",
                "required": True
            },
            {
                "label": "Email",
                "type": "email",
                "required": True
            },
            {
                "label": "Gender",
                "type": "radio",
                "options": ["Male", "Female", "Other"],
                "required": False
            },
            {
                "label": "Hobbies",
                "type": "checkbox",
                "options": ["Reading", "Traveling", "Gaming", "Cooking"]
            }
        ]
    }
    return form_data