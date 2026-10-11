import datetime

# Video Path
VIDEO_CONFIG = {
	"VIDEO_CAP" : r"assets\videoplayback.mp4",
	"IS_CAM" : False,
	"CAM_APPROX_FPS": 30,
	"HIGH_CAM": False,
	"START_TIME": datetime.datetime(2020, 11, 5, 0, 0, 0, 0)
}

# Load YOLOv3-tiny weights and config
YOLO_CONFIG = {
	"WEIGHTS_PATH" : "YOLOv4-tiny/yolov4-tiny.weights",
	"CONFIG_PATH" : "YOLOv4-tiny/yolov4-tiny.cfg"
}

# Show individuals detected
SHOW_PROCESSING_OUTPUT = True
# Show individuals detected
SHOW_DETECT = True
# Data record
DATA_RECORD = True
# Data record rate (data record per frame)
DATA_RECORD_RATE = 5
# Check for restricted entry
RE_CHECK = False
# Restricted entry time (H:M:S)
RE_START_TIME = datetime.time(0,0,0) 
RE_END_TIME = datetime.time(23,0,0)
# Check for social distance violation
SD_CHECK = True  # CHANGED: Enable to see violations in your crowd video
# Show violation count
SHOW_VIOLATION_COUNT = True  # CHANGED: Enable to see violation counts
# Show tracking id
SHOW_TRACKING_ID = True  # CHANGED: Enable to see tracking IDs
# Threshold for distance violation
SOCIAL_DISTANCE = 100  # CHANGED: Increased for better detection in crowds
# Check for abnormal crowd activity
ABNORMAL_CHECK = True
# Min number of people to check for abnormal
ABNORMAL_MIN_PEOPLE = 3  # CHANGED: Lowered threshold
# Abnormal energy level threshold
ABNORMAL_ENERGY = 1000  # CHANGED: Lowered for better sensitivity
# Abnormal activity ratio threshold
ABNORMAL_THRESH = 0.3  # CHANGED: Lowered for better detection
# Threshold for human detection minimum confidence
MIN_CONF = 0.15  # CHANGED: Lowered from 0.3 to 0.15 for better detection
# Threshold for Non-maxima suppression
NMS_THRESH = 0.4  # CHANGED: Increased from 0.2 to 0.4 for better box filtering
# Resize frame for processing
FRAME_SIZE = 640  # CHANGED: Reduced from 1080 to 640 for better performance
# Tracker max missing age before removing (seconds)
TRACK_MAX_AGE = 3
# ADD these to the bottom of your existing config.py

# DeepSORT tracker tuning (dense crowd settings)
DS_MAX_COSINE_DISTANCE = 0.5    # was 0.7 in main.py — tighter = more accurate
DS_NN_BUDGET = 200              # was None — limits memory, improves speed
DS_N_INIT = 1                   # tracks confirmed after 1 frame (default 3 is too slow)
DS_MAX_IOU_DISTANCE = 0.9       # allow more overlap in crowd

# Crowd count display stabilization
CROWD_BUFFER_SIZE = 15          # frames to average over (~0.5s at 30fps)

# Large video dataset export
SAMPLE_EVERY_N_FRAMES = 5       # skip frames for speed on large videos