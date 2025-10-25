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