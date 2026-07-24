pkgname = "ldacbt"
pkgver = "2.0.2.6"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "AOSP libldac dispatcher"
license = "Apache-2.0"
url = "https://github.com/EHfive/ldacBT"
source = f"{url}/releases/download/v{pkgver}/ldacBT-{pkgver}.tar.gz"
sha256 = "fee05740e86ee66f4540486d92683ee8e8071119907b57ca762c7e5d943ecef0"
# no test suite
options = ["!check"]

if self.profile().endian == "big":
    broken = "big endian is not supported"


@subpackage("ldacbt-devel")
def _(self):
    return self.default_devel()
