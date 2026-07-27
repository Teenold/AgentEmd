from transformers import pipeline


# Load once when the module starts
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)


def summarize_article(content: str) -> str:
    """
    Generate a concise fuel market intelligence summary.
    """

    try:

        prompt = f"""
        Fuel Market Intelligence Summary

        Requirements:
        - Focus on the main market-moving event.
        - Include important crude oil price figures.
        - Explain why prices moved.
        - Keep the summary under 3 sentences.

        Article:

        {content[:2000]}
        """

        result = summarizer(
            prompt,
            max_length=130,
            min_length=30,
            do_sample=False
        )

        return result[0]["summary_text"]

    except Exception as e:

        print(
            f"Error generating summary: {e}"
        )

        return "Summary unavailable."


def summarize_news(articles: list) -> list:
    """
    Accepts output from news.py and adds summaries.

    Input:
    [
        {
            'title': ...,
            'content': ...,
            'url': ...
        }
    ]
    """

    summarized_articles = []

    try:

        for article in articles:

            summary = summarize_article(
                article["content"]
            )

            summarized_articles.append(
                {
                    "title": article["title"],
                    "summary": summary,
                    "url": article["url"]
                }
            )

        return summarized_articles

    except Exception as e:

        print(
            f"Error processing article summaries: {e}"
        )

        return []
