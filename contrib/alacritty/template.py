pkgname = "alacritty"
pkgver = "0.12.1"
pkgrel = 0
build_style = "cargo"
make_install_args = ["--path", "alacritty"]
hostmakedepends = [
    "cargo",
    "cargo-auditable",
    "cmake",
    "fontconfig-devel",
    "freetype-devel",
    "gmake",
    "libxcb-devel",
    "libxkbcommon-devel",
    "pkgconf",
    "python",
    "rust",
]
depends = ["ncurses-base", "wayland", "libxi", "libxcursor"]
pkgdesc = "Cross-platform, GPU-accelerated terminal emulator"
maintainer = "nbfritch <nbfritch@gmail.com>"
license = "Apache-2.0"
url = "https://github.com/alacritty/alacritty"
source = (
    f"https://github.com/alacritty/alacritty/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "14bce0bfc538872c97e0e38b9233a9d1fa992dcf83a22b6035da5fe58a55bc6c"


def post_install(self):
    self.install_license("LICENSE-MIT")
    self.install_file(
        "extra/completions/alacritty.bash",
        "usr/share/bash-completion/completions",
        name="alacritty",
    )
    self.install_file(
        "extra/completions/_alacritty",
        "usr/share/zsh/site-functions",
    )
    self.install_file(
        "extra/completions/alacritty.fish",
        "usr/share/fish/completions",
    )
    self.install_file("extra/linux/Alacritty.desktop", "usr/share/applications")
    self.install_file(
        "extra/linux/org.alacritty.Alacritty.appdata.xml",
        "usr/share/metainfo/org.alacritty.Alacritty.appdata.xml",
    )
    self.install_file(
        "extra/logo/alacritty-term.svg",
        "usr/share/icons/hicolor/scalable/apps/",
        name="Alacritty",
    )
