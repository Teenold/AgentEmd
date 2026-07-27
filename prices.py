import requests

BASE_URL = (
    "https://api.petroleumprice.ng/api/v2/prices/depot-prices/preview"
)


def get_prices(product: str, limit: int = 8):

    try:
        response = requests.get(
            BASE_URL,
            params={
                "product": product,
                "limit": limit
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return [
            {
                "station": item.get("depot_name", "Unknown"),
                "price": float(item.get("price", 0))
            }
            for item in data.get("prices", [])
        ]

    except requests.exceptions.Timeout:
        print(f"Timeout while retrieving {product.upper()} prices.")
        return []

    except requests.exceptions.ConnectionError:
        print(f"Connection error while retrieving {product.upper()} prices.")
        return []

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error for {product.upper()}: {e}")
        return []

    except ValueError:
        print(f"Invalid JSON response for {product.upper()}.")
        return []

    except Exception as e:
        print(f"Unexpected error retrieving {product.upper()} prices: {e}")
        return []


def get_pms_prices():
    return get_prices("pms")


def get_ago_prices():
    return get_prices("ago")