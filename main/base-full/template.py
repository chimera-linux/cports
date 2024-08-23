pkgname = "base-full"
pkgver = "0.6"
pkgrel = 0
build_style = "meta"
provides = [self.with_pkgver("base-core")]
pkgdesc = "Chimera base package for bare metal and virtual machines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


@subpackage("base-full-console")
def _(self):
    self.subdesc = "console tools"
    self.install_if = [self.parent]
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
def _(self):
    self.subdesc = "core tools"
    self.install_if = [self.parent]
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
def _(self):
    self.subdesc = "firmware"
    self.install_if = [self.parent, "linux", "!base-minimal"]
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
def _(self):
    self.subdesc = "fonts"
    self.install_if = [self.parent, "fontconfig", "!base-minimal"]
    self.depends = [
        "fonts-dejavu",
        "fonts-liberation",
        "fonts-noto",
        "fonts-noto-sans-cjk",
        "fonts-noto-emoji-ttf",
    ]
    return []


@subpackage("base-full-fs")
def _(self):
    self.subdesc = "filesystem tools"
    self.install_if = [self.parent]
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
def _(self):
    self.subdesc = "kernel tooling"
    self.install_if = [self.parent, "linux", "!base-minimal"]
    # transitional
    self.provides = [self.with_pkgver("base-core-kernel")]
    self.depends = [
        "base-kernel",
        "initramfs-tools",
    ]
    return []


@subpackage("base-full-locale")
def _(self):
    self.subdesc = "locale"
    self.install_if = [self.parent]
    self.depends = [
        "base-locale",
    ]
    return []


@subpackage("base-full-man")
def _(self):
    self.subdesc = "manpages"
    self.install_if = [self.parent]
    # transitional
    self.provides = [self.with_pkgver("base-core-man")]
    self.depends = [
        "base-man",
        "man-pages",
    ]
    return []


@subpackage("base-full-misc")
def _(self):
    self.subdesc = "miscellaneous"
    self.install_if = [self.parent, "!base-minimal"]
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
def _(self):
    self.subdesc = "network tools"
    self.install_if = [self.parent]
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
def _(self):
    self.subdesc = "network"
    self.install_if = [self.parent, "!base-minimal"]
    self.depends = [
        "dhcpcd",
        "iwd",
        "openssh",
    ]
    return []


@subpackage("base-full-session")
def _(self):
    self.subdesc = "session management"
    self.install_if = [self.parent, "!base-minimal"]
    self.depends = [
        "elogind-meta",
        "dinit-dbus",
    ]
    return []


@subpackage("base-full-sound")
def _(self):
    self.subdesc = "sound"
    self.install_if = [self.parent, "!base-minimal"]
    self.depends = [
        "pipewire",
    ]
    return []


@subpackage("base-minimal")
def _(self):
    self.subdesc = "metapackage for small installations"
    self.depends = [self.parent]
    return []
