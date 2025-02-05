pkgname = "base-full"
pkgver = "0.6"
pkgrel = 3
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
        "cmd:dmesg!util-linux-dmesg",
        "console-setup",
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
        "cmd:tar!libarchive-progs",
        "chimera-install-scripts",
        "dinit-chimera",
        "procps",
        "turnstile",
    ]
    return []


@subpackage("base-full-firmware")
def _(self):
    self.subdesc = "firmware"
    self.install_if = [self.parent, "linux", "!base-full-minimal"]
    self.depends = [
        "firmware-linux-meta",
        "firmware-ipw2100",
        "firmware-ipw2200",
        "firmware-zd1211",
    ]
    if self.rparent.profile().arch == "x86_64":
        self.depends += ["firmware-sof-meta"]
    return []


@subpackage("base-full-fonts")
def _(self):
    self.subdesc = "fonts"
    self.install_if = [self.parent, "fontconfig", "!base-full-minimal"]
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
        "util-linux-fdisk",
        "util-linux-fstrim",
        "util-linux-mkfs",
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
    self.install_if = [self.parent, "linux", "!base-full-minimal"]
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
    self.install_if = [self.parent, "!base-full-minimal"]
    # transitional
    self.provides = [self.with_pkgver("base-core-misc")]
    self.depends = [
        "bc-gh",
        "chimera-artwork",
        "chimerautils-extra",
        "chrony",
        "file",
        "less",
        "nano",
        "pciutils",
        "syslog-ng",
        "opendoas",
        "usbutils",
        "util-linux-lscpu",
        "util-linux-zramctl",
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
        "util-linux-rfkill",
    ]
    return []


@subpackage("base-full-net")
def _(self):
    self.subdesc = "network"
    self.install_if = [self.parent, "!base-full-minimal"]
    self.depends = [
        "dhcpcd",
        "iwd",
        "openssh",
    ]
    return []


@subpackage("base-full-session")
def _(self):
    self.subdesc = "session management"
    self.install_if = [self.parent, "!base-full-minimal"]
    self.depends = [
        "elogind-meta",
        "dinit-dbus",
    ]
    return []


@subpackage("base-full-sound")
def _(self):
    self.subdesc = "sound"
    self.install_if = [self.parent, "!base-full-minimal"]
    self.depends = [
        "pipewire",
    ]
    return []


@subpackage("base-full-minimal")
def _(self):
    self.subdesc = "metapackage for small installations"
    self.depends = [self.parent]
    self.provides = [self.with_pkgver("base-minimal")]
    return []
