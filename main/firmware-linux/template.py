# also update ucode-amd when updating
pkgname = "firmware-linux"
pkgver = "20251011"
pkgrel = 0
hostmakedepends = ["rdfind"]
pkgdesc = "Binary firmware blobs for the Linux kernel"
license = "custom:linux-firmware"
url = "https://www.kernel.org"
# stuck and eventually generates 502
# source = f"https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/snapshot/linux-firmware-{pkgver}.tar.gz"
source = f"https://gitlab.com/kernel-firmware/linux-firmware/-/archive/{pkgver}.tar.gz"
sha256 = "96d11031a0dac837fd05ac711d5515ce35e18851b79fc61f0fce4de35553915e"
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
    ("aeonsemi", "Aeonsemi Ethernet PHY", None, "network", ["aeonsemi"]),
    ("airoha", "Airoha Ethernet PHY", None, "network", ["airoha"]),
    ("amd-ucode", "AMD CPU microcode", _arch_x86, "misc", ["amd-ucode"]),
    ("amd-sev", "AMD SEV firmware", _arch_x86, "misc", ["amd"]),
    ("amdgpu", "Newer AMD GPUs", None, "gpu", ["amdgpu"]),
    ("amdnpu", "AMD AI junk", None, "misc", ["amdnpu"]),
    ("amphion", "i.MX8Q VPU", _arch_arm64, "misc", ["amphion"]),
    ("amdtee", "AMD ASP TEE", _arch_x86, "misc", ["amdtee"]),
    (
        "amlogic-bt",
        "Amlogic Bluetooth",
        None,
        "network",
        ["amlogic/aml_w*_bt_uart.bin*"],
    ),
    ("ar3k", "Atheros AR3K Bluetooth", None, "network", ["ar3k"]),
    ("ar3011", "AR3011 Bluetooth", None, "network", ["ath3k*.fw*"]),
    ("ar5523", "AR5523 WLAN", None, "network", ["ar5523.bin*"]),
    ("ar9170", "AR9170 WLAN", None, "network", ["ar9170*.fw*", "carl9170*"]),
    ("ath6k", "AR6000x WLAN", None, "network", ["ath6k"]),
    (
        "ath9k_htc",
        "AR7010/9271 WLAN",
        None,
        "network",
        ["ar*.fw*", "ath9k_htc", "htc_*.fw*"],
    ),
    ("ath10k", "ath10k WLAN", None, "network", ["ath10k"]),
    ("ath11k", "ath11k WLAN", None, "network", ["ath11k"]),
    ("ath12k", "ath12k WLAN", None, "network", ["ath12k"]),
    ("atwilc", "Atmel WILC WLAN", None, "network", ["atmel"]),
    ("atusb", "ATUSB IEEE 802.15.4 transceiver", None, "network", ["atusb"]),
    ("bmi260", "BMI260 Inertial Measurement Unit", None, "misc", ["bmi260*"]),
    ("bnx2", "BNX2 1Gb Ethernet", None, "network", ["bnx2"]),
    ("bnx2x", "BNX2 10Gb Ethernet", None, "network", ["bnx2x"]),
    ("brcm", "Broadcom WLAN/Bluetooth", None, "network", ["brcm", "cypress"]),
    (
        "ca0132",
        "Creative CA0132 HD Audio codec",
        None,
        "audio",
        [
            "ctefx.bin*",
            "ctspeq.bin*",
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
    ("cs35l54", "Cirrus CS35L54 amplifier", None, "audio", ["cirrus/cs35l54*"]),
    ("cs35l56", "Cirrus CS35L56 amplifier", None, "audio", ["cirrus/cs35l56*"]),
    ("cs42l43", "Cirrus CS42L43 amplifier", None, "audio", ["cs42l43.bin*"]),
    ("cxgb3", "Chelsio T3 10Gb Ethernet", None, "network", ["cxgb3"]),
    ("cxgb4", "Chelsio T4/5/6 Ethernet", None, "network", ["cxgb4"]),
    ("cw1200", "ST-E CW1200 WLAN", None, "network", ["wsm_22.bin*"]),
    ("dpaa2", "NXP DPAA2", _arch_arm64, "misc", ["dpaa2"]),
    (
        "dvb",
        "Misc DVB devices",
        None,
        "misc",
        [
            "as102*.hex*",
            "dvb-*.fw*",
            "v4l-cx*.fw*",
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
    ("hfi1", "Intel OPA hfi1", _arch_x86, "network", ["hfi1_*.fw*"]),
    # comes first because it needs some stuff from i915
    (
        "xe",
        "Intel Xe GPUs",
        None,
        "gpu",
        [
            "i915/bmg*",  # battlemage
            "i915/dg*",  # dg1 and dg2
            "xe",
        ],
    ),
    ("i915", "Intel GPUs", _arch_x86, "gpu", ["i915"]),
    (
        "intel-audio",
        "Intel audio",
        _arch_x86,
        "audio",
        [
            "intel/IntcSST2.bin*",
            "intel/dsp_fw_*.bin*",
            "intel/fw_sst_*.bin*",
            "intel/avs",
            "intel/catpt",
        ],
    ),
    ("intel-bt", "Intel Bluetooth", _arch_x86, "network", ["intel/ibt*"]),
    ("intel-ice", "Intel E800 series", _arch_x86, "network", ["intel/ice"]),
    (
        "intel-ipu2",
        "Intel IPU2",
        _arch_x86,
        "misc",
        [
            "intel/ipu/shisp_*.bin*",
        ],
    ),
    (
        "intel-ipu3",
        "Intel IPU3",
        _arch_x86,
        "misc",
        [
            "intel/ipu/irci_*.bin*",
            "intel/ipu3-fw.bin*",
            "intel/irci_*.bin*",
        ],
    ),
    (
        "intel-ipu6",
        "Intel IPU6",
        _arch_x86,
        "misc",
        ["intel/ipu/ipu6*.bin*"],
    ),
    (
        "intel-ipu7",
        "Intel IPU7",
        _arch_x86,
        "misc",
        ["intel/ipu/ipu7*.bin*"],
    ),
    (
        "intel-ish",
        "Intel Integrated Sensor Hub",
        _arch_x86,
        "misc",
        ["HP/ish", "LENOVO/ish", "dell/ish", "intel/ish"],
    ),
    (
        "intel-ivsc",
        "Intel Visual Sensing Controller",
        _arch_x86,
        "misc",
        ["intel/vsc"],
    ),
    (
        "intel-vpu",
        "Intel VPU",
        _arch_x86,
        "misc",
        ["intel/vpu"],
    ),
    (
        "inside-secure",
        "Inside Secure SafeXcel",
        None,
        "misc",
        ["inside-secure"],
    ),
    ("isci", "Intel C600 SAS controller", _arch_x86, "storage", ["isci"]),
    ("iwlwifi", "Intel WLAN", None, "network", ["intel/iwlwifi", "iwlwifi*"]),
    ("ixp4xx", "IXP4xx", None, "network", ["ixp4xx"]),
    ("kaweth", "KL5KUSB101 Ethernet", None, "network", ["kaweth"]),
    ("keyspan", "Keyspan serial converters", None, "misc", ["keyspan*"]),
    ("korg", "Korg audio interfaces", None, "audio", ["korg"]),
    ("lgs8g75", "Legend Silicon LGS8GXX", None, "misc", ["lgs8g75.fw*"]),
    ("liquidio", "Cavium LiquidIO NICs", None, "network", ["liquidio"]),
    (
        "lt9611uxc",
        "LT9611UXC DSI to HDMI",
        None,
        "misc",
        ["lt9611uxc_fw.bin*"],
    ),
    ("mali", "ARM Mali GPUs", _arch_arm64, "gpu", ["arm/mali"]),
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
            "vpu_*.bin*",
        ],
    ),
    (
        "mediatek",
        "Mediatek WLAN/Bluetooth",
        None,
        "network",
        ["mediatek", "mt7*.bin*"],
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
        ["mrvl", "lbtf_usb.bin*", "libertas", "mwl8k"],
    ),
    ("multitech", "Multi-Tech modems", None, "network", ["mts_*.fw*"]),
    (
        "myricom",
        "Myricom Ethernet NICs",
        None,
        "network",
        ["myri10ge*", "myricom"],
    ),
    ("nfp", "Netronome Flow Processor", None, None, ["netronome"]),
    ("nxp-uwb", "NXP UWB firmware", None, "network", ["nxp/sr150_fw.bin*"]),
    (
        "nxp-bt",
        "NXP BT chipsets",
        None,
        "network",
        [
            "nxp/helper_uart*.bin*",
            "nxp/uartiw*.bin*",
            "nxp/uartspi*.se*",
            "nxp/uartuart*",
        ],
    ),
    (
        "nvidia-gsp",
        "Nvidia GSP",
        None,
        "gpu",
        ["nvidia/*/gsp"],
    ),
    ("nvidia", "Nvidia GPUs", None, "gpu", ["nvidia"]),
    ("powervr", "PowerVR GPUs", None, "gpu", ["powervr"]),
    (
        "qat",
        "Intel QuickAssist Technology",
        _arch_x86,
        "misc",
        ["intel/qat", "qat*"],
    ),
    ("qca", "Qualcomm Atheros WLAN/Bluetooth", None, "network", ["qca"]),
    ("qcom", "Qualcomm SoCs", _arch_arm64, "soc", ["a300_*.fw*", "qcom"]),
    (
        "qlogic",
        "QLogic HBAs",
        None,
        "network",
        [
            "cbfw*.bin*",
            "ct2fw*.bin*",
            "ctfw*.bin*",
            "qed",
            "ql2*.bin*",
            "qlogic",
            "phanfw.bin*",
        ],
    ),
    ("radeon", "Older AMD GPUs", None, "gpu", ["radeon"]),
    ("ralink", "Ralink WLAN", None, "network", ["rt*.bin*"]),
    ("rockchip", "Rockchip SoCs", _arch_arm64, "soc", ["rockchip"]),
    ("rp2", "Comtrol RocketPort 2", None, "misc", ["rp2.fw*"]),
    ("rsi", "Redpine RSI91X WLAN/Bluetooth", None, "network", ["rsi*"]),
    ("rt1320", "Realtek sound MCU", None, "audio", ["realtek/rt1320"]),
    ("rtl_bt", "Realtek Bluetooth", None, "network", ["rtl_bt"]),
    ("rtl_nic", "Realtek Ethernet", None, "network", ["rtl_nic"]),
    (
        "rtlwifi",
        "Realtek WLAN",
        None,
        "network",
        ["rtlwifi", "rtw88", "rtw89"],
    ),
    (
        "sagrad",
        "Sagrad SG901-1091/1098 WLAN",
        None,
        "network",
        ["sdd_sagrad_*.bin*"],
    ),
    (
        "sensoray",
        "Sensoray webcams",
        None,
        "misc",
        [
            "f2255usb.bin*",
            "s2250*.fw*",
        ],
    ),
    (
        "s5p-mfc",
        "Samsung Multi Format Codec",
        _arch_arm64,
        "misc",
        ["s5p-mfc*.fw*"],
    ),
    ("siano", "Siano DTV", None, "misc", ["sms1xxx*.fw*", "*.inp*"]),
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
    ("ti-serial", "TI USB 3410/5052", None, "misc", ["ti_*.fw*"]),
    (
        "ti-tas",
        "Texas Instruments amplifiers",
        None,
        "audio",
        ["INT88*", "TAS2*", "TIAS2*", "TXNW*", "ti/tas*"],
    ),
    ("tigon", "Tigon I/II/III Ethernet", None, "network", ["acenic", "tigon"]),
    (
        "tsse",
        "Mont-TSSE crypto algorithm accelerator",
        None,
        "misc",
        ["tsse_firmware.bin*"],
    ),
    ("typhoon", "3Com Typhoon Ethernet", None, "network", ["3com"]),
    ("ueagle-atm", "Eagle USB modems", None, "network", ["ueagle-atm"]),
    ("vicam", "ViCam USB camera", None, "misc", ["vicam"]),
    ("vntwusb", "Via VNT6656 USB WLAN", None, "network", ["vntwusb.fw*"]),
    (
        "vsc85xx",
        "Microchip VSX85xx Ethernet PHYs",
        None,
        "network",
        ["microchip/mscc_vsc85*.bin*"],
    ),
    ("vxge", "Exar X3100 10Gb Ethernet", None, "network", ["vxge"]),
    ("wave521c", "WAVE521C encoder IP", None, "misc", ["cnm/wave521c*"]),
    ("wave633c", "WAVE633C codec IP", None, "misc", ["cnm/wave633c*"]),
    ("whiteheat", "WhiteHEAT USB-Serial", None, "misc", ["whiteheat*"]),
    ("wil6210", "Qualcomm wil6210 60GHz WLAN", None, "network", ["wil6210*"]),
    ("wfx", "Silicon Laboratories WFx WLAN", None, "network", ["wfx"]),
    ("yamaha", "Yamaha audio drivers", None, "audio", ["yamaha"]),
]


def install(self):
    self.install_dir("usr/lib/firmware")
    self.do(
        "./copy-firmware.sh",
        "--zstd",
        "-v",
        str(self.chroot_destdir / "usr/lib/firmware"),
        env={
            "ZSTD_CLEVEL": "9",
            "ZSTD_NBTHREADS": str(min(4, self.make_jobs)),
        },
    )
    self.do(
        "./dedup-firmware.sh",
        "-v",
        str(self.chroot_destdir / "usr/lib/firmware"),
    )

    self.install_license("WHENCE")

    for lc in self.cwd.glob("LICEN*"):
        self.install_license(lc)


# remove unused junk
def post_install(self):
    # deprecated driver
    self.uninstall("usr/lib/firmware/av7110")
    # pcmcia stuff unlikely to ever be used
    self.uninstall("usr/lib/firmware/cis")
    # only present in ancient kernels
    self.uninstall("usr/lib/firmware/dabusb")
    # m68k-specific
    self.uninstall("usr/lib/firmware/dsp56k")
    # 32-bit imx6/7
    self.uninstall("usr/lib/firmware/imx")
    # not mainline
    self.uninstall("usr/lib/firmware/mwlwifi")
    # not in our kernels, mostly 32-bit socs etc.
    self.uninstall("usr/lib/firmware/ositech")
    self.uninstall("usr/lib/firmware/r128")
    self.uninstall("usr/lib/firmware/r8a779x_usb3_v1.dlmem*", glob=True)
    self.uninstall("usr/lib/firmware/r8a779x_usb3_v2.dlmem*", glob=True)
    self.uninstall("usr/lib/firmware/r8a779x_usb3_v3.dlmem*", glob=True)
    self.uninstall("usr/lib/firmware/sb16")
    self.uninstall("usr/lib/firmware/sxg")
    self.uninstall("usr/lib/firmware/ti-keystone")
    self.uninstall("usr/lib/firmware/ti/vpdma-1b8.bin*", glob=True)
    self.uninstall("usr/lib/firmware/usbdux_firmware.bin*", glob=True)
    self.uninstall("usr/lib/firmware/usbduxfast_firmware.bin*", glob=True)
    self.uninstall("usr/lib/firmware/usbduxsigma_firmware.bin*", glob=True)
    self.uninstall("usr/lib/firmware/yam")

    # fix up nvidia gsp firmware links to allow take() to function correctly
    def _fixup_gsp(f):
        # base path
        if not f.is_symlink():
            return
        # read what it should be pointing to
        bp = f.readlink()
        # remove the symlink and replace it with a directory
        f.unlink()
        f.mkdir(mode=0o755)
        # make the gsp symlink inside, using the base path
        (f / "gsp").symlink_to(f"../{bp}/gsp")

    # now do the fixups for relevant firmware, only stuff that *only* has
    # gsp has toplevel links that we want to replace to avoid confusing apk
    for f in (self.destdir / "usr/lib/firmware/nvidia").glob("ad*"):
        _fixup_gsp(f)
    for f in (self.destdir / "usr/lib/firmware/nvidia").glob("gb*"):
        _fixup_gsp(f)


@subpackage("firmware-linux-audio")
def _(self):
    self.subdesc = "audio"
    self.options = ["empty"]
    self.install_if = [self.with_pkgver("base-firmware-linux")]

    return []


@subpackage("firmware-linux-gpu")
def _(self):
    self.subdesc = "graphics"
    self.options = ["empty"]
    self.install_if = [self.with_pkgver("base-firmware-linux")]

    return []


@subpackage("firmware-linux-network")
def _(self):
    self.subdesc = "network devices"
    self.options = ["empty"]
    self.install_if = [self.with_pkgver("base-firmware-linux")]

    return []


@subpackage("firmware-linux-storage")
def _(self):
    self.subdesc = "storage devices"
    self.options = ["empty"]
    self.install_if = [self.with_pkgver("base-firmware-linux")]

    return []


@subpackage("firmware-linux-misc")
def _(self):
    self.subdesc = "misc"
    self.options = ["empty"]
    self.install_if = [self.parent]

    return []


@subpackage("firmware-linux-soc")
def _(self):
    self.subdesc = "systems on chip"
    self.options = ["empty"]
    self.install_if = [self.parent]

    return []


@subpackage("firmware-linux-meta")
def _(self):
    self.subdesc = "base metapackage"
    self.options = ["empty"]
    self.install_if = [self.parent]
    # transitional
    self.provides = [self.with_pkgver("base-firmware-linux")]

    return []


def _gen_pkg(name, desc, iifcond, iifpkg, cont):
    @subpackage(f"firmware-linux-{name}")
    def _(self):
        self.subdesc = desc
        self.options = ["!strip", "foreignelf", "execstack"]

        if (iifcond is None or iifcond) and iifpkg:
            self.install_if = [self.with_pkgver(f"firmware-linux-{iifpkg}")]

        return list(map(lambda p: f"usr/lib/firmware/{p}", cont))


# generate subpackages
for _tup in _pkgs:
    _gen_pkg(*_tup)
