pkgname = "opensbi"
pkgver = "1.9"
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
sha256 = "f6c4985843d6d878b5b511d7d7a930b6b541d3d9305371f2d9780765428f66f4"
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
