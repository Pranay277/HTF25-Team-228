export const MOCK_WARDROBE = [
  { id: 1, image_url: 'https://images.unsplash.com/photo-1512436991641-6745cdb1723f' },
  { id: 2, image_url: 'https://images.unsplash.com/photo-1517841905240-472988babdf9' },
  { id: 3, image_url: 'https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e' },
  { id: 4, image_url: 'https://images.unsplash.com/photo-1503342452485-86a096e79ad7' }
];

// Mock fetch function
export const fetchWardrobe = async () => MOCK_WARDROBE;

// Mock outfit generation (replace with API call when backend ready)
export const generateOutfit = async () => [
  {
    outfit_items: [
      { image_url: 'https://images.unsplash.com/photo-1512436991641-6745cdb1723f' },
      { image_url: 'https://images.unsplash.com/photo-1517841905240-472988babdf9' }
    ],
    explanation: "Demo classic summer outfit, backend not yet ready.",
    tip: "Swap tops for a new look every day!"
  },
  {
    outfit_items: [
      { image_url: 'https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e' },
      { image_url: 'https://images.unsplash.com/photo-1503342452485-86a096e79ad7' }
    ],
    explanation: "Layered autumn outfit demo. Good for campus or office!",
    tip: "Add a scarf for easy transitions."
  }
];
