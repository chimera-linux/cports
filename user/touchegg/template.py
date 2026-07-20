pkgname = "touchegg"
pkgver = "2.0.18"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DUSE_SYSTEMD=OFF",
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
]
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
sha256 = "7cf0b9239f414d9484495f2a57a28c1c99b3d7a7ae5767d10f0464809ae32e0b"
options = ["etcfiles"]


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_service(self.files_path / "touchegg")
