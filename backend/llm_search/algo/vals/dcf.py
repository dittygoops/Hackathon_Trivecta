import yfinance as yf
import numpy as np
import pandas as pd

def growthrate(stock):
    revenue = stock.financials.loc['Total Revenue'][::-1][-3:]
    rev_list = revenue.values
    gw = []

    if len(rev_list) < 2:
        print("Not enough revenue data for growth calculation.")
        return 0

    for i in range(1, len(rev_list)):
        if rev_list[i - 1] == 0:
            print(f"Warning: Revenue for year {i - 1} is zero, skipping growth calculation.")
            continue
        growth_percent = ((rev_list[i] - rev_list[i - 1]) / rev_list[i - 1]) * 100
        gw.append(growth_percent)

    return sum(gw) / len(gw) if gw else 0

def calc_Cogs(rev, cogs):
    percents = []
    for i in range(len(rev)):
        if rev[i] == 0:
            print(f"Warning: Revenue for year {i} is zero, skipping COGS calculation.")
            continue
        percents.append(cogs[i] / rev[i])

    return sum(percents) / len(percents) if percents else 0

def Profit_Estimations(ticker, forecast_years):
    stock = yf.Ticker(ticker)
    revenue = stock.financials.loc['Total Revenue'][::-1][-3:]
    df = pd.DataFrame([revenue.values], columns=revenue.index, index=["Revenue"])

    stock_growth_rate = growthrate(stock)
    last_revenue = revenue.values[-1]
    future_revenue_dict = {}

    for i in range(1, forecast_years + 1):
        growth_dec = stock_growth_rate / 100
        forecast_rev = last_revenue * (1 + growth_dec)
        year_key = f"Year {2024 + i}"
        future_revenue_dict[year_key] = forecast_rev
        last_revenue = forecast_rev
    
    future_revenue_df = pd.DataFrame(list(future_revenue_dict.values()), columns=["Revenue F"], index=future_revenue_dict.keys())
    combined_df = pd.concat([df, future_revenue_df.T])

    cogs = stock.financials.loc['Cost Of Revenue'][::-1][-3:]
    cogs_df = pd.DataFrame([cogs.values], columns=cogs.index, index=["COGS"])
    combined_df = pd.concat([combined_df, cogs_df])

    r_values = revenue.values
    cogs_values = cogs.values
    CogsPercent = calc_Cogs(r_values, cogs_values)

    last_cogs = cogs_values[-1]
    future_cogs_dict = {}

    for i in range(1, forecast_years + 1):
        forecast_cogs = last_cogs * (1 + (CogsPercent / 100))
        year_key = f"Year {2024 + i}"
        future_cogs_dict[year_key] = forecast_cogs
        last_cogs = forecast_cogs

    future_cogs_df = pd.DataFrame(list(future_cogs_dict.values()), columns=["COGs [Forecast]"], index=future_cogs_dict.keys())
    combined_df = pd.concat([combined_df, future_cogs_df.T])

    combined_df = combined_df.set_axis(['FY 2021', 'FY 2022', 'FY 2023', 'FY 2024', 'FY 2025', 'FY 2026', 'FY 2027', 'FY 2028'], axis=1)
    combined_df.loc['Revenue'] = combined_df.loc['Revenue'].combine_first(combined_df.loc['Revenue F'])
    combined_df.loc['COGS'] = combined_df.loc['COGS'].combine_first(combined_df.loc['COGs [Forecast]'])
    combined_df = combined_df.drop(['COGs [Forecast]', 'Revenue F'], errors='ignore')

    GrossProfit = combined_df.loc['Revenue'] - combined_df.loc['COGS']
    gross_profit_df = pd.DataFrame([GrossProfit.values], columns=GrossProfit.index, index=["Gross Profit"])
    combined_df = pd.concat([combined_df, gross_profit_df])

    return combined_df

def has_minimum_years_of_data(ticker, min_years):
    stock = yf.Ticker(ticker)
    revenue = stock.financials.loc['Total Revenue'][::-1]
    available_revenue_years = revenue.dropna()
    cogs = stock.financials.loc['Cost Of Revenue'][::-1]
    available_cogs_years = cogs.dropna()
    return len(available_revenue_years) >= min_years and len(available_cogs_years) >= min_years

def DCF_Implied_Value(ticker, forecast_years, discount_rate, perpetual_growth_rate):
    stock = yf.Ticker(ticker)

    if not has_minimum_years_of_data(ticker, 3):
        print("Not enough data to perform accurate FCF analysis")
        return None

    combined_df = Profit_Estimations(ticker, forecast_years)
    if combined_df is None or 'Gross Profit' not in combined_df.index:
        print("Gross Profit data unavailable.")
        return None
    
    gross_profit = combined_df.loc['Gross Profit']
    projected_fcf = gross_profit * 0.8  

    fcf_values = projected_fcf[-forecast_years:].values
    discounted_fcfs = []
    for year in range(1, forecast_years + 1):
        discount_factor = (1 + discount_rate) ** year
        discounted_fcfs.append(fcf_values[year - 1] / discount_factor)

    terminal_value = (fcf_values[-1] * (1 + perpetual_growth_rate)) / (discount_rate - perpetual_growth_rate)
    discounted_terminal_value = terminal_value / ((1 + discount_rate) ** forecast_years)
    
    enterprise_value = sum(discounted_fcfs) + discounted_terminal_value

    # Use .get() to avoid KeyError and ensure a default value
    balance_sheet = stock.balance_sheet
    total_debt = balance_sheet.get('Total Debt', 0)  # Default to 0 if not present
    cash = balance_sheet.get('Cash', 0)  # Default to 0 if not present
    
    print(f"Total Debt: {total_debt}, Cash: {cash}")

    # Make sure both total_debt and cash are numbers
    if total_debt is None or cash is None:
        print("Total Debt or Cash is None, returning None.")
        return None

    net_debt = total_debt - cash  # This line might be causing the error

    equity_value = enterprise_value - net_debt
    shares_outstanding = stock.info.get('sharesOutstanding', 0)  # Default to 0 if not present

    if shares_outstanding == 0:
        print("Shares outstanding is zero, cannot calculate implied stock price.")
        return None

    implied_stock_price = equity_value / shares_outstanding

    # print("Discounted Cash Flow (DCF) Analysis")
    # print(f"Implied Stock Price: ${implied_stock_price:.2f}")

    return implied_stock_price

# if __name__ == "__main__":
#     ticker = "COIN"
#     forecast_years = 5
#     discount_rate = 0.1
#     perpetual_growth_rate = 0.02
#     implied_value = DCF_Implied_Value(ticker, forecast_years, discount_rate, perpetual_growth_rate)



# implied_value = DCF_Implied_Value(ticker, forecast_years, discount_rate, perpetual_growth_rate)