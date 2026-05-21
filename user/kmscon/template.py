pkgname = "kmscon"
pkgver = "10.0.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
]
hostmakedepends = ["libxslt-progs", "meson", "ncurses", "pkgconf"]
makedepends = [
    "check-devel",
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
sha256 = "7074956472c42d14977922f9ef6d2ec101f8d88e549f0108c1f51cb9d2b437dd"


def post_install(self):
    self.install_license("COPYING")
    self.rename("etc/pam.d", "usr/lib/pam.d", relative=False)
    self.rename("etc/kmscon", "usr/share/etc/kmscon", relative=False)
    self.uninstall("usr/lib/systemd")
    # our dinit services
    self.install_service(self.files_path / "kmsconvt-service")
