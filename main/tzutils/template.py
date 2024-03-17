pkgname = "tzutils"
pkgver = "2024a"
pkgrel = 1
build_style = "makefile"
make_build_args = ["KSHELL=/bin/sh"]
make_install_args = ["ZICDIR=/usr/bin", "ZFLAGS=-b fat"]
hostmakedepends = []
checkdepends = ["curl", "perl"]
pkgdesc = "Time zone and daylight-saving time utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "http://www.iana.org/time-zones"
source = (
    f"https://www.iana.org/time-zones/repository/releases/tzdb-{pkgver}.tar.lz"
)
sha256 = "511af6b467f40b1ec9ac3684d1701793af470f3e29ddfb97b82be438e8601a7a"
hardening = ["vis", "cfi"]
# needs network access
options = ["!check"]


if self.profile().cross:
    hostmakedepends += ["tzutils"]
    make_install_args += ["zic=/usr/bin/zic"]


def post_install(self):
    # localtime
    self.rm(self.destdir / "etc", recursive=True)
    # useless static lib
    self.rm(self.destdir / "usr/lib", recursive=True)
    # irrelevant c manpages
    self.rm(self.destdir / "usr/share/man/man3", recursive=True)
    # for clean upgrades
    self.mv(
        self.destdir / "usr/share/zoneinfo-leaps",
        self.destdir / "usr/share/zoneinfo/right",
    )
    self.install_link("zoneinfo/right", "usr/share/zoneinfo-leaps")
    # ditto
    self.rm(self.destdir / "usr/share/zoneinfo-posix")
    self.install_link("zoneinfo/posix", "usr/share/zoneinfo-posix")
    # now build up the posix dir
    dst = "usr/share/zoneinfo/posix"
    self.install_dir(dst)
    # we need links to individual files and just the whole directory,
    # because apk cannot transition dirs to links without failing
    # and we don't want a pre-upgrade hook (apk is expected to be
    # fixed eventually, at that point we could migrate this)
    for d in (self.destdir / "usr/share/zoneinfo").glob("[A-Z]*"):
        if d.is_dir():
            self.install_dir(f"{dst}/{d.name}")
            for dd in d.iterdir():
                # max nesting level is two deep
                if dd.is_dir():
                    self.install_dir(f"{dst}/{d.name}/{dd.name}")
                    for f in dd.iterdir():
                        self.install_link(
                            f"../../../{d.name}/{dd.name}/{f.name}",
                            f"{dst}/{d.name}/{dd.name}/{f.name}",
                        )
                else:
                    self.install_link(
                        f"../../{d.name}/{dd.name}", f"{dst}/{d.name}/{dd.name}"
                    )
        else:
            self.install_link(f"../{d.name}", f"{dst}/{d.name}")
    # now convert all hardlinks to symlinks; in order to avoid duplicating
    # the files (as apk does not track hardlinks) we can save some two
    # megabytes of space here, at seemingly no cost
    #
    # first collect hardlinks in a set of lists
    hlinks = {}
    for f in (self.destdir / "usr/share/zoneinfo").rglob("*"):
        if not f.is_file():
            continue
        st = f.lstat()
        # first summatize in a dictionary
        if st.st_ino not in hlinks:
            hlinks[st.st_ino] = [f]
        else:
            hlinks[st.st_ino].append(f)
    # now go over each hardlink list with multiple items and sort it
    for hk in hlinks:
        hv = hlinks[hk]
        # skip uniques
        if len(hv) < 2:
            continue
        # sorted so it's stable
        hv.sort()
        fl = hv[0]
        for sl in hv[1:]:
            sl.unlink()
            # use relative symlinks
            sl.symlink_to(fl.relative_to(sl))
    # tmpfiles
    self.install_file(self.files_path / "tzdata.conf", "usr/lib/tmpfiles.d")


@subpackage("tzdata")
def _tzdata(self):
    self.pkgdesc = "Time zone and daylight-saving time data"

    return ["usr/lib/tmpfiles.d", "usr/share/zoneinfo*"]
