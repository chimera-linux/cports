pkgname = "rpi-boot"
pkgver = "1.20250915"
pkgrel = 0
archs = ["aarch64"]
_gitrev = "676efed1194de38975889a34276091da1f5aadd3"
replaces = ["firmware-rpi<=20220905-r0"]
pkgdesc = "Bootloader for Raspberry Pi"
license = "custom:raspberry"
url = "https://github.com/raspberrypi/firmware"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "6eec37086202a11b2d5d936233c198292aa9628f869714708bdd8c358bb45e85"
options = ["!strip", "foreignelf", "execstack"]


def install(self):
    self.install_license("boot/LICENCE.broadcom")

    for f in (self.cwd / "boot").glob("*.bin"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.dat"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.elf"):
        self.install_file(f"boot/{f.name}", "boot")
