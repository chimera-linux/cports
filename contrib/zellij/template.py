pkgname = "zellij"
pkgver = "0.40.1"
pkgrel = 0
build_style = "cargo"
make_check_args = ["--release"]
hostmakedepends = ["cargo-auditable", "pkgconf", "openssl-devel", "go-md2man"]
pkgdesc = "Terminal workspace with batteries included"
maintainer = "Denis Strizhkin <strdenis02@gmail.com>"
license = "MIT"
url = "https://github.com/zellij-org/zellij"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1f0bfa13f2dbe657d76341a196f98a3b4caa47ac63abee06b39883a11ca220a8"

def post_build(self):
    with open(self.cwd / "docs/MANPAGE.md", "rb") as i:
        with open(self.cwd / f"docs/{pkgname}.1", "w") as o:
            self.do("go-md2man", input=i.read(), stdout=o)

    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"assets/{pkgname}.{shell}", "w") as o:
            self.do(
                f"target/{self.profile().triplet}/release/{pkgname}",
                "setup", "--generate-completion", shell, stdout=o
            )
    
    
def post_install(self):
    self.install_man(self.cwd / f"docs/{pkgname}.1")
    self.install_license(self.cwd / "LICENSE.md")

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"assets/{pkgname}.{shell}", shell, pkgname)

    self.install_file("assets/logo.png", "usr/share/pixmaps", name=f"{pkgname}.png")
    self.install_file(f"assets/{pkgname}.desktop", "usr/share/applications")
