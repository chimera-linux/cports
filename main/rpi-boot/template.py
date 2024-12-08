pkgname = "rpi-boot"
pkgver = "1.20241205"
pkgrel = 0
archs = ["aarch64"]
_gitrev = "b543406ce066d3fcaa03078511bc47e62ad0bbec"
replaces = ["firmware-rpi<=20220905-r0"]
pkgdesc = "Bootloader for Raspberry Pi"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:raspberry"
url = "https://github.com/raspberrypi/firmware"
source = f"{url}/archive/{_gitrev}.tar.gz"
sha256 = "a27ffcdb8b16bdba8edca5fd038bd32c2ebab7e3a2c8b86de67e6dd7aabff784"
options = ["!strip", "foreignelf", "execstack"]


def install(self):
    self.install_license("boot/LICENCE.broadcom")

    for f in (self.cwd / "boot").glob("*.bin"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.dat"):
        self.install_file(f"boot/{f.name}", "boot")
    for f in (self.cwd / "boot").glob("*.elf"):
        self.install_file(f"boot/{f.name}", "boot")
