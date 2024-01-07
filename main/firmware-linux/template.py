# also update ucode-amd when updating
pkgname = "firmware-linux"
pkgver = "20231211"
pkgrel = 1
hostmakedepends = ["python", "rdfind"]
pkgdesc = "Binary firmware blobs for the Linux kernel"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:linux-firmware"
url = "https://www.kernel.org"
source = f"https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/snapshot/linux-firmware-{pkgver}.tar.gz"
sha256 = "d0ba54f05f5dd34b0fc5a1e1970cd9cbc48491d2da97f3798a9e13530dc18298"
options = ["empty"]

_arch = self.profile().arch
_arch_x86 = _arch == "x86_64"
_arch_arm64 = _arch == "aarch64"
# These together make up the complete contents; there must be nothing
# left in the main package. The fields are:
#
# name | description | install-if condition | install-if parent | contents
_pkgs = [
    ("advansys", "Advansys SCSI", None, "storage", ["advansys"]),
    ("airoha", "Airoha Ethernet PHY", None, "network", ["airoha"]),
    ("amd-ucode", "AMD CPU microcode", _arch_x86, "misc", ["amd-ucode"]),
    ("amd-sev", "AMD SEV firmware", _arch_x86, "misc", ["amd"]),
    ("amdgpu", "Newer AMD GPUs", None, "gpu", ["amdgpu"]),
    ("amphion", "i.MX8Q VPU", _arch_arm64, "misc", ["amphion"]),
    ("amdtee", "AMD ASP TEE", _arch_x86, "misc", ["amdtee"]),
    ("amlogic-bt", "Amlogic Bluetooth", None, "network", ["amlogic/bluetooth"]),
    ("ar3k", "Atheros AR3K Bluetooth", None, "network", ["ar3k"]),
    ("ar3011", "AR3011 Bluetooth", None, "network", ["ath3k*.fw"]),
    ("ar5523", "AR5523 WLAN", None, "network", ["ar5523.bin"]),
    ("ar9170", "AR9170 WLAN", None, "network", ["ar9170*.fw", "carl9170*"]),
    ("ath6k", "AR6000x WLAN", None, "network", ["ath6k"]),
    (
        "ath9k_htc",
        "AR7010/9271 WLAN",
        None,
        "network",
        ["ar*.fw", "ath9k_htc", "htc_*.fw"],
    ),
    ("ath10k", "ath10k WLAN", None, "network", ["ath10k"]),
    ("ath11k", "ath11k WLAN", None, "network", ["ath11k"]),
    ("atwilc", "Atmel WILC WLAN", None, "network", ["atmel"]),
    ("atusb", "ATUSB IEEE 802.15.4 transceiver", None, "network", ["atusb"]),
    ("bnx2", "BNX2 1Gb Ethernet", None, "network", ["bnx2"]),
    ("bnx2x", "BNX2 10Gb Ethernet", None, "network", ["bnx2x"]),
    ("brcm", "Broadcom WLAN/Bluetooth", None, "network", ["brcm", "cypress"]),
    (
        "ca0132",
        "Creative CA0132 HD Audio codec",
        None,
        "audio",
        [
            "ctefx.bin",
            "ctspeq.bin",
        ],
    ),
    ("cassini", "Sun Cassini Ethernet", None, "network", ["sun/cassini*"]),
    (
        "cnn55xx",
        "Cavium CNN55XX crypto accelerator",
        None,
        "misc",
        ["cavium/cnn55xx*"],
    ),
    ("cpia2", "STM CPIA2 cameras", None, "misc", ["cpia2"]),
    ("cs35l41", "Cirrus CS35L41 amplifier", None, "audio", ["cirrus/cs35l41*"]),
    ("cxgb3", "Chelsio T3 10Gb Ethernet", None, "network", ["cxgb3"]),
    ("cxgb4", "Chelsio T4/5/6 Ethernet", None, "network", ["cxgb4"]),
    ("cw1200", "ST-E CW1200 WLAN", None, "network", ["wsm_22.bin"]),
    ("dpaa2", "NXP DPAA2", _arch_arm64, "misc", ["dpaa2"]),
    (
        "dvb",
        "Misc DVB devices",
        None,
        "misc",
        [
            "as102*.hex",
            "dvb-*.fw",
            "v4l-cx*.fw",
            "tlg2300*",
            "ttusb-budget",
        ],
    ),
    ("e100", "Intel PRO/100 Ethernet", None, "network", ["e100"]),
    ("edgeport", "Edgeport USB Serial Converter", None, "misc", ["edgeport"]),
    ("emi", "Emagic EMI audo interfaces", None, "misc", ["emi26", "emi62"]),
    ("ene-ub6250", "ENE UB6250 SD card reader", None, "misc", ["ene-ub6250"]),
    ("ess", "ESS audio controllers", None, "audio", ["ess"]),
    ("go7007", "WIS GO7007 MPEG encoder", None, "misc", ["go7007"]),
    ("hermes", "Orinoco Hermes WLAN", None, "network", ["agere*"]),
    ("hfi1", "Intel OPA hfi1", _arch_x86, "network", ["hfi1_*.fw"]),
    ("i915", "Intel GPUs", _arch_x86, "gpu", ["i915"]),
    (
        "intel-audio",
        "Intel audio",
        _arch_x86,
        "audio",
        [
            "intel/IntcSST2.bin",
            "intel/dsp_fw_*.bin",
            "intel/fw_sst_*.bin*",
            "intel/avs",
            "intel/catpt",
        ],
    ),
    ("intel-bt", "Intel Bluetooth", _arch_x86, "network", ["intel/ibt*"]),
    ("intel-ice", "Intel E800 series", _arch_x86, "network", ["intel/ice"]),
    (
        "intel-ipu3",
        "Intel IPU3",
        _arch_x86,
        "misc",
        [
            "intel/ipu3-fw.bin",
            "intel/irci_*.bin",
        ],
    ),
    (
        "inside-secure",
        "Inside Secure SafeXcel",
        None,
        "misc",
        ["inside-secure"],
    ),
    ("isci", "Intel C600 SAS controller", _arch_x86, "storage", ["isci"]),
    ("iwlwifi", "Intel WLAN", _arch_x86, "network", ["iwlwifi*"]),
    ("ixp4xx", "IXP4xx", None, "network", ["ixp4xx"]),
    ("kaweth", "KL5KUSB101 Ethernet", None, "network", ["kaweth"]),
    ("keyspan", "Keyspan serial converters", None, "misc", ["keyspan*"]),
    ("korg", "Korg audio interfaces", None, "audio", ["korg"]),
    ("lgs8g75", "Legend Silicon LGS8GXX", None, "misc", ["lgs8g75.fw"]),
    ("liquidio", "Cavium LiquidIO NICs", None, "network", ["liquidio"]),
    ("lt9611uxc", "LT9611UXC DSI to HDMI", None, "misc", ["lt9611uxc_fw.bin"]),
    ("matrox", "Matrox G200/400", None, "gpu", ["matrox"]),
    (
        "mediatek-soc",
        "Mediatek SoCs",
        _arch_arm64,
        "soc",
        [
            "mediatek/mt798*",
            "mediatek/mt81*",
            "mediatek/sof",
            "vpu_*.bin",
        ],
    ),
    (
        "mediatek",
        "Mediatek WLAN/Bluetooth",
        None,
        "network",
        ["mediatek", "mt7*.bin"],
    ),
    ("mellanox", "Mellanox Ethernet", None, "network", ["mellanox"]),
    (
        "meson-vdec",
        "Amlogic Meson decoders",
        _arch_arm64,
        "misc",
        ["meson/vdec"],
    ),
    (
        "mhdp8546",
        "Cadence MHDP8546 DP bridge",
        None,
        "misc",
        ["cadence/mhdp8546*"],
    ),
    ("moxa", "Moxa USB-Serial hubs", None, "misc", ["moxa"]),
    ("mrvl-cpt", "Marvell Octeon crypto", _arch_arm64, "misc", ["mrvl/cpt*"]),
    (
        "mrvl-prestera",
        "Marvell Prestera switches",
        None,
        None,
        ["mrvl/prestera"],
    ),
    (
        "mrvl",
        "Marvell WLAN/Bluetooth",
        None,
        "network",
        ["mrvl", "lbtf_usb.bin", "libertas", "mwl8k"],
    ),
    ("multitech", "Multi-Tech modems", None, "network", ["mts_*.fw"]),
    (
        "myricom",
        "Myricom Ethernet NICs",
        None,
        "network",
        ["myri10ge*", "myricom"],
    ),
    ("nfp", "Netronome Flow Processor", None, None, ["netronome"]),
    ("nxp-uwb", "NXP UWB firmware", None, "network", ["nxp/sr150_fw.bin"]),
    (
        "nxp-bt",
        "NXP BT chipsets",
        None,
        "network",
        [
            "nxp/helper_uart*.bin",
            "nxp/uartiw*.bin",
            "nxp/uartspi*.se",
            "nxp/uartuart*",
        ],
    ),
    ("nvidia-gsp", "Nvidia GSP", None, "gpu", ["nvidia/*/gsp"]),
    ("nvidia", "Nvidia GPUs", None, "gpu", ["nvidia"]),
    ("powervr", "PowerVR GPUs", None, "gpu", ["powervr"]),
    ("qat", "Intel QuickAssist Technology", _arch_x86, "misc", ["qat*"]),
    ("qca", "Qualcomm Atheros WLAN/Bluetooth", None, "network", ["qca"]),
    ("qcom", "Qualcomm SoCs", _arch_arm64, "soc", ["a300_*.fw", "qcom"]),
    (
        "qlogic",
        "QLogic HBAs",
        None,
        "network",
        [
            "cbfw*.bin",
            "ct2fw*.bin",
            "ctfw*.bin",
            "qed",
            "ql2*.bin",
            "qlogic",
            "phanfw.bin",
        ],
    ),
    ("radeon", "Older AMD GPUs", None, "gpu", ["radeon"]),
    ("ralink", "Ralink WLAN", None, "network", ["rt*.bin"]),
    ("rockchip", "Rockchip SoCs", _arch_arm64, "soc", ["rockchip"]),
    ("rp2", "Comtrol RocketPort 2", None, "misc", ["rp2.fw"]),
    ("rsi", "Redpine RSI91X WLAN/Bluetooth", None, "network", ["rsi*"]),
    ("rtl_bt", "Realtek Bluetooth", None, "network", ["rtl_bt"]),
    ("rtl_nic", "Realtek Ethernet", None, "network", ["rtl_nic"]),
    (
        "rtlwifi",
        "Realtek WLAN",
        None,
        "network",
        ["RTL8192E", "rtlwifi", "rtw88", "rtw89"],
    ),
    (
        "sagrad",
        "Sagrad SG901-1091/1098 WLAN",
        None,
        "network",
        ["sdd_sagrad_*.bin"],
    ),
    (
        "sensoray",
        "Sensoray webcams",
        None,
        "misc",
        [
            "f2255usb.bin",
            "s2250*.fw",
        ],
    ),
    (
        "s5p-mfc",
        "Samsung Multi Format Codec",
        _arch_arm64,
        "misc",
        ["s5p-mfc*.fw"],
    ),
    ("siano", "Siano DTV", None, "misc", ["sms1xxx*.fw", "*.inp"]),
    ("slicoss", "Alacritech Slicoss NICs", None, "network", ["slicoss"]),
    (
        "starfire",
        "Adaptec Starfire Ethernet",
        None,
        "network",
        ["adaptec/starfire*"],
    ),
    ("tehuti", "Tehuti 10GbE NICs", None, "network", ["tehuti"]),
    (
        "ti-connectivity",
        "TI WLAN/Bluetooth",
        None,
        "network",
        ["ti-connectivity"],
    ),
    ("ti-serial", "TI USB 3410/5052", None, "misc", ["ti_*.fw"]),
    ("tigon", "Tigon I/II/III Ethernet", None, "network", ["acenic", "tigon"]),
    ("typhoon", "3Com Typhoon Ethernet", None, "network", ["3com"]),
    ("ueagle-atm", "Eagle USB modems", None, "network", ["ueagle-atm"]),
    ("vicam", "ViCam USB camera", None, "misc", ["vicam"]),
    ("vntwusb", "Via VNT6656 USB WLAN", None, "network", ["vntwusb.fw"]),
    (
        "vsc85xx",
        "Microchip VSX85xx Ethernet PHYs",
        None,
        "network",
        ["microchip/mscc_vsc85*.bin"],
    ),
    ("vxge", "Exar X3100 10Gb Ethernet", None, "network", ["vxge"]),
    ("wave521c", "WAVE521C encoder IP", None, "misc", ["cnm/wave521c*"]),
    ("whiteheat", "WhiteHEAT USB-Serial", None, "misc", ["whiteheat*"]),
    ("wil6210", "Qualcomm wil6210 60GHz WLAN", None, "network", ["wil6210*"]),
    ("wfx", "Silicon Laboratories WFx WLAN", None, "network", ["wfx"]),
    ("yamaha", "Yamaha audio drivers", None, "audio", ["yamaha"]),
]


