pkgname = "base-full"
pkgver = "0.7"
pkgrel = 0
build_style = "meta"
provides = [self.with_pkgver("base-core")]
pkgdesc = "Chimera base package for bare metal and virtual machines"
license = "custom:meta"
url = "https://chimera-linux.org"


@split("console")
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


@split("core")
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


@split("firmware")
def _(self):
    self.subdesc = "firmware"
    self.install_if = [self.parent, "linux", "!base-full-minimal"]
    self.depends = [
        "firmware-linux-meta",
        "firmware-ipw2100",
        "firmware-ipw2200",
        "firmware-zd1211",
    ]
    if self.rparent.profile.arch == "x86_64":
        self.depends += ["firmware-sof-meta"]
    return []


@split("fonts")
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


@split("fs")
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
    match self.rparent.profile.arch:
        case "ppc64" | "ppc":
            # ppc mac disk tools
            self.depends += ["hfsutils", "mac-fdisk"]
    return []


@split("kernel")
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


@split("locale")
def _(self):
    self.subdesc = "locale"
    self.install_if = [self.parent]
    self.depends = [
        "base-locale",
    ]
    return []


@split("man")
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


@split("misc")
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


@split("net-tools")
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


@split("net")
def _(self):
    self.subdesc = "network"
    self.install_if = [self.parent, "!base-full-minimal"]
    self.depends = [
        "dhcpcd",
        "networkmanager",
        "openssh",
    ]
    return []


@split("session")
def _(self):
    self.subdesc = "session management"
    self.install_if = [self.parent, "!base-full-minimal"]
    self.depends = [
        "elogind-meta",
        "dinit-dbus",
    ]
    return []


@split("sound")
def _(self):
    self.subdesc = "sound"
    self.install_if = [self.parent, "!base-full-minimal"]
    self.depends = [
        "pipewire",
    ]
    return []


@split("minimal")
def _(self):
    self.subdesc = "metapackage for small installations"
    self.depends = [self.parent]
    self.provides = [self.with_pkgver("base-minimal")]
    return []
