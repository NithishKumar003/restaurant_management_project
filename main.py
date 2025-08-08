
def get_menu_items():
    return [
        {"name": "Margherita Pizza", "description": "Classic cheese pizza", "price": 249},
        {"name": "Pasta", "description": "Creamy white sauce pasta", "price":199},
        {"name": "Paneer tikka", "description": "Spicy grilled paneer cubes", "price": 179},
    ]

def display_menu(menu_items):
    print("\n=== Welcome to my tasty restaurant ===\n")
    print("Our Menu: \n")
    for item in menu_items:
        print(f"{item['name']} - Rs{item['price']}")
        print(f" {item['description']}\n")

def main():
    menu = get_menu_items()
    display_menu(menu)

if __name__ == "__main__":
    main()