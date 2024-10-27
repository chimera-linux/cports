pkgname = "rpi-boot"
pkgver = "1.20241023"
pkgrel = 0
archs = ["aarch64"]
_gitrev = "c3a480143e6697e121a0e1da81cfb9e1ff5f8070"
replaces = ["firmware-rpi<=20220905-r0"]
pkgdesc = "Bootloader for Raspberry Pi"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:raspberry"
url = "https://github.com/raspberrypi/firmware"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "4d614ff0b28f2395f98a46a7ee862105d2ca9de0425ee93e6e418931965cb615"
options = ["!strip", "foreignelf", "execstack"]


def install(self):
    self.install_license("boot/LICENCE.broadcom")

    for f in (self.cwd / "boot").glob("*.bin"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.dat"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.elf"):
        self.install_file(f"boot/{f.name}", "boot")
