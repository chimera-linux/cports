pkgname = "apk-tools"
pkgver = "2.12.5"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlua=disabled", "-Ddocs=disabled", "-Dhelp=disabled", "-Dstatic_apk=true"
]
makedepends = ["zlib-devel", "openssl-devel"]
depends = ["ca-certificates"]
pkgdesc = "Alpine package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://git.alpinelinux.org/cgit/apk-tools"
sources = [f"http://git.alpinelinux.org/cgit/{pkgname}/snapshot/{pkgname}-{pkgver}.tar.bz2"]
sha256 = ["a3cbabbcd3072f197b19f85e13e526b8b769d1e537f8156457b1779bcc9300fe"]

options = ["bootstrap", "!check", "!lint"]

tool_flags = {
    "CFLAGS": ["-Wno-error"]
}

if not current.bootstrapping:
    hostmakedepends = ["pkgconf", "meson"]

@subpackage("apk-tools-devel")
def _devel(self):
    self.pkgdesc = pkgdesc + " - development files"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/include",
        "usr/lib/*.so",
        "usr/lib/*.a",
        "usr/lib/pkgconfig",
    ]

@subpackage("apk-tools-static")
def _static(self):
    self.pkgdesc = pkgdesc + " - static build"

    return ["usr/bin/apk.static"]
