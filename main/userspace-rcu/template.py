pkgname = "userspace-rcu"
pkgver = "0.15.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool"]
checkdepends = ["bash"]
pkgdesc = "Userspace RCU library"
license = "LGPL-2.1-or-later"
url = "https://liburcu.org"
source = f"https://www.lttng.org/files/urcu/userspace-rcu-{pkgver}.tar.bz2"
sha256 = "26687ec84e3e114759454c884a08abeaf79dec09b041895ddf4c45ec150acb6d"
tool_flags = {"CFLAGS": ["-DLITTLE_ENDIAN=4321", "-DBIG_ENDIAN=1234"]}

if self.profile().endian == "big":
    tool_flags["CFLAGS"] += ["-DBYTE_ORDER=1234"]
else:
    tool_flags["CFLAGS"] += ["-DBYTE_ORDER=4321"]


@subpackage("userspace-rcu-devel")
def _(self):
    return self.default_devel(extra=["usr/share/doc"])
