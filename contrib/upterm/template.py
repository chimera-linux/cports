pkgname = "upterm"
pkgver = "0.14.3"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/upterm", "./cmd/uptermd"]
make_install_args = make_build_args
hostmakedepends = ["go"]
pkgdesc = "Instant terminal sharing"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/owenthereal/upterm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3ca2bb64943ba8ecd31ae83036794749bb32618a1929f4b22d535cfb28dda367"
# cross: generates completions with host binary
# check: uses -race that conflicts with -buildmode=pie
options = ["!cross", "!check"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"upterm.{shell}", "w") as outf:
            self.do(
                "build/upterm",
                "completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_service(self.files_path / "uptermd")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_man("etc/man/man1/*.1", glob=True)
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"upterm.{shell}", shell)


@subpackage("uptermd")
def _daemon(self):
    self.pkgdesc = f"{pkgdesc} (daemon)"
    return [
        "usr/bin/uptermd",
        "etc/dinit.d/uptermd",
        "usr/lib/tmpfiles.d/upterm.conf",
        "usr/lib/sysusers.d/upterm.conf",
    ]
