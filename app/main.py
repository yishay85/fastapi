from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# This the command tal the  sqlalchemy to run the
# create statement its generated all the tables when its first started
# but since we have the alembic nuw ,we don't need this command

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# "*" -allow to all to contact
origins =["*"] #["https://www.google.com",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


# request Get method url: "/"
@app.get("/")  # get - Method, "/"- path (URL)
def root():  # root- Function
    return {"message": "welcom to my api!"}
