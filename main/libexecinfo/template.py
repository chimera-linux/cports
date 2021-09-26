pkgname = "libexecinfo"
version = "1.1"
revision = 0
build_style = "makefile"
make_build_args = ["PREFIX=/usr"]
short_desc = "BSD licensed clone of the GNU libc backtrace facility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
homepage = "http://www.freshports.org/devel/libexecinfo"
distfiles = [f"http://distcache.freebsd.org/local-distfiles/itetcu/libexecinfo-{version}.tar.bz2"]
checksum = ["c9a21913e7fdac8ef6b33250b167aa1fc0a7b8a175145e26913a4c19d8a59b1f"]

options = ["!check"]

def do_install(self):
    self.install_dir("usr/lib/pkgconfig")
    self.install_dir("usr/include")
    self.install_file("libexecinfo.pc", "usr/lib/pkgconfig")
    self.install_file("execinfo.h", "usr/include")
    self.install_file("stacktraverse.h", "usr/include")
    self.install_file("libexecinfo.a", "usr/lib")
    self.install_lib("libexecinfo.so.1")
    self.install_link("libexecinfo.so.1", "usr/lib/libexecinfo.so")

@subpackage("libexecinfo-devel")
def _devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = [f"{pkgname}={version}-r{revision}"]

    return [
        "usr/include", "usr/lib/*.so", "usr/lib/*.a", "usr/lib/pkgconfig"
    ]
