pkgname = "runc"
pkgver = "1.1.15"
pkgrel = 0
build_style = "makefile"
make_build_args = ["all", "man", f"COMMIT=chimera-r{pkgrel}"]
make_check_target = "localunittest"
hostmakedepends = [
    "bash",
    "go",
    "go-md2man",
    "pkgconf",
]
makedepends = [
    "libseccomp-devel",
    "linux-headers",
]
pkgdesc = "CLI tool for spawning and running containers on Linux"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/opencontainers/runc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8446718a107f3e437bc33a4c9b89b94cb24ae58ed0a49d08cd83ac7d39980860"
# tests create namespaces and fail because no perms
options = ["!check"]


def post_extract(self):
    # delete stray incomplete vendor dir
    self.rm("vendor/", recursive=True)


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def install(self):
    # rather than patch -D, just copy the files
    self.install_file("runc", "usr/bin")
    self.install_files("man/man8", "usr/share/man")
