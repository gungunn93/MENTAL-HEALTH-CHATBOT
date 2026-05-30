from google import genai

# Paste your key directly here to test
API_KEY = "AQ.Ab8RN6JiqmaYh1x5KvqL0z8z0X6WYb7Yvc_nf41v_PrljI5jCw"   # paste your actual key here

client = genai.Client(api_key=API_KEY)

try:
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents="Say hello"
    )
    print("✅ SUCCESS:", response.text)
except Exception as e:
    print("❌ ERROR:", e)