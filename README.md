# Vizij Ros Face Launcher

ROS 2 launch package for starting the **Vizij face** together with the `vizij_face_bridge` and the Vizij ROS4HRI face demo, so that it is displayed on full-screen using Firefox. 

The launcher:

1. Starts the `vizij_face_bridge` ROS 2 node.
2. Starts the Vizij web development server.
3. Waits for the web server to become available.
4. Disables the GNOME on-screen keyboard.
5. Opens the Vizij web face in Firefox kiosk mode.

The Vizij face provides the web-based robot face and ROS4HRI tutorial functionality described in the [`vizij_face_bridge`](https://github.com/SaraCooperAmun/vizij_face_bridge) package.

---

# Requirements

You need:

* ROS 2
* `vizij_face_bridge`
* `vizij_ros_face_launcher`
* Node.js
* `pnpm`
* Firefox
* `curl`
* `vizij-web`

Both ROS packages and their dependencies should be available in the `src` directory of your ROS 2 workspace:

```text
ros_ws/
└── src/
    ├── communication_skills/
    ├── emojivoice_tts/
    ├── vizij_ros_face_launcher/
    ├── interaction_skills/
    ├── tts_ros/
    └── vizij_face_bridge/
```

The required ROS 2 packages are:

* `communication_skills`
* `emojivoice_tts`
* `vizij_ros_face_launcher`
* `interaction_skills`
* `tts_ros`
* `vizij_face_bridge`

---

# Clone the repositories

Clone all the above repository packages into the `src` directory of your ROS 2 workspace.

```bash
cd ~/your_ros_workspace/src
```

Clone:

```bash
git clone https://github.com/SaraCooperAmun/vizij_face_bridge
git clone https://github.com/SaraCooperAmun/vizij_ros_face_launcher
git clone https://github.com/ros4hri/interaction_skills
git clone https://github.com/ros4hri/communication_skills.git
git clone https://github.com/EMOROBOCARE/coqui_tts
git clone https://github.com/SaraCooperAmun/emojivoice_tts
```

Note: remaining ones will be added here. 

---

# Clone vizij-web

The launcher also requires the **vizij-web** project.

Clone it somewhere on the robot, for example:

```bash
cd ~/sara_vizij
git clone https://github.com/SaraCooperAmun/vizij-web
```


After cloning, the directory should contain the Vizij web project, for example:

```text
~/sara_vizij/
└── vizij-web/
```

---

# Configure the Vizij web path

The launch ``scripts/launch-vizij-face.sh`` currently contains a hardcoded path to the Vizij web project:

```bash
REPO_DIR="/home/nvidia/sara_vizij/vizij-web"
```

**You must change this path** to the location where you cloned `vizij-web`.

For example:

```bash
REPO_DIR="/home/<user>/path/to/vizij-web"
```

Make sure this points to the root directory of the `vizij-web` repository.


---

# Build the ROS workspace

From the root of the ROS workspace:

```bash
cd ~/your_ros_workspace
```

Source ROS 2:

```bash
source /opt/ros/<your_ros_distro>/setup.bash
```

Build the packages:

```bash
colcon build
```

Then source the workspace:

```bash
source install/setup.bash
```

---

# Launch the Vizij face

Once everything is configured, launch the face with:

```bash
ros2 launch vizij_ros_face_launcher vizij_ros_face.launch.py
```

The launcher will:

```text
Start vizij_face_bridge
        ↓
Start vizij-web development server
        ↓
Wait for localhost:5173
        ↓
Disable GNOME on-screen keyboard
        ↓
Open Firefox in kiosk mode
        ↓
Vizij face + ROS4HRI tutorial
```

The Vizij web application is served at:

```text
http://localhost:5173
```

---

# ROS4HRI Face Demo

The launcher starts the following Vizij web command:

```bash
pnpm run dev:demo-ros4hri-face --host
```

This launches the **ROS4HRI face demo** tuned by Sara and based on `vizij-web` apps. 

The demo contains the face functionality and ROS4HRI tutorial behavior described in the [`vizij_face_bridge`](../vizij_face_bridge/README.md) documentation.

The `vizij_face_bridge` provides the connection between ROS 2 and the web face.

For example, ROS 2 commands can be used to control:

* Expressions
* Look At
* TTS / speech synchronization
* Visemes

See the `vizij_face_bridge` README for the available commands and examples.

---

# Firefox kiosk mode

The launcher opens Firefox using:

```bash
firefox --kiosk --remote-debugging-port 9222 http://localhost:5173
```

This displays the Vizij face in fullscreen kiosk mode.

Firefox is also started with remote debugging enabled on port:

```text
9222
```

---

# Stopping the face

Press:

```text
Ctrl+C
```

The launcher will stop the web development server and Firefox.

The cleanup function also terminates existing Firefox, `pnpm`, and Node.js processes before starting a new instance.

---

# Troubleshooting

## vizij-web does not start

Check that the configured `REPO_DIR` points to the correct directory:

```bash
REPO_DIR="/home/<user>/path/to/vizij-web"
```

Then check that the project can be started manually:

```bash
cd /path/to/vizij-web
pnpm run dev:face-ros4hri-demo --host
```

The server should become available at:

```text
http://localhost:5173
```

---

## Dev server timeout

The launcher waits up to approximately 30 seconds for:

```text
http://localhost:5173
```

If the server does not start within this time, the launcher exits.

Check the terminal output from:

```bash
pnpm run dev:face-ros4hri-demo --host
```

for errors.

---

## Firefox does not open

Check that Firefox is installed:

```bash
firefox --version
```

You can also open the page manually:

```text
http://localhost:5173
```

---

## Face does not respond to ROS commands

Make sure the `vizij_face_bridge` is running.

Check:

```bash
ros2 node list
```

You should see:

```text
/vizij_face_bridge
```

Then check the available ROS interfaces:

```bash
ros2 topic list
ros2 action list
ros2 service list
```

For expression, Look At, TTS, and viseme commands, see the `vizij_face_bridge` README.

---

# Developer Notes

## GLB configuration

Currently, the **GLB files are hardcoded inside the `vizij-web` application code**.

This should eventually be made configurable from outside the web application.

A possible future improvement would be to allow the selected GLB/model to be provided through configuration or communicated to `vizij-web`, rather than requiring changes to the web application code.
