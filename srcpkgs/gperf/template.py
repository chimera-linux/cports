pkgname = "gperf"
version = "3.1"
revision = 3
build_style = "gnu_configure"
short_desc = "Perfect hash function generator"
maintainer = "Orphaned <orphan@voidlinux.org>"
license = "GPL-3.0-or-later"
homepage = "https://www.gnu.org/software/gperf/"

from cbuild import sites

distfiles = [f"{sites.gnu}/{pkgname}/{pkgname}-{version}.tar.gz"]
checksum = ["588546b945bba4b70b6a3a616e80b4ab466e3f33024a352fc2198112cdbb3ae2"]
