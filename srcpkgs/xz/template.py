pkgname = "xz"
version = "5.2.5"
revision = 0
build_style = "gnu_configure"
short_desc = "The XZ compression utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Public domain, GPL-2.0-or-later, GPL-3.0-or-later, LGPL-2.1-or-later"
homepage = "https://tukaani.org/xz"
distfiles = [f"https://tukaani.org/xz/xz-{version}.tar.bz2"]
checksum = ["5117f930900b341493827d63aa910ff5e011e0b994197c3b71c08a20228a42df"]

options = ["bootstrap"]

def post_install(self):
    import shutil
    shutil.rmtree(self.destdir / "usr/share/doc")
    for tool in [
        "xzgrep", "xzfgrep", "xzegrep", "lzgrep", "lzfgrep", "lzegrep"
    ]:
        (self.destdir / "usr/bin" / tool).unlink()
        (self.destdir / "usr/share/man/man1" / (tool + ".1")).unlink()

@subpackage("liblzma")
def _lib(self):
    self.short_desc = "XZ-format compression library"

    return ["usr/lib/*.so.*"]

@subpackage("liblzma-devel")
def _devel(self):
    self.short_desc = "XZ-format compression library - development files"
    self.depends = [f"liblzma={version}-r{revision}"]

    return [
        "usr/include",
        "usr/lib/*.a",
        "usr/lib/*.so",
        "usr/lib/pkgconfig",
    ]