def do_install(self):
    self.install_dir("usr/lib/firmware")
    self.do(
        "./copy-firmware.sh",
        "-v",
        str(self.chroot_destdir / "usr/lib/firmware"),
    )

    self.install_license("WHENCE")

    for lc in self.cwd.glob("LICEN*"):
        self.install_license(lc)


# remove unused junk
def post_install(self):
    dp = self.destdir / "usr/lib/firmware"
    # deprecated driver
    self.rm(dp / "av7110", recursive=True)
    # pcmcia stuff unlikely to ever be used
    self.rm(dp / "cis", recursive=True)
    # only present in ancient kernels
    self.rm(dp / "dabusb", recursive=True)
    # m68k-specific
    self.rm(dp / "dsp56k", recursive=True)
    # 32-bit imx6/7
    self.rm(dp / "imx", recursive=True)
    # not mainline
    self.rm(dp / "mwlwifi", recursive=True)
    # not in our kernels, mostly 32-bit socs etc.
    self.rm(dp / "ositech", recursive=True)
    self.rm(dp / "r128", recursive=True)
    self.rm(dp / "r8a779x_usb3_v1.dlmem")
    self.rm(dp / "r8a779x_usb3_v2.dlmem")
    self.rm(dp / "r8a779x_usb3_v3.dlmem")
    self.rm(dp / "sb16", recursive=True)
    self.rm(dp / "sxg", recursive=True)
    self.rm(dp / "ti-keystone", recursive=True)
    self.rm(dp / "ti/vpdma-1b8.bin")
    self.rm(dp / "usbdux_firmware.bin")
    self.rm(dp / "usbduxfast_firmware.bin")
    self.rm(dp / "usbduxsigma_firmware.bin")
    self.rm(dp / "yam", recursive=True)


