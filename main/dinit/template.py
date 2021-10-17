pkgname = "dinit"
pkgver = "0.12.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_install_args = ["SBINDIR=/usr/bin"]
hostmakedepends = ["gmake", "bsdm4"]
pkgdesc = "Service manager and init system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = f"https://github.com/davmac314/{pkgname}"
source = f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d5f9afe7005da7c08224dddcf2b63f37a6c4120b7493bed4669ef362cde1b544"
tool_flags = {"CXXFLAGS": ["-fno-rtti"], "LDFLAGS": ["-fno-rtti"]}

def init_configure(self):
    eflags = ["CXXOPTS=" + self.get_cxxflags(shell = True)]
    self.make_build_args += eflags
    self.make_check_args += eflags
