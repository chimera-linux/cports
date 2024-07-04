pkgname = "firmware-linux-steamdeck"
pkgver = "20240605.1"
pkgrel = 0
archs = ["x86_64"]
hostmakedepends = ["zstd-progs"]
replaces = ["firmware-linux-qca"]
pkgdesc = "Additional firmware for Steam Deck"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:linux-firmware"
url = "https://gitlab.com/evlaV/linux-firmware-neptune"
source = f"{url}/-/archive/jupiter-{pkgver}/linux-firmware-neptune-jupiter-{pkgver}.tar.gz"
sha256 = "3c5c71843de67b0e2a0339bd103e71c45ebb84a442c4b4f16cc1c6a6ddaef6d5"
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
        self.uninstall(f"usr/lib/firmware/{tof}")
        self.install_link(f"usr/lib/firmware/{tof}", fromf)
    # dsp
    self.install_file("cs35l41-dsp1-*", "usr/lib/firmware", glob=True)
    # compress
    for file in self.destdir.rglob("*"):
        if file.is_dir():
            continue
        dfile = file.relative_to(self.destdir)
        if file.is_symlink():
            ltgt = file.readlink()
            file.unlink()
            self.install_link(f"{dfile}.zst", f"{ltgt}.zst")
        else:
            self.do(
                "zstd",
                "--compress",
                "--quiet",
                "--rm",
                self.chroot_destdir / dfile,
            )
    # license
    self.install_license("LICENSE.QualcommAtheros_ath10k")
    self.install_license("LICENSE.cirrus")
    self.install_license("qca/NOTICE.txt")
