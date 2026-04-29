pkgname = "niri"
pkgver = "26.04"
pkgrel = 1
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "dbus,dinit,xdp-gnome-screencast",
]
make_check_args = [*make_build_args]
make_check_env = {"XDG_RUNTIME_DIR": "/tmp", "RAYON_NUM_THREADS": "2"}
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
    "dinit-chimera",
    "dinit-dbus",
    "glib-devel",
    "libdisplay-info-devel",
    "libinput-devel",
    "libseat-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "pango-devel",
    "pipewire-devel",
    "pixman-devel",
    "rust-std",
    "udev-devel",
]
depends = ["bash", "so:libEGL.so.1!mesa-egl-libs", "xwayland-satellite"]
checkdepends = ["xkeyboard-config"]
pkgdesc = "Scrollable-tiling wayland compositor"
license = "GPL-3.0-or-later"
url = "https://github.com/niri-wm/niri"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "134c602d8e0d53413a52d6cd58f9ce7e79a07d03288ee0a51ba1abd5db1b1ad9"
# cross: generates completions using host binary
options = ["!cross"]

if self.profile().arch in ["ppc64le", "riscv64"]:
    # fails some xkeyboard stuff mysteriously? FIXME
    options += ["!check"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"niri.{shell}", "w") as f:
            self.do(
                f"./target/{self.profile().triplet}/release/niri",
                "completions",
                shell,
                stdout=f,
            )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/niri")
    self.install_bin("resources/niri-session")
    self.install_service("resources/dinit/niri.user")
    self.install_service("resources/dinit/niri.target.user")
    self.install_file("resources/niri.desktop", "usr/share/wayland-sessions")
    self.install_file("resources/default-config.kdl", "usr/share/doc/niri")
    self.install_file(
        "resources/niri-portals.conf", "usr/share/xdg-desktop-portal"
    )
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"niri.{shell}", shell, "niri")
