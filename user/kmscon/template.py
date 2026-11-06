pkgname = "kmscon"
pkgver = "10.1.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dlibseat=enabled"]
hostmakedepends = [
    "docbook-xsl-nons",
    "libxslt-progs",
    "meson",
    "ncurses",
    "pkgconf",
]
makedepends = [
    "check-devel",
    "dbus-devel",
    "dinit-chimera",
    "freetype-devel",
    "libdrm-devel",
    "libseat-devel",
    "libtsm-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "pango-devel",
    "udev-devel",
]
checkdepends = ["fonts-dejavu"]
pkgdesc = "Linux KMS/DRM virtual console terminal emulator"
license = "MIT"
url = "https://github.com/kmscon/kmscon"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0459d111eb9a12d7b8981492957043b5326a6ee91b7351575f8fd402d745eeb3"
options = ["etcfiles"]


def post_install(self):
    self.install_license("COPYING")
    self.rename("etc/kmscon", "usr/share/etc/kmscon", relative=False)
    self.uninstall("usr/lib/systemd")
    # our dinit services
    self.install_service(self.files_path / "kmsconvt-service")
