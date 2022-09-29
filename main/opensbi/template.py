pkgname = "opensbi"
pkgver = "1.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["PLATFORM=generic", "LLVM=1"]
make_use_env = True
hostmakedepends = ["gmake", "bash"]
pkgdesc = "RISC-V Open Source Supervisor Binary Interface"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/riscv-software-src/opensbi"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d183cb890130983a4f01e75fc03ee4f7ea0e16a7923b8af9c6dff7deb2fedaec"
# no test suite
options = ["!check"]

def do_install(self):
    instp = "build/platform/generic/firmware"
    destp = "usr/lib/opensbi/generic"
    for f in ["dynamic", "jump"]:
        self.install_file(f"{instp}/fw_{f}.bin", destp)
        self.install_file(f"{instp}/fw_{f}.elf", destp)
