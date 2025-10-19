pkgname = "alacritty"
pkgver = "0.16.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "ncurses",
    "pkgconf",
    "scdoc",
]
makedepends = ["fontconfig-devel", "freetype-devel", "libxcb-devel", "rust-std"]
pkgdesc = "Cross-platform, GPU-accelerated terminal emulator"
license = "MIT OR Apache-2.0"
url = "https://github.com/alacritty/alacritty"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7baaf26acd80f6b7ceceb2c984b0d43b4089af2d12db3cbaa60ad1243d712e72"


def install(self):
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
