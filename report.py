from datetime import datetime

def get_report_period():
    
    current_hour = datetime.now().hour
    
    if current_hour < 12:
        return "Morning"
        
    elif current_hour < 15:
        return "Afternoon"
        
    else:
        return "Evening"


def get_greeting():
    
    current_hour = datetime.now().hour
    
    if current_hour < 12:
        return "Good morning Sir,"
        
    elif current_hour < 15:
        return "Good afternoon Sir,"
        
    else:
        return "Good evening Sir,"


def build_price_table(title, prices):

    try:

        average_price = (
            sum(item["price"] for item in prices)
            / len(prices)
        )

        rows = ""

        for item in prices:

            rows += f"""
            <tr>
                <td>{item['depot']}</td>
                <td>₦{item['price']:,.2f}</td>
            </tr>
            """

        return f"""
        <h2 style="color:#d42e12;">
            {title}
        </h2>

        <div
            style="
                background:#fad5a1;
                padding:12px;
                border-left:5px solid #f28e05;
                margin-bottom:10px;
                font-size:16px;
                font-weight:bold;
            "
        >
            Average {title}: ₦{average_price:,.2f}/L
        </div>

        <table
            width="100%"
            cellspacing="0"
            cellpadding="10"
            style="
                border-collapse:collapse;
                border:1px solid #ddd;
            "
        >

            <tr style="background:#d42e12;color:white;">
                <th align="left">Station</th>
                <th align="left">Price</th>
            </tr>

            {rows}

        </table>

        <br>
        """

    except Exception as e:

        print(
            f"Error building {title} table: {e}"
        )

        return f"""
        <h2>{title}</h2>
        <p>Price data unavailable.</p>
        """

def build_news_section(news_items):

    try:

        html = """
        <h2 style="color:#d42e12;">
            Market News
        </h2>
        """

        for item in news_items:

            html += f"""
            <div
                style="
                    border:1px solid #fad5a1;
                    padding:15px;
                    margin-bottom:15px;
                    border-radius:8px;
                    
                "
            >

                <h3>
                    {item['title']}
                </h3>

                <p>
                    {item['summary']}
                </p>

                <a
                    href="{item['url']}"
                    target="_blank"
                    style="
                        color:#d42e12;
                        font-weight:bold;
                        text-decoration:none;
                    "
                >
                    Full Article →
                </a>

            </div>
            """

        return html

    except Exception as e:

        print(
            f"Error building news section: {e}"
        )

        return """
        <h2 style="color:#d42e12;">
            Market News
        </h2>

        <p>
            News data unavailable.
        </p>
        """
    
def build_report(pms_prices, ago_prices, news_items):
    
    try:

        current_date = datetime.now().strftime(
            "%d %B %Y"
        )
        report_period = get_report_period()

        greeting = get_greeting()

        html = f"""
        <html>

        <body
            style="
                font-family:Segoe UI, Arial, sans-serif;
                margin:20px;
            "
        >

            <div
                style="
                    background:#d42e12;
                    color:white;
                    padding:15px;
                    border-radius:8px;
                "
            >


               <h1 style="margin:0;">
                    Fuel Market Intelligence {report_period} Report
                </h1>

                <p style="margin:5px 0 0 0;">
                    {current_date}
                </p>

            </div>

            <p
                style="
                    font-size:16px;
                    margin-top:20px;
                    margin-bottom:20px;
                "
            >
                {greeting}
                <br><br>
                
                Here is today's fuel market intelligence report highlighting
                the latest PMS and AGO depot prices together with key industry
                developments and market news.
            </p>

            <br>

            {build_price_table(
                "PMS Prices",
                pms_prices
            )}

            {build_price_table(
                "AGO Prices",
                ago_prices
            )}

            {build_news_section(
                news_items
            )}

        </body>

        </html>
        """

        return html

    except Exception as e:

        print(
            f"Error building report: {e}"
        )

        return f"""
        <html>

        <body>

            <h1>
                Fuel Market Intelligence Report
            </h1>

            <p>
                Report generation failed.
            </p>

            <p>
                Error: {e}
            </p>

        </body>

        </html>
        """


