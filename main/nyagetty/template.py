pkgname = "nyagetty"
pkgver = "2.38.99"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
makedepends = ["linux-headers"]
pkgdesc = "Standalone util-linux agetty"
maintainer = "q66 <q66@chimera-linux.org>"
license = "0BSD"
url = "https://github.com/chimera-linux/nyagetty"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7033d6840f839a6ad6d788d92f45efd0bb10c835c0560dba5d15ad8a6b9dff90"
hardening = ["vis", "cfi"]

def post_install(self):
    # agetty dinit helper
    self.install_file(
        self.files_path / "dinit-agetty", "usr/libexec", mode = 0o755
    )

    # services
    for s in [
        "agetty", "agetty-console", "agetty-hvc0", "agetty-hvsi0",
        "agetty-tty1", "agetty-tty2", "agetty-tty3", "agetty-tty4",
        "agetty-tty5", "agetty-tty6", "agetty-ttyS0", "agetty-ttyUSB0",
    ]:
        self.install_service(self.files_path / s, enable = (s == "agetty"))

@subpackage("nyagetty-dinit")
def _dinit(self):
    self.pkgdesc = f"{pkgdesc} (service files)"

    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "dinit-chimera"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "dinit-chimera"]

    return ["etc/dinit.d/agetty*", "usr/libexec/dinit-agetty"]
