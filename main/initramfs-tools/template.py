pkgname = "initramfs-tools"
pkgver = "0.143.1"
pkgrel = 0
build_style = "makefile"
depends = [
    "base-kernel",
    "dracut-install",
    "klibc-kinit-standalone",
    "klibc-utils-standalone",
    "virtual:cmd:ischroot!debianutils",
    "virtual:cmd:run-parts!debianutils",
    "virtual:cmd:zstd!zstd",
    "virtual:cmd:cpio!bsdtar",
    "virtual:cmd:ugetopt!ugetopt",
    "virtual:cmd:setupcon!console-setup",
    "virtual:cmd:awk!chimerautils",
    "virtual:cmd:logsave!e2fsprogs",
]
pkgdesc = "Generic modular initramfs generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://salsa.debian.org/kernel-team/initramfs-tools"
source = f"{url}/-/archive/v{pkgver}/initramfs-tools-v{pkgver}.tar.gz"
sha256 = "3b8d89dfdf3c341a9513c03fe7c8c2a1c8de747a35bec74b4b133aeae912eda9"
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
