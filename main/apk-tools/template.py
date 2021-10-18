pkgname = "apk-tools"
pkgver = "2.12.7"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlua=disabled", "-Ddocs=disabled", "-Dhelp=disabled", "-Dstatic_apk=true"
]
hostmakedepends = ["pkgconf", "meson"]
makedepends = ["zlib-devel", "openssl-devel"]
depends = ["ca-certificates"]
pkgdesc = "Alpine package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://git.alpinelinux.org/cgit/apk-tools"
source = f"http://git.alpinelinux.org/cgit/{pkgname}/snapshot/{pkgname}-{pkgver}.tar.bz2"
sha256 = "269831b60d0008d3f4420293971ebbe951b04ee72f8359f2cc3ee89e649b1705"
tool_flags = {
    "CFLAGS": ["-Wno-error"]
}
options = ["bootstrap"]

if not current.bootstrapping:
    makedepends += ["kernel-libc-headers"]

@subpackage("apk-tools-devel")
def _devel(self):
    return self.default_devel(man = True)

@subpackage("apk-tools-static")
def _static(self):
    self.pkgdesc += " (static build)"

    return ["usr/bin/apk.static"]
