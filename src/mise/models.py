from typing import Literal

from pydantic import BaseModel


class Ingredient(BaseModel):
    name: str
    quantity: float | None
    unit: str | None
    raw_text: str


class NutritionInfo(BaseModel):
    calories: float
    # the following are all in grams, as that's the standard unit
    protein: float
    fat: float
    carbs: float
    fiber: float
    source: Literal["usda", "llm_estimate"]


class IngredientNutrition(BaseModel):
    ingredient: Ingredient
    nutrition: NutritionInfo


class ServingSize(BaseModel):
    grams: float
    ml: float | None
    oz: float | None
    cups: float | None
    description: str


class RecipeMetadata(BaseModel):
    name: str
    author: str | None
    source_url: str | None
    servings: int | None
    serving_sizes: list[ServingSize]


class RecipeAnalysis(BaseModel):
    metadata: RecipeMetadata
    ingredients: list[IngredientNutrition]
    total_nutrition: NutritionInfo
    per_serving_nutrition: NutritionInfo | None
