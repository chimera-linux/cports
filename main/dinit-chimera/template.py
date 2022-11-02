pkgname = "dinit-chimera"
_commit = "51db437d5869b0cc2a2891a6e70a1e7f40ff3c33"
pkgver = "0.1"
pkgrel = 0
build_style = "makefile"
makedepends = ["linux-headers"]
depends = ["dinit", "util-linux", "eudev"]
pkgdesc = "Chimera core services suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = f"https://github.com/chimera-linux/dinit-chimera"
source = f"https://github.com/chimera-linux/dinit-chimera/archive/{_commit}.tar.gz"
sha256 = "9af446e572ee0e39be01d2e321645c9e45e5880465f49ac778f4b8cc65aa564a"
# no tests
options = ["!check", "brokenlinks"]

def post_install(self):
    self.install_file(self.files_path / "hostname", "etc")
    self.install_file(self.files_path / "locale.conf", "etc")
    # init symlink
    self.install_link("dinit", "usr/bin/init")
    # x11 support
    self.install_dir("etc/X11/Xsession.d")
    self.install_file(
        self.files_path / "01dinit-env", "etc/X11/Xsession.d", mode = 0o755
    )

@subpackage("dinit-chimera-x11")
def _x11(self):
    self.pkgdesc = f"{pkgdesc} (X11 support)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "xinit"]
    return [
        "etc/X11/Xsession.d",
    ]

@subpackage("dinit-chimera-links")
def _def(self):
    self.pkgdesc = f"{pkgdesc} (service links)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.options = ["brokenlinks"]
    return [
        "usr/lib/dinit.d/boot.d/agetty-*"
    ]
