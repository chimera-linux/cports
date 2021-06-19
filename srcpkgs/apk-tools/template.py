pkgname = "apk-tools"
version = "2.12.5"
revision = 1
bootstrap = True
build_style = "meson"
configure_args = ["-Dlua=disabled", "-Ddocs=disabled", "-Dhelp=disabled"]
makedepends = ["zlib-devel", "openssl-devel"]
short_desc = "Alpine package manager"
maintainer = "q66 <daniel@octaforge.org>"
license = "GPL-2.0-only"
homepage = "http://git.alpinelinux.org/cgit/apk-tools"
distfiles = [f"http://git.alpinelinux.org/cgit/{pkgname}/snapshot/{pkgname}-{version}.tar.bz2"]
checksum = ["a3cbabbcd3072f197b19f85e13e526b8b769d1e537f8156457b1779bcc9300fe"]

CFLAGS = ["-Wno-error"]

if not current.bootstrapping:
    hostmakedepends = ["pkgconf", "meson"]

@subpackage("apk-tools-devel")
def _devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = [f"{pkgname}>={version}_{revision}"]

    return [
        "usr/include",
        "usr/lib/*.so",
        "usr/lib/*.a",
        "usr/lib/pkgconfig",
    ]
