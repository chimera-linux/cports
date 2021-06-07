pkgname = "patch"
version = "2.7.6"
revision = 4
_gitrev = "31491e1de2e1241885984cd9e4b978965f14eda4"
wrksrc = f"bsdpatch-{_gitrev}"
bootstrap = True
build_style = "gnu_makefile"
short_desc = "Patch files using diff output"
maintainer = "Enno Boland <gottox@voidlinux.org>"
license = "GPL-3.0-or-later"
homepage = "http://www.gnu.org/software/patch/patch.html"
distfiles = [
    f"https://github.com/chimera-linux/bsdpatch/archive/{_gitrev}.tar.gz"
]
checksum = ["b18842ce300b2193b0991105cd94f57c094267887f8dca73baf5c6513daaaa1d"]
