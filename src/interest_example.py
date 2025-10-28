# Investment variables
principal = 50000
annual_rate = 0.04

df_bool = True  # Set to False to print plain table

# Calculations
per_year = principal * annual_rate
per_3_months = per_year / 4
per_month = per_year / 12
per_day = per_year / 365

# Percentages
pct_year = (per_year / principal) * 100
pct_3_months = (per_3_months / principal) * 100
pct_month = (per_month / principal) * 100
pct_day = (per_day / principal) * 100

if df_bool:
    import pandas as pd

    data = {
        "Time Period": ["Per Year", "Per 3 Months", "Per Month", "Per Day"],
        "Interest Earned": [per_year, per_3_months, per_month, per_day],
        "Percentage Gain (%)": [pct_year, pct_3_months, pct_month, pct_day],
        "Total Value": [
            principal + per_year,
            principal + per_3_months,
            principal + per_month,
            principal + per_day,
        ],
    }

    df = pd.DataFrame(data)
    print(df)

else:
    # Printing table
    print(
        "| Time Period      | Interest Earned | Percentage Gain (%) | Total Value    |"
    )
    print(
        "|------------------|-----------------|----------------------|----------------|"
    )
    print(
        f"| Per Year         | ${per_year:,.2f}      | {pct_year:.2f}%                | ${principal + per_year:,.2f} |"
    )
    print(
        f"| Per 3 Months     | ${per_3_months:,.2f}      | {pct_3_months:.2f}%                | ${principal + per_3_months:,.2f} |"
    )
    print(
        f"| Per Month        | ${per_month:,.2f}      | {pct_month:.2f}%                | ${principal + per_month:,.2f} |"
    )
    print(
        f"| Per Day          | ${per_day:,.2f}      | {pct_day:.3f}%               | ${principal + per_day:,.2f} |"
    )
