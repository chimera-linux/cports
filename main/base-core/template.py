pkgname = "base-core"
pkgver = "0.1"
pkgrel = 3
build_style = "meta"
depends = ["base-minimal"]
pkgdesc = "Common Chimera packages for most deployments"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


@subpackage("base-core-console")
def _console(self):
    self.pkgdesc = f"{pkgdesc} (console tools)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "console-setup",
        "dmesg",
        "kbd",
    ]
    return []


@subpackage("base-core-fs")
def _fs(self):
    self.pkgdesc = f"{pkgdesc} (filesystem tools)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
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


@subpackage("base-core-kernel")
def _kern(self):
    self.pkgdesc = f"{pkgdesc} (kernel tooling)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "base-kernel",
        "initramfs-tools",
    ]
    return []


@subpackage("base-core-man")
def _man(self):
    self.pkgdesc = f"{pkgdesc} (manpages)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "base-man",
        "man-pages",
    ]
    return []


@subpackage("base-core-net")
def _net(self):
    self.pkgdesc = f"{pkgdesc} (network tools)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "iputils",
        "iproute2",
        "traceroute",
        "iw",
    ]
    return []


@subpackage("base-core-misc")
def _misc(self):
    self.pkgdesc = f"{pkgdesc} (miscellaneous)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "chimerautils-extra",
        "bc-gh",
        "file",
        "less",
        "lscpu",
        "pciutils",
    ]
    return []
