# Vizij ROS Face Launcher

ROS 2 launch package for starting the **Vizij face** together with the `vizij_face_bridge` and the Vizij ROS4HRI face demo, displayed full-screen using Firefox.

The launcher:

1. Starts the `vizij_face_bridge` ROS 2 node.
2. Starts the Vizij web development server.
3. Waits for the web server to become available.
4. Disables the GNOME on-screen keyboard.
5. Opens the Vizij web face in Firefox kiosk mode.

The Vizij face provides the web-based robot face and ROS4HRI tutorial functionality described in the `vizij_face_bridge` package.

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

Clone the required repositories into the `src` directory of your ROS 2 workspace:

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

Note: additional required repositories can be added here as needed.

---

# Clone vizij-web

The launcher also requires the **vizij-web** project.

Clone it somewhere on the robot, for example:

```bash
cd ~/sara_vizij

git clone https://github.com/SaraCooperAmun/vizij-web
```

After cloning:

```text
~/sara_vizij/
└── vizij-web/
```

---

# Configure the Vizij web path

The location of the `vizij-web` repository is provided through the `vizij_repo_dir` launch argument.

For example:

```bash
ros2 launch vizij_ros_face_launcher vizij_ros_face.launch.py \
  vizij_repo_dir:=/home/nvidia/sara_vizij/vizij-web
```

This should point to the root directory of the `vizij-web` repository.

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
ros2 launch vizij_ros_face_launcher vizij_ros_face.launch.py \
  vizij_repo_dir:=/home/nvidia/sara_vizij/vizij-web
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

# Configuration

The launcher supports the following arguments:

| Argument         | Description                        | Default          |
| ---------------- | ---------------------------------- | ---------------- |
| `vizij_repo_dir` | Path to the `vizij-web` repository | No default       |
| `face_asset`     | GLB filename                       | `emy.glb`        |
| `robot_ip`       | Robot IP address                   | `192.168.50.201` |

For example:

```bash
ros2 launch vizij_ros_face_launcher vizij_ros_face.launch.py \
  vizij_repo_dir:=/home/nvidia/sara_vizij/vizij-web \
  face_asset:=Quori_Current_Extended.glb \
  robot_ip:=192.168.50.202
```

GLB files should be located in:

```text
demo-ros4hri/public/assets/
```

The browser connects to the robot bridge using:

```text
ws://<robot_ip>:9001
```

---

# Starting without the ROS launcher

The face can also be started directly from the terminal.

This is useful for development and testing.

Go to the `vizij-web` repository:

```bash
cd /home/nvidia/sara_vizij/vizij-web
```

Set the face model:

```bash
export VITE_FACE_ASSET=emy.glb
```

Set the robot WebSocket address:

```bash
export VITE_FACE_WS_URL=ws://192.168.50.201:9001
```

Then start the web application:

```bash
pnpm run dev:demo-ros4hri-face --host
```

The web application will be available at:

```text
http://localhost:5173
```

To use another face or robot:

```bash
export VITE_FACE_ASSET=Quori_Current_Extended.glb
export VITE_FACE_WS_URL=ws://192.168.50.202:9001
```

Then restart the development server.

---

# ROS4HRI Face Demo

The launcher starts the following Vizij web command:

```bash
pnpm run dev:demo-ros4hri-face --host
```

This launches the **ROS4HRI face demo** based on `vizij-web`.

The demo contains the face functionality and ROS4HRI tutorial behavior described in the `vizij_face_bridge` documentation.

The `vizij_face_bridge` provides the connection between ROS 2 and the web face.

ROS 2 commands can be used to control:

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

Check that `vizij_repo_dir` points to the correct directory:

```bash
ros2 launch vizij_ros_face_launcher vizij_ros_face.launch.py \
  vizij_repo_dir:=/path/to/vizij-web
```

You can also test the web application manually:

```bash
cd /path/to/vizij-web

export VITE_FACE_ASSET=emy.glb
export VITE_FACE_WS_URL=ws://192.168.50.201:9001

pnpm run dev:demo-ros4hri-face --host
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
pnpm run dev:demo-ros4hri-face --host
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

Then check the available ROS interfaces:

```bash
ros2 topic list
ros2 action list
ros2 service list
```

For expression, Look At, TTS, and viseme commands, see the `vizij_face_bridge` README.

---

## Face connects to the wrong robot

Check the configured WebSocket address:

```bash
echo $VITE_FACE_WS_URL
```

It should contain the IP address of the robot running `vizij_face_bridge`.

For example:

```text
ws://192.168.50.201:9001
```

If using the ROS launcher, set the robot IP with:

```bash
robot_ip:=192.168.50.201
```

If running manually, set:

```bash
export VITE_FACE_WS_URL=ws://192.168.50.201:9001
```

Then restart the web development server.

---

## Wrong face model is displayed

Check the configured model:

```bash
echo $VITE_FACE_ASSET
```

The selected GLB should exist in:

```text
demo-ros4hri/public/assets/
```

When using the ROS launcher:

```bash
face_asset:=Quori_Current_Extended.glb
```

When running manually:

```bash
export VITE_FACE_ASSET=Quori_Current_Extended.glb
```

Then restart the web development server.

---

# Developer Notes

The face model and robot WebSocket address can be configured without modifying the web application code.

GLB files should be placed in:

```text
demo-ros4hri/public/assets/
```

The ROS launcher passes the selected model and robot IP to the web application through environment variables.
