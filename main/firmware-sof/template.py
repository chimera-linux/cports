pkgname = "firmware-sof"
pkgver = "2024.03"
pkgrel = 0
archs = ["x86_64"]
install_if = [f"base-firmware-sof={pkgver}-r{pkgrel}"]
pkgdesc = "Sound Open Firmware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://thesofproject.github.io/latest/index.html"
source = f"https://github.com/thesofproject/sof-bin/releases/download/v{pkgver}/sof-bin-{pkgver}.tar.gz"
sha256 = "4fd932f7bbc1517b06fa7911e6d566814d5dc4fec5608bdb44e7c4fe4929fbf6"
options = ["!strip", "foreignelf"]


def do_install(self):
    for folder in ["sof", "sof-ace-tplg", "sof-ipc4", "sof-tplg"]:
        self.install_files(
            folder, "usr/lib/firmware/intel", name=f"{folder}-v{pkgver}"
        )
        self.install_link(
            f"usr/lib/firmware/intel/{folder}", f"{folder}-v{pkgver}"
        )
    self.install_license("LICENCE.NXP")
    self.install_license("LICENCE.Intel")


@subpackage("base-firmware-sof")
def _base(self):
    self.pkgdesc = f"{pkgdesc} (base metapackage)"
    self.options = ["empty"]

    return []
