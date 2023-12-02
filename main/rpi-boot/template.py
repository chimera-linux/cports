pkgname = "rpi-boot"
pkgver = "1.20231129"
pkgrel = 0
archs = ["aarch64"]
_gitrev = "5ffb2e29c0e14dede001447a6977e126e950cf3e"
replaces = ["firmware-rpi<=20220905-r0"]
pkgdesc = "Bootloader for Raspberry Pi"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:raspberry"
url = "https://github.com/raspberrypi/firmware"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "70810987352f8f9d88fc729cce3ad5fa6c03a69e5702a8ba7b2bb797f23be5d5"
options = ["!strip", "foreignelf", "execstack"]


def do_install(self):
    self.install_license("boot/LICENCE.broadcom")

    for f in (self.cwd / "boot").glob("*.bin"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.dat"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.elf"):
        self.install_file(f"boot/{f.name}", "boot")
