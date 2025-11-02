from typing import Dict, Any
import requests
import base64
import logging
import time

# Set up logging for better debugging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def create_packshot(
    api_key: str,
    image_data: bytes,
    background_color: str = "#FFFFFF",
    sku: str = None,
    force_rmbg: bool = False,
    content_moderation: bool = False
) -> Dict[str, Any]:
    """
    Create a professional packshot from a product image.
    
    Args:
        api_key: Bria AI API key
        image_data: Image data in bytes
        background_color: Background color in hex format or 'transparent'
        sku: Optional SKU identifier for the product
        force_rmbg: Whether to force background removal even if alpha channel exists
        content_moderation: Whether to enable content moderation
    
    Returns:
        Dict containing the API response
    """
    url = "https://engine.prod.bria-api.com/v1/product/packshot"
    
    # Validate image size (Bria limit: ~12MB)
    image_size_mb = len(image_data) / (1024 * 1024)
    if image_size_mb > 12:
        raise ValueError(f"Image size ({image_size_mb:.2f} MB) exceeds Bria's 12MB limit. Resize the image.")
    
    headers = {
        'api_token': api_key,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    # Base64 encode the image
    image_base64 = base64.b64encode(image_data).decode('utf-8')
    
    # Prepare request data
    data = {
        'file': image_base64,
        'background_color': background_color,
        'force_rmbg': force_rmbg,
        'content_moderation': content_moderation
    }
    
    if sku:
        data['sku'] = sku
    
    # Retry logic for transient 500 errors
    max_retries = 3
    for attempt in range(max_retries):
        try:
            logger.debug(f"Making request to: {url} (attempt {attempt + 1})")
            logger.debug(f"Headers: {headers}")
            logger.debug(f"Data keys: {list(data.keys())}")
            logger.debug(f"Image size: {image_size_mb:.2f} MB")
            
            response = requests.post(url, headers=headers, json=data, timeout=60)
            response.raise_for_status()
            
            logger.debug(f"Response status: {response.status_code}")
            logger.debug(f"Response body: {response.text}")
            
            return response.json()
        
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 500:
                logger.warning(f"500 Internal Server Error on attempt {attempt + 1}. Retrying in {2 ** attempt} seconds...")
                logger.error(f"Full 500 response: Status={e.response.status_code}, Body={e.response.text}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)  # Exponential backoff: 1s, 2s, 4s
                    continue
                else:
                    raise Exception(f"Packshot creation failed after {max_retries} retries: 500 Internal Server Error. Server response: {e.response.text}")
            else:
                raise e
        
        except Exception as e:
            logger.error(f"Unexpected error on attempt {attempt + 1}: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise Exception(f"Packshot creation failed: {str(e)}")

# Example usage (for testing)
if __name__ == "__main__":
    # Test with a sample image (replace with your image bytes)
    sample_image_data = open("test_image.jpg", "rb").read()  # Load a small test image
    result = create_packshot(
        api_key="your_api_key_here",
        image_data=sample_image_data,
        background_color="#FFFFFF"
    )
    print("Success:", result)