pkgname = "helix"
pkgver = "23.10"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "git"]
makedepends = ["rust-std"]
pkgdesc = "Fast modal terminal-based text editor"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MPL-2.0"
url = "https://github.com/helix-editor/helix"
source = f"{url}/releases/download/{pkgver}/helix-{pkgver}-source.tar.xz"
sha256 = "4e7bcac200b1a15bc9f196bdfd161e4e448dc670359349ae14c18ccc512153e8"


def do_install(self):
    self.cargo.install(wrksrc="helix-term")
    runtime_dir = "usr/libexec/helix/runtime"
    self.install_dir(runtime_dir)
    self.mv(self.destdir / "usr/bin/hx", self.destdir / "usr/libexec/helix")
    self.install_link("/usr/libexec/helix/hx", "usr/bin/hx")

    self.install_files("runtime/queries", runtime_dir)
    self.install_files("runtime/themes", runtime_dir)
    self.install_file("runtime/tutor", runtime_dir)
    self.install_file(
        "runtime/grammars/*.so",
        f"{runtime_dir}/grammars",
        mode=0o755,
        glob=True,
    )

    self.install_completion("contrib/completion/hx.bash", "bash", "hx")
    self.install_completion("contrib/completion/hx.fish", "fish", "hx")
    self.install_completion("contrib/completion/hx.zsh", "zsh", "hx")

    self.install_file(f"contrib/{pkgname}.png", "usr/share/pixmaps")
    self.install_file("contrib/Helix.desktop", "usr/share/applications")
