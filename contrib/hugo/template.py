pkgname = "hugo"
pkgver = "0.126.2"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Static site generator"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://gohugo.io"
source = f"https://github.com/gohugoio/hugo/archive/v{pkgver}.tar.gz"
sha256 = "1ee1a7948303937e6f846bdbb99fc3681d25418d25772edb7a367b3456ef05db"
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
