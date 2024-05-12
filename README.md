# ShopSmall

Introduction

ShopSmall is a brand new shopping website specifically designed to help marketize small businesses. As we know, running a small business is incredibly difficult and thus owners can’t spend time marketing with billboards as they need to tend their budget elsewhere and take care of the business. Thus ShopSmall is designed to specifically help small businesses and allow them to have an online presence that customers can shop from and view their products and business online. Users can choose to either create an account as a business or a customer. A business user can set up their business profile along with their inventory and product information. Users can choose to search what products they desire and add them to their cart. 

Installation
Steps:
1. **Clone the repository:**
    ```bash
    git clone https://github.com/KunalPradhan1/ShopSmall.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd shopsmall
    ```

3. **Create a virtual environment and activate it:**
   - For Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
   - For Mac/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. **Install Pillow (Python image management library):**
    ```bash
    pip install pillow
    ```
    - For Mac/Linux:
    ```bash
    pip3 install pillow
    ```

5. **Apply migrations and start the development server:**
   - For Windows:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
   - For Mac/Linux:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver
    ```

6. **Access the application:**
   - Visit `http://127.0.0.1:8000/` in your browser.

7. Enjoy


