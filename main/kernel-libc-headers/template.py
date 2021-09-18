pkgname = "kernel-libc-headers"
_mver = "5"
version = f"{_mver}.10.4"
revision = 0
make_cmd = "gmake"
short_desc = "Linux API headers for userland development"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
homepage = "http://www.kernel.org"
distfiles = [f"$(KERNEL_SITE)/kernel/v{_mver}.x/linux-{version}.tar.xz"]
checksum = ["904e396c26e9992a16cd1cc989460171536bed7739bf36049f6eb020ee5d56ec"]
options = ["bootstrap", "!check"]

if not current.bootstrapping:
    hostmakedepends = ["gmake", "perl"]

_arch = {
    "x86_64": "x86",
    "aarch64": "arm64",
    "ppc64le": "powerpc",
    "ppc64": "powerpc",
    "riscv64": "riscv",
}[current.build_profile.arch]

def do_build(self):
    from cbuild.util import make

    mk = make.Make(self, jobs = 1)

    tcfl = self.get_cflags(shell = True)
    tlfl = self.get_ldflags(shell = True)
    tcc = self.get_tool("CC")
    with self.profile("host"):
        hcfl = self.get_cflags(shell = True)
        hlfl = self.get_ldflags(shell = True)
        hcc = self.get_tool("CC")

    mk.invoke("mrproper", [
        "ARCH=" + _arch,
        "CC=" + tcc,
        "HOSTCC=" + hcc,
        "CFLAGS=" + tcfl,
        "HOSTCFLAGS=" + hcfl,
        "LDFLAGS=" + tlfl,
        "HOSTLDFLAGS=" + hlfl,
        "headers"
    ])

    # remove extra files and drm headers
    for fn in self.find(".", ".*", files = True):
        self.rm(fn)

    self.rm("usr/include/Makefile")
    self.rm("usr/include/drm", recursive = True)

def do_install(self):
    self.install_files("usr/include", "usr")
