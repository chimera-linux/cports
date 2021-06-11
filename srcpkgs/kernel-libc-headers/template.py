pkgname = "kernel-libc-headers"
_mver = "5.10"
version = f"{_mver}.4"
revision = 1
bootstrap = True
wrksrc = f"linux-{version}"
make_cmd = "gmake"
hostmakedepends = []
short_desc = "Linux API headers for userland development"
maintainer = "Érico Nogueira <ericonr@disroot.org>"
license = "GPL-2.0-only"
homepage = "http://www.kernel.org"

from cbuild import sites, cpu

distfiles = [f"{sites.kernel}/kernel/v{_mver}.x/linux-{version}.tar.xz"]
checksum = ["904e396c26e9992a16cd1cc989460171536bed7739bf36049f6eb020ee5d56ec"]

if not current.bootstrapping:
    hostmakedepends.append("perl")

_arch = cpu.match_target(
    "x86_64*", lambda a: "x86",
    "aarch64*", lambda a: "arm64",
    "ppc*", lambda a: "powerpc"
)

def do_build(self):
    from cbuild.util import make
    import glob

    mk = make.Make(self, jobs = 1)
    mk.invoke("mrproper", ["ARCH=" + _arch, "headers"])

    # remove extra files and drm headers
    for fn in self.find(".*", files = True, root = self.abs_wrksrc):
        self.unlink(fn, root = self.abs_wrksrc)

    self.unlink("usr/include/Makefile", root = self.abs_wrksrc)
    self.rmtree("usr/include/drm", root = self.abs_wrksrc)

def do_install(self):
    self.install_files("usr/include", "usr")
