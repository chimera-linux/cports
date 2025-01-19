pkgname = "userspace-rcu"
pkgver = "0.15.0"
pkgrel = 0
build_style = "gnu_configure"
make_check_args = ["-j1"]
hostmakedepends = ["automake", "pkgconf", "slibtool"]
pkgdesc = "Userspace RCU library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://liburcu.org"
source = f"https://www.lttng.org/files/urcu/userspace-rcu-{pkgver}.tar.bz2"
sha256 = "4f2d839af67905ad396d6d53ba5649b66113d90840dcbc89941e0da64bccd38c"
tool_flags = {"CFLAGS": ["-DLITTLE_ENDIAN=4321", "-DBIG_ENDIAN=1234"]}
# XXX: tests pass when run outside the suite...
options = ["!check"]

if self.profile().endian == "big":
    tool_flags["CFLAGS"] += ["-DBYTE_ORDER=1234"]
else:
    tool_flags["CFLAGS"] += ["-DBYTE_ORDER=4321"]


@subpackage("userspace-rcu-devel")
def _(self):
    return self.default_devel(extra=["usr/share/doc"])
