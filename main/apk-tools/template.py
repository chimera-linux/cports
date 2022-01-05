pkgname = "apk-tools"
pkgver = "2.12.9"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dlua=disabled", "-Dstatic_apk=true"]
hostmakedepends = ["pkgconf", "meson", "lua5.4", "lua5.4-zlib", "scdoc"]
makedepends = [
    "openssl-devel-static", "zlib-devel-static", "libunwind-devel-static"
]
pkgdesc = "Alpine package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://git.alpinelinux.org/cgit/apk-tools"
source = f"http://git.alpinelinux.org/cgit/{pkgname}/snapshot/{pkgname}-{pkgver}.tar.bz2"
sha256 = "f4ead0a3722bc7c6760634b6c8abfe139b5359c934b7fca8661704828f5f6dd9"
tool_flags = {
    "CFLAGS": ["-Wno-error"]
}
options = ["bootstrap"]

if self.stage > 0:
    makedepends += ["linux-headers", "musl-devel-static"]
else:
    configure_args += ["-Dhelp=disabled", "-Ddocs=disabled"]

@subpackage("apk-tools-devel")
def _devel(self):
    return self.default_devel()

@subpackage("apk-tools-static-bin")
def _staticbin(self):
    self.pkgdesc += " (static binary)"
    self.depends = []

    return ["usr/bin/apk.static"]
