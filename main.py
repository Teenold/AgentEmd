import json

from prices import get_pms_prices
from prices import get_ago_prices
from news import get_latest_news
from summarizer import summarize_news
from report import build_report

def main():
    try:
        print("Retrieving PMS prices...")
        pms_prices = get_pms_prices()

        print("Retrieving AGO prices...")
        ago_prices = get_ago_prices()

        print("Retrieving news...")
        articles = get_latest_news(limit=5)

        print("Generating summaries...")
        summarized_news = summarize_news(articles)

        print("Generating report...")
        html_report = build_report(
            pms_prices,
            ago_prices,
            summarized_news
        )

        with open("report.html", "w", encoding="utf-8") as f:
            f.write(html_report)

        report = {
            "emailBody": html_report
        }

        with open("report.json", "w", encoding="utf-8") as f:
            json.dump(
                report,
                f,
                indent=2,
                ensure_ascii=False
            )

        print("report.json generated successfully.")

    except Exception as e:
        print(f"Main process failed: {e}")


if __name__ == "__main__":
    main()