pkgname = "hugo"
pkgver = "0.127.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Static site generator"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://gohugo.io"
source = f"https://github.com/gohugoio/hugo/archive/v{pkgver}.tar.gz"
sha256 = "549c7ebdf2ee6b3107ea10a9fbd9932a91bb3f30f7e8839245f6d8e318aca88c"
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
