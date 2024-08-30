pkgname = "river"
pkgver = "0.3.5"
pkgrel = 0
hostmakedepends = ["zig", "pkgconf"]
makedepends = [
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.18-devel",
]
depends = ["xwayland"]
pkgdesc = "Dynamic tiling wayland compositor"
maintainer = "Denis Strizhkin <strdenis02@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://codeberg.org/river/river"
source = [
    f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz",
    f"https://codeberg.org/ifreund/zig-pixman/archive/v0.2.0.tar.gz > {pkgname}-{pkgver}-pixman.tar.gz",
    f"https://codeberg.org/ifreund/zig-wayland/archive/v0.2.0.tar.gz > {pkgname}-{pkgver}-wayland.tar.gz",
    f"https://codeberg.org/ifreund/zig-wlroots/archive/v0.18.0.tar.gz > {pkgname}-{pkgver}-wlroots.tar.gz",
    f"https://codeberg.org/ifreund/zig-xkbcommon/archive/v0.2.0.tar.gz > {pkgname}-{pkgver}-xkbcommon.tar.gz",
]
source_paths = [
    ".",
    "zig-pixman",
    "zig-wayland",
    "zig-wlroots",
    "zig-xkbcommon",
]
sha256 = [
    "fcf51a00e9c89f8092824b7fd23faba42f8cfa41e8c66753eca632322c305fa2",  # river
    "09880520e47d1f9abc514a458256a2c4ea1c08c4fa146a5c2904015155a90ca4",  # pixman
    "831ce41cb0aad8da97de5e27125cbdd80454e5da8fd52aa78e918c0e0c784d70",  # wayland
    "0e4d865b99b8ab399950511f51a250a827f7b837008434bd74070def3e91c1db",  # wlroots
    "7f9a04254e62daa795377181ae741cab31090a2393ee5e1a93b190ea0c39707d",  # xkbcommon
]
restricted = "work in progress (needs proper zig integration)"
# same as restricted
options = ["!check", "!cross"]


def prepare(self):
    for p in source_paths[1:]:
        self.do(
            "zig",
            "fetch",
            "--global-cache-dir",
            "deps",
            p,
        )


def build(self):
    self.do(
        "zig",
        "build",
        "--system",
        "deps/p",
        "-Dpie",
        "-Doptimize=ReleaseSafe",
        "-Dxwayland",
        "--prefix",
        "zig_output",
    )


def install(self):
    self.install_bin("zig_output/bin/river")
    self.install_bin("zig_output/bin/riverctl")
    self.install_bin("zig_output/bin/rivertile")
    self.install_license("LICENSE")
    self.install_file(
        "zig_output/share/river-protocols/river-layout-v3.xml",
        dest="usr/share/river-protocols",
    )
