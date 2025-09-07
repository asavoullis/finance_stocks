import matplotlib.pyplot as plt
import numpy as np

# Create a range of stock prices
S = np.linspace(0, 200, 500)

# Define strike price and premium for examples
K = 100  # strike price
premium_call = 10
premium_put = 8

# Payoff functions
# Long call: max(S - K, 0) - premium
long_call = np.maximum(S - K, 0) - premium_call

# Short call: -long_call
short_call = -long_call

# Long put: max(K - S, 0) - premium
long_put = np.maximum(K - S, 0) - premium_put

# Short put: -long_put
short_put = -long_put

# Plotting
strategies = {
    "Long Call": long_call,
    "Short Call": short_call,
    "Long Put": long_put,
    "Short Put": short_put,
}

for name, payoff in strategies.items():
    plt.figure(figsize=(6, 4))
    plt.plot(S, payoff, label=f"{name} payoff", linewidth=2)
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(K, color="red", linestyle="--", label="Strike Price")
    plt.title(f"Payoff Diagram: {name}")
    plt.xlabel("Stock Price at Expiration (S)")
    plt.ylabel("Profit / Loss")
    plt.legend()
    plt.grid(True)
    plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Create a range of stock prices
S = np.linspace(0, 200, 500)

# Define strike price and premium for examples
K = 100  # strike price
premium_call = 10
premium_put = 8

# Payoff functions
# Long call: max(S - K, 0) - premium
long_call = np.maximum(S - K, 0) - premium_call

# Short call: -long_call
short_call = -long_call

# Long put: max(K - S, 0) - premium
long_put = np.maximum(K - S, 0) - premium_put

# Short put: -long_put
short_put = -long_put

# Plotting
strategies = {
    "Long Call": long_call,
    "Short Call": short_call,
    "Long Put": long_put,
    "Short Put": short_put,
}

for name, payoff in strategies.items():
    plt.figure(figsize=(6, 4))
    plt.plot(S, payoff, label=f"{name} payoff", linewidth=2)
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(K, color="red", linestyle="--", label="Strike Price")
    plt.title(f"Payoff Diagram: {name}")
    plt.xlabel("Stock Price at Expiration (S)")
    plt.ylabel("Profit / Loss")
    plt.legend()
    plt.grid(True)
    plt.show()
