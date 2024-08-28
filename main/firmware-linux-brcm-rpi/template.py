pkgname = "firmware-linux-brcm-rpi"
pkgver = "20231024"
pkgrel = 1
_fw_rev = "88aa085bfa1a4650e1ccd88896f8343c22a24055"
_bt_rev = "d9d4741caba7314d6500f588b1eaa5ab387a4ff5"
archs = ["aarch64"]
hostmakedepends = ["zstd-progs"]
replaces = ["firmware-linux-brcm", "firmware-rpi<=20220905-r0"]
replaces_priority = 100  # always overrides files of firmware-linux-brcm
pkgdesc = "Broadcom firmware for Raspberry Pi"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:Broadcom AND custom:Cypress"
url = "https://github.com/raspberrypi/firmware"
source = [
    f"https://github.com/RPi-Distro/firmware-nonfree/archive/{_fw_rev}.tar.gz",
    f"https://github.com/RPi-Distro/bluez-firmware/archive/{_bt_rev}.tar.gz",
]
sha256 = [
    "bb3d8fed40546e03e29d9e635745433f8083391e62d6ff151c895b892776964a",
    "ae076a08ece89624b0449ea2495b0dfe2ea1223f683f5b57f2b89966e6a093d6",
]
options = ["!strip", "foreignelf", "execstack"]


def install(self):
    bfw = f"bluez-firmware-{_bt_rev}/debian/firmware"
    wfw = f"firmware-nonfree-{_fw_rev}/debian/config/brcm80211"

    # need either standard or minimal
    self.ln_s(
        "cyfmac43455-sdio-standard.bin", f"{wfw}/cypress/cyfmac43455-sdio.bin"
    )
    # install all wifi firmware
    self.install_files(f"{wfw}/cypress", "usr/lib/firmware")
    self.install_files(f"{wfw}/brcm", "usr/lib/firmware")

    # install bluetooth firmware
    self.install_file(
        f"{bfw}/broadcom/BCM*", "usr/lib/firmware/brcm", glob=True
    )
    self.install_file(
        f"{bfw}/synaptics/SYN*", "usr/lib/firmware/synaptics", glob=True
    )

    # compress
    for file in self.destdir.rglob("*"):
        if file.is_dir():
            continue
        elif file.name == "README.txt":
            # cypress
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

    # links
    with (self.cwd / bfw / "../bluez-firmware.links").open() as lf:
        for ln in lf:
            froml, tol = ln.split()
            froml = froml.removeprefix("/lib/firmware/")
            tol = tol.replace("/lib/", "usr/lib/")
            if froml.startswith("brcm/"):
                froml = froml.removeprefix("brcm/")
            elif froml.startswith("synaptics/"):
                froml = f"../{froml}"
            else:
                self.error(f"unknown firmware path{froml}")
            self.install_link(f"{tol}.zst", f"{froml}.zst")

    # license files
    self.install_license(f"{bfw}/broadcom/LICENSE.cypress")
    self.install_license(f"{bfw}/synaptics/LICENSE.synaptics")
