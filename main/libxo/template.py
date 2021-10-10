pkgname = "libxo"
pkgver = "1.6.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-gettext", "--disable-dependency-tracking"]
pkgdesc = "Library for generating text, XML, JSON, and HTML output"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/Juniper/libxo"
source = f"https://github.com/Juniper/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "9f2f276d7a5f25ff6fbfc0f38773d854c9356e7f985501627d0c0ee336c19006"

options = ["bootstrap", "!check", "!lint"]

if not current.bootstrapping:
    hostmakedepends = ["pkgconf"]

def post_patch(self):
    self.mkdir("libxo/sys")
    self.cp(self.files_path / "queue.h", "libxo/sys")

@subpackage("libxo-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/libxo-config",
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
        "usr/lib/pkgconfig",
        "usr/share/doc",
        "usr/share/man/man3"
    ]

@subpackage("libxo-progs")
def _progs(self):
    return [
        "usr/bin",
    ]
