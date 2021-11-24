pkgname = "initramfs-tools"
pkgver = "0.140"
pkgrel = 0
build_style = "makefile"
depends = ["klibc-progs", "bsdtar", "kmod", "debianutils", "awk"]
triggers = ["/boot"]
pkgdesc = "Generic modular initramfs generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = f"https://salsa.debian.org/kernel-team/initramfs-tools"
source = f"{url}/-/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz"
sha256 = "f46ae0e490a8a46975afd23a09202dee86756ebad1c8b795e862470a47dfac6b"
# no tests
options = ["!check"]

def post_install(self):
    for f in ["50-initramfs"]:
        self.install_file(
            self.files_path / (f + ".sh"), "etc/initramfs-tools/triggers",
            mode = 0o755
        )
