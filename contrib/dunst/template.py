pkgname = "dunst"
pkgver = "1.11.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
make_use_env = True
hostmakedepends = ["gmake", "perl", "pkgconf", "wayland-progs"]
makedepends = [
    "cairo-devel",
    "dbus-devel",
    "glib-devel",
    "libnotify-devel",
    "linux-headers",
    "libxinerama-devel",
    "libxrandr-devel",
    "libxscrnsaver-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
checkdepends = ["bash", "dbus"]
pkgdesc = "Notification daemon"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://dunst-project.org"
source = (
    f"https://github.com/dunst-project/dunst/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "31c0eb749ca83dab7f5af33beb951c9f9a8451263fcee6cbcf8ba3dedbf2e1f1"
env = {"SYSCONFDIR": "/etc"}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_service(self.files_path / "dunst.user")
