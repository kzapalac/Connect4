import numpy as np
import tensorflow as tf
import anvil.server
import os
from dotenv import load_dotenv

# Load environment variable
load_dotenv()

# Connect AWS to Anvil using Uplink key
anvil.server.connect(os.getenv("ANVIL_UPLINK_KEY"))

# Load CNN Model
#cnn_model_path = "/home/bitnami/connect4/best_connect4_cnn.h5"
cnn_model = tf.keras.models.load_model("best_connect4_cnn.h5")

@anvil.server.callable
def test_function():
    return "Backend connection successful!"

@anvil.server.callable
def get_best_cnn_move(board):
    """
    Receives board from Anvil, runs CNN model, and returns the best move"
    """
    try:
        # 

    except Exception as e:
        return f"Error processing board: {str(e)}"

# Keep the script running for Anvil Uplink
anvil.server.wait_forever()
