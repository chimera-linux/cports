pkgname = "firmware-linux-brcm-rpi"
pkgver = "20241222"
pkgrel = 0
_fw_rev = "a6ed59a078d52ad72f0f2b99e68f324e7411afa1"
_bt_rev = "78d6a07730e2d20c035899521ab67726dc028e1c"
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
    "41783dd15e21f591eb65d47bd013eba4c1bfccd6f52a43963b8971f32e89190b",
    "56bcee9bac20720ceeef983949ba4d6b8d81c2f9602613232e642de547240841",
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
