pkgname = "skint"
pkgver = "0.6.7"
pkgrel = 0
build_style = "configure"
pkgdesc = "Fast implementation of the R7RS Scheme programming language"
license = "BSD-3-Clause"
url = "https://github.com/false-schemers/skint"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6f9c648e80ccfa2c5bb71b4e7e2ccfda26aac9bc845533960be5e6478286f2ad"

self.make_check_target = ["test", "libtest"]
self.make_install_target = ["install", "libinstall"]


def configure(self):
    # Upstream makefile doesn't respect DESTDIR
    self.configure_args.append(f"--prefix={self.chroot_destdir}/usr")
    # Upstream configure has #!/bin/bash shebang, use sh explicitly
    self.do(
        "sh",
        self.chroot_cwd / self.configure_script,
        *self.configure_args,
        wrksrc=self.make_dir,
        env=self.configure_env,
    )


def post_install(self):
    self.install_license("LICENSE")


@subpackage("skint-libs")
def _(self):
    return ["usr/share/skint"]
