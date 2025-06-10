def calculate_discount(product_name):
    """Function to calculate discount based on product name"""
    if product_name == "A":
        return 0.9
    elif product_name == "B":
        return 0.8
    else:
        return 0.95


if __name__ == "__main__":
    print(calculate_discount("A"))  # This runs only when the file is run directly
