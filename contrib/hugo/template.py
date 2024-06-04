pkgname = "hugo"
pkgver = "0.126.3"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Static site generator"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://gohugo.io"
source = f"https://github.com/gohugoio/hugo/archive/v{pkgver}.tar.gz"
sha256 = "2a1d65b09884e3c57a8705db99487404856c947dd847cf7bb845e0e1825b33ec"
# tests require network access
# manpages and completions are generated with the resulting binary so no cross
options = ["!check", "!cross"]


def post_build(self):
    self.do(self.make_dir + "/hugo", "gen", "man")

    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"hugo.{shell}", "w") as f:
            self.do(
                self.make_dir + "/hugo",
                "completion",
                shell,
                stdout=f,
            )


def post_install(self):
    self.install_man("man/*", glob=True)

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"hugo.{shell}", shell)
