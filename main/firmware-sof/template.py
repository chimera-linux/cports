pkgname = "firmware-sof"
pkgver = "2.2.5"
pkgrel = 0
archs = ["x86_64"]
install_if = [f"base-firmware-sof={pkgver}-r{pkgrel}"]
pkgdesc = "Sound Open Firmware"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://thesofproject.github.io/latest/index.html"
source = f"https://github.com/thesofproject/sof-bin/releases/download/v{pkgver}/sof-bin-v{pkgver}.tar.gz"
sha256 = "577f450875bd833af9b8b716e368d873aac913a35dd996c7aa0f52adddef92ee"
options = ["!strip", "foreignelf"]


def do_install(self):
    self.install_files(f"sof-v{pkgver}", "usr/lib/firmware/intel")
    self.install_files(f"sof-tplg-v{pkgver}", "usr/lib/firmware/intel")
    self.install_link(f"sof-v{pkgver}", "usr/lib/firmware/intel/sof")
    self.install_link(f"sof-tplg-v{pkgver}", "usr/lib/firmware/intel/sof-tplg")
    self.install_license("LICENCE.NXP")
    self.install_license("LICENCE.Intel")


@subpackage("base-firmware-sof")
def _base(self):
    self.pkgdesc = f"{pkgdesc} (base metapackage)"
    self.build_style = "meta"

    return []
