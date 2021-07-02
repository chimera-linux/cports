pkgname = "musl-rpmatch"
version = "1.0"
revision = 1
wrksrc = f"musl-rpmatch-{version}-mk"
bootstrap = True
build_style = "gnu_makefile"
make_build_args = ["PREFIX=/usr"]
short_desc = "Implementation of rpmatch(3) for musl libc"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
homepage = "https://github.com/chimera-linux/musl-rpmatch"
distfiles = [f"https://github.com/chimera-linux/{pkgname}/archive/refs/tags/v{version}-mk.tar.gz"]
checksum = ["ccc55d3822dda0a355dd4fb376e64feea7c327e134a630e954a84ba8d7cf0c03"]

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
