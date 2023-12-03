# **Medi-Flow: Medicinal Plant Flower Identifier**

Medi-Flow is a web application that utilizes transfer learning to identify medicinal plant flowers from user-uploaded images. It employs the powerful DenseNet image classification model to achieve high accuracy in its predictions.

**Features**

* **Plant Identification:** Accurately identifies medicinal plant flowers from images.
* **Transfer Learning:** Leverages transfer learning to optimize the DenseNet model for medicinal plant flower classification.
* **Web Interface:** Provides a user-friendly web interface for uploading images and viewing predictions.

**Requirements**

* Python 3.7 or higher
* TensorFlow 2.x
* Streamlit 0.86 or higher
* OpenCV 4.x or higher
* PIL (Python Imaging Library)

**Installation**

1. Install the required dependencies:
   ```bash
   pip install tensorflow streamlit opencv-python pillow
   ```

2. Clone the project repository:
   ```bash
   git clone https://github.com/majipa007/Medi-Flow-Wiki.git
   ```

3. Navigate to the project directory:
   ```bash
   cd Medi-Flow-Wiki
   ```

**Usage**

1. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open the application in your web browser:
   ```
   http://localhost:8080
   ```

3. Upload an image of a medicinal plant flower using the file uploader.
4. The application will process the image and display the predicted flower name along with its confidence score.
