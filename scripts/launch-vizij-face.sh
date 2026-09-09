#!/bin/bash

# Vizij web project
REPO_DIR="/home/nvidia/sara_vizij/vizij-web"

# URL opened by Firefox
URL="http://localhost:5173"

# Clean up when Ctrl+C or termination happens
cleanup() {
    echo ""
    echo "Stopping tutorial agent face..."
    kill "$DEV_PID" 2>/dev/null || true
    killall firefox 2>/dev/null || true
    exit 0
}

trap cleanup SIGINT SIGTERM

# Stop previous instances
killall firefox 2>/dev/null || true
killall pnpm 2>/dev/null || true
killall node 2>/dev/null || true
sleep 1

echo "Starting tutorial-agent-face..."
cd "$REPO_DIR" || exit 1

pnpm run dev:face-ros4hri-demo --host &
DEV_PID=$!

echo "Waiting for dev server..."

for i in $(seq 1 30); do
    if curl -s -o /dev/null http://localhost:5173; then
        echo "Dev server is ready."
        break
    fi

    if [ "$i" -eq 30 ]; then
        echo "Timed out waiting for dev server."
        kill "$DEV_PID" 2>/dev/null || true
        exit 1
    fi

    sleep 1
done

echo "Disabling on-screen keyboard..."

DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
gsettings set org.gnome.desktop.a11y.applications screen-keyboard-enabled false

echo "Launching Firefox kiosk..."
firefox --kiosk --remote-debugging-port 9222 "$URL" &
echo "ROS4HRI face demo running in kiosk mode."

wait "$DEV_PID"
