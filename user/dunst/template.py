pkgname = "dunst"
pkgver = "1.13.2"
pkgrel = 0
build_style = "meson"
make_check_target = "test"
make_use_env = True
hostmakedepends = [
    "meson",
    "perl",
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
sha256 = "c68645cecef4a45840cd67c19a18a3a21ecae6b331e9864c2b745c31aee5fc85"
env = {"SYSCONFDIR": "/etc"}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "dunst.user")
