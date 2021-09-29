def convert_gallons_to_ounces(gallon):
    """
    Functions: convert_gallon_to_ounces
    Description: convert gallons to ounces
    Params:
        gallons (float) - The amoun in gallons
    returns: 
        Float - The amoun in ounces
    """
    return gallon * 128

def convert_gallons_to_litiets(gallons):
    """
    Functions: convert_gallons_to_litiers
    Description: Converts gallons to litiers
    Params:
        gallons (float) - The amount in gallons
    Returns:
        float: The amount in litiers
    """
    return gallons * 3.751

def main():
    starting_number = int(input("How many bottles of milk do you want to start with? "))

    for bottle_count in range(starting_number, 0, -1):
        ounces = convert_gallons_to_ounces(bottle_count)
        litiers = convert_gallons_to_litiets(bottle_count)
        print(f"{bottle_count} gallons ({ounces} oz, {litiers:.2f} litiers) of milk on the wall... ")
    
main()
# print(convert_gallons_to_litiers())