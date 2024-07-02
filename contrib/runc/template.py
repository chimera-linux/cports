pkgname = "runc"
pkgver = "1.1.13"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["all", "man", f"COMMIT=chimera-r{pkgrel}"]
make_check_target = "localunittest"
hostmakedepends = [
    "bash",
    "gmake",
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
sha256 = "789d5749a08ef1fbe5d1999b67883206a68a4e58e6ca0151c411d678f3480b25"
# objcopy fails on ppc
# tests create namespaces and fail because no perms
options = ["!debug", "!check"]


def post_extract(self):
    # delete stray incomplete vendor dir
    self.rm("vendor/", recursive=True)


def post_prepare(self):
    from cbuild.util import golang

    golang.Golang(self).mod_download()


def init_build(self):
    from cbuild.util import golang

    self.make_env.update(golang.get_go_env(self))


def do_install(self):
    # rather than patch -D, just copy the files
    self.install_file("runc", "usr/bin")
    self.install_files("man/man8", "usr/share/man")
