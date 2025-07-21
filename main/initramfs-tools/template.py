pkgname = "initramfs-tools"
pkgver = "0.147"
pkgrel = 0
build_style = "makefile"
make_install_args = [f"VERSION={pkgver}"]
depends = [
    "base-kernel",
    "cmd:awk!chimerautils",
    "cmd:cpio!libarchive-progs",
    "cmd:ischroot!debianutils",
    "cmd:logsave!e2fsprogs",
    "cmd:run-parts!debianutils",
    "cmd:setupcon!console-setup",
    "cmd:ugetopt!ugetopt",
    "cmd:zstd!zstd",
    "dracut-install",
    "klibc-kinit-standalone",
    "klibc-utils-standalone",
]
pkgdesc = "Generic modular initramfs generator"
license = "GPL-2.0-or-later"
url = "https://salsa.debian.org/kernel-team/initramfs-tools"
source = f"{url}/-/archive/v{pkgver}/initramfs-tools-v{pkgver}.tar.gz"
sha256 = "313b605dd67f0ba83f19b16ede9e9074ba989bf805aa60dafb136b9cb4b25c7f"
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
