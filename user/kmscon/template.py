pkgname = "kmscon"
pkgver = "10.1.0"
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
sha256 = "ac8e763b3c0e88f155daa7c4273009a9042fd43b2f7d54bc95dccfab0d81d953"
options = ["etcfiles"]


def post_install(self):
    self.install_license("COPYING")
    self.rename("etc/kmscon", "usr/share/etc/kmscon", relative=False)
    self.uninstall("usr/lib/systemd")
    # our dinit services
    self.install_service(self.files_path / "kmsconvt-service")
