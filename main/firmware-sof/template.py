pkgname = "firmware-sof"
pkgver = "2025.12.2"
pkgrel = 0
archs = ["x86_64"]
install_if = [self.with_pkgver("base-firmware-sof")]
pkgdesc = "Sound Open Firmware"
license = "BSD-3-Clause"
url = "https://thesofproject.github.io/latest/index.html"
source = f"https://github.com/thesofproject/sof-bin/releases/download/v{pkgver}/sof-bin-{pkgver}.tar.gz"
sha256 = "533f63e3a6d94c09ce05a782657b675fa683ff20787c0979226cf563ec79f517"
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
