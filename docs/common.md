# Common Role

## Tasks

- Generate locales and unset default locale.
- Install essential packages.
- Set timezone.
- Configure time syncronization with `timesyncd`.
- Create users and fetch their `autorized_keys` form GitHub.
- Clone user's dotfiles to `.dotfiles` directory and execute `make` if available.
- Revoke system access for deactivated users.
- Configure passwordless sudo for members of the `sudo` group.
- Set up OpenSSH server.
- Configure `nftables` rules.

## Variables

| Variable             | Required | Default               | Description                                           |
| -------------------- | -------- | --------------------- | ----------------------------------------------------- |
| `common_locales`     | no       | `[en_US.UTF-8 UTF-8]` | List of locales                                       |
| `common_timezone`    | no       | `Etc/UTC`             | Timezone                                              |
| `common_ntp_servers` | no       | `[]`                  | List of NTP servers                                   |
| `common_users`       | yes      | —                     | See [`common_users` variable](#common_users-variable) |

### `common_users` variable

`common_users` is list of objects with following properties:

| Property           | Required | Default         | Description                                           |
| ------------------ | -------- | --------------- | ----------------------------------------------------- |
| `name`             | yes      | —               | Name of the user                                      |
| `gecos`            | yes      | —               | Description (aka GECOS) of user account               |
| `shell`            | no       | `/bin/bash`     | User's shell                                          |
| `github_name`      | no       | `{{user.name}}` | Github account name. Used to obtain `authorized_keys` |
| `dotfiles_repo`    | no       | `dotfiles`      | Name of repo to clone to `~/.dotfiles` directory      |
| `dotfiles_version` | no       | —               | Version of the dotfiles repository to check out       |
| `sudo`             | no       | `false`         | If `true` user can execute `sudo` command             |
| `active`           | no       | `false`         | If `true` user can login to the system                |
