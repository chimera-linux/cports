pkgname = "libxkbcommon"
pkgver = "1.3.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Denable-x11=true", "-Denable-wayland=true", "-Denable-xkbregistry=true",
    "-Denable-docs=false", "-Db_ndebug=false",
]
hostmakedepends = [
    "meson", "pkgconf", "bison", "wayland-protocols", "wayland-progs"
]
makedepends = [
    "xkeyboard-config", "libxcb-devel", "wayland-devel", "wayland-protocols",
    "xorgproto", "libxml2-devel"
]
depends = ["xkeyboard-config"]
pkgdesc = "Library to handle keyboard descriptions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xkbcommon.org"
source = f"https://github.com/xkbcommon/{pkgname}/archive/xkbcommon-{pkgver}.tar.gz"
sha256 = "8eda6782c6ed4b83296521f2f7e6bea88aba76d49c39fb4fce0f8d355a9181ce"

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libxkbcommon-x11")
def _x11(self):
    self.pkgdesc = f"{pkgdesc} (X11 support)"

    return ["usr/lib/*x11*.so.*"]

@subpackage("libxkbregistry")
def _registry(self):
    self.pkgdesc = "XKB API to query keyboard descriptions"

    return ["usr/lib/libxkbregistry.so.*"]

@subpackage("libxkbcommon-static")
def _static(self):
    return self.default_static()

@subpackage("libxkbcommon-devel")
def _devel(self):
    self.depends += ["libxcb-devel"]

    return self.default_devel()

@subpackage("libxkbcommon-progs")
def _progs(self):
    return self.default_progs(man = True, extra = ["usr/libexec"])
