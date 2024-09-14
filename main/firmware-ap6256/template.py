pkgname = "firmware-ap6256"
pkgver = "2020.02"
pkgrel = 0
_commit = "056d5f6776e515f90bbbbead1be06857aaef17d0"
archs = ["aarch64"]
pkgdesc = "Firmware files for AP6256 WiFi/BT module"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = (
    "https://gitlab.manjaro.org/manjaro-arm/packages/community/ap6256-firmware"
)
source = f"{url}/-/archive/{_commit}/ap6256-firmware-${_commit}.tar.gz"
sha256 = "e933c27c68102b32cc0e4cb0ea69d8c95cc29d3efe486c4dd78e8af5a13520ad"
options = ["!strip", "foreignelf"]


def install(self):
    destp = "usr/lib/firmware/brcm"
    self.install_file("BCM4345C5.hcd", destp)
    self.install_file(
        "fw_bcm43456c5_ag.bin", destp, name="brcmfmac43456-sdio.bin"
    )
    self.install_file("brcmfmac43456-sdio.clm_blob", destp)
    self.install_file("brcmfmac43456-sdio.AP6256.txt", destp)
    self.install_link(
        f"{destp}/brcmfmac43456-sdio.txt", "brcmfmac43456-sdio.AP6256.txt"
    )
    for ln in [
        "radxa,rockpi4b",
        "radxa,rockpi4c",
        "radxa,zero",
        "radxa,zero2",
        "pine64,pinebook-pro",
        "pine64,rockpro64-v2.1",
        "pine64,quartz64-a",
        "pine64,quartz64-b",
        "rockchip,rk3399-orangepi",
    ]:
        self.install_link(
            f"{destp}/brcmfmac43456-sdio.{ln}.txt",
            "brcmfmac43456-sdio.AP6256.txt",
        )
