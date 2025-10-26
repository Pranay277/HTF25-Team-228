# AI Outfit Planner - API Contract

This document is the single source of truth for the API.
**Frontend:** Build your UI using this.
**Backend:** Build your endpoints to match this.

---

## `POST /api/v1/wardrobe/add`

* **Description:** Uploads a photo, AI analyzes it, and saves the item.
* **Request:** `FormData` containing an image file.
* **Response: (200 OK)** - The new wardrobe item object.

```json
{
  "item_id": "uuid-1234-abcd",
  "owner_id": "user-uuid-5678",
  "description": "Blue ripped jeans",
  "image_url": "https://<your-supabase-url>/.../image.png",
  "category": "bottom",
  "subcategory": "jeans",
  "colors": ["blue"],
  "pattern": "solid",
  "style_tags": ["casual", "streetwear", "gen z"],
  "formality_level": 1
}
{
  "occasion": "Work Party",
  "style_vibe": "Gen X",
  "weather": "Cold"
}
[
  {
    "outfit_items": [
      "uuid-for-blazer", 
      "uuid-for-shirt", 
      "uuid-for-pants"
    ],
    "explanation": "This is a great look because the classic blazer is updated by the modern cut of the pants, fitting the Gen X vibe.",
    "tip": "Layer the blazer over the shirt for a smart-casual look."
  },
  {
    "outfit_items": [
      "uuid-for-sweater", 
      "uuid-for-jeans"
    ],
    "explanation": "This alternative is more relaxed but still appropriate for a party.",
    "tip": "Tuck in the sweater with a 'French tuck' to define your waist."
  }
]
[
  {
    "item_id": "uuid-1234-abcd",
    "description": "Blue ripped jeans",
    "image_url": "https://.../image.png",
    "category": "bottom",
    ...
  },
  {
    "item_id": "uuid-5678-efgh",
    "description": "White Graphic T-Shirt",
    "image_url": "https://.../image2.png",
    "category": "top",
    ...
  }
]