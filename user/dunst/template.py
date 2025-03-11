pkgname = "dunst"
pkgver = "1.12.2"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
make_use_env = True
hostmakedepends = ["perl", "pkgconf", "wayland-progs"]
makedepends = [
    "cairo-devel",
    "dbus-devel",
    "glib-devel",
    "libnotify-devel",
    "libxinerama-devel",
    "libxrandr-devel",
    "libxscrnsaver-devel",
    "linux-headers",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
checkdepends = ["bash", "dbus"]
depends = ["dinit-dbus"]
pkgdesc = "Notification daemon"
license = "BSD-3-Clause"
url = "https://dunst-project.org"
source = (
    f"https://github.com/dunst-project/dunst/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "8f7664bd4e6083e9604e282145fe5b8dee7655fa0b099a5b682a2549e1f33d32"
env = {"SYSCONFDIR": "/etc"}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "dunst.user")
