pkgname = "mingw-w64-libssp-static"
pkgver = "0.1"
pkgrel = 0
build_style = "meta"
depends = []
pkgdesc = "Metapackage providing libssp for Windows development"
license = "custom:meta"
url = "https://chimera-linux.org"

_targets = ["x86_64", "i686", "armv7", "aarch64"]


def _gen(an):
    at = an + "-w64-mingw32"

    @subpackage(f"mingw-w64-libssp-static-{an}")
    def _(self):
        self.subdesc = f"{an} support"
        self.depends = ["musl-libssp-static", f"mingw-w64-crt-{an}"]
        self.options = ["brokenlinks"]

        return [
            f"@usr/{at}/lib/libssp.a=>../../lib/libssp_nonshared.a",
            f"@usr/{at}/lib/libssp_nonshared.a=>../../lib/libssp_nonshared.a",
        ]

    depends.append(self.with_pkgver(f"mingw-w64-libssp-static-{an}"))


for _an in _targets:
    _gen(_an)
