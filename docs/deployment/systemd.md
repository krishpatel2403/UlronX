# systemd Service (Linux)

ULTRONX includes a systemd unit file for running the API server as a managed background service on Linux. This provides automatic startup on boot, crash recovery, and integration with standard Linux service management tools.

## Prerequisites

Before installing the service, ensure that:

1. ULTRONX is installed in a virtual environment at `/opt/ULTRONX/.venv` (or adjust paths accordingly).
2. A dedicated `ULTRONX` system user exists (recommended for security).
3. An inference engine (such as Ollama) is running and accessible.

Create the user and installation directory:

```bash
sudo useradd --system --create-home --home-dir /opt/ULTRONX ULTRONX
sudo -u ULTRONX python3 -m venv /opt/ULTRONX/.venv
sudo -u ULTRONX git clone https://github.com/ultronx/ULTRONX.git /opt/ULTRONX/ULTRONX
cd /opt/ULTRONX/ULTRONX && sudo -u ULTRONX uv sync --extra server
```

## Installing the Service

The unit binds `0.0.0.0`, so an **API key is required** — and the unit
declares `EnvironmentFile=/etc/ULTRONX/env` (no `-` prefix), so it will
**fail to start** until that file exists with a key. Create it first:

```bash
sudo mkdir -p /etc/ULTRONX
echo "ULTRONX_API_KEY=$(jarvis auth generate-key)" | sudo tee /etc/ULTRONX/env
sudo chmod 600 /etc/ULTRONX/env
```

Then copy the unit file, reload the daemon, and enable the service:

```bash
sudo cp deploy/systemd/ULTRONX.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable ULTRONX
sudo systemctl start ULTRONX
```

Clients must send `Authorization: Bearer <key>` on `/v1/*` and `/api/*`
requests. (If you instead bind to `127.0.0.1`, the key is optional and you
can drop the `EnvironmentFile` line.)

Verify it is running:

```bash
sudo systemctl status ULTRONX
```

## Service File Reference

The provided unit file at `deploy/systemd/ULTRONX.service`:

```ini
[Unit]
Description=ULTRONX API Server
After=network.target

[Service]
Type=simple
User=ULTRONX
WorkingDirectory=/opt/ULTRONX
ExecStart=/opt/ULTRONX/.venv/bin/jarvis serve --host 0.0.0.0 --port 8000
Restart=on-failure
RestartSec=5
Environment=HOME=/opt/ULTRONX

[Install]
WantedBy=multi-user.target
```

### `[Unit]` Section

| Directive     | Value              | Description                                                                 |
|---------------|--------------------|-----------------------------------------------------------------------------|
| `Description` | `ULTRONX API Server` | Human-readable name shown in `systemctl status` and logs.              |
| `After`       | `network.target`   | Delays startup until the network stack is available, since the server binds to a network socket and may need to reach a remote engine. |

### `[Service]` Section

| Directive          | Value                                                              | Description                                                                                     |
|--------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `Type`             | `simple`                                                           | The process started by `ExecStart` is the main service process. systemd considers the service started immediately. |
| `User`             | `ULTRONX`                                                       | Runs the server as the `ULTRONX` user rather than root, limiting the blast radius of any security issue. |
| `WorkingDirectory` | `/opt/ULTRONX`                                                  | Sets the working directory for the process. This is where ULTRONX looks for local files and writes data. |
| `ExecStart`        | `/opt/ULTRONX/.venv/bin/jarvis serve --host 0.0.0.0 --port 8000` | The command to start the server. Uses the full path to the `jarvis` binary inside the virtual environment. |
| `Restart`          | `on-failure`                                                       | Automatically restarts the service if it exits with a non-zero exit code. Does not restart on clean shutdown (`systemctl stop`). |
| `RestartSec`       | `5`                                                                | Waits 5 seconds before attempting a restart, preventing rapid restart loops if the service crashes immediately on startup. |
| `Environment`      | `HOME=/opt/ULTRONX`                                             | Sets the `HOME` environment variable so ULTRONX finds its configuration at `~/.ULTRONX/config.toml` (resolving to `/opt/ULTRONX/.ULTRONX/config.toml`). |

### `[Install]` Section

| Directive    | Value               | Description                                                                                 |
|--------------|---------------------|---------------------------------------------------------------------------------------------|
| `WantedBy`   | `multi-user.target` | The service starts when the system reaches multi-user mode (standard boot target for servers). `systemctl enable` creates a symlink under this target. |

