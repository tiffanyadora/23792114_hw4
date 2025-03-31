# WildcatWear
### By: Tiffany Adora (23792114)

WildcatWear is an e-commerce website project for selling UA merchandise that uses HTML/CSS for the frontend, JavaScript for dynamic content, and Django for the backend. This project now features dynamic client-side functionalities including real-time searching, product submission, and interactive features.

This is a continuation of the WildcatWear-website project (https://github.com/tiffanyadora/WildcatWear-website).

## New JavaScript Features

For Assignment 4, the following client-side JavaScript features have been implemented:

1. **Live Search with Filtering**
   - Dynamic search results without page refresh
   - Recent searches stored in localStorage
   - Last three searches accessible via search history buttons

2. **Product Submission Form**
   - Admin tools section for adding new products
   - Dynamic product addition to the product feed

3. **Rating System**
   - Interactive star rating that updates the UI
   - Product ratings persist in localStorage

4. **Sorting Options**
   - Sort products by price (low to high, high to low)
   - Sort products by rating (highest rated first)

## Project Structure

```bash
wildcatwear/
├── data/                       # CSV data files
|   ├── product.csv             # Product information (Name, Desc, Price, etc.)
|   ├── visual.content.csv      # Visual content information (ID, Name, File type,etc)
|
├── static/                     # Static Files (CSS, images, JavaScript)
|   ├── css/        
|   |   ├── store.css           # Product page styles
|   |   ├── style.css           # Site-wide style
|   |   ├── utility-styles.css  # Utility classes
|   ├── js/                     # JavaScript files
|   |   ├── search.js           # Live search functionality
|   |   ├── product-form.js     # Product submission logic
|   |   ├── rating.js           # Star rating system
|   |   ├── sorting.js          # Product sorting functionality
|   ├── images/                 # Images assets
|
├── store/                      # Main application
|   ├── migrations/             # Django migrations
|   ├── templates/              # HTML templates
|   |   ├── index.html          # Home page template
|   |   ├── search.html         # Search results template
|   |   ├── store.html          # Product details template
|   |   ├── admin-tools.html    # Admin tools template
|   |
|   ├── templatetags/           # Custom template tags
|   |   ├── custom_filters.py   # Custom filters for template
|   |
|   ├── models.py               # Data Model
|   ├── views.py                # View functions
|   ├── urls.py                 # App URL Routing
|   ├── tests.py                # Test script
|
├── wildcatwear/                # Project configuration
|   ├── settings.py             # Django settings  
|   ├── urls.py                 # Project URL Routing
|   ├── wsgi.py, asgi.py        # WSGI & ASGI config
|
├── manage.py                   # Django management script
├── db.sqlite3                  # SQLite database (not used for CSV-based data)
```

## Installation & Setup

### Prerequisites
- Python 3.9 or higher
- Django (latest version recommended)
- Virtual environment (venv)
- Modern web browser with JavaScript enabled

### How to Set-up

To run this project, please follow the steps below:

1. **Clone the Repository**
    ```
    git clone [repository-url]
    cd wildcatwear
    ```

2. **Set up the virtual environment**
    ```
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Linux/Mac
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install required packages**
    ```
    pip install django
    ```

4. **Collect static files**
    ```
    python manage.py collectstatic
    ```
    **This is very important.** If prompted, type "Yes" to copy all the static files.

5. **Run the development server**
    ```
    python manage.py runserver
    ```

6. **Open the website!**
    Open your browser and go to: http://127.0.0.1:8000/

## Test the Application

### Testing JavaScript Functionality

1. **Live Search Feature**
   - Navigate to any page with the search bar (present in the navigation)
   - Begin typing to see real-time filtered results
   - Submit a search, then refresh the page - notice your last search is pre-filled
   - Search for multiple terms, then check the search history buttons at the top of the search results page

2. **Product Submission**
   - Navigate to the admin tools section (link in the footer)
   - Fill out the product submission form with:
     - Product name
     - Description
     - Price
     - Category
     - Image filename (e.g., "arizona-tshirt.jpg")
   - Submit the form and verify the product appears in the product feed without page refresh

3. **Rating System**
   - Navigate to any product page
   - Click on the stars to rate the product
   - Refresh the page and verify your rating persists
   - Try rating multiple products and verify all ratings are maintained

4. **Sorting Options**
   - On the main product listing page, use the dropdown menu to sort products
   - Try sorting by price (low to high)
   - Try sorting by price (high to low)
   - Try sorting by highest rated first
   - Verify the product order changes accordingly without page refresh

### Original Features Testing

1. **Home Page**
   - Visit http://127.0.0.1:8000/ to see the home page
   - All images and page contents should display correctly

2. **Product Page**
   - Click on any product on the home page in the 'Featured Products' section
   - The product information appears (description, features, price, rating, etc.)
   - Check that visuals load correctly
   - Suggested products at the bottom will display 4 randomized products

3. **Search Page**
   - Use the search in navigation bar to search for products
   - Try searching for:
     - Query: "Arizona" -> Shows all merchandise that includes "Arizona" in the name
     - Query: "  University  of Arizona " (with scattered blank spaces) -> Shows results for "University of Arizona"

### Running Tests

To run the test script, in the project folder:
```
cd store
python tests.py
```

What is tested:
- Fetching all products
- Fetching single product by ID
- Retrieving visuals for a product
- HTML generation for visuals

## JavaScript Implementation Details

- **PapaParse:** The project uses PapaParse to read and parse CSV files directly in the browser
- **localStorage:** Used to store search history and product ratings
- **DOM Manipulation:** All dynamic updates are performed without page refresh
- **Event Listeners:** Used to capture user interactions such as search input, form submission, and product rating

## Acknowledgements
- University of Arizona for brand guidelines
- Font Awesome for icons
- PapaParse for CSV parsing in JavaScript
- All images are used for demonstration purposes only

For any questions or issues, please open a Github issue or contact me at tiffanytjhin@arizona.edu. Thanks! :]
