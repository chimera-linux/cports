pkgname = "base-full"
pkgver = "0.3"
pkgrel = 0
build_style = "meta"
depends = [
    "base-bootstrap",
    "dinit-chimera",
    "turnstile",
]
provides = [f"base-core={pkgver}-r{pkgrel}"]
pkgdesc = "Chimera base package for bare metal and virtual machines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


@subpackage("base-full-console")
def _console(self):
    self.pkgdesc = f"{pkgdesc} (console tools)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provider_priority = 100
    # transitional
    self.provides = [f"base-core-console={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "console-setup",
        "dmesg",
        "kbd",
        "nyagetty",
    ]
    return []


@subpackage("base-full-core")
def _core(self):
    self.pkgdesc = f"{pkgdesc} (core tools)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provider_priority = 100
    self.depends = [
        "bsdtar",
        "chimera-install-scripts",
        "procps",
    ]
    return []


@subpackage("base-full-firmware")
def _fw(self):
    self.pkgdesc = f"{pkgdesc} (firmware)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provider_priority = 100
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


@subpackage("base-full-fs")
def _fs(self):
    self.pkgdesc = f"{pkgdesc} (filesystem tools)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provider_priority = 100
    # transitional
    self.provides = [f"base-core-fs={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "fdisk",
        "fstrim",
        "mkfs",
        "e2fsprogs",
        "f2fs-tools",
        "xfsprogs",
        "btrfs-progs",
        "dosfstools",
    ]
    match self.rparent.profile().arch:
        case "ppc64" | "ppc":
            # ppc mac disk tools
            self.depends += ["hfsutils", "mac-fdisk"]
    return []


@subpackage("base-full-kernel")
def _kern(self):
    self.pkgdesc = f"{pkgdesc} (kernel tooling)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provider_priority = 100
    # transitional
    self.provides = [f"base-core-kernel={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "base-kernel",
        "initramfs-tools",
    ]
    return []


@subpackage("base-full-locale")
def _locale(self):
    self.pkgdesc = f"{pkgdesc} (locale)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provider_priority = 100
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "base-locale",
    ]
    return []


@subpackage("base-full-man")
def _man(self):
    self.pkgdesc = f"{pkgdesc} (manpages)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provider_priority = 100
    # transitional
    self.provides = [f"base-core-man={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "base-man",
        "man-pages",
    ]
    return []


@subpackage("base-full-misc")
def _misc(self):
    self.pkgdesc = f"{pkgdesc} (miscellaneous)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provider_priority = 100
    # transitional
    self.provides = [f"base-core-misc={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "bc-gh",
        "chimera-artwork",
        "chimerautils-extra",
        "chrony",
        "file",
        "less",
        "lscpu",
        "nano",
        "pciutils",
        "syslog-ng",
        "zramctl",
        "opendoas",
        "usbutils",
    ]
    return []


@subpackage("base-full-net-tools")
def _net_tools(self):
    self.pkgdesc = f"{pkgdesc} (network tools)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provider_priority = 100
    # transitional
    self.provides = [f"base-core-net={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "ethtool",
        "iputils",
        "iproute2",
        "traceroute",
        "iw",
        "rfkill",
    ]
    return []


@subpackage("base-full-net")
def _net(self):
    self.pkgdesc = f"{pkgdesc} (network)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provider_priority = 100
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "dhcpcd",
        "iwd",
        "openssh",
    ]
    return []


@subpackage("base-full-session")
def _session(self):
    self.pkgdesc = f"{pkgdesc} (session management)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provider_priority = 100
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "elogind-meta",
        "dbus",
    ]
    return []


@subpackage("base-full-sound")
def _sound(self):
    self.pkgdesc = f"{pkgdesc} (sound)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provider_priority = 100
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "pipewire",
    ]
    return []


@subpackage("base-minimal")
def _minimal(self):
    self.pkgdesc = f"{pkgdesc} (metapackage for small installations)"
    self.provides = [
        f"base-full-firmware={pkgver}-r{pkgrel}",
        f"base-full-kernel={pkgver}-r{pkgrel}",
        f"base-full-misc={pkgver}-r{pkgrel}",
        f"base-full-net={pkgver}-r{pkgrel}",
        f"base-full-session={pkgver}-r{pkgrel}",
        f"base-full-sound={pkgver}-r{pkgrel}",
    ]
    self.provider_priority = 0
    return []
