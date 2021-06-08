pkgname = "file"
version = "5.40"
revision = 2
bootstrap = True
build_style = "gnu_configure"
configure_args = ["--enable-static", "--disable-libseccomp"]
makedepends = ["zlib-devel"]
short_desc = "File type identification utility"
maintainer = "Enno Boland <gottox@voidlinux.org>"
license = "BSD-2-Clause"
homepage = "http://www.darwinsys.com/file/"
distfiles = [f"https://astron.com/pub/file/file-{version}.tar.gz"]
checksum = ["167321f43c148a553f68a0ea7f579821ef3b11c27b8cbe158e4df897e4a5dd57"]

if cross_build:
    hostmakedepends = ["file"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libmagic")
def _libmagic(self):
    self.short_desc = "File type identification library"

    def install():
        self.take("usr/lib/*.so.*")
        self.take("usr/share/misc")
        self.take("usr/share/man/man4")

    return install

@subpackage("file-devel")
def _devel(self):
    self.depends = makedepends + [f"libmagic>={version}_{revision}"]
    self.short_desc = "File type identification library - development files"

    def install():
        self.take("usr/include")
        self.take("usr/lib/*.a")
        self.take("usr/lib/*.so")
        self.take("usr/lib/pkgconfig")
        self.take("usr/share/man/man3")

    return install