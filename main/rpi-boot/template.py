pkgname = "rpi-boot"
pkgver = "1.20260508"
pkgrel = 0
archs = ["aarch64"]
_gitrev = "30b5888797a83afc8613669b685062e328b003d8"
replaces = ["firmware-rpi<=20220905-r0"]
pkgdesc = "Bootloader for Raspberry Pi"
license = "custom:raspberry"
url = "https://github.com/raspberrypi/firmware"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "02161aed1c3be82af16ab2143ddcc3469a3b0ff216c7276a67f47a2f5d6120b7"
options = ["!strip", "foreignelf", "execstack"]


def install(self):
    self.install_license("boot/LICENCE.broadcom")

    for f in (self.cwd / "boot").glob("*.bin"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.dat"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.elf"):
        self.install_file(f"boot/{f.name}", "boot")
