pkgname = "helix"
pkgver = "24.03"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "git"]
makedepends = ["rust-std"]
pkgdesc = "Fast modal terminal-based text editor"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MPL-2.0"
url = "https://github.com/helix-editor/helix"
source = f"{url}/releases/download/{pkgver}/helix-{pkgver}-source.tar.xz"
sha256 = "c59a5988f066c2ab90132e03a0e6b35b3dd89f48d3d78bf0ec81bd7d88c7677e"


def do_install(self):
    self.cargo.install(wrksrc="helix-term")
    runtime_dir = "usr/libexec/helix/runtime"
    self.install_dir(runtime_dir)
    self.rename("usr/bin/hx", "usr/libexec/helix/hx", relative=False)
    self.install_link("usr/bin/hx", "../libexec/helix/hx")

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
