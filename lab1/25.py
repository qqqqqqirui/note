def numPages(digits):
    total_pages = 0
    current_digits = 1
    remaining_digits = digits
    while remaining_digits > 0:
        digits_on_page = min(remaining_digits, len(str(current_digits)))
        total_pages += digits_on_page
        remaining_digits -= digits_on_page
        current_digits += 1
    return total_pages


print(numPages(13))
print(numPages(21))
print(numPages(192))
print(numPages(1578))
