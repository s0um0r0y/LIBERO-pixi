import os

# Force the headless EGL variables locally before importing robosuite
os.environ["MUJOCO_GL"] = "egl"
os.environ["PYOPENGL_PLATFORM"] = "egl"

print("[1/4] Environment variables set. Importing libraries...")
import robosuite as suite
from robosuite.environments.base import make

print("[2/4] Libraries loaded. Initializing 'Lift' environment...")
env = make(
    'Lift', 
    robots='Panda', 
    has_renderer=False, 
    has_offscreen_renderer=True, 
    use_camera_obs=True
)

print("[3/4] Environment built. Resetting state...")
env.reset()

print("[4/4] SUCCESS: MuJoCo headless rendering is fully operational!")