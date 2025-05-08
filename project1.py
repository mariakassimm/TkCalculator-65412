import math
from scipy.stats import norm, t


def get_critical_value(confidence_level, df, use_t_distribution):
    """Compute the critical value based on the distribution type."""
    alpha = 1 - confidence_level
    if use_t_distribution:
        return t.ppf(1 - alpha / 2, df)
    else:
        return norm.ppf(1 - alpha / 2)


def calculate_confidence_interval():
    print("\nInferential Statistics – Confidence Interval Estimation for Population Mean")
    print("-----------------------------------------------------------------------\n")

    # Get variable name
    variable_name = input("What is the name of the variable you're analyzing?\n"
                          "(Example: duration of calls, test scores, etc.)\n"
                          "> ").strip()

    # Get sample size category
    n_category = input("\nIs your sample size n less than 30 or greater than or equal to 30?\n"
                       "(Enter 'less' for n < 30, or 'greater' for n ≥ 30)\n"
                       "> ").strip().lower()

    while n_category not in ['less', 'greater']:
        print("Invalid input. Please enter 'less' or 'greater'.")
        n_category = input("> ").strip().lower()

    use_t_distribution = (n_category == 'less')

    # Get numerical inputs
    try:
        x_bar = float(input("\nEnter the sample mean x̄:\n"
                            "(This is the average of your sample data.)\n"
                            "> "))

        s = float(input("\nEnter the sample standard deviation s:\n"
                        "(This measures how spread out your data is.)\n"
                        "> "))

        n = int(input("\nEnter the sample size n:\n"
                      "(How many observations are in your sample?)\n"
                      "> "))

        confidence_percent = float(input("\nEnter the desired confidence level (in percentage, e.g., 95):\n"
                                         "(This determines the range within which the true population mean is expected to lie.)\n"
                                         "> "))

    except ValueError:
        print("\nError: Please enter valid numerical values.")
        return

    # Validate inputs
    if n <= 0:
        print("\nError: Sample size must be positive.")
        return
    if confidence_percent <= 0 or confidence_percent >= 100:
        print("\nError: Confidence level must be between 0 and 100%.")
        return

    confidence_level = confidence_percent / 100
    df = n - 1  # degrees of freedom

    # Calculate critical value
    critical_value = get_critical_value(confidence_level, df, use_t_distribution)

    # Calculate margin of error and confidence interval
    standard_error = s / math.sqrt(n)
    margin_of_error = critical_value * standard_error
    lower_bound = x_bar - margin_of_error
    upper_bound = x_bar + margin_of_error

    # Display results
    print("\n\n=== Confidence Interval Estimation Results ===")
    print(f"Variable analyzed: {variable_name}")
    print(f"Distribution used: {'t-distribution' if use_t_distribution else 'z-distribution'}")
    print(f"Sample mean (x̄): {x_bar:.4f}")
    print(f"Sample standard deviation (s): {s:.4f}")
    print(f"Sample size (n): {n}")
    print(f"Confidence level: {confidence_percent}%")
    print("\nConfidence Interval for Population Mean:")
    print(f"{confidence_percent}% CI = ({lower_bound:.4f}, {upper_bound:.4f})")
    print(f"Margin of Error: ±{margin_of_error:.4f}")
    print("\nInterpretation:")
    print(f"We are {confidence_percent}% confident that the true population mean of {variable_name}")
    print(f"lies between {lower_bound:.4f} and {upper_bound:.4f}.")


if __name__ == "__main__":
    calculate_confidence_interval()