import requests
from bs4 import BeautifulSoup

NEWS_API_URL = (
    "https://api.petroleumprice.ng/api/v2/news/articles/latest"
)

BASE_ARTICLE_URL = (
    "https://petroleumprice.ng/news/articles/"
)


def get_article_content(article_url: str) -> str:
    """
    Extract the article body from a PetroleumPrice article page.
    """

    try:

        response = requests.get(
            article_url,
            timeout=30
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        article = soup.find("article")

        if not article:

            print(
                f"Article container not found: {article_url}"
            )

            return ""

        return article.get_text(
            separator=" ",
            strip=True
        )

    except requests.exceptions.Timeout:

        print(
            f"Timeout while retrieving article: {article_url}"
        )

        return ""

    except requests.exceptions.ConnectionError:

        print(
            f"Connection error retrieving article: {article_url}"
        )

        return ""

    except requests.exceptions.HTTPError as e:

        print(
            f"HTTP error retrieving article: {e}"
        )

        return ""

    except Exception as e:

        print(
            f"Unexpected error retrieving article: {e}"
        )

        return ""


def get_latest_news(limit: int = 5) -> list:
    """
    Retrieve latest petroleum news and article content.
    """

    try:

        response = requests.get(
            NEWS_API_URL,
            params={"limit": limit},
            timeout=30
        )

        response.raise_for_status()

        articles = response.json()

        results = []

        for article in articles:

            try:

                title = article.get(
                    "title",
                    "Untitled"
                )

                slug = article.get("slug")

                if not slug:
                    continue

                article_url = (
                    BASE_ARTICLE_URL + slug
                )

                content = get_article_content(
                    article_url
                )

                results.append(
                    {
                        "title": title,
                        "content": content,
                        "url": article_url
                    }
                )

            except Exception as e:

                print(
                    f"Error processing article: {e}"
                )

                continue

        return results

    except requests.exceptions.Timeout:

        print(
            "Timeout while retrieving latest news."
        )

        return []

    except requests.exceptions.ConnectionError:

        print(
            "Connection error while retrieving latest news."
        )

        return []

    except requests.exceptions.HTTPError as e:

        print(
            f"HTTP error retrieving latest news: {e}"
        )

        return []

    except ValueError:

        print(
            "Invalid JSON response from news API."
        )

        return []

    except Exception as e:

        print(
            f"Unexpected error retrieving news: {e}"
        )

        return []