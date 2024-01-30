pkgname = "cronie"
pkgver = "1.7.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-anacron",
    "--with-inotify",
    "--with-pam",
    "--without-selinux",
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "autoconf", "automake"]
makedepends = ["linux-pam-devel", "musl-obstack-devel"]
depends = ["bash", "debianutils"]
pkgdesc = "Cronie cron daemon project"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "ISC AND GPL-2.0-only"
url = "https://github.com/cronie-crond/cronie"
source = f"{url}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "78033100c24413f0c40f93e6138774d6a4f55bc31050567b90db45a2f9f1b954"
tool_flags = {"LDFLAGS": ["-lobstack"]}
suid_files = ["usr/bin/crontab"]
file_modes = {"usr/bin/crontab": ("root", "root", 0o6755)}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")

    # NOTE: Sets '-s': log to syslog instead of mailer by default
    self.install_service(self.files_path / "crond")

    self.install_file(self.files_path / "crontab", "etc")
    self.install_file(self.files_path / "cron-deny", "etc", name="cron.deny")
    self.install_file(
        self.files_path / "default-anacron", "etc/default", name="anacron"
    )

    self.install_file("contrib/0anacron", "etc/cron.hourly")
    self.install_file("contrib/0hourly", "etc/cron.d")
    self.install_file("contrib/anacrontab", "etc")
