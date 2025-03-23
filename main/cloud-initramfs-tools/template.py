pkgname = "cloud-initramfs-tools"
pkgver = "0.18_p14"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["scdoc", "pkgconf", "wayland-progs"]
makedepends = [
    "cairo-devel",
    "libx11-devel",
    "libxinerama-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "ncurses-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Initramfs hooks for cloud and embedded environments"
license = "GPL-3.0-or-later"
url = "https://salsa.debian.org/cloud-team/cloud-initramfs-tools"
source = f"{url}/-/archive/debian/{pkgver.replace('_p', '.debian')}/cloud-initramfs-tools-debian-{pkgver.replace('_p', '.debian')}.tar.gz"
sha256 = "b746cdd93d35ac48318051eb09c1c21eb350f4b5a9477798ee6a29b446999e02"
# no tests
options = ["!check", "empty"]


@subpackage("cloud-initramfs-tools-dyn-netconf")
def _(self):
    self.subdesc = "write a network interface file in /run for BOOTIF"
    self.depends = ["initramfs-tools"]
    self.install_if = [self.parent]
    self.options = ["!autosplit"]
    return [
        "usr/share/initramfs-tools/hooks/*netconf",
        "usr/share/initramfs-tools/scripts/init-*/*netconf",
    ]


@subpackage("cloud-initramfs-tools-growroot")
def _(self):
    self.subdesc = "automatically resize the root partition on first boot"
    self.depends = [
        "cloud-utils-growpart",
        "initramfs-tools",
        "util-linux-fdisk",
    ]
    self.install_if = [self.parent]
    self.options = ["!autosplit"]
    return [
        "usr/share/initramfs-tools/hooks/growroot",
        "usr/share/initramfs-tools/scripts/local-bottom/growroot",
    ]


@subpackage("cloud-initramfs-tools-rescuevol")
def _(self):
    self.subdesc = "boot off a rescue volume rather than root filesystem"
    self.depends = ["initramfs-tools"]
    self.install_if = [self.parent]
    self.options = ["!autosplit"]
    return [
        "usr/share/initramfs-tools/hooks/rescuevol",
        "usr/share/initramfs-tools/scripts/local-premount/rescuevol",
    ]


@subpackage("cloud-initramfs-tools-overlayroot")
def _(self):
    self.subdesc = "use an overlayfs on top of read-only root filesystem"
    self.depends = ["cryptsetup-scripts", "initramfs-tools"]
    self.install_if = [self.parent]
    self.options = ["!autosplit"]
    return [
        "etc/overlayroot.conf",
        "etc/update-motd.d/97-overlayroot",
        "usr/bin/overlayroot-chroot",
        "usr/share/initramfs-tools/conf-hooks.d/overlayroot",
        "usr/share/initramfs-tools/hooks/overlayroot",
        "usr/share/initramfs-tools/scripts/init-bottom/overlayroot",
        "usr/share/man/man8/overlayroot-chroot.8",
    ]
