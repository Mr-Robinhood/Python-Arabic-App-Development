
# Guide to Packaging the Reflex App for Android

This guide explains how to package the existing Reflex web application into a native Android application (`.apk` or `.aab` file) that can be installed on Android devices.

We will use a tool called **Capacitor** to wrap the web app. Capacitor is a modern tool that makes it easy to embed web applications inside a native mobile shell.

## The Process Overview

The basic steps are:
1.  **Export the Reflex Frontend**: We will generate a static version of our web application (HTML, CSS, JavaScript).
2.  **Create a Capacitor Project**: We will set up a new Capacitor project and add the Android platform to it.
3.  **Copy Web Assets**: We will move our exported frontend into the Capacitor project.
4.  **Build the Android App**: We will use Android Studio to build the final Android application.

---

## Step-by-Step Instructions

### Step 1: Install Required Tools

Before you begin, make sure you have the following installed on your system:
-   **Node.js and npm**: Required for Capacitor. [Download here](https://nodejs.org/).
-   **Java Development Kit (JDK)**: Required for Android development.
-   **Android Studio**: The official IDE for Android development. [Download here](https://developer.android.com/studio).
    -   During installation, make sure to install the Android SDK and command-line tools.

### Step 2: Export the Reflex Frontend

First, we need to export the user interface of our Reflex app into a static `_static` folder.

1.  Open your terminal in the root directory of this project.
2.  Run the following Reflex command:

    bash
    reflex export --frontend-only
    

    This command will create a `frontend.zip` file. Unzip it. Inside, you will find an `_static` directory. This directory contains the complete web frontend of your application.

### Step 3: Set Up the Capacitor Project

Next, we'll create a new project to house our Android app.

1.  In your terminal, navigate to a directory where you want to create your mobile app project (this can be outside the Reflex project).

2.  Run the following commands to create a new Capacitor project:

    bash
    # Create a new directory for the mobile app and navigate into it
    mkdir smartcloud-mobile && cd smartcloud-mobile

    # Initialize a new npm project
    npm init -y

    # Install the Capacitor CLI
    npm install @capacitor/cli

    # Initialize Capacitor in your project
    npx cap init "Smart Cloud" "com.university.smartcloud"
    
    -   `"Smart Cloud"` is the name of your app.
    -   `"com.university.smartcloud"` is the unique package ID for your app.

3.  Now, add the Android platform to your project:

    bash
    # Install the Capacitor Android library
    npm install @capacitor/android

    # Add the Android platform
    npx cap add android
    

    This will create an `android` directory in your project.

### Step 4: Add Web Assets and Configure

1.  In your Capacitor project (`smartcloud-mobile`), you will see a `www` directory. **Delete this default `www` directory.**

2.  Copy the `_static` folder (which you exported from Reflex in Step 2) into the root of your Capacitor project.

3.  Rename the `_static` folder to `www`.

4.  Open the `capacitor.config.json` file in your Capacitor project and make sure the `webDir` property is set to `"www"`:

    on
    {
      "appId": "com.university.smartcloud",
      "appName": "Smart Cloud",
      "webDir": "www",
      "bundledWebRuntime": false
    }
    

### Step 5: Build and Run in Android Studio

Now you are ready to build the native Android app.

1.  Sync your web assets with the native Android project:

    bash
    npx cap sync
    

2.  Open your project in Android Studio:

    bash
    npx cap open android
    

3.  Android Studio will open and start building your project. This may take a few minutes.

4.  Once the project is loaded and synced, you can run the app on an emulator or a connected Android device.
    -   Select a device from the dropdown menu at the top of Android Studio.
    -   Click the **'Run'** button (the green play icon).

You have now successfully packaged your Reflex web application as a native Android app!

