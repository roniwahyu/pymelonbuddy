import google.generativeai as genai
import config
from PIL import Image
import io

class GeminiService:
    def __init__(self):
        self.api_key = config.GEMINI_API_KEY
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.vision_model = genai.GenerativeModel('gemini-pro-vision')
        
        # Set up a default system prompt for melon cultivation expertise
        self.system_prompt = """
        You are PyMelonBuddy, an expert assistant for hydroponic melon farmers.
        You provide advice on growing media, irrigation systems, nutrient solutions,
        pest management, and general cultivation practices for melons.
        Your responses should be practical, actionable, and based on horticultural science.
        When uncertain, acknowledge limitations and suggest reliable resources.
        """
    
    def get_response(self, prompt, chat_history=None):
        """Get a text response from Gemini"""
        try:
            if not chat_history:
                chat = self.model.start_chat(history=[])
                chat.send_message(self.system_prompt)
            else:
                chat = self.model.start_chat(history=chat_history)
            
            response = chat.send_message(prompt)
            return response.text
        except Exception as e:
            return f"Error communicating with Gemini API: {str(e)}"
    
    def analyze_image(self, image_data, prompt=None):
        """Analyze an image using Gemini Vision"""
        try:
            if isinstance(image_data, bytes):
                image = Image.open(io.BytesIO(image_data))
            else:
                image = image_data
                
            if not prompt:
                prompt = """
                Analyze this melon plant image. Identify:
                1. Overall plant health
                2. Any visible diseases or deficiencies
                3. Growth stage
                4. Recommendations for the farmer
                """
            
            response = self.vision_model.generate_content([prompt, image])
            return response.text
        except Exception as e:
            return f"Error analyzing image: {str(e)}"