## Configuration Options

### Changing the Bind Address and Port

Edit the `ExecStart` line to change the host or port:

```ini
ExecStart=/opt/ULTRONX/.venv/bin/jarvis serve --host 127.0.0.1 --port 9000
```

!!! tip
    Binding to `127.0.0.1` restricts access to localhost only. Use this when running behind a reverse proxy like Nginx or Caddy.

### Setting the Engine and Model

Pass additional flags to `jarvis serve`:

```ini
ExecStart=/opt/ULTRONX/.venv/bin/jarvis serve --host 0.0.0.0 --port 8000 --engine ollama --model qwen3:8b
```

### Adding Environment Variables

Add multiple `Environment` directives or use `EnvironmentFile` for complex configurations:

```ini
[Service]
Environment=HOME=/opt/ULTRONX
Environment=ULTRONX_ENGINE_DEFAULT=vllm
Environment=ULTRONX_OLLAMA_HOST=http://localhost:11434
```

Or load from a file:

```ini
[Service]
EnvironmentFile=/opt/ULTRONX/.env
```

### Changing the User

If you prefer a different service user, update both the `User` directive and the paths:

```ini
[Service]
User=myuser
WorkingDirectory=/home/myuser/ULTRONX
ExecStart=/home/myuser/ULTRONX/.venv/bin/jarvis serve --host 0.0.0.0 --port 8000
Environment=HOME=/home/myuser/ULTRONX
```

### Using a Configuration File

Ensure the configuration file exists at the path where `HOME` points:

```bash
sudo -u ULTRONX mkdir -p /opt/ULTRONX/.ULTRONX
sudo -u ULTRONX cp config.toml /opt/ULTRONX/.ULTRONX/config.toml
```

The server reads `~/.ULTRONX/config.toml` on startup, where `~` resolves from the `HOME` environment variable.

## Viewing Logs

ULTRONX logs are captured by journald. View them with `journalctl`:

```bash
# View all logs for the service
sudo journalctl -u ULTRONX

# Follow logs in real time
sudo journalctl -u ULTRONX -f

# View logs since the last boot
sudo journalctl -u ULTRONX -b

# View logs from the last hour
sudo journalctl -u ULTRONX --since "1 hour ago"

# View only error-level messages
sudo journalctl -u ULTRONX -p err
```

## Managing the Service

### Start, Stop, and Restart

```bash
# Start the service
sudo systemctl start ULTRONX

# Stop the service
sudo systemctl stop ULTRONX

# Restart the service (stop + start)
sudo systemctl restart ULTRONX

# Reload configuration without full restart (sends SIGHUP)
sudo systemctl reload-or-restart ULTRONX
```

### Check Status

```bash
sudo systemctl status ULTRONX
```

Example output:

```
● ULTRONX.service - ULTRONX API Server
     Loaded: loaded (/etc/systemd/system/ULTRONX.service; enabled; preset: enabled)
     Active: active (running) since Fri 2026-02-21 10:00:00 UTC; 2h ago
   Main PID: 12345 (jarvis)
      Tasks: 4 (limit: 4915)
     Memory: 256.0M
        CPU: 1min 23s
     CGroup: /system.slice/ULTRONX.service
             └─12345 /opt/ULTRONX/.venv/bin/python /opt/ULTRONX/.venv/bin/jarvis serve --host 0.0.0.0 --port 8000
```

### Enable and Disable on Boot

```bash
# Enable automatic start on boot
sudo systemctl enable ULTRONX

# Disable automatic start on boot
sudo systemctl disable ULTRONX
```

### Apply Changes After Editing the Unit File

After modifying `/etc/systemd/system/ULTRONX.service`, reload the systemd daemon and restart the service:

```bash
sudo systemctl daemon-reload
sudo systemctl restart ULTRONX
```

## Running Alongside Ollama

If Ollama is also managed via systemd, you can add an ordering dependency so the ULTRONX service waits for Ollama to start:

```ini
[Unit]
Description=ULTRONX API Server
After=network.target ollama.service
Requires=ollama.service
```

| Directive  | Description                                                              |
|------------|--------------------------------------------------------------------------|
| `After`    | Ensures ULTRONX starts after Ollama.                                  |
| `Requires` | If Ollama fails to start, ULTRONX will not start either.              |

!!! note
    Use `Wants` instead of `Requires` if you want ULTRONX to start even when Ollama is unavailable (for example, if you plan to start Ollama manually later).
