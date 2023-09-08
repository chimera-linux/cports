pkgname = "firmware-linux-brcm-rpi"
pkgver = "20221215"
pkgrel = 0
archs = ["aarch64"]
replaces = ["firmware-linux-brcm", "firmware-rpi<=20220905-r0"]
replaces_priority = 100  # always overrides files of firmware-linux-brcm
pkgdesc = "Broadcom firmware for Raspberry Pi"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:Broadcom AND custom:Cypress"
url = "https://github.com/raspberrypi/firmware"
source = [
    "!https://raw.githubusercontent.com/RPi-Distro/firmware-nonfree/buster/LICENCE.broadcom_bcm43xx",
    "!https://raw.githubusercontent.com/RPi-Distro/firmware-nonfree/buster/LICENCE.cypress",
    # rpi3 b wifi
    "!https://raw.githubusercontent.com/RPi-Distro/firmware-nonfree/buster/brcm/brcmfmac43430-sdio.bin",
    "!https://raw.githubusercontent.com/RPi-Distro/firmware-nonfree/buster/brcm/brcmfmac43430-sdio.txt",
    # rpi3 b bluetooth
    "!https://raw.githubusercontent.com/RPi-Distro/bluez-firmware/master/broadcom/BCM43430A1.hcd",
    # rpi3 b+ wifi
    "!https://raw.githubusercontent.com/RPi-Distro/firmware-nonfree/buster/brcm/brcmfmac43455-sdio.bin",
    "!https://raw.githubusercontent.com/RPi-Distro/firmware-nonfree/buster/brcm/brcmfmac43455-sdio.txt",
    "!https://raw.githubusercontent.com/RPi-Distro/firmware-nonfree/buster/brcm/brcmfmac43455-sdio.clm_blob",
    # rpi3 b+ bluetooth
    "!https://raw.githubusercontent.com/RPi-Distro/bluez-firmware/master/broadcom/BCM4345C0.hcd",
    # rpi4/400 wifi
    "!https://raw.githubusercontent.com/RPi-Distro/firmware-nonfree/buster/brcm/brcmfmac43456-sdio.bin",
    "!https://raw.githubusercontent.com/RPi-Distro/firmware-nonfree/buster/brcm/brcmfmac43456-sdio.txt",
    "!https://raw.githubusercontent.com/RPi-Distro/firmware-nonfree/buster/brcm/brcmfmac43456-sdio.clm_blob",
    # rpi4/400 bluetooth
    "!https://raw.githubusercontent.com/RPi-Distro/bluez-firmware/master/broadcom/BCM4345C5.hcd",
    "!https://raw.githubusercontent.com/RPi-Distro/bluez-firmware/master/broadcom/BCM43430B0.hcd",
    # rpi zero 2w wifi
    "!https://raw.githubusercontent.com/RPi-Distro/firmware-nonfree/buster/brcm/brcmfmac43436-sdio.bin",
    "!https://raw.githubusercontent.com/RPi-Distro/firmware-nonfree/buster/brcm/brcmfmac43436-sdio.txt",
    "!https://raw.githubusercontent.com/RPi-Distro/firmware-nonfree/buster/brcm/brcmfmac43436-sdio.clm_blob",
    "!https://raw.githubusercontent.com/RPi-Distro/firmware-nonfree/buster/brcm/brcmfmac43436s-sdio.bin",
    "!https://raw.githubusercontent.com/RPi-Distro/firmware-nonfree/buster/brcm/brcmfmac43436s-sdio.txt",
]
sha256 = [
    "b16056fc91b82a0e3e8de8f86c2dac98201aa9dc3cbd33e8d38f1b087fcec30d",
    "ae0db6cc4db33941148df0f67de53e76a77b1b5a46b3165edb7040aa2750015f",
    # rpi3 b wifi
    "023fd9b345fc0bbabae75721bc8702a905077daacc2c36b10b0616fb910e846b",
    "fc3949a4c32f07c18308e7e145c7615be314158e7d714a80e04e4791f16495f9",
    # rpi3 b bluetooth
    "c096ad4a5c3f06ed7d69eba246bf89ada9acba64a5b6f51b1e9c12f99bb1e1a7",
    # rpi3 b+ wifi
    "cf79e8e8727d103a94cd243f1d98770fa29f5da25df251d0d31b3696f3b4ac6a",
    "ca709be81a78bdb6932936374f39943acbd7af07fae6151011127599a3ce9e3d",
    "2dbd7d22fc9af0eb560ceab45b19646d211bc7b34a1dd00c6bfac5dd6ba25e8a",
    # rpi3 b+ bluetooth
    "51c45e77ddad91a19e96dc8fb75295b2087c279940df2634b23baf71b6dea42c",
    # rpi4/400 wifi
    "ddf83f2100885b166be52d21c8966db164fdd4e1d816aca2acc67ee9cc28d726",
    "44e0bb322dc1f39a4b0a89f30ffdd28bc93f7d7aaf534d06d229fe56f6198194",
    "2dbd7d22fc9af0eb560ceab45b19646d211bc7b34a1dd00c6bfac5dd6ba25e8a",
    # rpi4/400 bluetooth
    "fb9f4ec2df5301bd35f416384e103c012c5983024c49aa72fbbaf90177512caa",
    "338c2c6631131f516bfc7e64ef0872bd0402e1f98ef9d0c900eef0c814d90a25",
    # rpi zero 2w wifi
    "6dc7b3b53a1b69637a9e10e675e73ef56ca689d5bd279b78bd2f2719970cb80b",
    "67b0e325bf76d096ce06044d2a442b95626f274096ce5724daaa8bcdd179b599",
    "fce7cbb62ffa6a5a65ca97b13f6fbf28d06c02d986c2072d65bf72164755fc34",
    "bdc4fc14ca428130f474bb2f8bcb34c0684b0f9a0f31b05b4da39d64a2e1a333",
    "0441797884bbbd40a86e4579ff0e1c84ce69bb41f7bcf902a5c867ebb79b6ac3",
]
options = ["!strip", "foreignelf", "execstack"]


