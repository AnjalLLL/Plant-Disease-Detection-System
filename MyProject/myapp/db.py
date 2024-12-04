from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from django.conf import settings
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import urllib.parse

# Load environment variables from the .env file
load_dotenv()

def get_db():
    # Fetch the raw MongoDB username and password from the environment
    username = os.getenv("MONGO_USERNAME")
    password = os.getenv("MONGO_PASSWORD")

    # Ensure the username and password are strings before encoding
    if not isinstance(username, str) or not isinstance(password, str):
        raise TypeError("Username and password must be strings")

    # Encode the username and password as bytes, then URL encode
    encoded_username = urllib.parse.quote_plus(username.encode('utf-8'))
    encoded_password = urllib.parse.quote_plus(password.encode('utf-8'))

    # Construct the MongoDB URI with the encoded credentials
    mongo_uri = f"mongodb+srv://{encoded_username}:{encoded_password}@project-1.ourfx.mongodb.net/Project_Database?retryWrites=true&w=majority"
    
    # Debug: Print out the value of the MongoDB URI
    print(f"MongoDB URI loaded: {mongo_uri}")

    if not mongo_uri:
        raise ValueError("MongoDB URI is not set in the .env file")

    # Connect to MongoDB using the constructed URI
    client = MongoClient(mongo_uri)
    
    # Assuming you're using the 'Project_Database'
    db = client.get_database("Project_Database")
    
    return db

# Get the MongoDB connection and perform any action
try:
    db = get_db()
    print("MongoDB connection established successfully!")
except Exception as e:
    print(f"Error: {e}")

    
   

db=get_db()
# Step 3: Access the 'disease_info' collection (will be created if it doesn't exist)
disease_collection = db.disease_data

