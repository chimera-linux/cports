pkgname = "touchegg"
pkgver = "2.0.17"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DUSE_SYSTEMD=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "cairo-devel",
    "dinit-chimera",
    "glib-devel",
    "gtk+3-devel",
    "libinput-devel",
    "libx11-devel",
    "libxi-devel",
    "libxrandr-devel",
    "libxtst-devel",
    "pugixml-devel",
    "udev-devel",
]
pkgdesc = "Linux multi-touch gesture recognizer"
license = "GPL-3.0-or-later"
url = "https://github.com/JoseExposito/touchegg"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0600c4c57d6c96b6f0a84a56cb4f5d8ce0fa42831bfa0d6cf94ce6a1a23823f8"


def post_install(self):
    self.install_sysusers("^/sysusers.conf")
    self.install_service("^/touchegg")
