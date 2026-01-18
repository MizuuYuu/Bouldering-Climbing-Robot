import mujoco
import mujoco.viewer
import numpy as np

model = mujoco.MjModel.from_xml_path("scene.xml")
data = mujoco.MjData(model)

try:
  with mujoco.viewer.launch_passive(model, data) as viewer:
    while viewer.is_running():
      # for i in range (0,16):
      #   if i == 2:
      #     data.ctrl[i] = 0.
      #   elif i == 3:
      #     data.ctrl[i] = 0.
      #   elif i == 6:
      #     data.ctrl[i] = 0.
      #   elif i == 7:
      #     data.ctrl[i] = 0.
      #   elif i == 10:
      #     data.ctrl[i] = 0.785
      #   elif i == 11:
      #     data.ctrl[i] = 1.571
      #   elif i == 13:
      #     data.ctrl[i] = -0.785
      #   elif i == 14:
      #     data.ctrl[i] = -1.571
      #   else:
      #     data.ctrl[i] = 0
      mujoco.mj_step(model, data)
      viewer.sync()

except KeyboardInterrupt:
  viewer.close()