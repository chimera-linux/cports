pkgname = "hugo"
pkgver = "0.140.2"
pkgrel = 0
build_style = "go"
make_build_args = [
    "-ldflags=-X github.com/gohugoio/hugo/common/hugo.vendorInfo=ChimeraLinux"
]
hostmakedepends = ["go"]
go_build_tags = ["extended"]
pkgdesc = "Static site generator"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://gohugo.io"
source = f"https://github.com/gohugoio/hugo/archive/v{pkgver}.tar.gz"
sha256 = "45594ddf39d62d227cfd54c19fb9a09ab851cf537caee6138de0ddd4f1f6f117"
# tests require network access
# manpages and completions are generated with the resulting binary so no cross
options = ["!check", "!cross"]


def post_build(self):
    self.do(f"{self.make_dir}/hugo", "gen", "man")

    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"hugo.{shell}", "w") as f:
            self.do(f"{self.make_dir}/hugo", "completion", shell, stdout=f)


def post_install(self):
    self.install_man("man/*", glob=True)

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"hugo.{shell}", shell)
