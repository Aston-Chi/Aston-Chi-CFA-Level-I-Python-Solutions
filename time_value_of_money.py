# CFA Level I - Time Value of Money Problems
# Author: Chi Binwei (Aston Chi)

def future_value(present_value, rate, periods):
    """
    Calculate Future Value using compound interest
    FV = PV * (1 + r)^n
    """
    return present_value * (1 + rate) ** periods

def present_value(future_value, rate, periods):
    """
    Calculate Present Value
    PV = FV / (1 + r)^n
    """
    return future_value / (1 + rate) ** periods

def calculate_effective_rate(nominal_rate, compounding_frequency):
    """
    Calculate Effective Annual Rate
    EAR = (1 + r/m)^m - 1
    """
    return (1 + nominal_rate/compounding_frequency) ** compounding_frequency - 1

# Example Problems from CFA Level I Practice

# Problem 1: Future Value Calculation
print("=== CFA Problem 1: Future Value ===")
pv = 10000  # $10,000 initial investment
rate = 0.08  # 8% annual interest
years = 5   # 5 years

fv = future_value(pv, rate, years)
print(f"Initial Investment: ${pv:,.2f}")
print(f"Interest Rate: {rate:.1%}")
print(f"Time Period: {years} years")
print(f"Future Value: ${fv:,.2f}")
print()

# Problem 2: Present Value Calculation
print("=== CFA Problem 2: Present Value ===")
fv_target = 50000  # Need $50,000 in future
rate = 0.06        # 6% discount rate
years = 10         # 10 years from now

pv_needed = present_value(fv_target, rate, years)
print(f"Future Value Needed: ${fv_target:,.2f}")
print(f"Discount Rate: {rate:.1%}")
print(f"Time Period: {years} years")
print(f"Present Value Required: ${pv_needed:,.2f}")
print()

# Problem 3: Effective Annual Rate
print("=== CFA Problem 3: Effective Annual Rate ===")
nominal = 0.12      # 12% nominal rate
monthly_comp = 12   # Monthly compounding

ear = calculate_effective_rate(nominal, monthly_comp)
print(f"Nominal Rate: {nominal:.1%}")
print(f"Compounding Frequency: {monthly_comp} times per year")
print(f"Effective Annual Rate: {ear:.4%}")
