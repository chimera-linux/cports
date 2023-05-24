pkgname = "u-boot-imx8mq_reform2"
pkgver = "2018.07"
pkgrel = 0
archs = ["aarch64"]
pkgdesc = "U-Boot for MNT Reform 2"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://source.mnt.re/reform/reform-boundary-uboot"
source = f"https://repo.chimera-linux.org/distfiles/{pkgname}-{pkgver}.tar.gz"
sha256 = "d8699b465c8d09549aee622e3a42d4101e765abfe4f3f0be54a45a3d878a152a"
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug"]


def do_install(self):
    for x in self.cwd.iterdir():
        if x.is_dir():
            continue
        self.install_file(x, "usr/lib/u-boot/imx8mq_reform2")
    # flasher
    self.install_file(
        self.files_path / "flash.sh",
        "usr/lib/u-boot/imx8mq_reform2",
        mode=0o755,
    )
    # licenses
    for f in (self.cwd / "Licenses").iterdir():
        self.install_license(f"Licenses/{f.name}")
    # readme
    self.install_file("README.txt", f"usr/share/doc/{self.pkgname}")
