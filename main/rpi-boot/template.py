pkgname = "rpi-boot"
pkgver = "1.20230810"
pkgrel = 0
archs = ["aarch64"]
_gitrev = "7cb8f19514cd01ba53fff6792c519f88ed31963b"
replaces = ["firmware-rpi<=20220905-r0"]
pkgdesc = "Bootloader for Raspberry Pi"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:raspberry"
url = "https://github.com/raspberrypi/firmware"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "2d88e5a666f44de582575ec941337f3289037849f2703392665a8bcd66cc848c"
options = ["!strip", "foreignelf", "execstack"]


def do_install(self):
    self.install_license("boot/LICENCE.broadcom")

    for f in (self.cwd / "boot").glob("*.bin"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.dat"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.elf"):
        self.install_file(f"boot/{f.name}", "boot")
