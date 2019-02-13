import argparse
import cv2
import pytesseract as pt
import linkedinUrl
import numpy as np
import pandas as pd
from flask import Flask, render_template ,request, send_from_directory
from flask import jsonify
from flask_cors import CORS
from werkzeug import secure_filename
import os
import pandas as pd
from flask import Markup
# import save_path
import webbrowser