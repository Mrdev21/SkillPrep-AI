from pydantic import BaseModel, Field


class ProfileCreate(BaseModel):
    full_name: str = Field(min_length=1, max_length=255)
    education: str | None = None
    university: str | None = None
    branch: str | None = None
    secondary_specialization: str | None = None
    experience_years: float = Field(default=0, ge=0)
    target_role: str | None = None
    interview_language: str = "English"
    prep_time_available: str | None = None
    learning_preference: str | None = None


class ProfileUpdate(BaseModel):
    full_name: str | None = Field(default=None, min_length=1, max_length=255)
    education: str | None = None
    university: str | None = None
    branch: str | None = None
    secondary_specialization: str | None = None
    experience_years: float | None = Field(default=None, ge=0)
    target_role: str | None = None
    interview_language: str | None = None
    prep_time_available: str | None = None
    learning_preference: str | None = None


class ProfileResponse(ProfileCreate):
    id: str
    user_id: str