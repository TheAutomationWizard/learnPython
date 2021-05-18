def valid_triangle(side1, side2, side3):
    if (side2 + side3 > side1) or (side3 + side1 > side2) or (side1 + side2 > side3):
        print('Triangle is possible.')
        return True
    print('Triangle not possible.')
    return False
