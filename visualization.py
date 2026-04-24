import matplotlib.pyplot as plt

# Creating line chart

def create_line_chart(df, base: str, target: str) -> None:
    """Create a line chart showing historical exchange rate trends."""
    plt.figure(figsize=(10, 6))
    plt.plot(df["Date"], df["Rate"], marker="o")

    plt.title(f"Historical Exchange Rate: {base} to {target}")
    plt.xlabel("Date")
    plt.ylabel("Exchange Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Creating comparison bar chart

def create_comparison_bar_chart(df, base: str) -> None:
    """Create a bar chart comparing the base currency to multiple currencies."""
    plt.figure(figsize=(9, 6))
    plt.bar(df["Currency"], df["Converted Value"])

    plt.title(f"Currency Comparison from {base}")
    plt.xlabel("Target Currency")
    plt.ylabel("Converted Value")
    plt.tight_layout()
    plt.show()