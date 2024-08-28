pkgname = "rpi-boot"
pkgver = "1.20240321"
pkgrel = 0
archs = ["aarch64"]
_gitrev = "45319db29eb5e4f67feab5c4194bc1f28c574ed0"
replaces = ["firmware-rpi<=20220905-r0"]
pkgdesc = "Bootloader for Raspberry Pi"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:raspberry"
url = "https://github.com/raspberrypi/firmware"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "369074ba1a574e6f1c84c780cf77908b3778ed588643fcaae1a39b8a3d555334"
options = ["!strip", "foreignelf", "execstack"]


def install(self):
    self.install_license("boot/LICENCE.broadcom")

    for f in (self.cwd / "boot").glob("*.bin"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.dat"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.elf"):
        self.install_file(f"boot/{f.name}", "boot")
