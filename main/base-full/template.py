pkgname = "base-full"
pkgver = "0.2"
pkgrel = 4
build_style = "meta"
depends = ["base-core"]
pkgdesc = "Chimera base package for bare metal and virtual machines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


@subpackage("base-full-firmware")
def _fw(self):
    self.pkgdesc = f"{pkgdesc} (firmware)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "base-firmware-linux",
        "firmware-ipw2100",
        "firmware-ipw2200",
        "firmware-zd1211",
    ]
    if self.rparent.profile().arch == "x86_64":
        self.depends += ["base-firmware-sof"]
    return []


@subpackage("base-full-locale")
def _locale(self):
    self.pkgdesc = f"{pkgdesc} (locale)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "base-locale",
    ]
    return []


@subpackage("base-full-misc")
def _misc(self):
    self.pkgdesc = f"{pkgdesc} (miscellaneous)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "chimera-artwork",
        "chrony",
        "nano",
        "syslog-ng",
        "zramctl",
        "opendoas",
        "usbutils",
    ]
    return []


@subpackage("base-full-session")
def _session(self):
    self.pkgdesc = f"{pkgdesc} (session management)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "elogind-meta",
        "dbus",
    ]
    return []


@subpackage("base-full-net")
def _net(self):
    self.pkgdesc = f"{pkgdesc} (network)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "ethtool",
        "dhcpcd",
        "iwd",
        "openssh",
        "rfkill",
    ]
    return []