# Step 4: Define disease information to insert
disease_data = [
    
  {
    "disease_name": "Apple___Apple_scab",
    "description": "Apple scab is caused by the fungus Venturia inaequalis, resulting in olive-green to black spots on leaves, fruit, and sometimes flowers. This disease thrives in cool, wet weather, leading to premature leaf drop, fruit deformation, and significant yield losses if not managed.",
    "prevention": [
      "Plant resistant varieties such as Liberty and Enterprise.",
      "Practice proper pruning to improve air circulation and reduce humidity around the tree.",
      "Clean up and destroy fallen leaves and debris in the fall to remove overwintering fungal spores."
    ],
    "treatment": [
      "Apply fungicides containing captan or myclobutanil during the early growing season.",
      "Use dormant oil sprays during winter to kill overwintering spores.",
      "Regularly monitor trees and remove infected leaves or fruit."
    ]
  },
  {
    "disease_name": "Apple___Black_rot",
    "description": "Black rot is caused by the fungus Botryosphaeria obtusa, resulting in sunken, black lesions on fruit and cankers on branches. The disease can weaken the tree, reduce fruit quality, and lead to premature defoliation. It is prevalent in warm, humid conditions.",
    "prevention": [
      "Remove and destroy infected fruit, leaves, and branches promptly.",
      "Avoid wounding trees during pruning, as the fungus enters through cuts.",
      "Plant apple varieties with higher resistance to fungal diseases."
    ],
    "treatment": [
      "Spray fungicides like thiophanate-methyl during early stages of infection.",
      "Use lime-sulfur sprays during dormancy to kill fungal spores.",
      "Prune and discard infected branches and cankers."
    ]
  },
  {
    "disease_name": "Apple___Cedar_apple_rust",
    "description": "This disease is caused by the fungus Gymnosporangium juniperi-virginianae and requires both apple and cedar/juniper trees to complete its lifecycle. Symptoms include bright orange or yellow leaf spots and deformed fruit. Severe infections weaken trees and reduce yield.",
    "prevention": [
      "Avoid planting apple trees near cedar or juniper trees.",
      "Remove and destroy galls from nearby cedar trees during winter.",
      "Plant resistant varieties like Freedom or Redfree."
    ],
    "treatment": [
      "Apply fungicides containing myclobutanil or propiconazole during the growing season.",
      "Prune infected areas to reduce the spread of spores.",
      "Ensure proper spacing and pruning to promote airflow."
    ]
  },
  {
    "disease_name": "Apple___healthy",
    "description": "Healthy apple trees show no signs of infection or stress, producing high-quality fruit and lush green leaves. Proper care is essential to maintain tree health.",
    "prevention": [
      "Regularly inspect trees for early signs of disease.",
      "Provide balanced fertilization and adequate watering.",
      "Maintain orchard hygiene by removing debris and dead branches."
    ],
    "treatment": [
      "No treatment required.",
      "Continue routine care and monitoring for early detection of potential problems."
    ]
  },
  {
    "disease_name": "Corn___Cercospora_leaf_spot Gray_leaf_spot",
    "description": "Gray leaf spot is caused by Cercospora zeae-maydis, resulting in rectangular, gray to tan lesions on leaves. It reduces photosynthesis, weakening the plant and significantly reducing yield in severe cases. The disease thrives in warm, humid conditions and spreads via fungal spores from crop debris.",
    "prevention": [
      "Rotate crops with non-host plants like soybeans.",
      "Plant resistant corn hybrids.",
      "Remove infected crop residues by tilling or destroying debris."
    ],
    "treatment": [
      "Apply fungicides such as pyraclostrobin or strobilurin-based products during early symptoms.",
      "Use preventative fungicides in wet and humid conditions.",
      "Monitor fields closely and maintain proper plant spacing for airflow."
    ]
  },
  {
    "disease_name": "Corn___Common_rust",
    "description": "Common rust is caused by the fungus Puccinia sorghi. It appears as small, reddish-brown pustules on both sides of leaves. Under favorable conditions, severe infections can weaken the plant, reducing photosynthetic efficiency and yield. The disease spreads through windborne spores, especially in cool, moist climates.",
    "prevention": [
      "Plant rust-resistant corn hybrids.",
      "Avoid overhead irrigation to reduce moisture on leaves.",
      "Monitor plants during periods of cool, wet weather for early signs."
    ],
    "treatment": [
      "Apply fungicides such as tebuconazole or azoxystrobin at the first sign of infection.",
      "Remove and destroy infected plant parts to prevent further spread.",
      "Ensure proper nutrition to strengthen plant immunity."
    ]
  },
  {
    "disease_name": "Corn___Northern_Leaf_Blight",
    "description": "Northern leaf blight is caused by Exserohilum turcicum, characterized by elongated, gray-green lesions on leaves that later turn brown. The disease thrives in warm, humid environments and can cause substantial yield losses if not managed properly.",
    "prevention": [
      "Plant resistant hybrids to minimize susceptibility.",
      "Rotate crops and avoid planting corn continuously in the same fields.",
      "Remove and destroy crop debris after harvest."
    ],
    "treatment": [
      "Apply fungicides like propiconazole or pyraclostrobin at early stages.",
      "Monitor fields regularly during humid conditions.",
      "Use balanced fertilization to maintain strong plant health."
    ]
  },
  {
    "disease_name": "Corn___healthy",
    "description": "Healthy corn plants are free from disease or stress, with vibrant green leaves, strong stalks, and optimal grain production. Proper management practices ensure high-quality crops.",
    "prevention": [
      "Inspect fields regularly for early signs of disease or stress.",
      "Follow good agricultural practices such as crop rotation, proper fertilization, and irrigation.",
      "Maintain field hygiene by removing plant debris."
    ],
    "treatment": [
      "No treatment required.",
      "Continue regular monitoring and proper management to sustain crop health."
    ]
  },
  {
    "disease_name": "Grape___Black_rot",
    "description": "Black rot, caused by Guignardia bidwellii, manifests as small, circular, brown spots on leaves and black, shriveled fruit. The disease thrives in warm, humid weather and can devastate grape yields if left unmanaged.",
    "prevention": [
      "Plant resistant grape varieties where available.",
      "Prune vines to improve airflow and reduce humidity.",
      "Remove and destroy infected leaves, fruit, and canes promptly."
    ],
    "treatment": [
      "Apply fungicides like myclobutanil or mancozeb during the growing season.",
      "Use dormant sprays to kill overwintering fungal spores.",
      "Maintain proper canopy management to reduce moisture."
    ]
  },
  {
    "disease_name": "Grape___Esca_(Black_Measles)",
    "description": "Esca or black measles is caused by a complex of fungi, including Phaeoacremonium and Phaeomoniella species. Symptoms include dark streaks in wood, leaf spots, and berries with sunken black lesions. It can weaken vines and reduce yield over time.",
    "prevention": [
      "Avoid wounding vines during pruning to minimize fungal entry.",
      "Remove and destroy infected wood and debris.",
      "Ensure proper irrigation to reduce stress on vines."
    ],
    "treatment": [
      "Apply fungicides like benzimidazoles early in the growing season.",
      "Use trunk injections with systemic fungicides in severe cases.",
      "Monitor plants closely for early symptoms."
    ]
  },
  {
    "disease_name": "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "description": "Leaf blight, caused by Isariopsis clavispora, produces brown or reddish spots on leaves. Severe infections cause defoliation, reducing photosynthesis and grape quality.",
    "prevention": [
      "Prune vines to improve ventilation and reduce humidity.",
      "Avoid overhead irrigation to keep leaves dry.",
      "Plant resistant varieties when available."
    ],
    "treatment": [
      "Apply fungicides like mancozeb or copper-based sprays.",
      "Remove infected leaves to prevent the spread of spores.",
      "Monitor fields during wet weather for early detection."
    ]
  },
  {
    "disease_name": "Grape___healthy",
    "description": "Healthy grapevines exhibit strong growth, lush green leaves, and high-quality fruit. Proper vineyard management ensures healthy crops and optimal yield.",
    "prevention": [
      "Conduct regular inspections to detect early signs of disease.",
      "Maintain proper irrigation, fertilization, and pruning practices.",
      "Ensure proper spacing between vines for good airflow."
    ],
    "treatment": [
      "No treatment required.",
      "Continue routine care and monitoring to sustain vineyard health."
    ]
  },
  {
    "disease_name": "Tomato___Bacterial_spot",
    "description": "Bacterial spot is caused by Xanthomonas spp., producing small, water-soaked spots on leaves, stems, and fruits. Over time, the spots turn brown and cause defoliation, reducing fruit quality and yield. The disease thrives in warm, humid conditions and spreads through contaminated seeds, soil, and water splash.",
    "prevention": [
      "Use disease-free seeds and transplants.",
      "Avoid overhead irrigation to reduce water splash.",
      "Practice crop rotation to minimize pathogen persistence in soil."
    ],
    "treatment": [
      "Apply copper-based bactericides during early stages of the disease.",
      "Remove and destroy infected plants and debris.",
      "Improve plant spacing for better air circulation."
    ]
  },
  {
    "disease_name": "Tomato___Early_blight",
    "description": "Early blight is caused by the fungus Alternaria solani, resulting in concentric dark brown lesions on leaves, stems, and fruit. The disease often starts on older leaves and can lead to defoliation, reducing the plant's ability to produce quality fruit.",
    "prevention": [
      "Rotate crops to prevent the buildup of soil-borne fungi.",
      "Use mulch to minimize soil splash and fungal spread.",
      "Choose resistant tomato varieties."
    ],
    "treatment": [
      "Apply fungicides such as chlorothalonil or mancozeb when symptoms appear.",
      "Remove infected leaves and fruit immediately.",
      "Ensure proper fertilization to maintain plant health."
    ]
  },
  {
    "disease_name": "Tomato___Late_blight",
    "description": "Late blight is a devastating disease caused by Phytophthora infestans. It appears as water-soaked lesions on leaves, stems, and fruit that rapidly expand. Under favorable conditions, the disease can destroy an entire crop within days.",
    "prevention": [
      "Plant resistant varieties and avoid planting in low, damp areas.",
      "Ensure proper plant spacing for good airflow.",
      "Remove infected plant debris promptly."
    ],
    "treatment": [
      "Apply fungicides containing chlorothalonil or copper at the first signs of infection.",
      "Use systemic fungicides during wet, cool conditions.",
      "Monitor plants closely and act quickly to remove infected parts."
    ]
  },
  {
    "disease_name": "Tomato___Leaf_Mold",
    "description": "Leaf mold is caused by the fungus Passalora fulva, leading to yellowish spots on the upper side of leaves and gray or brown mold on the underside. The disease thrives in high humidity and can result in significant leaf loss, reducing yields.",
    "prevention": [
      "Improve ventilation in greenhouses or plant areas.",
      "Avoid overhead watering to reduce leaf wetness.",
      "Remove and destroy infected leaves and debris."
    ],
    "treatment": [
      "Apply fungicides like chlorothalonil or mancozeb.",
      "Maintain lower humidity levels through proper irrigation techniques.",
      "Ensure adequate plant spacing for better airflow."
    ]
  },
  {
    "disease_name": "Tomato___Septoria_leaf_spot",
    "description": "This fungal disease, caused by Septoria lycopersici, creates small, circular, water-soaked spots on lower leaves, which eventually turn brown and may cause defoliation. It spreads rapidly under wet and warm conditions.",
    "prevention": [
      "Avoid overhead irrigation to minimize water splash.",
      "Rotate crops and avoid planting tomatoes in the same location each year.",
      "Use disease-resistant varieties where available."
    ],
    "treatment": [
      "Apply fungicides like chlorothalonil or copper sprays at early stages.",
      "Remove and destroy infected plant debris.",
      "Practice proper pruning to improve air circulation."
    ]
  },
  {
    "disease_name": "Tomato___Spider_mites Two-spotted_spider_mite",
    "description": "Spider mites are small pests that suck sap from tomato leaves, causing yellowing, stippling, and webbing. Severe infestations weaken the plant and reduce fruit production.",
    "prevention": [
      "Encourage beneficial insects like ladybugs, which prey on spider mites.",
      "Avoid water stress as it makes plants more susceptible.",
      "Inspect plants regularly for early signs of infestation."
    ],
    "treatment": [
      "Spray plants with insecticidal soap or neem oil.",
      "Use miticides in severe infestations.",
      "Wash leaves with water to dislodge mites and their webs."
    ]
  },
  {
    "disease_name": "Tomato___Target_Spot",
    "description": "Target spot, caused by Corynespora cassiicola, results in concentric lesions on leaves, stems, and fruit. It reduces photosynthetic activity and fruit quality, thriving in warm, moist conditions.",
    "prevention": [
      "Ensure proper plant spacing to improve airflow.",
      "Avoid overhead irrigation and reduce leaf wetness.",
      "Remove infected debris and practice crop rotation."
    ],
    "treatment": [
      "Apply fungicides such as mancozeb or azoxystrobin at the first sign of symptoms.",
      "Remove and destroy infected plant parts.",
      "Monitor fields during humid weather for early detection."
    ]
  },
  {
    "disease_name": "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "description": "This viral disease is transmitted by whiteflies and causes yellowing, upward curling leaves, and stunted growth. It significantly reduces fruit yield and quality.",
    "prevention": [
      "Use whitefly-resistant tomato varieties.",
      "Implement proper whitefly control measures, such as sticky traps.",
      "Cover plants with fine mesh netting to block insect access."
    ],
    "treatment": [
      "Apply insecticides to control whitefly populations.",
      "Remove and destroy infected plants to prevent the spread.",
      "Maintain good field hygiene to reduce virus hosts."
    ]
  },
  {
    "disease_name": "Tomato___Tomato_mosaic_virus",
    "description": "Tomato mosaic virus causes mottled, distorted leaves and stunted growth. Fruits may develop discoloration and poor texture. The virus spreads through contaminated tools, seeds, and touch.",
    "prevention": [
      "Use virus-free seeds and transplants.",
      "Sterilize tools and wash hands after handling plants.",
      "Rotate crops to reduce virus build-up in the soil."
    ],
    "treatment": [
      "Remove and destroy infected plants immediately.",
      "Control weeds and other hosts of the virus.",
      "Use resistant varieties to minimize losses."
    ]
  },
  {
    "disease_name": "Tomato___healthy",
    "description": "The tomato plants are in excellent health, showing no signs of pests or diseases. They are producing high-quality fruit under optimal growing conditions.",
    "prevention": [
      "Follow proper watering, fertilization, and pruning practices.",
      "Inspect plants regularly to identify potential problems early.",
      "Rotate crops and maintain soil health to avoid pathogen buildup."
    ],
    "treatment": [
      "No treatment required.",
      "Continue routine care and monitoring to sustain plant health."
    ]
  }
]

