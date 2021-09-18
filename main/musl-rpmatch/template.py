pkgname = "musl-rpmatch"
version = "1.0"
revision = 0
build_style = "gnu_makefile"
make_build_args = ["PREFIX=/usr"]
short_desc = "Implementation of rpmatch(3) for musl libc"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
homepage = "https://github.com/chimera-linux/musl-rpmatch"
distfiles = [f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{version}-mk2.tar.gz"]
checksum = ["a7b9649b49a8a59da09cf61228dc812cae6f0aea8be036788a9173c6f15a1a77"]

options = ["bootstrap", "!check"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("musl-rpmatch-devel")
def _devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = [f"{pkgname}={version}-r{revision}"]

    return [
        "usr/include", "usr/lib/*.a", "usr/lib/*.so",
        "usr/lib/pkgconfig"
    ]
