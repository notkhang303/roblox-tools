import json
from typing import Any, Dict, List, Union


def parse_roblox_data(data: str) -> Union[Dict[str, Any], List[Any]]:
    """Parse JSON string from Roblox API into Python dict or list."""
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON: {e}")


def format_roblox_data(data: Union[Dict[str, Any], List[Any]]) -> str:
    """Convert Python dict or list back to JSON string for Roblox API."""
    return json.dumps(data, ensure_ascii=False, indent=4)


def get_roblox_asset_id(asset_name: str, assets: List[Dict[str, Any]]) -> Union[int, None]:
    """Retrieve asset ID from a list of assets by name."""
    for asset in assets:
        if asset.get('name') == asset_name:
            return asset.get('id')
    return None


def filter_assets_by_type(assets: List[Dict[str, Any]], asset_type: str) -> List[Dict[str, Any]]:
    """Filter assets by their type (e.g., 'Image', 'Model')."""
    return [asset for asset in assets if asset.get('type') == asset_type]
