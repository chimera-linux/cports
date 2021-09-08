pkgname = "file"
version = "5.40"
revision = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-static", "--disable-libseccomp",
    "--disable-bzlib", "--disable-xzlib"
]
makedepends = ["zlib-devel"]
short_desc = "File type identification utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
homepage = "http://www.darwinsys.com/file/"
distfiles = [f"https://astron.com/pub/file/file-{version}.tar.gz"]
checksum = ["167321f43c148a553f68a0ea7f579821ef3b11c27b8cbe158e4df897e4a5dd57"]

options = ["bootstrap", "!check"]

if current.cross_build:
    hostmakedepends = ["file"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libmagic")
def _libmagic(self):
    self.short_desc = "File type identification library"

    return [
        "usr/lib/*.so.*",
        "usr/share/misc",
        "usr/share/man/man4",
    ]

@subpackage("file-devel")
def _devel(self):
    self.depends = makedepends + [f"libmagic={version}-r{revision}"]
    self.short_desc = "File type identification library - development files"

    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
        "usr/lib/pkgconfig",
        "usr/share/man/man3",
    ]
