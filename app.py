from flask import Flask, request, jsonify
import app as mp
import numpy as np

app = Flask(__name__)

# Initialize MediaPipe Pose model
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5)

@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        # Receive the input image data as JSON
        data = request.get_json()

        # Extract the image data from JSON
        image_data = data['image']

        # Convert the image data back to NumPy array format
        cv_image = np.array(image_data, dtype=np.uint8)
        cv_image = cv_image.reshape((480, 640, 3))  # Reshape to the original image shape

        # Process the image using MediaPipe Pose
        results = pose.process(cv_image)

        # Return the results variable directly as JSON response
        return jsonify(results), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
