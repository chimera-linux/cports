pkgname = "dunst"
pkgver = "1.13.1"
pkgrel = 0
build_style = "meson"
make_check_target = "test"
make_use_env = True
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "cairo-devel",
    "dbus-devel",
    "dinit-chimera",
    "dinit-dbus",
    "glib-devel",
    "libnotify-devel",
    "libxinerama-devel",
    "libxrandr-devel",
    "libxscrnsaver-devel",
    "linux-headers",
    "pango-devel",
    "turnstile",
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
sha256 = "a578e5c2cdb546187355c710f1aa84c472e6e23828e692fe1cb0ebb9635b11a6"
env = {"SYSCONFDIR": "/etc"}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "dunst.user")
