pkgname = "dunst"
pkgver = "1.10.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
make_use_env = True
hostmakedepends = ["gmake", "perl", "pkgconf"]
makedepends = [
    "cairo-devel",
    "dbus-devel",
    "glib-devel",
    "libnotify-devel",
    "linux-headers",
    "libxinerama-devel",
    "libxrandr-devel",
    "libxscrnsaver-devel",
    "pango-devel",
    "wayland-devel",
    "wayland-protocols",
]
checkdepends = ["bash", "dbus"]
pkgdesc = "Notification daemon"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-3-Clause"
url = "https://dunst-project.org"
source = (
    f"https://github.com/dunst-project/dunst/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "d1fbeba329b3801b931ad804f1fadd96a36be5edf2e49c8e30f081443079759f"
env = {"SYSCONFDIR": "/etc"}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    with self.pushd("contrib"):
        self.install_completion("_dunst.zshcomp", "zsh", "dunst")
        self.install_completion("_dunstctl.zshcomp", "zsh", "dunstctl")
        self.install_completion("dunst.bashcomp", "bash", "dunst")
        self.install_completion("dunstctl.bashcomp", "bash", "dunstctl")
        self.install_completion("dunst.fishcomp", "fish", "dunst")
        self.install_completion("dunstctl.fishcomp", "fish", "dunstctl")
        self.install_completion("dunstify.fishcomp", "fish", "dunstify")
