pkgname = "base-full"
pkgver = "0.3"
pkgrel = 2
build_style = "meta"
provides = [self.with_pkgver("base-core")]
pkgdesc = "Chimera base package for bare metal and virtual machines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


@subpackage("base-full-console")
def _console(self):
    self.pkgdesc = f"{pkgdesc} (console tools)"
    self.install_if = [self.parent]
    self.provider_priority = 100
    # transitional
    self.provides = [self.with_pkgver("base-core-console")]
    self.depends = [
        "console-setup",
        "dmesg",
        "kbd",
        "nyagetty",
    ]
    return []


@subpackage("base-full-core")
def _core(self):
    self.pkgdesc = f"{pkgdesc} (core tools)"
    self.install_if = [self.parent]
    self.provider_priority = 100
    self.depends = [
        "base-bootstrap",
        "bsdtar",
        "chimera-install-scripts",
        "dinit-chimera",
        "procps",
        "turnstile",
    ]
    return []


@subpackage("base-full-firmware")
def _fw(self):
    self.pkgdesc = f"{pkgdesc} (firmware)"
    self.install_if = [self.parent]
    self.provider_priority = 100
    self.depends = [
        "base-firmware-linux",
        "firmware-ipw2100",
        "firmware-ipw2200",
        "firmware-zd1211",
    ]
    if self.rparent.profile().arch == "x86_64":
        self.depends += ["base-firmware-sof"]
    return []


@subpackage("base-full-fonts")
def _fonts(self):
    self.pkgdesc = f"{pkgdesc} (fonts)"
    self.install_if = [self.parent, "fontconfig"]
    self.provider_priority = 100
    self.depends = [
        "fonts-dejavu",
    ]
    return []


@subpackage("base-full-fs")
def _fs(self):
    self.pkgdesc = f"{pkgdesc} (filesystem tools)"
    self.install_if = [self.parent]
    self.provider_priority = 100
    # transitional
    self.provides = [self.with_pkgver("base-core-fs")]
    self.depends = [
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
    self.install_if = [self.parent]
    self.provider_priority = 100
    # transitional
    self.provides = [self.with_pkgver("base-core-kernel")]
    self.depends = [
        "base-kernel",
        "initramfs-tools",
    ]
    return []


@subpackage("base-full-locale")
def _locale(self):
    self.pkgdesc = f"{pkgdesc} (locale)"
    self.install_if = [self.parent]
    self.provider_priority = 100
    self.depends = [
        "base-locale",
    ]
    return []


@subpackage("base-full-man")
def _man(self):
    self.pkgdesc = f"{pkgdesc} (manpages)"
    self.install_if = [self.parent]
    self.provider_priority = 100
    # transitional
    self.provides = [self.with_pkgver("base-core-man")]
    self.depends = [
        "base-man",
        "man-pages",
    ]
    return []


@subpackage("base-full-misc")
def _misc(self):
    self.pkgdesc = f"{pkgdesc} (miscellaneous)"
    self.install_if = [self.parent]
    self.provider_priority = 100
    # transitional
    self.provides = [self.with_pkgver("base-core-misc")]
    self.depends = [
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
    self.install_if = [self.parent]
    self.provider_priority = 100
    # transitional
    self.provides = [self.with_pkgver("base-core-net")]
    self.depends = [
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
    self.install_if = [self.parent]
    self.provider_priority = 100
    self.depends = [
        "dhcpcd",
        "iwd",
        "openssh",
    ]
    return []


@subpackage("base-full-session")
def _session(self):
    self.pkgdesc = f"{pkgdesc} (session management)"
    self.install_if = [self.parent]
    self.provider_priority = 100
    self.depends = [
        "elogind-meta",
        "dbus",
    ]
    return []


@subpackage("base-full-sound")
def _sound(self):
    self.pkgdesc = f"{pkgdesc} (sound)"
    self.install_if = [self.parent]
    self.provider_priority = 100
    self.depends = [
        "pipewire",
    ]
    return []


@subpackage("base-minimal")
def _minimal(self):
    self.pkgdesc = f"{pkgdesc} (metapackage for small installations)"
    self.depends = [self.parent]
    self.provides = [
        self.with_pkgver("base-full-firmware"),
        self.with_pkgver("base-full-fonts"),
        self.with_pkgver("base-full-kernel"),
        self.with_pkgver("base-full-misc"),
        self.with_pkgver("base-full-net"),
        self.with_pkgver("base-full-session"),
        self.with_pkgver("base-full-sound"),
    ]
    self.provider_priority = 0
    return []
