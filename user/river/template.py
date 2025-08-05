pkgname = "river"
pkgver = "0.3.5"
pkgrel = 0
hostmakedepends = ["zig", "pkgconf", "scdoc"]
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
    f"https://codeberg.org/ifreund/zig-pixman/archive/v0.2.0.tar.gz > {pkgname}-pixman-0.2.0.tar.gz",
    f"https://codeberg.org/ifreund/zig-wayland/archive/v0.2.0.tar.gz > {pkgname}-wayland-0.2.0.tar.gz",
    f"https://codeberg.org/ifreund/zig-wlroots/archive/v0.18.0.tar.gz > {pkgname}-wlroots-0.18.0.tar.gz",
    f"https://codeberg.org/ifreund/zig-xkbcommon/archive/v0.2.0.tar.gz > {pkgname}-xkbcommon-0.2.0.tar.gz",
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
# same as restricted
options = ["!check", "!cross"]
restricted = "work in progress (needs proper zig integration)"


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
        "-Dman-pages",
        "--prefix",
        "zig_output",
    )


def install(self):
    from pathlib import Path

    out = Path("zig_output")
    out_bin = out / "bin"
    out_share = out / "share"
    for bin in ["river", "riverctl", "rivertile"]:
        self.install_bin(out_bin / bin)
        self.install_man(out_share / f"man/man1/{bin}.1")
    self.install_license("LICENSE")
    self.install_file(
        out_share / "river-protocols/river-layout-v3.xml",
        dest="usr/share/river-protocols",
    )
    self.install_completion(out_share / "zsh/site-functions/_riverctl", "zsh")
    self.install_completion(
        out_share / "bash-completion/completions/riverctl", "bash"
    )
    self.install_completion(
        out_share / "fish/vendor_completions.d/riverctl.fish", "fish"
    )
