pkgname = "opensbi"
pkgver = "1.6"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "PLATFORM=generic",
    "FW_PAYLOAD=n",
    "PLATFORM_RISCV_XLEN=64",
    "LLVM=1",
]
make_use_env = True
hostmakedepends = ["bash", "python"]
pkgdesc = "RISC-V Open Source Supervisor Binary Interface"
license = "BSD-2-Clause"
url = "https://github.com/riscv-software-src/opensbi"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d11702103f177a2914e94eec57ce5ed820296d874f6b6525c4482e55d71a3667"
hardening = ["!int"]
# no test suite
options = ["!check", "!lto", "!strip", "!debug", "foreignelf"]


def install(self):
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
