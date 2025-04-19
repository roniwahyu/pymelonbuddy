import cv2
import numpy as np
from PIL import Image
import io
import config
from app.services.gemini_service import GeminiService
from app.services.openrouter_service import OpenRouterService

class ImageAnalysisService:
    def __init__(self, ai_service=None):
        self.threshold = config.IMAGE_ANALYSIS_THRESHOLD
        
        # Use the specified AI service or default to Gemini
        if ai_service:
            self.ai_service = ai_service
        elif config.DEFAULT_AI_MODEL.lower() == "gemini":
            self.ai_service = GeminiService()
        else:
            self.ai_service = OpenRouterService()
    
    def analyze_plant_image(self, image_data, prompt=None):
        """Analyze a plant image using computer vision and AI"""
        try:
            # Convert to OpenCV format if needed
            if isinstance(image_data, bytes):
                nparr = np.frombuffer(image_data, np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            elif isinstance(image_data, Image.Image):
                img = cv2.cvtColor(np.array(image_data), cv2.COLOR_RGB2BGR)
            else:
                return {"error": "Unsupported image format"}
            
            # Perform basic image preprocessing
            processed_img = self._preprocess_image(img)
            
            # Extract features (color analysis, etc.)
            features = self._extract_features(processed_img)
            
            # Get AI analysis
            if not prompt:
                prompt = f"""
                Analyze this melon plant image. Consider these extracted features:
                - Green intensity: {features['green_intensity']:.2f}
                - Yellow/brown ratio: {features['yellow_brown_ratio']:.2f}
                - Leaf area estimate: {features['leaf_area_estimate']} pixels
                
                Please provide:
                1. Overall plant health assessment
                2. Identification of any visible diseases or nutrient deficiencies
                3. Growth stage estimation
                4. Specific recommendations for the farmer
                """
            
            # Get AI analysis from the selected service
            ai_analysis = self.ai_service.analyze_image(image_data, prompt)
            
            # Combine computer vision results with AI analysis
            result = {
                "features": features,
                "ai_analysis": ai_analysis
            }
            
            return result
            
        except Exception as e:
            return {"error": f"Error analyzing image: {str(e)}"}
    
    def _preprocess_image(self, img):
        """Preprocess image for analysis"""
        # Resize for consistency
        resized = cv2.resize(img, (800, 600))
        
        # Convert to HSV for better color analysis
        hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
        
        # Apply slight Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(hsv, (5, 5), 0)
        
        return blurred
    
    def _extract_features(self, img):
        """Extract relevant features from the image"""
        # Convert back to BGR for some operations
        bgr = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        
        # Split into channels
        h, s, v = cv2.split(img)
        b, g, r = cv2.split(bgr)
        
        # Calculate green intensity (higher in healthy plants)
        green_intensity = np.mean(g) / (np.mean(r) + np.mean(b) + 1e-5)
        
        # Calculate yellow/brown ratio (higher in stressed plants)
        # Yellow: high R, high G, low B
        yellow_mask = cv2.inRange(bgr, (0, 100, 100), (50, 255, 255))
        yellow_ratio = np.sum(yellow_mask) / (img.shape[0] * img.shape[1])
        
        # Estimate leaf area (green pixels)
        green_mask = cv2.inRange(img, (35, 40, 40), (85, 255, 255))
        leaf_area = np.sum(green_mask > 0)
        
        return {
            "green_intensity": float(green_intensity),
            "yellow_brown_ratio": float(yellow_ratio),
            "leaf_area_estimate": int(leaf_area)
        }