@subpackage("firmware-linux-audio")
def _audio(self):
    self.pkgdesc = f"{pkgdesc} (audio)"
    self.options = ["empty"]
    self.install_if = [f"base-firmware-linux={pkgver}-r{pkgrel}"]

    return []


@subpackage("firmware-linux-gpu")
def _gpu(self):
    self.pkgdesc = f"{pkgdesc} (graphics)"
    self.options = ["empty"]
    self.install_if = [f"base-firmware-linux={pkgver}-r{pkgrel}"]

    return []


@subpackage("firmware-linux-network")
def _net(self):
    self.pkgdesc = f"{pkgdesc} (network devices)"
    self.options = ["empty"]
    self.install_if = [f"base-firmware-linux={pkgver}-r{pkgrel}"]

    return []


@subpackage("firmware-linux-storage")
def _storage(self):
    self.pkgdesc = f"{pkgdesc} (storage devices)"
    self.options = ["empty"]
    self.install_if = [f"base-firmware-linux={pkgver}-r{pkgrel}"]

    return []


@subpackage("firmware-linux-misc")
def _misc(self):
    self.pkgdesc = f"{pkgdesc} (misc)"
    self.options = ["empty"]
    self.install_if = [f"firmware-linux={pkgver}-r{pkgrel}"]

    return []


@subpackage("firmware-linux-soc")
def _soc(self):
    self.pkgdesc = f"{pkgdesc} (systems on chip)"
    self.options = ["empty"]
    self.install_if = [f"firmware-linux={pkgver}-r{pkgrel}"]

    return []


@subpackage("base-firmware-linux")
def _base(self):
    self.pkgdesc = f"{pkgdesc} (base metapackage)"
    self.options = ["empty"]
    self.install_if = [f"firmware-linux={pkgver}-r{pkgrel}"]

    return []


def _gen_pkg(name, desc, iifcond, iifpkg, cont):
    @subpackage(f"firmware-linux-{name}")
    def _sub(self):
        self.pkgdesc = f"{pkgdesc} ({desc})"
        self.options = ["!strip", "foreignelf", "execstack"]

        if (iifcond is None or iifcond) and iifpkg:
            self.install_if = [f"firmware-linux-{iifpkg}={pkgver}-r{pkgrel}"]

        return list(map(lambda p: f"usr/lib/firmware/{p}", cont))


# generate subpackages
for _tup in _pkgs:
    _gen_pkg(*_tup)
