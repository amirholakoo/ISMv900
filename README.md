# ISMv900
Inventory and Sales Management in Python using Django and JavaScrips using Vue.JS

## setup project: 
we use python 3.9 and django 4.2

```bach
pip3 install pandas openpyxl jdatetime qrcode channels psycopg2-binary

```

### Step 1: Create a Virtual Environment

To create a virtual environment, open your terminal or command prompt and navigate to the directory where you want to create the virtual environment. Then, run the following command:

```bash
python3 -m venv myenv
```

Replace `myenv` with the name you want to give to your virtual environment. This command creates a new directory with the specified name, which contains the virtual environment.

### Step 2: Activate the Virtual Environment

#### On Windows:

To activate the virtual environment on Windows, run the following command in your terminal:

```cmd
myenv\Scripts\activate
```

Replace `myenv` with the name of your virtual environment.

#### On macOS and Linux:

To activate the virtual environment on macOS or Linux, run the following command in your terminal:

```bash
source myenv/bin/activate
```

Replace `myenv` with the name of your virtual environment.

### Step 3: Verify the Virtual Environment

After activating the virtual environment, your terminal prompt should change to indicate that you are now working inside the virtual environment. It will look something like this:

```bash
(myenv) $
```

This indicates that the virtual environment `myenv` is active.

### Step 4: Install Packages from `requirements.txt`

To install the packages listed in the `requirements.txt` file, you can use the following command:

```bash
pip install -r requirements.txt
```

This command tells `pip` to install all the packages listed in the `requirements.txt` file. It's a convenient way to ensure that your project has all the necessary dependencies installed.


### Step 5: Deactivate the Virtual Environment

When you're done working in the virtual environment, you can deactivate it by running the following command:

```bash
deactivate
```


### Step 6: Run the Django Development Server

Within your project directory, you can start the Django development server by running:

```bash
python manage.py runserver
```

This command starts the Django development server, which by default runs on port 8000.

### Step 7: Access Your Django Project

Open your web browser and navigate to `http://127.0.0.1:8000/`. You should see the default Django welcome page, indicating that your Django project is running successfully.

### Additional Tips

- **Using a Different Port**: If port 8000 is already in use, you can specify a different port by appending it to the `runserver` command, like so: `python manage.py runserver 8080`.
- **Running Migrations**: After creating models in your app, you'll need to create and apply migrations to update your database schema. Run `python manage.py makemigrations` followed by `python manage.py migrate`.



### Step 8: Create the Superuser

Run the following command to create a superuser:

```bash
python manage.py createsuperuser
```

This command will prompt you to enter a username, email address, and password for the superuser. The email address is optional, but it's recommended to provide one.

### Step 9: Follow the Prompts

You'll be asked to enter the username, email (optional), and password for the superuser. Make sure to choose a strong password.

### Step 10: Access the Django Admin Site

After creating the superuser, you can access the Django admin site by running:

```bash
python manage.py runserver
```

Then, open your web browser and navigate to `http://127.0.0.1:8000/admin/`. Log in with the superuser credentials you just created.

