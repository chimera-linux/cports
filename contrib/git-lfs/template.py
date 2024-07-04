pkgname = "git-lfs"
pkgver = "3.5.1"
pkgrel = 2
build_style = "go"
make_dir = "bin"  # needed for tests
make_build_args = [
    "-ldflags=-X github.com/git-lfs/git-lfs/v3/config.Vendor=ChimeraLinux"
]
hostmakedepends = ["asciidoctor", "go"]
checkdepends = ["bash", "curl", "git", "gmake", "perl"]
depends = ["git"]
pkgdesc = "Git extension for versioning large files"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "MIT"
url = "https://git-lfs.com"
source = f"https://github.com/git-lfs/git-lfs/releases/download/v{pkgver}/git-lfs-v{pkgver}.tar.gz"
sha256 = "fc19c7316e80a6ef674aa4e1863561c1263cd4ce0588b9989e4be9461664d752"


def post_build(self):
    self.mkdir("man")
    for file in self.find("docs/man", "*.adoc"):
        self.do(
            "asciidoctor",
            "-bmanpage",
            "-Dman",
            "-a",
            f"mansource={pkgname} {pkgver}",
            file,
        )


def do_check(self):
    from cbuild.util import golang

    self.golang.check()
    self.do("gmake", "test", "-C", "t", env=golang.get_go_env(self))


def do_install(self):
    self.install_bin("bin/git-lfs")
    self.install_license("LICENSE.md")
    self.install_man("man/*", glob=True)
    for shell in ("bash", "fish", "zsh"):
        self.install_completion(
            f"t/fixtures/completions/git-lfs-completion.{shell}",
            shell,
        )
