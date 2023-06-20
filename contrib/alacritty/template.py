pkgname = "alacritty"
pkgver = "0.12.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "cmake", "pkgconf", "python", "ncurses"]
makedepends = ["fontconfig-devel", "freetype-devel", "libxcb-devel", "rust"]
depends = [f"alacritty-terminfo={pkgver}-r{pkgrel}"]
pkgdesc = "Cross-platform, GPU-accelerated terminal emulator"
maintainer = "nbfritch <nbfritch@gmail.com>"
license = "MIT OR Apache-2.0"
url = "https://github.com/alacritty/alacritty"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "285b44d2d2e83118ab7fe61d575811bb85d5e21147808171bd0e583e9e794748"


def do_install(self):
    self.cargo.install(wrksrc="alacritty")
    self.install_man("extra/alacritty.man", name="alacritty", cat=1)
    self.install_man("extra/alacritty-msg.man", name="alacritty-msg", cat=1)
    self.install_license("LICENSE-MIT")
    self.install_completion("extra/completions/alacritty.bash", "bash")
    self.install_completion("extra/completions/alacritty.fish", "fish")
    self.install_completion("extra/completions/_alacritty", "zsh")
    self.install_file("extra/linux/Alacritty.desktop", "usr/share/applications")
    self.install_file(
        "extra/logo/alacritty-term.svg",
        "usr/share/icons/hicolor/scalable/apps/",
        name="Alacritty.svg",
    )
    self.install_dir("usr/share/terminfo")
    self.do(
        "tic",
        "-xe",
        "alacritty,alacritty-direct",
        "-o",
        self.chroot_destdir / "usr/share/terminfo",
        "extra/alacritty.info",
    )


@subpackage("alacritty-terminfo")
def _tinfo(self):
    self.pkgdesc = f"{pkgdesc} (terminfo data)"

    return ["usr/share/terminfo"]
