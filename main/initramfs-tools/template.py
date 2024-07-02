pkgname = "initramfs-tools"
pkgver = "0.143"
pkgrel = 1
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
source = f"{url}/-/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz"
sha256 = "5d3091b0393c4246bcdae499cfd5ba490c78194d7eede01d951f4124ff2f9895"
# no tests
options = ["!check"]


def post_install(self):
    for f in ["50-initramfs"]:
        self.install_file(
            self.files_path / (f + ".sh"), "usr/lib/kernel.d", mode=0o755
        )

    # hook for core userland
    self.install_file(
        self.files_path / "chimerautils.initramfs-tools",
        "usr/share/initramfs-tools/hooks",
        mode=0o755,
        name="chimerautils",
    )