# Step 5: Insert data into the 'disease_info' collection
for disease in disease_data:
    # Check if the disease already exists in the database
    if not disease_collection.find_one({"disease_name": disease["disease_name"]}):
        # Insert the disease data if not found
        disease_collection.insert_one(disease)

    
plant_data=db.plant_info
plant_info=[
  
  {
    "plant_name": "Apple",
    "facts": "Apples are a good source of fiber and vitamin C, making them a healthy snack option. They are one of the most widely cultivated fruits globally, with over 7,500 varieties. The apple tree originated in Central Asia and has been spread and cultivated across the world due to its versatility and health benefits.",
    "image_url": "/static/img/apple.jpg"
  },
  {
    "plant_name": "Corn",
    "facts": "Corn is a staple crop grown widely around the world and is a key ingredient in many foods and products, such as corn syrup and ethanol. This versatile grain comes in various colors, including yellow, white, red, and purple. It has been a fundamental part of diets and industries for centuries, especially in the Americas.",
    "image_url": "/static/img/corn.jpg"
  },
  {
    "plant_name": "Grape",
    "facts": "Grapes are small, juicy fruits that have been cultivated for thousands of years, primarily for consumption and wine production. Rich in antioxidants like resveratrol, grapes are beneficial for heart health. They are available in many varieties, including seedless and seeded, and come in colors like green, red, and purple.",
    "image_url": "/static/img/grapes.jpg"
  },
  {
    "plant_name": "Tomato",
    "facts": "Tomatoes are technically a fruit but are often treated as a vegetable in culinary uses. They are rich in lycopene, a powerful antioxidant linked to numerous health benefits. Native to South America, tomatoes have become a key ingredient in cuisines worldwide and are valued for their vibrant flavor and nutritional content.",
    "image_url": "/static/img/tomato.jpg"
  }
]
for plant in plant_info:
    # Check if the disease already exists in the database
    if not plant_data.find_one({"plant_name": plant["plant_name"]}):
        # Insert the disease data if not found
        plant_data.insert_one(plant)


        