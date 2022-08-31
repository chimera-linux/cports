pkgname = "firmware-linux"
pkgver = "20220815"
pkgrel = 0
make_cmd = "gmake"
hostmakedepends = ["gmake"]
depends = [
    f"firmware-linux-amd={pkgver}-r{pkgrel}",
    f"firmware-linux-network={pkgver}-r{pkgrel}"
]
pkgdesc = "Binary firmware blobs for the Linux kernel"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:linux-firmware"
url = "https://www.kernel.org"
source = f"https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/snapshot/linux-firmware-{pkgver}.tar.gz"
sha256 = "5b053102645d23e5f070f0d3f3b1a538eb26b14778564c42dc6112e419233d2b"
options = ["!strip", "foreignelf"]

def do_install(self):
    from cbuild.util import make
    make.Make(self).install(["FIRMWAREDIR=/usr/lib/firmware"])

    self.install_license("WHENCE")

    for l in self.cwd.glob("LICEN*"):
        self.install_license(l)

@subpackage("firmware-linux-amd")
def _amd(self):
    self.pkgdesc = f"{pkgdesc} (AMD)"
    self.options = ["!strip", "foreignelf"]

    return [
        "usr/lib/firmware/amd*",
        "usr/lib/firmware/radeon",
        "usr/share/licenses/firmware-linux/LICENSE.amdgpu",
        "usr/share/licenses/firmware-linux/LICENSE.amd-ucode",
        "usr/share/licenses/firmware-linux/LICENSE.radeon",
    ]

@subpackage("firmware-linux-broadcom")
def _bcm(self):
    self.pkgdesc = f"{pkgdesc} (Broadcom)"
    self.options = ["!strip", "foreignelf"]

    return [
        "usr/lib/firmware/brcm",
        "usr/lib/firmware/cypress", # brcm contains symlinks
        "usr/share/licenses/firmware-linux/LICENCE.broadcom_bcm43xx",
        "usr/share/licenses/firmware-linux/LICENCE.cypress",
    ]

@subpackage("firmware-linux-intel")
def _intel(self):
    self.pkgdesc = f"{pkgdesc} (Intel)"
    self.options = ["!strip", "foreignelf"]

    return [
        "usr/lib/firmware/i915",
        "usr/share/licenses/firmware-linux/LICENSE.i915",
    ]

@subpackage("firmware-linux-nvidia")
def _nvidia(self):
    self.pkgdesc = f"{pkgdesc} (Nvidia)"
    self.options = ["!strip", "foreignelf"]

    return [
        "usr/lib/firmware/nvidia",
        "usr/share/licenses/firmware-linux/LICENCE.nvidia*",
    ]

@subpackage("firmware-linux-network")
def _network(self):
    self.pkgdesc = f"{pkgdesc} (network)"
    self.options = ["!strip", "foreignelf"]

    match self.rparent.profile().arch:
        case "aarch64":
            self.depends += [f"firmware-linux-qualcomm={pkgver}-r{pkgrel}"]

    return [
        "usr/lib/firmware/3com",
        "usr/lib/firmware/RTL8192E",
        "usr/lib/firmware/rt*",
        "usr/lib/firmware/ath*",
        "usr/lib/firmware/ar*",
        "usr/lib/firmware/bnx2*",
        "usr/lib/firmware/cxgb*",
        "usr/lib/firmware/htc*",
        "usr/lib/firmware/iwl*",
        "usr/lib/firmware/intel*",
        "usr/lib/firmware/kaweth",
        "usr/lib/firmware/libertas",
        "usr/lib/firmware/mrvl",
        "usr/lib/firmware/mt*.bin",
        "usr/lib/firmware/ueagle-atm",
        "usr/lib/firmware/ti-connectivity",
        "usr/lib/firmware/dpaa2",
        "usr/lib/firmware/qca",
    ]

@subpackage("firmware-linux-qualcomm")
def _nvidia(self):
    self.pkgdesc = f"{pkgdesc} (Qualcomm SoC)"
    self.options = ["!strip", "brokenlinks", "foreignelf"]
    self.depends = [f"firmware-linux-network={pkgver}-r{pkgrel}"]

    return [
        "usr/lib/firmware/qcom",
    ]
