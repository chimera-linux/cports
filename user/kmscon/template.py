pkgname = "kmscon"
pkgver = "10.0.1"
pkgrel = 0
build_style = "meson"
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
sha256 = "62a8db81eebacaf959fd3b062c931c8789594f3bb9368d3c1e9a50280d81198b"


def post_install(self):
    self.install_license("COPYING")
    self.rename("etc/kmscon", "usr/share/etc/kmscon", relative=False)
    self.uninstall("usr/lib/systemd")
    # our dinit services
    self.install_service(self.files_path / "kmsconvt-service")
