from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Data models
class User(BaseModel):
    id: str
    name: str
    email: str
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class Profile(BaseModel):
    id: str
    user_id: str
    name: str
    age: int

class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

class Movie(BaseModel):
    id: str
    title: str
    genre: str
    description: str
    year: int

class MovieUpdate(BaseModel):
    title: Optional[str] = None
    genre: Optional[str] = None
    description: Optional[str] = None
    year: Optional[int] = None

class Subscription(BaseModel):
    id: str
    user_id: str
    plan: str
    status: str

class SubscriptionUpdate(BaseModel):
    plan: Optional[str] = None
    status: Optional[str] = None

# Example data stores
users = []
profiles = []
movies = []
subscriptions = []

@app.post("/api/users", response_model=User)
def create_user(user: User):
    users.append(user)
    return user

@app.get("/api/users/{user_id}", response_model=User)
def get_user(user_id: str = Path(..., title="The ID of the user to get")):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/api/users/{user_id}", response_model=User)
def update_user(user_id: str, user_update: UserUpdate):
    for user in users:
        if user.id == user_id:
            if user_update.name is not None:
                user.name = user_update.name
            if user_update.email is not None:
                user.email = user_update.email
            if user_update.password is not None:
                user.password = user_update.password
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/api/users/{user_id}")
def delete_user(user_id: str):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/api/profiles", response_model=Profile)
def create_profile(profile: Profile):
    profiles.append(profile)
    return profile

@app.get("/api/profiles/{profile_id}", response_model=Profile)
def get_profile(profile_id: str = Path(..., title="The ID of the profile to get")):
    for profile in profiles:
        if profile.id == profile_id:
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

@app.put("/api/profiles/{profile_id}", response_model=Profile)
def update_profile(profile_id: str, profile_update: ProfileUpdate):
    for profile in profiles:
        if profile.id == profile_id:
            if profile_update.name is not None:
                profile.name = profile_update.name
            if profile_update.age is not None:
                profile.age = profile_update.age
            return profile
    raise HTTPException(status_code=404, detail="Profile not found")

@app.delete("/api/profiles/{profile_id}")
def delete_profile(profile_id: str):
    for profile in profiles:
        if profile.id == profile_id:
            profiles.remove(profile)
            return {"detail": "Profile deleted"}
    raise HTTPException(status_code=404, detail="Profile not found")

@app.post("/api/movies", response_model=Movie)
def create_movie(movie: Movie):
    movies.append(movie)
    return movie

@app.get("/api/movies/{movie_id}", response_model=Movie)
def get_movie(movie_id: str = Path(..., title="The ID of the movie to get")):
    for movie in movies:
        if movie.id == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

@app.put("/api/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: str, movie_update: MovieUpdate):
    for movie in movies:
        if movie.id == movie_id:
            if movie_update.title is not None:
                movie.title = movie_update.title
            if movie_update.genre is not None:
                movie.genre = movie_update.genre
            if movie_update.description is not None:
                movie.description = movie_update.description
            if movie_update.year is not None:
                movie.year = movie_update.year
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")

@app.delete("/api/movies/{movie_id}")
def delete_movie(movie_id: str):
    for movie in movies:
        if movie.id == movie_id:
            movies.remove(movie)
            return {"detail": "Movie deleted"}
    raise HTTPException(status_code=404, detail="Movie not found")

@app.post("/api/subscriptions", response_model=Subscription)
def create_subscription(subscription: Subscription):
    subscriptions.append(subscription)
    return subscription

@app.get("/api/subscriptions/{subscription_id}", response_model=Subscription)
def get_subscription(subscription_id: str = Path(..., title="The ID of the subscription to get")):
    for subscription in subscriptions:
        if subscription.id == subscription_id:
            return subscription
    raise HTTPException(status_code=404, detail="Subscription not found")

@app.put("/api/subscriptions/{subscription_id}", response_model=Subscription)
def update_subscription(subscription_id: str, subscription_update: SubscriptionUpdate):
    for subscription in subscriptions:
        if subscription.id == subscription_id:
            if subscription_update.plan is not None:
                subscription.plan = subscription_update.plan
            if subscription_update.status is not None:
                subscription.status = subscription_update.status
            return subscription
    raise HTTPException(status_code=404, detail="Subscription not found")

@app.delete("/api/subscriptions/{subscription_id}")
def delete_subscription(subscription_id: str):
    for subscription in subscriptions:
        if subscription.id == subscription_id:
            subscriptions.remove(subscription)
            return {"detail": "Subscription deleted"}
    raise HTTPException(status_code=404, detail="Subscription not found")
