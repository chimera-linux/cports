pkgname = "kmscon"
pkgver = "10.0.3"
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
pkgdesc = "Linux KMS/DRM virtual console terminal emulator"
license = "MIT"
url = "https://github.com/kmscon/kmscon"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4a0552d3cd3ba16df4fcff61f2b1431650bcd9e7ecabc03625ce52345b9c95c5"
hardening = ["vis", "!cfi"]
options = ["etcfiles"]


def post_install(self):
    self.install_license("COPYING")
    self.rename("etc/pam.d", "usr/lib/pam.d", relative=False)
    self.rename("etc/kmscon", "usr/share/etc/kmscon", relative=False)
    self.uninstall("usr/lib/systemd")
    # our dinit services
    self.install_service(self.files_path / "kmsconvt-service")
