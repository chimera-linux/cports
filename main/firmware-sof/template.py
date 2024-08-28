pkgname = "firmware-sof"
pkgver = "2024.06"
pkgrel = 0
archs = ["x86_64"]
install_if = [self.with_pkgver("base-firmware-sof")]
pkgdesc = "Sound Open Firmware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://thesofproject.github.io/latest/index.html"
source = f"https://github.com/thesofproject/sof-bin/releases/download/v{pkgver}/sof-bin-{pkgver}.tar.gz"
sha256 = "581ca3285bb56837a8954953f629ebddce644152b673ecd4bbfae1504306d7d6"
options = ["!strip", "foreignelf"]


def install(self):
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
def _(self):
    self.subdesc = "base metapackage"
    self.options = ["empty"]

    return []
