pkgname = "firmware-sof"
pkgver = "2023.12"
pkgrel = 0
archs = ["x86_64"]
install_if = [f"base-firmware-sof={pkgver}-r{pkgrel}"]
pkgdesc = "Sound Open Firmware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://thesofproject.github.io/latest/index.html"
source = f"https://github.com/thesofproject/sof-bin/releases/download/v{pkgver}/sof-bin-{pkgver}.tar.gz"
sha256 = "55e47eb63e6248dbdab7da232bb1e31ca2e7155b37dc116f6dc5b173cba3503b"
options = ["!strip", "foreignelf"]


def do_install(self):
    for folder in ["sof", "sof-ace-tplg", "sof-ipc4", "sof-tplg"]:
        self.install_files(
            folder, "usr/lib/firmware/intel", name=f"{folder}-v{pkgver}"
        )
        self.install_link(
            f"{folder}-v{pkgver}", f"usr/lib/firmware/intel/{folder}"
        )
    self.install_license("LICENCE.NXP")
    self.install_license("LICENCE.Intel")


@subpackage("base-firmware-sof")
def _base(self):
    self.pkgdesc = f"{pkgdesc} (base metapackage)"
    self.build_style = "meta"

    return []
