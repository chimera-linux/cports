pkgname = "firmware-sof"
pkgver = "2024.09.1"
pkgrel = 0
archs = ["x86_64"]
install_if = [self.with_pkgver("base-firmware-sof")]
pkgdesc = "Sound Open Firmware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://thesofproject.github.io/latest/index.html"
source = f"https://github.com/thesofproject/sof-bin/releases/download/v{pkgver}/sof-bin-{pkgver}.tar.gz"
sha256 = "a9b94d96648ab139d8270c728522d0ad7470276bc6a30efaf3752650d21e84e6"
options = ["!strip", "foreignelf"]


def install(self):
    for folder in [
        "sof",
        "sof-ipc4",
        "sof-ipc4-lib",
        "sof-ipc4-tplg",
        "sof-tplg",
    ]:
        self.install_files(
            folder, "usr/lib/firmware/intel", name=f"{folder}-v{pkgver}"
        )
        self.install_link(
            f"usr/lib/firmware/intel/{folder}", f"{folder}-v{pkgver}"
        )
    # compat link, following the default install.sh
    self.install_link("usr/lib/firmware/intel/sof-ace-tplg", "sof-ipc4-tplg")
    self.install_license("LICENCE.NXP")
    self.install_license("LICENCE.Intel")


@subpackage("base-firmware-sof")
def _(self):
    self.subdesc = "base metapackage"
    self.options = ["empty"]

    return []
