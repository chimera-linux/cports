pkgname = "firmware-linux-steamdeck"
pkgver = "20231113.1"
pkgrel = 0
archs = ["x86_64"]
replaces = ["firmware-linux-qca"]
pkgdesc = "Additional firmware for Steam Deck"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:linux-firmware"
url = "https://gitlab.com/evlaV/linux-firmware-neptune"
source = f"{url}/-/archive/jupiter-{pkgver}/linux-firmware-neptune-jupiter-{pkgver}.tar.gz"
sha256 = "de4966a7c49d07252c84b04f6d5c1c880ccf15aee01a8b556cff306055a3d832"
options = ["!strip", "foreignelf", "execstack"]


def do_install(self):
    # wifi
    self.install_file(
        "ath11k/QCA206X/hw2.1/*",
        "usr/lib/firmware/ath11k/QCA206X/hw2.1",
        glob=True,
    )
    # bluetooth
    self.install_file("qca/hp*21*", "usr/lib/firmware/qca", glob=True)
    # dedup
    for fromf, tof in [
        ("board.bin", "ath11k/QCA206X/hw2.1/boardg.bin"),
        ("hpnv21.301", "qca/hpnv21.302"),
        ("hpnv21g.301", "qca/hpnv21g.302"),
        ("hpnv21.bin", "qca/hpnv21.309"),
        ("hpnv21g.bin", "qca/hpnv21g.309"),
    ]:
        self.rm(self.destdir / f"usr/lib/firmware/{tof}")
        self.install_link(fromf, f"usr/lib/firmware/{tof}")
    # dsp
    self.install_file("cs35l41-dsp1-*", "usr/lib/firmware", glob=True)
    # license
    self.install_license("LICENSE.QualcommAtheros_ath10k")
    self.install_license("LICENSE.cirrus")
    self.install_license("qca/NOTICE.txt")
