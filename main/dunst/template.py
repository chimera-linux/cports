pkgname = "dunst"
pkgver = "1.12.0"
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
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://dunst-project.org"
source = (
    f"https://github.com/dunst-project/dunst/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "217075fa52ac9cd9b87b6dafb094019c4b07a1572259f7bd2adc4fc31771ed95"
env = {"SYSCONFDIR": "/etc"}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "dunst.user")
