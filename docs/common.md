# Common Role

## Tasks

- Configure DNS resolver (tag: `dns`).
- Generate locales and unset default locale (tag: `locales`).
- Configure APT and install essential packages (tag: `packages`).
- Configure time syncronization with `timesyncd` and set timezone (tag: `time`).
- Create users, fetch their `autorized_keys` form GitHub and revoke system
  access for deactivated users; also clone user's dotfiles to `.dotfiles`
  directory and execute `make` if available (tag: `users`).
- Configure passwordless sudo for members of the `sudo` group (tag: `sudo`).
- Set up OpenSSH server (tag: `ssh`).
- Configure `nftables` rules (tag: `firewall`).
- Empty `/etc/sysctl.conf` and create `/etc/sysctl.d/local.conf` for future
  modifications (tag: `sysctl`).

## Variables

| Variable                | Required | Default                        | Description                                           |
| ----------------------- | -------- | ------------------------------ | ----------------------------------------------------- |
| `common_nameservers`    | no       | Cloudflare 1.1.1.1             | List of nameservers                                   |
| `common_search_domains` | no       | `[]`                           | List of additional DNS search domains                 |
| `common_apt_repo_url`   | no       | `http://deb.debian.org/debian` | URL of APT repository                                 |
| `common_locales`        | no       | `[en_US.UTF-8 UTF-8]`          | List of locales                                       |
| `common_ntp_servers`    | no       | `[]`                           | List of NTP servers                                   |
| `common_ssh_port`       | no       | 22                             | SSH server port                                       |
| `common_timezone`       | no       | `Etc/UTC`                      | Timezone                                              |
| `common_users`          | yes      | —                              | See [`common_users` variable](#common_users-variable) |

### `common_users` variable

`common_users` is list of objects with following properties:

| Property           | Required | Default         | Description                                           |
| ------------------ | -------- | --------------- | ----------------------------------------------------- |
| `active`           | no       | `false`         | If `true` user can login to the system                |
| `dotfiles_repo`    | no       | `dotfiles`      | Name of repo to clone to `~/.dotfiles` directory      |
| `dotfiles_version` | no       | —               | Version of the dotfiles repository to check out       |
| `gecos`            | yes      | —               | Description (aka GECOS) of user account               |
| `github_name`      | no       | `{{user.name}}` | Github account name. Used to obtain `authorized_keys` |
| `name`             | yes      | —               | Name of the user                                      |
| `shell`            | no       | `/bin/bash`     | User's shell                                          |
| `sudo`             | no       | `false`         | If `true` user can execute `sudo` command             |
