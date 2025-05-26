pkgname = "niri"
pkgver = "25.05.1"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "dbus,dinit,xdp-gnome-screencast",
]
make_check_args = [*make_build_args]
make_check_env = {"XDG_RUNTIME_DIR": "/tmp"}
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "cairo-devel",
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
depends = [
    "so:libEGL.so.1!mesa-egl-libs",
]
checkdepends = ["xkeyboard-config"]
pkgdesc = "Scrollable-tiling wayland compositor"
license = "GPL-3.0-or-later"
url = "https://github.com/YaLTeR/niri"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2df192fa85adbb0eabcfddbd8aa812c3d3329a582a7e62212ea9fcddafa79b00"
# cross: generates completions using host binary
options = ["!cross"]

if self.profile().wordsize == 32:
    broken = "weird pipewire api stuff"

if self.profile().arch in ["loongarch64"]:
    broken = "cannot find value `MADV_SOFT_OFFLINE` in module `c`"

if self.profile().arch in ["ppc64le", "riscv64"]:
    # fails some xkeyboard stuff mysteriously? FIXME
    options += ["!check"]

# TODO: dinit graphical user session service, --notify-fd, etc


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
    self.install_file("resources/niri.desktop", "usr/share/wayland-sessions")
    self.install_file(
        "resources/niri-portals.conf", "usr/share/xdg-desktop-portal"
    )
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"niri.{shell}", shell, "niri")
