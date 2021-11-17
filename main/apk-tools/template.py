pkgname = "apk-tools"
pkgver = "2.12.8"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dlua=disabled", "-Dstatic_apk=true"]
hostmakedepends = ["pkgconf", "meson", "lua5.4", "lua5.4-zlib", "scdoc"]
makedepends = ["zlib-devel", "openssl-devel"]
pkgdesc = "Alpine package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://git.alpinelinux.org/cgit/apk-tools"
source = f"http://git.alpinelinux.org/cgit/{pkgname}/snapshot/{pkgname}-{pkgver}.tar.bz2"
sha256 = "d976d625d5ede5ccdd1bae4a56627c26a11f323475f85d7bc5cb29b04781f7b5"
tool_flags = {
    "CFLAGS": ["-Wno-error"]
}
options = ["bootstrap"]

if self.stage > 0:
    makedepends += ["linux-headers"]
else:
    configure_args += ["-Dhelp=disabled", "-Ddocs=disabled"]

@subpackage("apk-tools-devel")
def _devel(self):
    return self.default_devel(man = True)

@subpackage("apk-tools-static")
def _static(self):
    self.pkgdesc += " (static build)"

    return ["usr/bin/apk.static"]
