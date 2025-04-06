pkgname = "firmware-sof"
pkgver = "2025.01.1"
pkgrel = 0
archs = ["x86_64"]
install_if = [self.with_pkgver("base-firmware-sof")]
pkgdesc = "Sound Open Firmware"
license = "BSD-3-Clause"
url = "https://thesofproject.github.io/latest/index.html"
source = f"https://github.com/thesofproject/sof-bin/releases/download/v{pkgver}/sof-bin-{pkgver}.tar.gz"
sha256 = "a36210d9c245e81b0d9674d6b27d1fd4122968cf925aefc55b486d3650f88323"
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


@subpackage("firmware-sof-meta")
def _(self):
    self.subdesc = "base metapackage"
    self.options = ["empty"]
    # transitional
    self.provides = [self.with_pkgver("base-firmware-sof")]

    return []
