pkgname = "opensbi"
pkgver = "1.2"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = [
    "PLATFORM=generic",
    "FW_PAYLOAD=n",
    "PLATFORM_RISCV_XLEN=64",
    "LLVM=1",
]
make_use_env = True
hostmakedepends = ["gmake", "bash", "python"]
pkgdesc = "RISC-V Open Source Supervisor Binary Interface"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/riscv-software-src/opensbi"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8fcbce598a73acc2c7f7d5607d46b9d5107d3ecbede8f68f42631dcfc25ef2b2"
hardening = ["!int"]
# no test suite
options = ["!check", "!lto", "!strip", "!debug", "foreignelf"]


def do_install(self):
    instp = "build/platform/generic/firmware"
    destp = "usr/lib/opensbi/generic"
    for f in ["dynamic", "jump"]:
        self.install_file(f"{instp}/fw_{f}.bin", destp, mode=0o644)
        self.install_file(f"{instp}/fw_{f}.elf", destp, mode=0o755)
        self.do(
            "/usr/bin/llvm-strip",
            "--remove-section=.comment",
            "--remove-section=.note",
            self.chroot_destdir / destp / f"fw_{f}.elf",
        )

    self.install_license("COPYING.BSD")
