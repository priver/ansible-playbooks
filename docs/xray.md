# Xray Role

## Tasks

- Install and configure Xray (tag: `xray`).

## Variables

| Variable              | Required | Default     | Description                           |
| --------------------- | -------- | ----------- | ------------------------------------- |
| `xray_version`        | no       | `25.1.30`   | Version of Xray binary                |
| `xray_platform`       | no       | `linux-64`  | Platform of Xray binary               |
| `xray_path`           | no       | `/opt/xray` | Path where Xray will be installed     |
| `xray_uuid`           | yes      | —           | Generate with `/opt/xray/xray uuid`   |
| `xray_x25519_private` | yes      | —           | Generate with `/opt/xray/xray x25519` |
| `xray_x25519_public`  | yes      | —           | Generate with `/opt/xray/xray x25519` |
| `xray_reality_dest`   | yes      | —           | Xray REALITY destination hostname     |
