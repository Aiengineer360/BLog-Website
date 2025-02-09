### Blogging Website Project

#### Project Features

1. **User Features**
   - **User Authentication**
     - **Registration, Login, Logout**: Users can register, log in, and log out securely.
     - **Password Reset Functionality**: Users can reset their password via email.
   - **Post Management**
     - **Create, Edit, and Delete Posts**: Users can create, update, and delete their own posts.
     - **Post Fields**: Posts include the following attributes:
       - Title
       - Content
       - Created Date (automatically generated)
   - **Post Listing and Filtering**
     - **Home View**: Displays a list of all posts.
     - **Filtering**: Users can filter posts by category, tag, or author.
   - **Post Ownership**
     - Users can only edit or delete their own posts. Access control has been implemented to enforce this.
   - **Comment System**
     - **Post Comments**: Users can add comments to posts.
     - **Display Comments**: Comments are displayed below each post.

2. **Templates and Static Files**
   - **Navigation Bar**
     - Links included for:
       - Home
       - Create Post
       - Login
       - Logout
       - Register
     - Displays the username of the logged-in user.
   - **Styling**
     - Custom CSS has been used for a clean and user-friendly layout.

3. **Admin Features**
   - Django Admin panel is configured to manage:
     - Posts
     - Users
     - Comments

4. **Security**
   - **Access Control**: Non-owners are restricted from editing or deleting posts.

#### Project Structure

```
scd_blog/
├── blogging_website/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── media/
│   └── post_images/
├── posts/
│   ├── migrations/
│   │   ├── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/
├── templates/
├── users/
│   ├── migrations/
│   │   ├── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
```

#### Website Architecture

1. **User Interface (UI) Layer**
   - **Templates**: HTML files for rendering the front-end.
     - `base.html`
     - `index.html`
     - `post_detail.html`
     - `user_profile.html`
   - **Static Files**: CSS, JavaScript, and images.
     - `styles.css`
     - `scripts.js`
     - `images/`

2. **Application Layer**
   - **Posts App**
     - **Models**: `Post`, `Comment`, `Category`
     - **Views**: `PostListView`, `PostDetailView`, `PostCreateView`, `PostUpdateView`, `PostDeleteView`
     - **Forms**: `PostForm`, `CommentForm`
     - **URLs**: Define routes for post-related views.
   - **Users App**
     - **Models**: `UserProfile`, `CustomUser`
     - **Views**: `UserRegisterView`, `UserLoginView`, `UserLogoutView`, `UserProfileView`
     - **Forms**: `UserRegisterForm`, `UserProfileForm`
     - **URLs**: Define routes for user-related views.

3. **Data Layer**
   - **Database**: SQLite (default), PostgreSQL, MySQL, etc.
     - Tables: `posts_post`, `posts_comment`, `users_userprofile`, etc.
   - **Media Files**: User-uploaded images and files.
     - `media/post_images/`

4. **Configuration Layer**
   - **Settings**: `settings.py` for project settings.
   - **URLs**: `urls.py` for project-wide URL routing.
   - **WSGI/ASGI**: `wsgi.py` and `asgi.py` for deployment.

5. **Admin Interface**
   - **Admin Panel**: Customizable admin interface for managing posts, users, and comments.
     - `admin.py` in each app.

#### Interaction Flow

1. **User Interaction**: The user interacts with the UI, making requests (e.g., viewing a post, registering).
2. **Request Handling**: The request is routed through `urls.py` to the appropriate view in the `views.py` of the respective app.
3. **Business Logic**: The view processes the request, interacts with models, and performs necessary business logic.
4. **Data Access**: Models interact with the database to fetch or store data.
5. **Response Rendering**: The view renders a template with the context data and sends it back to the user.

#### Steps to Run the Project Locally

1. **Clone the Repository**
   ```bash
   $ git clone <https://github.com/Aiengineer360/BLog-Website>
   $ cd blogging_website
   ```

2. **Set Up a Virtual Environment**
   ```bash
   $ python3 -m venv myenv
   $ source myenv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   $ pip install -r requirements.txt
   ```

4. **Configure Environment Variables (Optional)**
   - Set up environment variables for the following sensitive data:
     - `SECRET_KEY`
     - `EMAIL_HOST_USER`
     - `EMAIL_HOST_PASSWORD`

5. **Apply Database Migrations**
   ```bash
   $ python manage.py migrate
   ```

6. **Create a Superuser for Admin Access**
   ```bash
   $ python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```bash
   $ python manage.py runserver
   ```

8. **Access the Application**
   - Open `http://localhost:8000` in your web browser.

#### Usage Instructions

- **Home Page**: View all posts.
- **User Authentication**: Register, log in, and log out.
- **Post Management**: Create, edit, and delete your own posts.
- **Commenting**: Add comments to posts.
- **Admin Panel**: Manage content at `http://localhost:8000/admin`.

#### Security Recommendations

- **Disable Debug Mode**: Set `DEBUG = False` in `settings.py` for production.
- **Update ALLOWED_HOSTS**: Configure appropriate hostnames in `ALLOWED_HOSTS`.
- **Secure Secret Key**: Use environment variables for the `SECRET_KEY`.
