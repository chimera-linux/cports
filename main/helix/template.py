pkgname = "helix"
pkgver = "24.07"
pkgrel = 1
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "git"]
makedepends = ["rust-std"]
pkgdesc = "Fast modal terminal-based text editor"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MPL-2.0"
url = "https://github.com/helix-editor/helix"
source = f"{url}/releases/download/{pkgver}/helix-{pkgver}-source.tar.xz"
sha256 = "44d9eb113a54a80a2891ac6374c74bcd2bce63d317f1e1c69c286a6fc919922c"
env = {"HELIX_DEFAULT_RUNTIME": "/usr/lib/helix/runtime"}

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def install(self):
    self.cargo.install(wrksrc="helix-term")
    runtime_dir = "usr/lib/helix/runtime"
    self.install_dir(runtime_dir)

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