def do_install(self):
    inp = self.sources_path

    self.install_license(inp / "LICENCE.broadcom_bcm43xx")
    self.install_license(inp / "LICENCE.cypress")
    # rpi3 b wifi
    self.install_file(inp / "brcmfmac43430-sdio.bin", "usr/lib/firmware/brcm")
    self.install_file(inp / "brcmfmac43430-sdio.txt", "usr/lib/firmware/brcm")
    # rpi3 b bluetooth
    self.install_file(inp / "BCM43430A1.hcd", "usr/lib/firmware/brcm")
    # rpi3 b+ wifi
    self.install_file(inp / "brcmfmac43455-sdio.bin", "usr/lib/firmware/brcm")
    self.install_file(inp / "brcmfmac43455-sdio.txt", "usr/lib/firmware/brcm")
    self.install_file(
        inp / "brcmfmac43455-sdio.clm_blob", "usr/lib/firmware/brcm"
    )
    # rpi3 b+ bluetooth
    self.install_file(inp / "BCM4345C0.hcd", "usr/lib/firmware/brcm")
    # rpi4/400 wifi
    self.install_file(inp / "brcmfmac43456-sdio.bin", "usr/lib/firmware/brcm")
    self.install_file(inp / "brcmfmac43456-sdio.txt", "usr/lib/firmware/brcm")
    self.install_file(
        inp / "brcmfmac43456-sdio.clm_blob", "usr/lib/firmware/brcm"
    )
    # rpi4/400 bluetooth
    self.install_file(inp / "BCM4345C5.hcd", "usr/lib/firmware/brcm")
    self.install_file(inp / "BCM43430B0.hcd", "usr/lib/firmware/brcm")
    # rpi zero 2w wifi
    self.install_file(inp / "brcmfmac43436-sdio.bin", "usr/lib/firmware/brcm")
    self.install_file(inp / "brcmfmac43436-sdio.txt", "usr/lib/firmware/brcm")
    self.install_file(
        inp / "brcmfmac43436-sdio.clm_blob", "usr/lib/firmware/brcm"
    )
    self.install_file(inp / "brcmfmac43436s-sdio.bin", "usr/lib/firmware/brcm")
    self.install_file(inp / "brcmfmac43436s-sdio.txt", "usr/lib/firmware/brcm")
