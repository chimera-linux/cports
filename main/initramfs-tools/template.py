pkgname = "initramfs-tools"
pkgver = "0.145"
pkgrel = 4
build_style = "makefile"
depends = [
    "base-kernel",
    "dracut-install",
    "klibc-kinit-standalone",
    "klibc-utils-standalone",
    "cmd:ischroot!debianutils",
    "cmd:run-parts!debianutils",
    "cmd:zstd!zstd",
    "cmd:cpio!libarchive-progs",
    "cmd:ugetopt!ugetopt",
    "cmd:setupcon!console-setup",
    "cmd:awk!chimerautils",
    "cmd:logsave!e2fsprogs",
]
pkgdesc = "Generic modular initramfs generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://salsa.debian.org/kernel-team/initramfs-tools"
source = f"{url}/-/archive/v{pkgver}/initramfs-tools-v{pkgver}.tar.gz"
sha256 = "e2c2db8f096e0a71e0e55362c74e48b621ce8a2f455f309eefca8d113f31e0ff"
# no tests
options = ["!check"]


def post_install(self):
    for f in ["50-initramfs"]:
        self.install_file(
            self.files_path / (f + ".sh"), "usr/lib/kernel.d", mode=0o755
        )

    # hook for core userland
    self.install_initramfs(
        self.files_path / "chimerautils.initramfs-tools", name="chimerautils"
    )
