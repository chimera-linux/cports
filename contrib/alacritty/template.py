pkgname = "alacritty"
pkgver = "0.13.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo",
    "ncurses",
    "pkgconf",
    "scdoc",
]
makedepends = ["fontconfig-devel", "freetype-devel", "libxcb-devel", "rust-std"]
depends = [f"alacritty-terminfo={pkgver}-r{pkgrel}"]
pkgdesc = "Cross-platform, GPU-accelerated terminal emulator"
maintainer = "nbfritch <nbfritch@gmail.com>"
license = "MIT OR Apache-2.0"
url = "https://github.com/alacritty/alacritty"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1c1cebf20e10bb26dc8bc735bb2d02eb88df89180d6c59f5d946a0a1d3d585b2"


def do_install(self):
    self.cargo.install(wrksrc="alacritty")

    for man in [
        "alacritty.1",
        "alacritty-msg.1",
        "alacritty.5",
        "alacritty-bindings.5",
    ]:
        with open(self.cwd / f"extra/man/{man}.scd", "rb") as i:
            with open(self.cwd / f"extra/man/{man}", "w") as o:
                self.do("scdoc", input=i.read(), stdout=o)
                self.install_man(self.cwd / f"extra/man/{man}")

    self.install_license("LICENSE-MIT")
    self.install_completion("extra/completions/alacritty.bash", "bash")
    self.install_completion("extra/completions/alacritty.fish", "fish")
    self.install_completion("extra/completions/_alacritty", "zsh")
    self.install_file("extra/linux/Alacritty.desktop", "usr/share/applications")
    self.install_file(
        "extra/linux/org.alacritty.Alacritty.appdata.xml", "usr/share/metainfo"
    )
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
