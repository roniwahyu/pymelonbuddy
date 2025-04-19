import requests
import json
import config
from PIL import Image
import base64
import io

class OpenRouterService:
    def __init__(self):
        self.api_key = config.OPENROUTER_API_KEY
        self.base_url = "https://openrouter.ai/api/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        # Set up a default system prompt for melon cultivation expertise
        self.system_prompt = """
        You are PyMelonBuddy, an expert assistant for hydroponic melon farmers.
        You provide advice on growing media, irrigation systems, nutrient solutions,
        pest management, and general cultivation practices for melons.
        Your responses should be practical, actionable, and based on horticultural science.
        When uncertain, acknowledge limitations and suggest reliable resources.
        """
    
    def get_response(self, prompt, model="anthropic/claude-3-opus", temperature=0.7, max_tokens=1000):
        """Get a text response from OpenRouter API"""
        try:
            url = f"{self.base_url}/chat/completions"
            
            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                "temperature": temperature,
                "max_tokens": max_tokens
            }
            
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            return result["choices"][0]["message"]["content"]
        
        except Exception as e:
            return f"Error communicating with OpenRouter API: {str(e)}"
    
    def analyze_image(self, image_data, prompt=None, model="openai/gpt-4-vision"):
        """Analyze an image using OpenRouter Vision models"""
        try:
            if isinstance(image_data, bytes):
                # Convert bytes to base64
                base64_image = base64.b64encode(image_data).decode('utf-8')
            elif isinstance(image_data, Image.Image):
                # Convert PIL Image to base64
                buffer = io.BytesIO()
                image_data.save(buffer, format="JPEG")
                base64_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
            else:
                return "Unsupported image format"
                
            if not prompt:
                prompt = """
                Analyze this melon plant image. Identify:
                1. Overall plant health
                2. Any visible diseases or deficiencies
                3. Growth stage
                4. Recommendations for the farmer
                """
            
            url = f"{self.base_url}/chat/completions"
            
            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                    ]}
                ]
            }
            
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            result = response.json()
            return result["choices"][0]["message"]["content"]
        
        except Exception as e:
            return f"Error analyzing image: {str(e)}"