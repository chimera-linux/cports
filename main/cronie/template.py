pkgname = "cronie"
pkgver = "1.7.2"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--enable-anacron",
    "--with-inotify",
    "--with-pam",
    "--without-selinux",
]
hostmakedepends = ["automake", "libtool"]
makedepends = ["linux-pam-devel", "musl-obstack-devel"]
depends = ["cmd:run-parts!debianutils"]
pkgdesc = "Cron daemon"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC AND BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-or-later"
url = "https://github.com/cronie-crond/cronie"
source = f"{url}/releases/download/cronie-{pkgver}/cronie-{pkgver}.tar.gz"
sha256 = "f1da374a15ba7605cf378347f96bc8b678d3d7c0765269c8242cfe5b0789c571"
tool_flags = {"LDFLAGS": ["-lobstack"]}
file_modes = {"usr/bin/crontab": ("root", "root", 0o4755)}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")

    self.install_service(self.files_path / "crond")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

    self.install_file("contrib/anacrontab", "usr/share/cronie")
    self.install_file(self.files_path / "crontab", "usr/share/cronie")

    self.install_file("contrib/0anacron", "usr/share/cronie", mode=0o755)
    self.install_file("contrib/0hourly", "usr/share/cronie")

    self.install_file(self.files_path / "cron.deny", "usr/share/cronie")
    self.install_file(self.files_path / "anacron.default", "usr/share/cronie")

    # new-style pam.d paths
    self.rename("etc/pam.d", "usr/lib/pam.d", relative=False)
