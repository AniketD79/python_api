from fastapi import APIRouter

router =APIRouter()

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